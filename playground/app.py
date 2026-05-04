import streamlit as st
import os
import warnings

# Silencia os warnings incômodos do transformers no terminal
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")
warnings.filterwarnings("ignore")

import json
import tempfile
import glob
import re
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# ---------------------------------------------------------
# Dependências e Verificações
# ---------------------------------------------------------
try:
    from faster_whisper import WhisperModel
    import ollama
    from langchain_ollama import OllamaLLM, OllamaEmbeddings
    from langchain_chroma import Chroma
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import TextLoader
    from langchain_core.prompts import PromptTemplate
    from langchain_community.document_transformers import LongContextReorder
except ImportError:
    st.error("Dependências faltando. Verifique se instalou faster-whisper, langchain-ollama, chromadb, etc.")
    st.stop()

# ---------------------------------------------------------
# Configurações Globais (Playground Rules)
# ---------------------------------------------------------
class Settings(BaseSettings):
    MODEL_NAME: str = Field(default="gemma4:e4b", validation_alias="LLM_MODEL_PATH")
    EMBEDDING_MODEL_NAME: str = "nomic-embed-text"
    WHISPER_MODEL: str = "small"
    DEVICE: str = "cpu" # Força CPU para evitar conflito de VRAM com Ollama
    COMPUTE_TYPE: str = "int8"
    
    _BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
    
    def get_db_path(self, kb_name: str) -> str:
        # Mudamos o prefixo para evitar conflitos com FDs fantasmas de processos anteriores
        return os.path.join(self._BASE_DIR, f"vector_db_{kb_name}")
        
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

@st.cache_resource
def get_vector_db(kb_name: str, force_reindex: bool = False):
    db_path = settings.get_db_path(kb_name)
    docs_dir = settings.get_docs_path(kb_name)
    embeddings = get_embeddings()
    
    os.makedirs(db_path, exist_ok=True)
    
    # Verifica se a base existe e não está vazia
    exists = os.path.exists(os.path.join(db_path, "chroma.sqlite3"))
    if exists and not force_reindex:
        try:
            db = Chroma(persist_directory=db_path, embedding_function=embeddings)
            if db._collection.count() > 0:
                return db
        except Exception as e:
            st.error(f"Erro ao acessar banco {kb_name}: {e}")

    # Reindexação
    if os.path.exists(db_path):
        import shutil
        shutil.rmtree(db_path, ignore_errors=True)
    os.makedirs(db_path, exist_ok=True)
    
    files = glob.glob(os.path.join(docs_dir, "**/*.md"), recursive=True)
    documentos = []
    for f in files:
        try:
            loader = TextLoader(f, encoding="utf-8")
            documentos.extend(loader.load())
        except Exception as e:
            st.warning(f"Ignorando arquivo {f}: {e}")
            
    if not documentos:
        return None
        
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)
    chunks = splitter.split_documents(documentos)
    
    try:
        db = Chroma.from_documents(chunks, embeddings, persist_directory=db_path)
        return db
    except Exception as e:
        st.error(f"Falha ao criar banco de dados (provavelmente permissão): {e}")
        return None

# ---------------------------------------------------------
# Componentes: HERMES (RAG)
# ---------------------------------------------------------
class HermesService:
    def __init__(self, kb_name: str):
        self.kb_name = kb_name
        self.llm = get_llm()
        self.embeddings = get_embeddings()
        
        # Carrega o banco via cache global
        self.db = get_vector_db(kb_name)
        
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

    def rewrite_query(self, query: str):
        """Usa o LLM para tornar a busca mais rica semanticamente."""
        try:
            prompt = f"Converta esta pergunta clínica em 3 a 5 palavras-chave técnicas em português para busca em protocolos médicos. Retorne APENAS as palavras-chave separadas por espaço. Pergunta: {query}"
            rewritten = self.llm.invoke(prompt).strip()
            return re.sub(r'["\']', '', rewritten).split('\n')[0]
        except:
            return query

    def ask(self, query: str):
        if not self.db:
            return "Erro: Base de conhecimento não disponível ou vazia. Por favor, reindexe.", []
        
        search_query = self.rewrite_query(query)
        
        # Busca principal
        docs = self.db.as_retriever(search_kwargs={"k": 5}).invoke(search_query)
        
        # Fallback para busca literal
        if not docs:
            docs = self.db.as_retriever(search_kwargs={"k": 5}).invoke(query)
            
        reorder = LongContextReorder()
        docs = reorder.transform_documents(docs)
        
        contexto = "\n\n".join([f"[FONTE: {os.path.basename(d.metadata.get('source', 'Desconhecida'))}]\n{d.page_content}" for d in docs])
        
        with st.expander("🔍 Debug de Recuperação"):
            st.write(f"**Query Original:** {query}")
            st.write(f"**Query Otimizada:** {search_query}")
            st.write(f"**Documentos Encontrados:** {len(docs)}")
            
        chain = self.prompt | self.llm
        return chain.invoke({"contexto": contexto, "pergunta": query}), docs

