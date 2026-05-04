import streamlit as st
import os
import json
import numpy as np
import tempfile
import subprocess
import glob
import re
from typing import List, Optional
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings

# ---------------------------------------------------------
# Dependências e Verificações
# ---------------------------------------------------------
try:
    from faster_whisper import WhisperModel
    import yt_dlp
    import ollama
    from langchain_ollama import OllamaLLM, OllamaEmbeddings
    from langchain_chroma import Chroma
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import TextLoader
    from langchain_core.prompts import PromptTemplate
    from langchain_community.document_transformers import LongContextReorder
except ImportError:
    st.error("Dependências faltando. Verifique se instalou faster-whisper, yt-dlp, langchain-ollama, chromadb, etc.")
    st.stop()

# ---------------------------------------------------------
# Configurações Globais (Playground Rules)
# ---------------------------------------------------------
class Settings(BaseSettings):
    MODEL_NAME: str = "gemma3:4b-it-qat"
    EMBEDDING_MODEL_NAME: str = "nomic-embed-text"
    WHISPER_MODEL: str = "small"
    DEVICE: str = "cuda"
    COMPUTE_TYPE: str = "float16"
    
    _BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    
    def get_db_path(self, kb_name: str) -> str:
        return os.path.join(self._BASE_DIR, f"chroma_db_{kb_name}")
        
    def get_docs_path(self, kb_name: str) -> str:
        return os.path.join(os.path.dirname(self._BASE_DIR), "docs", "rag", kb_name)

settings = Settings()

# ---------------------------------------------------------
# Schemas Pydantic
# ---------------------------------------------------------
class ElectronicHealthRecord(BaseModel):
    queixa_principal: str = Field(description="O motivo principal da consulta")
    historia_doenca_atual: str = Field(description="Histórico detalhado da queixa")
    sintomas: list[str] = Field(description="Lista de sintomas mencionados")
    exames_solicitados: list[str] = Field(description="Exames pedidos pelo médico")
    diagnostico_hipotese: str = Field(description="Hipótese diagnóstica ou diagnóstico confirmado")
    conduta_tratamento: str = Field(description="Conduta, tratamento ou medicamentos prescritos")

class Conceito(BaseModel):
    tema: str = Field(description="O tema ou conceito principal abordado")
    explicacao: str = Field(description="A explicação ou os pontos-chave sobre esse tema")

class YouTubeSummary(BaseModel):
    titulo_sugerido: str = Field(description="Um título adequado que resuma o conteúdo do vídeo")
    resumo_geral: str = Field(description="Um parágrafo conciso resumindo o assunto geral")
    conceitos_principais: list[Conceito] = Field(description="Lista dos conceitos ou tópicos principais organizados")
    conclusao_ou_insights: str = Field(description="A conclusão, próximos passos ou insights finais do vídeo")

# ---------------------------------------------------------
# Cache de Modelos e Motores
# ---------------------------------------------------------
@st.cache_resource
def get_whisper():
    return WhisperModel(settings.WHISPER_MODEL, device=settings.DEVICE, compute_type=settings.COMPUTE_TYPE)

@st.cache_resource
def get_llm():
    return OllamaLLM(model=settings.MODEL_NAME, temperature=0.0)

@st.cache_resource
def get_embeddings():
    return OllamaEmbeddings(model=settings.EMBEDDING_MODEL_NAME)

