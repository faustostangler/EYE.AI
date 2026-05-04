import sys
import os
import subprocess
import tempfile
import math

def check_gpu():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        try:
            subprocess.check_output("nvidia-smi", shell=True, stderr=subprocess.DEVNULL)
            return True
        except Exception:
            return False

def install_deps(has_gpu):
    try:
        if has_gpu:
            print("GPU detectada. Verificando faster-whisper...")
            try:
                import faster_whisper
            except ImportError:
                print("Instalando faster-whisper...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "faster-whisper", "torch"])
        else:
            print("GPU não detectada. Verificando openai-whisper e pydub...")
            try:
                import whisper
                import pydub
            except ImportError:
                print("Instalando openai-whisper e pydub para fallback...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", "openai-whisper", "torch", "pydub"])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar dependências: {e}")
        sys.exit(1)

def format_timestamp(seconds: float):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def transcribe_faster_whisper(audio_path, output_srt):
    from faster_whisper import WhisperModel
    print("Carregando modelo faster-whisper (base)...")
    model = WhisperModel("base", device="cuda", compute_type="float16")
    segments, info = model.transcribe(audio_path, beam_size=5)
    
    print(f"Idioma detectado: {info.language} com probabilidade {info.language_probability:.2f}")
    
    with open(output_srt, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            start_str = format_timestamp(segment.start)
            end_str = format_timestamp(segment.end)
            text = segment.text.strip()
            
            chunk = f"{i}\n{start_str} --> {end_str}\n{text}\n\n"
            f.write(chunk)
            f.flush()
            print(f"Segmento {i} salvo: {start_str} -> {end_str}")

def transcribe_openai_whisper(audio_path, output_srt):
    import whisper
    from pydub import AudioSegment
    import warnings
    warnings.filterwarnings("ignore")
    
    print("Carregando modelo openai-whisper (base)...")
    model = whisper.load_model("base", device="cpu")
    
    # Processamento em chunks para economizar memória e permitir output incremental
    chunk_length_ms = 10 * 60 * 1000 # 10 minutos
    print(f"Carregando áudio para segmentação...")
    audio = AudioSegment.from_file(audio_path)
    
    total_length_ms = len(audio)
    num_chunks = math.ceil(total_length_ms / chunk_length_ms)
    
    segment_index = 1
    
    with open(output_srt, "w", encoding="utf-8") as f:
        for i in range(num_chunks):
            start_time_ms = i * chunk_length_ms
            end_time_ms = min((i + 1) * chunk_length_ms, total_length_ms)
            chunk_audio = audio[start_time_ms:end_time_ms]
            
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                chunk_path = tmp.name
            
            chunk_audio.export(chunk_path, format="wav")
            
            print(f"Processando chunk {i+1}/{num_chunks} ({(start_time_ms/1000):.1f}s a {(end_time_ms/1000):.1f}s)...")
            result = model.transcribe(chunk_path)
            
            # Ajustando timestamps e gravando incrementalmente
            for segment in result["segments"]:
                adjusted_start = (start_time_ms / 1000) + segment["start"]
                adjusted_end = (start_time_ms / 1000) + segment["end"]
                
                start_str = format_timestamp(adjusted_start)
                end_str = format_timestamp(adjusted_end)
                text = segment["text"].strip()
                
                chunk_str = f"{segment_index}\n{start_str} --> {end_str}\n{text}\n\n"
                f.write(chunk_str)
                f.flush()
                print(f"Segmento {segment_index} salvo: {start_str} -> {end_str}")
                segment_index += 1
                
            os.remove(chunk_path)

def main():
    if len(sys.argv) < 2:
        print("Uso: python transcribe.py <caminho_do_audio> [caminho_saida_srt]")
        sys.exit(1)
        
    audio_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_srt = sys.argv[2]
    else:
        base_name = os.path.splitext(audio_path)[0]
        output_srt = base_name + ".srt"
        
    has_gpu = check_gpu()
    install_deps(has_gpu)
    
    if has_gpu:
        print("Executando transcrição com faster-whisper...")
        transcribe_faster_whisper(audio_path, output_srt)
    else:
        print("Executando transcrição com openai-whisper (fallback CPU)...")
        transcribe_openai_whisper(audio_path, output_srt)
        
    print(f"Transcrição finalizada. Salvo em: {output_srt}")

if __name__ == "__main__":
    main()
