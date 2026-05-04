import streamlit as st
import os
import json
import numpy as np
import tempfile
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# Configurações da Página e Dependências
# ---------------------------------------------------------
st.set_page_config(page_title="Visio-Scribe Jonathan - Prontuário Eletrônico", page_icon="🩺", layout="wide")

try:
    from faster_whisper import WhisperModel
    from langchain_ollama import OllamaLLM
except ImportError:
    st.error("Dependências faltando. Certifique-se de instalar faster-whisper e langchain-ollama.")
    st.stop()

# ---------------------------------------------------------
# Schemas e Constantes
# ---------------------------------------------------------
class ElectronicHealthRecord(BaseModel):
    queixa_principal: str = Field(description="O motivo principal da consulta")
    historia_doenca_atual: str = Field(description="Histórico detalhado da queixa")
    sintomas: list[str] = Field(description="Lista de sintomas mencionados")
    exames_solicitados: list[str] = Field(description="Exames pedidos pelo médico")
    diagnostico_hipotese: str = Field(description="Hipótese diagnóstica ou diagnóstico confirmado")
    conduta_tratamento: str = Field(description="Conduta, tratamento ou medicamentos prescritos")

MODEL_SIZE = os.getenv("WHISPER_MODEL_NAME", "small")
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
def process_audio(audio_path: str):
    with st.spinner("Ouvindo e transcrevendo..."):
        segments, _ = whisper_model.transcribe(audio_path, beam_size=5, language="pt")
        transcript = " ".join([s.text.strip() for s in segments])
    return transcript

def generate_ehr(transcript: str):
    with st.spinner("Estruturando o Prontuário Eletrônico..."):
        prompt = f"""Você é um assistente médico especialista (Visio-Scribe Jonathan).
Sua tarefa é extrair as informações da transcrição bruta e preencher um Prontuário Eletrônico (EHR) estruturado.
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
        response = llm.invoke(prompt)
        import re
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if match:
            return ElectronicHealthRecord(**json.loads(match.group(0)))
        return None

# ---------------------------------------------------------
# UI Principal
# ---------------------------------------------------------
st.title("🩺 Visio-Scribe Jonathan")
st.markdown("Gravação de consulta e geração automática de Prontuário Eletrônico (EHR).")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Entrada de Áudio")
    input_method = st.radio("Método de Entrada:", ["Gravar pelo Navegador", "Fazer Upload de Áudio"])
    
    audio_data = None
    if input_method == "Gravar pelo Navegador":
        st.info("Clique no microfone para gravar a consulta.")
        audio_data = st.audio_input("Gravar Consulta")
    else:
        audio_data = st.file_uploader("Envie o arquivo de áudio", type=["wav", "mp3", "m4a", "ogg"])

    if audio_data and st.button("Processar Consulta"):
        # Salva o áudio temporariamente
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_data.getvalue())
            tmp_path = tmp.name
            
        try:
            # Transcrição
            st.session_state.transcript = process_audio(tmp_path)
            # Estruturação
            st.session_state.ehr = generate_ehr(st.session_state.transcript)
        finally:
            os.remove(tmp_path)

with col2:
    st.subheader("Prontuário Estruturado")
    if "ehr" in st.session_state and st.session_state.ehr:
        ehr = st.session_state.ehr
        
        st.success("Prontuário gerado com sucesso!")
        st.markdown(f"**Queixa Principal:** {ehr.queixa_principal}")
        st.markdown(f"**HDA:** {ehr.historia_doenca_atual}")
        
        st.markdown("**Sintomas:**")
        for s in ehr.sintomas:
            st.markdown(f"- {s}")
            
        st.markdown("**Exames Solicitados:**")
        for e in ehr.exames_solicitados:
            st.markdown(f"- {e}")
            
        st.markdown(f"**Hipótese Diagnóstica:** {ehr.diagnostico_hipotese}")
        st.markdown(f"**Conduta / Tratamento:** {ehr.conduta_tratamento}")
        
        with st.expander("Ver Transcrição Bruta"):
            st.write(st.session_state.transcript)
    else:
        st.caption("O prontuário aparecerá aqui após o processamento.")
