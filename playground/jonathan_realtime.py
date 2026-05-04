import sys
import os
import time
import queue
import numpy as np
import json
import argparse
from pydantic import BaseModel, Field

# Playground rules: we can put everything in one file for experimentation.
def check_gpu():
    import subprocess
    try:
        subprocess.check_output("nvidia-smi", shell=True, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

print("Verificando hardware e dependências...")
has_gpu = check_gpu()
if not has_gpu:
    print("Atenção: GPU não detectada. O faster-whisper rodará na CPU.")

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("Instalando faster-whisper...")
    os.system("uv pip install faster-whisper")
    from faster_whisper import WhisperModel

try:
    import sounddevice as sd
except ImportError:
    print("Instalando sounddevice...")
    os.system("uv pip install sounddevice numpy soundfile")
    import sounddevice as sd

try:
    import langchain_ollama
except ImportError:
    print("Instalando dependências de LLM...")
    os.system("uv pip install langchain-ollama pydantic")
    import langchain_ollama

from langchain_ollama import OllamaLLM

# ==========================================
# Estrutura do Prontuário (EHR) - Pydantic
# ==========================================
class ElectronicHealthRecord(BaseModel):
    queixa_principal: str = Field(description="O motivo principal da consulta")
    historia_doenca_atual: str = Field(description="Histórico detalhado da queixa")
    sintomas: list[str] = Field(description="Lista de sintomas mencionados")
    exames_solicitados: list[str] = Field(description="Exames pedidos pelo médico")
    diagnostico_hipotese: str = Field(description="Hipótese diagnóstica ou diagnóstico confirmado")
    conduta_tratamento: str = Field(description="Conduta, tratamento ou medicamentos prescritos")

# ==========================================
# Configurações de Áudio e Modelo
# ==========================================
SAMPLE_RATE = 16000
CHUNK_DURATION = 3.0  # seconds per chunk for processing
MODEL_SIZE = "small"
COMPUTE_TYPE = "float16" if has_gpu else "int8"
DEVICE = "cuda" if has_gpu else "cpu"
LLM_MODEL = "gemma3:4b-it-qat"

audio_queue = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    """Is called for each audio block by sounddevice."""
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())

def generate_ehr(transcript: str):
    print("\n[LLM] Estruturando Prontuário Eletrônico (EHR)...")
    llm = OllamaLLM(model=LLM_MODEL, temperature=0.0)
    
    prompt = f"""Você é um assistente médico especialista (Visio-Scribe Jonathan).
Abaixo está a transcrição bruta de uma consulta médica.
Sua tarefa é extrair as informações e preencher um Prontuário Eletrônico (EHR) estruturado em JSON.

Se alguma informação não estiver presente, use "Não informado".

Transmissão Bruta:
\"\"\"
{transcript}
\"\"\"

Responda APENAS com um JSON válido que siga esta estrutura exata:
{{
  "queixa_principal": "string",
  "historia_doenca_atual": "string",
  "sintomas": ["string", "string"],
  "exames_solicitados": ["string"],
  "diagnostico_hipotese": "string",
  "conduta_tratamento": "string"
}}
"""
    try:
        response = llm.invoke(prompt)
        import re
        # Extrai apenas o JSON da resposta
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            json_str = match.group(0)
            ehr_dict = json.loads(json_str)
            ehr = ElectronicHealthRecord(**ehr_dict)
            print("\n==================================================")
            print("🏥 PRONTUÁRIO ELETRÔNICO DO PACIENTE (ESTRUTURADO)")
            print("==================================================")
            print(f"🔹 Queixa Principal: {ehr.queixa_principal}")
            print(f"🔹 HDA: {ehr.historia_doenca_atual}")
            print(f"🔹 Sintomas: {', '.join(ehr.sintomas) if ehr.sintomas else 'Nenhum'}")
            print(f"🔹 Exames: {', '.join(ehr.exames_solicitados) if ehr.exames_solicitados else 'Nenhum'}")
            print(f"🔹 Hipótese: {ehr.diagnostico_hipotese}")
            print(f"🔹 Conduta: {ehr.conduta_tratamento}")
            print("==================================================")
            return ehr
        else:
            print("Erro ao extrair JSON da resposta:", response)
    except Exception as e:
        print(f"Erro no processamento do LLM: {e}")

def process_file_stream(file_path, model):
    import soundfile as sf
    print(f"Simulando streaming do arquivo: {file_path}")
    data, sr = sf.read(file_path, dtype='float32')
    
    # Resample se necessário (simplificado, assumes 16k or we just pass it)
    if sr != SAMPLE_RATE:
        print(f"Aviso: Arquivo está em {sr}Hz. Whisper espera 16000Hz.")
        
    if len(data.shape) > 1:
        data = data.mean(axis=1) # mix to mono
        
    chunk_samples = int(SAMPLE_RATE * CHUNK_DURATION)
    transcript_accumulated = []
    
    for i in range(0, len(data), chunk_samples):
        chunk = data[i:i+chunk_samples]
        if len(chunk) < SAMPLE_RATE * 0.5: # pula chunks mto pequenos no final
            continue
            
        segments, _ = model.transcribe(chunk, beam_size=5, language="pt", vad_filter=True, condition_on_previous_text=False)
        for segment in segments:
            text = segment.text.strip()
            if text:
                print(f"🗣️  {text}")
                transcript_accumulated.append(text)
                
    return " ".join(transcript_accumulated)

def process_microphone_stream(model):
    print("\n🎤 Pressione Ctrl+C para PARAR a gravação e gerar o Prontuário.\n")
    print("Iniciando captura de áudio...")
    
    transcript_accumulated = []
    try:
        with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32', callback=audio_callback):
            while True:
                frames = []
                target_frames = int(SAMPLE_RATE * CHUNK_DURATION)
                collected = 0
                while collected < target_frames:
                    data = audio_queue.get()
                    frames.append(data)
                    collected += len(data)
                
                audio_data = np.concatenate(frames, axis=0).flatten()
                
                # RMS simples para evitar inferência em ruído de fundo
                rms = np.sqrt(np.mean(audio_data**2))
                if rms < 0.01:
                    continue
                    
                segments, _ = model.transcribe(audio_data, beam_size=5, language="pt", condition_on_previous_text=False)
                for segment in segments:
                    text = segment.text.strip()
                    if text:
                        print(f"🗣️  {text}")
                        transcript_accumulated.append(text)
                        
    except KeyboardInterrupt:
        print("\n\n⏹️  Gravação finalizada.")
        
    return " ".join(transcript_accumulated)

def main():
    parser = argparse.ArgumentParser(description="Jonathan v2 Real-time transcriber & EHR generator")
    parser.add_argument("--file", type=str, help="Caminho para arquivo de áudio (simula streaming)", default=None)
    args = parser.parse_args()

    print(f"[Whisper] Carregando modelo {MODEL_SIZE} em {DEVICE} ({COMPUTE_TYPE})...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
    
    if args.file:
        full_transcript = process_file_stream(args.file, model)
    else:
        full_transcript = process_microphone_stream(model)
        
    if len(full_transcript.strip()) < 5:
        print("Transcrição vazia ou muito curta. Encerrando.")
        return
        
    print("\n📄 Transcrição Completa:")
    print(full_transcript)
    
    # Gerar Prontuário
    generate_ehr(full_transcript)

if __name__ == "__main__":
    main()
