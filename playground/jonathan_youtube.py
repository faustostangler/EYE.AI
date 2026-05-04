import sys
import os
import subprocess
import json
import argparse
from pydantic import BaseModel, Field

# Playground rules: single file script for Jonathan v3 (YouTube extraction)
def check_gpu():
    try:
        subprocess.check_output("nvidia-smi", shell=True, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

print("Verificando dependências...")
has_gpu = check_gpu()

try:
    import yt_dlp
except ImportError:
    print("Instalando yt-dlp...")
    os.system("uv pip install yt-dlp")
    import yt_dlp

try:
    from faster_whisper import WhisperModel
except ImportError:
    print("Instalando faster-whisper...")
    os.system("uv pip install faster-whisper")
    from faster_whisper import WhisperModel

try:
    import langchain_ollama
except ImportError:
    print("Instalando dependências de LLM...")
    os.system("uv pip install langchain-ollama pydantic")
    import langchain_ollama

from langchain_ollama import OllamaLLM

# ==========================================
# Estrutura do Documento Organizado (Pydantic)
# ==========================================
class Conceito(BaseModel):
    tema: str = Field(description="O tema ou conceito principal abordado")
    explicacao: str = Field(description="A explicação ou os pontos-chave sobre esse tema")

class YouTubeSummary(BaseModel):
    titulo_sugerido: str = Field(description="Um título adequado que resuma o conteúdo do vídeo")
    resumo_geral: str = Field(description="Um parágrafo conciso resumindo o assunto geral")
    conceitos_principais: list[Conceito] = Field(description="Lista dos conceitos ou tópicos principais organizados")
    conclusao_ou_insights: str = Field(description="A conclusão, próximos passos ou insights finais do vídeo")

# ==========================================
# Configurações do LLM e Whisper
# ==========================================
MODEL_SIZE = "small"
COMPUTE_TYPE = "float16" if has_gpu else "int8"
DEVICE = "cuda" if has_gpu else "cpu"
LLM_MODEL = "gemma3:4b-it-qat"

def download_youtube_audio(url: str, output_path: str = "temp_youtube_audio.wav"):
    print(f"\n[YouTube] Baixando áudio de: {url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path.replace(".wav", ""),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_path

def transcribe_audio(audio_path: str):
    print(f"\n[Whisper] Transcrevendo áudio com {MODEL_SIZE} em {DEVICE} ({COMPUTE_TYPE})...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
    
    segments, info = model.transcribe(audio_path, beam_size=5, language="pt")
    print(f"Idioma detectado: {info.language} (probabilidade: {info.language_probability:.2f})")
    
    transcript = []
    for segment in segments:
        print(f"[{segment.start:.1f}s -> {segment.end:.1f}s] {segment.text.strip()}")
        transcript.append(segment.text.strip())
        
    return " ".join(transcript)

def generate_structured_document(transcript: str):
    print("\n[LLM] Estruturando os conceitos principais...")
    llm = OllamaLLM(model=LLM_MODEL, temperature=0.0)
    
    prompt = f"""Você é o Jonathan v3, um analista especializado em estruturação de conhecimento.
Abaixo está a transcrição de um vídeo do YouTube.
Sua tarefa é extrair as informações e gerar um documento organizado com os conceitos principais.

Transmissão Bruta:
\"\"\"
{transcript}
\"\"\"

Responda APENAS com um JSON válido que siga esta estrutura exata:
{{
  "titulo_sugerido": "string",
  "resumo_geral": "string",
  "conceitos_principais": [
    {{
      "tema": "string",
      "explicacao": "string"
    }}
  ],
  "conclusao_ou_insights": "string"
}}
"""
    try:
        response = llm.invoke(prompt)
        import re
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            json_str = match.group(0)
            data_dict = json.loads(json_str)
            doc = YouTubeSummary(**data_dict)
            
            print("\n==================================================")
            print(f"📺 DOCUMENTO ESTRUTURADO: {doc.titulo_sugerido.upper()}")
            print("==================================================")
            print(f"📝 RESUMO GERAL:\n{doc.resumo_geral}\n")
            
            print("📌 CONCEITOS PRINCIPAIS:")
            for i, conceito in enumerate(doc.conceitos_principais, 1):
                print(f"  {i}. {conceito.tema.upper()}")
                print(f"     {conceito.explicacao}\n")
                
            print(f"💡 CONCLUSÃO / INSIGHTS:\n{doc.conclusao_ou_insights}")
            print("==================================================")
            
            return doc
        else:
            print("Erro ao extrair JSON da resposta:", response)
    except Exception as e:
        print(f"Erro no processamento do LLM: {e}")

def main():
    parser = argparse.ArgumentParser(description="Jonathan v3 - YouTube Extractor & Structurer")
    parser.add_argument("url", type=str, help="URL do vídeo do YouTube")
    args = parser.parse_args()

    audio_file = "temp_youtube_audio.wav"
    
    try:
        # 1. Download
        download_youtube_audio(args.url, audio_file)
        
        # 2. Transcrição
        if not os.path.exists(audio_file):
            print("Erro: Falha no download do áudio.")
            return
            
        transcript = transcribe_audio(audio_file)
        
        if len(transcript.strip()) < 10:
            print("A transcrição ficou muito curta ou vazia.")
            return
            
        # 3. Estruturação
        generate_structured_document(transcript)
        
    finally:
        # Cleanup
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()