# ---------------------------------------------------------
# Componentes: HERMES (RAG)
# ---------------------------------------------------------
class HermesService:
    def __init__(self, kb_name: str):
        self.kb_name = kb_name
        self.embeddings = get_embeddings()
        self.llm = get_llm()
        self.db_path = settings.get_db_path(kb_name)
        self.docs_dir = settings.get_docs_path(kb_name)
        self.db = None
        self.prompt = PromptTemplate.from_template("""
            Você é o Visio-Chat Hermes, um sistema de suporte à decisão clínica com RIGOR ABSOLUTO.
            Sua única fonte de verdade é o CONTEXTO INSTITUCIONAL fornecido abaixo.
            REGRAS:
            1. Se não encontrar no contexto, diga que não encontrou nos protocolos.
            2. Cite o nome da [FONTE] na resposta.
            CONTEXTO:
            {contexto}
            PERGUNTA:
            {pergunta}
            """)

    def load_db(self):
        if os.path.exists(self.db_path):
            self.db = Chroma(persist_directory=self.db_path, embedding_function=self.embeddings)
        else:
            st.warning(f"Banco {self.kb_name} não encontrado. Criando novo a partir de {self.docs_dir}...")
            files = glob.glob(os.path.join(self.docs_dir, "**/*.md"), recursive=True)
            documentos = []
            for f in files:
                loader = TextLoader(f, encoding="utf-8")
                documentos.extend(loader.load())
            splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
            chunks = splitter.split_documents(documentos)
            self.db = Chroma.from_documents(chunks, self.embeddings, persist_directory=self.db_path)
        return self.db

    def ask(self, query: str):
        if not self.db: self.load_db()
        docs = self.db.as_retriever(search_kwargs={"k": 5}).invoke(query)
        reorder = LongContextReorder()
        docs = reorder.transform_documents(docs)
        contexto = "\n\n".join([f"[FONTE: {os.path.basename(d.metadata.get('source', 'Desconhecida'))}]\n{d.page_content}" for d in docs])
        chain = self.prompt | self.llm
        return chain.invoke({"contexto": contexto, "pergunta": query}), docs

# ---------------------------------------------------------
# Componentes: JONATHAN (Transcription & Structuring)
# ---------------------------------------------------------
def transcribe_audio(file_path):
    model = get_whisper()
    segments, _ = model.transcribe(file_path, beam_size=5, language="pt")
    return " ".join([s.text.strip() for s in segments])

def download_yt(url, path):
    ydl_opts = {
        'format': 'bestaudio/best', 'outtmpl': path.replace(".wav", ""),
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '192'}],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
    return path

# ---------------------------------------------------------
# UI STREAMLIT
# ---------------------------------------------------------
st.set_page_config(page_title="EYE.AI Dashboard", layout="wide", page_icon="👁️")

st.sidebar.title("👁️ EYE.AI Dashboard")
service = st.sidebar.selectbox("Selecione o Serviço:", ["Hermes (Chat Clínico)", "Jonathan v2 (Scribe/EHR)", "Jonathan v3 (YouTube Analyser)"])

# --- HERMES ---
if service == "Hermes (Chat Clínico)":
    st.title("🛡️ Visio-Chat Hermes")
    kb = st.selectbox("Base de Conhecimento:", ["strabismus", "mock"])
    hermes = HermesService(kb)
    
    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
        
    if prompt := st.chat_input("Dúvida clínica..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            res, docs = hermes.ask(prompt)
            st.markdown(res)
            with st.expander("Fontes"):
                for d in docs: st.caption(f"Arquivo: {os.path.basename(d.metadata.get('source', ''))}")
        st.session_state.messages.append({"role": "assistant", "content": res})

# --- JONATHAN v2 ---
elif service == "Jonathan v2 (Scribe/EHR)":
    st.title("🩺 Visio-Scribe Jonathan v2")
    audio_data = st.audio_input("Grave a consulta ou upload")
    if audio_data:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_data.getvalue())
            path = tmp.name
        text = transcribe_audio(path)
        os.remove(path)
        st.text_area("Transcrição Bruta:", text, height=150)
        if st.button("Gerar Prontuário"):
            prompt = f"Extraia um Prontuário JSON desta consulta: {text}. Use a estrutura: queixa_principal, historia_doenca_atual, sintomas[], exames_solicitados[], diagnostico_hipotese, conduta_tratamento."
            res = get_llm().invoke(prompt)
            match = re.search(r'\{.*\}', res, re.DOTALL)
            if match:
                ehr = ElectronicHealthRecord(**json.loads(match.group(0)))
                st.success("Prontuário Estruturado:")
                st.json(ehr.model_dump())

# --- JONATHAN v3 ---
elif service == "Jonathan v3 (YouTube Analyser)":
    st.title("📺 Visio-Scribe Jonathan v3")
    url = st.text_input("URL do YouTube:")
    if url and st.button("Analisar"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            path = download_yt(url, tmp.name)
        text = transcribe_audio(path)
        os.remove(path)
        st.text_area("Transcrição:", text, height=150)
        prompt = f"Analise esta transcrição e gere um JSON com titulo_sugerido, resumo_geral, conceitos_principais[] (tema, explicacao), conclusao_ou_insights: {text}"
        res = get_llm().invoke(prompt)
        match = re.search(r'\{.*\}', res, re.DOTALL)
        if match:
            st.json(json.loads(match.group(0)))