# ---------------------------------------------------------
# Componentes: JONATHAN (Transcription)
# ---------------------------------------------------------
def transcribe_audio(file_path):
    model = get_whisper()
    segments, _ = model.transcribe(file_path, beam_size=5, language="pt")
    return " ".join([s.text.strip() for s in segments])

# ---------------------------------------------------------
# UI STREAMLIT
# ---------------------------------------------------------
st.set_page_config(page_title="EYE.AI Dashboard", layout="wide", page_icon="👁️")

st.sidebar.title("👁️ EYE.AI Dashboard")
service = st.sidebar.radio("Navegação:", ["🛡️ Hermes (Chat Clínico)", "🩺 Jonathan (Prontuário)"])

# --- HERMES ---
if service == "🛡️ Hermes (Chat Clínico)":
    st.title("🛡️ Visio-Chat Hermes")
    
    # Gerenciamento de Estado do RAG
    if "hermes_kb" not in st.session_state:
        st.session_state.hermes_kb = "strabismus"
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Painel Principal do Hermes (Controles)
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1.5])
        
        db_path = settings.get_db_path(st.session_state.hermes_kb)
        db_exists = os.path.exists(db_path)
        
        with col1:
            novo_kb = st.selectbox("Base de Conhecimento (RAG):", ["strabismus", "mock"], index=["strabismus", "mock"].index(st.session_state.hermes_kb))
            # Se o usuário trocou o KB, limpa o chat e avisa que o RAG atualizou
            if novo_kb != st.session_state.hermes_kb:
                st.session_state.hermes_kb = novo_kb
                st.session_state.messages = []
                st.toast(f"Base RAG alterada para '{novo_kb}' com sucesso!", icon="🔄")
                st.rerun()
                
        with col2:
            st.write("") # Alinhamento
            if st.button("♻️ Limpar Chat", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
                
        with col3:
            st.write("") # Alinhamento
            if st.button("🔄 Reindexar Base", use_container_width=True):
                # Limpa o cache para forçar reindexação
                get_vector_db.clear()
                with st.spinner(f"Reindexando documentos em {st.session_state.hermes_kb}..."):
                    db = get_vector_db(st.session_state.hermes_kb, force_reindex=True)
                if db:
                    st.success(f"Base '{st.session_state.hermes_kb}' reindexada com sucesso!")
                st.session_state.messages = []
                st.rerun()
                
        with col4:
            st.write("") # Alinhamento
            if db_exists:
                st.success(f"🟢 RAG Carregado ({st.session_state.hermes_kb})")
            else:
                st.error("🔴 RAG Não Inicializado")

    # Instancia o serviço ativo
    hermes = HermesService(st.session_state.hermes_kb)
    
    # Área do Chat
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
        
    if prompt := st.chat_input("Insira sua dúvida clínica aqui..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Consultando protocolos..."):
                res, docs = hermes.ask(prompt)
            st.markdown(res)
            with st.expander("📄 Fontes Consultadas"):
                for d in docs: st.caption(f"Arquivo: {os.path.basename(d.metadata.get('source', ''))}")
        st.session_state.messages.append({"role": "assistant", "content": res})

# --- JONATHAN ---
elif service == "🩺 Jonathan (Prontuário)":
    st.title("🩺 Visio-Scribe Jonathan")
    st.markdown("Gravação de consulta e geração automática de Prontuário Eletrônico.")
    
    col_input, col_out = st.columns(2)
    
    with col_input:
        audio_data = st.audio_input("Grave a consulta (ou use o ícone de pasta para Upload)")
        if audio_data:
            st.info("Áudio capturado. Clique no botão abaixo para processar.")
            if st.button("🚀 GERAR PRONTUÁRIO ESTRUTURADO", type="primary", use_container_width=True):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(audio_data.getvalue())
                    path = tmp.name
                    
                with st.status("Processando consulta...", expanded=True) as status:
                    st.write("Transcrevendo áudio (CPU)...")
                    text = transcribe_audio(path)
                    os.remove(path)
                    
                    st.write("Estruturando com IA (Gemma 3)...")
                    prompt = f"Extraia um Prontuário JSON desta consulta: {text}. Use a estrutura: queixa_principal, historia_doenca_atual, sintomas[], exames_solicitados[], diagnostico_hipotese, conduta_tratamento."
                    res = get_llm().invoke(prompt)
                    status.update(label="Processamento concluído!", state="complete", expanded=False)
                    
                match = re.search(r'\{.*\}', res, re.DOTALL)
                if match:
                    ehr = ElectronicHealthRecord(**json.loads(match.group(0)))
                    st.session_state.last_ehr = ehr.model_dump()
                    st.session_state.last_transcript = text
                    st.rerun()
            
            if "last_transcript" in st.session_state:
                st.text_area("Transcrição Bruta:", st.session_state.last_transcript, height=150)
                        
    with col_out:
        if "last_ehr" in st.session_state:
            st.success("✅ Prontuário Gerado")
            st.json(st.session_state.last_ehr)
        else:
            st.info("O prontuário aparecerá aqui.")
