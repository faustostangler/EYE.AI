import streamlit as st
import os
import json
import tempfile
import subprocess
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# Configurações da Página e Dependências
# ---------------------------------------------------------
st.set_page_config(page_title="Jonathan v3 - Analisador de YouTube", page_icon="📺", layout="wide")

try:
    from faster_whisper import WhisperModel
    from langchain_ollama import OllamaLLM
    import yt_dlp
except ImportError:
    st.error("Dependências faltando. Certifique-se de instalar faster-whisper, langchain-ollama e yt-dlp.")
    st.stop()

# ---------------------------------------------------------
# Schemas e Constantes
# ---------------------------------------------------------
class Conceito(BaseModel):
    tema: str = Field(description="O tema ou conceito principal abordado")
    explicacao: str = Field(description="A explicação ou os pontos-chave sobre esse tema")

class YouTubeSummary(BaseModel):
    titulo_sugerido: str = Field(description="Um título adequado que resuma o conteúdo do vídeo")
    resumo_geral: str = Field(description="Um parágrafo conciso resumindo o assunto geral")
    conceitos_principais: list[Conceito] = Field(description="Lista dos conceitos ou tópicos principais organizados")
    conclusao_ou_insights: str = Field(description="A conclusão, próximos passos ou insights finais do vídeo")

MODEL_SIZE = "small"
DEVICE = "cuda"
COMPUTE_TYPE = "float16"
LLM_MODEL = os.getenv("LLM_MODEL_PATH", "gemma4:e4b")

# ---------------------------------------------------------
# Cache de Modelos
# ---------------------------------------------------------
@st.cache_resource(show_spinner="Carregando modelo Whisper na GPU...")
def load_whisper():
    return WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

@st.cache_resource(show_spinner="Conectando ao Ollama...")
def load_llm():
    return OllamaLLM(model=LLM_MODEL, temperature=0.0)

whisper_model = load_whisper()
llm = load_llm()

# ---------------------------------------------------------
# Funções Core
# ---------------------------------------------------------
def download_youtube_audio(url: str, output_path: str):
    with st.spinner("Baixando áudio do YouTube..."):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path.replace(".wav", ""),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    return output_path

def process_audio(audio_path: str):
    with st.spinner("Transcrevendo o áudio..."):
        segments, _ = whisper_model.transcribe(audio_path, beam_size=5, language="pt")
        transcript = " ".join([s.text.strip() for s in segments])
    return transcript

def generate_summary(transcript: str):
    with st.spinner("Organizando os conceitos com LLM..."):
        prompt = f"""Você é o Jonathan v3, um analista especializado em estruturação de conhecimento.
Sua tarefa é extrair as informações da transcrição bruta e gerar um documento organizado.

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
        response = llm.invoke(prompt)
        import re
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            return YouTubeSummary(**json.loads(match.group(0)))
        return None

# ---------------------------------------------------------
# UI Principal
# ---------------------------------------------------------
st.title("📺 Visio-Scribe Jonathan v3")
st.markdown("Extração e estruturação automática de conceitos a partir de vídeos do YouTube.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Entrada de Dados")
    url = st.text_input("Cole o link do vídeo do YouTube aqui:", placeholder="https://www.youtube.com/watch?v=...")
    
    if st.button("Analisar Vídeo") and url:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            audio_path = tmp.name
            
        try:
            # 1. Download
            download_youtube_audio(url, audio_path)
            
            # 2. Transcrição
            if os.path.exists(audio_path):
                st.session_state.yt_transcript = process_audio(audio_path)
                
                # 3. Estruturação
                st.session_state.yt_summary = generate_summary(st.session_state.yt_transcript)
            else:
                st.error("Erro ao fazer o download do áudio.")
        except Exception as e:
            st.error(f"Erro durante o processamento: {e}")
        finally:
            if os.path.exists(audio_path):
                os.remove(audio_path)

with col2:
    st.subheader("Documento Estruturado")
    if "yt_summary" in st.session_state and st.session_state.yt_summary:
        summary = st.session_state.yt_summary
        
        st.success("Análise concluída!")
        st.markdown(f"### {summary.titulo_sugerido}")
        st.markdown(f"**Resumo:** {summary.resumo_geral}")
        
        st.markdown("#### 📌 Conceitos Principais:")
        for c in summary.conceitos_principais:
            st.markdown(f"- **{c.tema}**: {c.explicacao}")
            
        st.info(f"💡 **Insights Finais:**\n{summary.conclusao_ou_insights}")
        
        with st.expander("Ver Transcrição Bruta"):
            st.write(st.session_state.yt_transcript)
    else:
        st.caption("O documento organizado aparecerá aqui após o processamento.")
