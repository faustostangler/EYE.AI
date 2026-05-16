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
import time
import pandas as pd
from pydantic import BaseModel, Field, field_validator
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
    EMBEDDING_MODEL_NAME: str = Field(default="nomic-embed-text", validation_alias="EMBEDDING_MODEL_NAME")
    WHISPER_MODEL: str = Field(default="small", validation_alias="WHISPER_MODEL_NAME")
    DEVICE: str = "cpu" # Força CPU para o Whisper para evitar conflito de VRAM com Ollama
    COMPUTE_TYPE: str = "int8"
    OLLAMA_HOST: str = Field(default="http://localhost:11434", validation_alias="OLLAMA_HOST")
    NUM_GPU: int = Field(default=50, validation_alias="LLM_GPU_LAYERS")
    
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
    queixa_principal: str = Field(default="", description="O motivo principal da consulta")
    historia_doenca_atual: str = Field(default="", description="Histórico detalhado da queixa")
    sintomas: list[str] = Field(default_factory=list, description="Lista de sintomas mencionados")
    exames_solicitados: list[str] = Field(default_factory=list, description="Exames pedidos pelo médico")
    diagnostico_hipotese: str = Field(default="", description="Hipótese diagnóstica ou diagnóstico confirmado")
    conduta_tratamento: str = Field(default="", description="Conduta, tratamento ou medicamentos prescritos")
    especialidade: str = Field(default="mock", description="Especialidade do caso: 'strabismus' ou 'mock'")

    @field_validator("queixa_principal", "historia_doenca_atual", "diagnostico_hipotese", "conduta_tratamento", "especialidade", mode="before")
    @classmethod
    def cast_to_string(cls, v):
        if v is None:
            return ""
        if isinstance(v, (list, tuple)):
            return " ".join(str(item) for item in v)
        if isinstance(v, dict):
            # Tenta extrair um campo de texto principal se o LLM alucinou um objeto
            return v.get("descricao") or v.get("texto") or json.dumps(v, ensure_ascii=False)
        return str(v)

    @field_validator("sintomas", "exames_solicitados", mode="before")
    @classmethod
    def cast_to_list(cls, v):
        if v is None:
            return []
        if not isinstance(v, list):
            v = [v]
        
        processed = []
        for item in v:
            if isinstance(item, dict):
                # Extração defensiva: tenta campos comuns, senão serializa para não perder info
                text = item.get("nome") or item.get("sintoma") or item.get("exame") or json.dumps(item, ensure_ascii=False)
                processed.append(str(text))
            elif item is not None:
                processed.append(str(item))
        return processed


# ---------------------------------------------------------
# Cache de Modelos e Motores
# ---------------------------------------------------------
@st.cache_resource
def get_whisper():
    return WhisperModel(settings.WHISPER_MODEL, device=settings.DEVICE, compute_type=settings.COMPUTE_TYPE)

@st.cache_resource
def get_llm(model_name: str = None):
    target_model = model_name or settings.MODEL_NAME
    return OllamaLLM(
        model=target_model, 
        base_url=settings.OLLAMA_HOST,
        num_gpu=settings.NUM_GPU,
        temperature=0.0
    )

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
        
    splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=300)
    chunks = splitter.split_documents(documentos)
    
    try:
        db = Chroma.from_documents(chunks, embeddings, persist_directory=db_path)
        return db
    except Exception as e:
        st.error(f"Falha ao criar banco de dados (provavelmente permissão): {e}")
        return None

# ---------------------------------------------------------
# Componentes: VISIO-CHAT HERMES (RAG)
# ---------------------------------------------------------
class VisioChatHermesService:
    def __init__(self, kb_name: str):
        self.kb_name = kb_name
        # Carrega o banco via cache global
        self.db = get_vector_db(kb_name)
        
        # O LLM agora é carregado via settings.MODEL_NAME por padrão no RAG
        # mas no Playground Visio-Scribe ele pode ser dinâmico.
        self.llm = get_llm(settings.MODEL_NAME)
        
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

    def ask(self, query: str, search_query: str = None):
        if not self.db:
            return "Erro: Base de conhecimento não disponível ou vazia. Por favor, reindexe.", []
        
        if not search_query:
            search_query = self.rewrite_query(query)
        
        # Busca principal
        docs = self.db.as_retriever(search_kwargs={"k": 15}).invoke(search_query)
        
        # Fallback para busca literal
        if not docs:
            docs = self.db.as_retriever(search_kwargs={"k": 15}).invoke(query)
            
        reorder = LongContextReorder()
        docs = reorder.transform_documents(docs)
        
        contexto = "\n\n".join([f"[FONTE: {os.path.basename(d.metadata.get('source', 'Desconhecida'))}]\n{d.page_content}" for d in docs])
        
        with st.expander("🔍 Debug de Recuperação"):
            st.write(f"**Query Original:** {query}")
            st.write(f"**Query Otimizada:** {search_query}")
            st.write(f"**Snippets Encontrados:** {len(docs)}")
            
        chain = self.prompt | self.llm
        return chain.invoke({"contexto": contexto, "pergunta": query}), docs

# ---------------------------------------------------------
# Componentes: VISIO-SCRIBE JONATHAN (Transcription)
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
service = st.sidebar.radio("Navegação:", ["🛡️ Visio-Chat Hermes", "🩺 Visio-Scribe Jonathan"], index=1)

# --- VISIO-CHAT HERMES ---
if service == "🛡️ Visio-Chat Hermes":
    st.title("🛡️ Visio-Chat Hermes")
    
    # Gerenciamento de Estado do RAG
    if "visio_chat_hermes_kb" not in st.session_state:
        st.session_state.visio_chat_hermes_kb = "strabismus"
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Painel Principal do Visio-Chat Hermes (Controles)
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1.5])
        
        db_path = settings.get_db_path(st.session_state.visio_chat_hermes_kb)
        db_exists = os.path.exists(db_path)
        
        with col1:
            novo_kb = st.selectbox("Base de Conhecimento (RAG):", ["strabismus", "mock"], index=["strabismus", "mock"].index(st.session_state.visio_chat_hermes_kb))
            # Se o usuário trocou o KB, limpa o chat e avisa que o RAG atualizou
            if novo_kb != st.session_state.visio_chat_hermes_kb:
                st.session_state.visio_chat_hermes_kb = novo_kb
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
                with st.spinner(f"Reindexando documentos em {st.session_state.visio_chat_hermes_kb}..."):
                    db = get_vector_db(st.session_state.visio_chat_hermes_kb, force_reindex=True)
                if db:
                    st.success(f"Base '{st.session_state.visio_chat_hermes_kb}' reindexada com sucesso!")
                st.session_state.messages = []
                st.rerun()
                
        with col4:
            st.write("") # Alinhamento
            if db_exists:
                st.success(f"🟢 RAG Carregado ({st.session_state.visio_chat_hermes_kb})")
            else:
                st.error("🔴 RAG Não Inicializado")

    # Instancia o serviço ativo
    visio_chat_hermes = VisioChatHermesService(st.session_state.visio_chat_hermes_kb)
    
    # Área do Chat
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])
        
    if prompt := st.chat_input("Insira sua dúvida clínica aqui..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Consultando protocolos..."):
                res, docs = visio_chat_hermes.ask(prompt)
            st.markdown(res)
            with st.expander("📄 Fontes e Contextos Consultados"):
                for d in docs:
                    st.markdown(f"**Fonte:** `{os.path.basename(d.metadata.get('source', ''))}`")
                    st.caption(d.page_content)
                    st.divider()
        st.session_state.messages.append({"role": "assistant", "content": res})

    # --- VISIO-SCRIBE JONATHAN ---
elif service == "🩺 Visio-Scribe Jonathan":
    st.title("🩺 Visio-Scribe Jonathan")
    st.markdown("Gravação de consulta e geração automática de Prontuário Eletrônico.")
    
    audio_data = st.audio_input("Grave a consulta (ou use o ícone de pasta para Upload)")
    if audio_data:
        audio_id = hash(audio_data.getvalue())
        # Se for áudio novo, limpa o estado anterior
        if st.session_state.get("last_audio_id") != audio_id:
            st.session_state.last_audio_id = audio_id
            keys_to_clear = ["last_transcript", "last_ehr", "last_inference_error", "last_visio_chat_hermes_opinion", "last_visio_chat_hermes_kb", "last_visio_chat_hermes_docs", "inference_history"]
            for k in keys_to_clear:
                if k in st.session_state: del st.session_state[k]
            st.session_state.trigger_jonathan_inference = True


        # Etapa 1: Transcrição do Áudio
        with st.expander("🎧 Transcrição do Áudio", expanded=("last_transcript" not in st.session_state)):
            if "last_transcript" not in st.session_state:
                with st.spinner("🎧 Transcrevendo áudio..."):
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                        tmp.write(audio_data.getvalue())
                        path = tmp.name
                    text = transcribe_audio(path)
                    os.remove(path)
                    st.session_state.last_transcript = text
            st.write(st.session_state.last_transcript)

        # Etapa 2: Configuração de Inferência & Benchmarking
        if "last_transcript" in st.session_state:
            with st.expander("⚙️ Configuração de Inferência & Benchmarking", expanded=True):
                # Descoberta de modelos e fallback para modelos rápidos (SOTA)
                preferred_fast_models = [
                    "phi3:mini", "qwen3.5:4b", "gemma4:e4b", "gemma3:270m", 
                    "gemma3:4b-it-qat", "gemma4:e2b", "gemma:2b", 
                    "llama3:latest", "deepseek-r1:7b"
                ]
                try:
                    models_info = ollama.list()
                    installed_models = [m['name'] for m in models_info.get('models', []) if 'embed' not in m['name']]
                    # Mostra instalados primeiro, seguidos pelos preferidos que talvez não estejam na lista
                    available_models = sorted(list(set(installed_models + preferred_fast_models)))
                except:
                    available_models = preferred_fast_models
                
                # Garantir que o modelo padrão do settings está na lista
                if settings.MODEL_NAME not in available_models:
                    available_models.append(settings.MODEL_NAME)

                col_mod, col_spacer = st.columns([1, 2])
                
                with col_mod:
                    def trigger_new_inference():
                        st.session_state.trigger_jonathan_inference = True
                        if "last_ehr" in st.session_state: del st.session_state.last_ehr
                        if "last_inference_error" in st.session_state: del st.session_state.last_inference_error

                    current_model = st.selectbox(
                        "Selecionar LLM para Extração:", 
                        available_models, 
                        index=available_models.index(settings.MODEL_NAME) if settings.MODEL_NAME in available_models else 0,
                        key="selected_jonathan_model",
                        on_change=trigger_new_inference
                    )



                # Histórico de Performance posicionado ABAIXO
                st.write("---")
                st.write("**📊 Benchmarking de Inferência (Cumulativo)**")
                if "inference_history" not in st.session_state:
                    st.session_state.inference_history = []
                
                if st.session_state.inference_history:
                    # Renderiza tudo em um único bloco HTML para remover o padding entre linhas do Streamlit
                    history_html = "".join([
                        f"<div style='font-size: 0.85rem; line-height: 1.2; margin-bottom: 2px;'>"
                        f"{e['Modelo']} · <b>{e['Tempo (s)']}</b> · {e['Status']}</div>" 
                        for e in st.session_state.inference_history
                    ])
                    st.markdown(history_html, unsafe_allow_html=True)

                else:
                    st.info("Aguardando a primeira inferência para registrar performance.")





        # Etapa 3: Prontuário Estruturado
        should_run = st.session_state.get("trigger_jonathan_inference", False) and "last_transcript" in st.session_state
        
        with st.expander("📝 Prontuário Estruturado (Inferência)", expanded=(should_run or "last_ehr" in st.session_state or "last_inference_error" in st.session_state)):
            if should_run:
                # Consome o trigger para evitar loop
                st.session_state.trigger_jonathan_inference = False
                
                # Limpeza preventiva de estados subsequentes

                for k in ["last_visio_chat_hermes_opinion", "last_visio_chat_hermes_kb", "last_visio_chat_hermes_docs"]:
                    if k in st.session_state: del st.session_state[k]
                
                with st.spinner(f"📝 Organizando informações com {st.session_state.get('selected_jonathan_model', settings.MODEL_NAME)}..."):
                    active_model = st.session_state.get("selected_jonathan_model", settings.MODEL_NAME)
                    start_time = time.perf_counter()
                    
                    try:
                        # Prompt mais rigoroso para forçar JSON puro
                        prompt = (
                            f"Instrução: Extraia as informações clínicas da transcrição abaixo para o formato JSON.\n"
                            f"Estrutura esperada: queixa_principal, historia_doenca_atual, sintomas (lista), exames_solicitados (lista), diagnostico_hipotese, conduta_tratamento e especialidade ('strabismus' ou 'mock').\n"
                            f"IMPORTANTE: Retorne APENAS o objeto JSON. Não adicione comentários, introduções ou blocos de código markdown.\n\n"
                            f"Transcrição: {st.session_state.last_transcript}"
                        )
                        
                        # Chamada do LLM
                        res = get_llm(active_model).invoke(prompt).strip()
                        duration = time.perf_counter() - start_time
                        
                        # Limpeza defensiva do output (remove blocos de código se existirem)
                        json_str = res
                        if "```json" in json_str:
                            json_str = json_str.split("```json")[1].split("```")[0]
                        elif "```" in json_str:
                            json_str = json_str.split("```")[1].split("```")[0]
                            
                        # Tenta encontrar o primeiro { e o último } caso ainda haja texto em volta
                        match = re.search(r'(\{.*\})', json_str, re.DOTALL)
                        if match:
                            json_payload = match.group(1)
                            data = json.loads(json_payload)
                            ehr = ElectronicHealthRecord(**data)
                            st.session_state.last_ehr = ehr.model_dump()
                            st.session_state.temp_data = data
                            
                            st.session_state.inference_history.append({
                                "Modelo": active_model,
                                "Tempo (s)": f"{duration:.2f}s",
                                "Status": "✅ Sucesso"
                            })
                        else:
                            # Se falhou o regex, tenta dar o parse no que sobrou
                            data = json.loads(json_str)
                            ehr = ElectronicHealthRecord(**data)
                            st.session_state.last_ehr = ehr.model_dump()
                            st.session_state.temp_data = data
                            st.session_state.inference_history.append({
                                "Modelo": active_model, "Tempo (s)": f"{duration:.2f}s", "Status": "✅ Sucesso"
                            })
                    except Exception as e:
                        duration = time.perf_counter() - start_time
                        # Se ainda assim falhou o JSON, registra o erro específico
                        error_type = "Erro JSON" if isinstance(e, (json.JSONDecodeError, ValueError)) else type(e).__name__
                        st.session_state.inference_history.append({
                            "Modelo": active_model,
                            "Tempo (s)": f"{duration:.2f}s",
                            "Status": f"❌ {error_type}"
                        })
                        st.session_state.last_inference_error = f"**Falha na Extração ({error_type}):**\n{e}\n\n**Resposta Bruta do LLM:**\n```text\n{res if 'res' in locals() else 'Nenhuma resposta gerada'}\n```"

                    
                    st.rerun() # Força atualização da UI para mostrar o histórico imediatamente

            
            if "last_ehr" in st.session_state:
                st.subheader("📋 Prontuário Gerado")
                st.json(st.session_state.last_ehr)
            elif "last_inference_error" in st.session_state:
                st.subheader("⚠️ Erro de Inferência")
                st.error(st.session_state.last_inference_error)

        # Etapa 3: Consulta ao Especialista
        with st.expander("🗣️ Consulta ao Preceptor (Visio-Chat Hermes)", expanded=("last_visio_chat_hermes_opinion" not in st.session_state and "last_ehr" in st.session_state)):
            if "last_visio_chat_hermes_opinion" not in st.session_state and "last_ehr" in st.session_state:
                # Limpeza preventiva do parecer anterior
                for k in ["last_visio_chat_hermes_opinion", "last_visio_chat_hermes_kb", "last_visio_chat_hermes_docs"]:
                    if k in st.session_state: del st.session_state[k]

                with st.spinner("🗣️ Consultando Visio-Chat Hermes..."):
                    data = st.session_state.get("temp_data", {})
                    chosen_kb = data.get("especialidade", "mock").lower()
                    chosen_kb = "strabismus" if "strabismus" in chosen_kb else "mock"
                    
                    v_service = VisioChatHermesService(chosen_kb)
                    v_prompt = f"Atue como especialista. Avalie o seguinte prontuário: {json.dumps(st.session_state.last_ehr)}"
                    v_res, v_docs = v_service.ask(v_prompt, search_query=st.session_state.last_ehr.get("diagnostico_hipotese"))
                    
                    st.session_state.last_visio_chat_hermes_opinion = v_res
                    st.session_state.last_visio_chat_hermes_kb = chosen_kb
                    st.session_state.last_visio_chat_hermes_docs = v_docs
                    st.rerun() 
            
            if "last_visio_chat_hermes_opinion" in st.session_state:
                st.subheader(f"🗣️ Opinião do Especialista (Base: {st.session_state.last_visio_chat_hermes_kb})")
                st.info(st.session_state.last_visio_chat_hermes_opinion)
                with st.expander("📄 Fontes e Contextos Consultados"):
                    for d in st.session_state.last_visio_chat_hermes_docs:
                        st.markdown(f"**Fonte:** `{os.path.basename(d.metadata.get('source', ''))}`")
                        st.caption(d.page_content)
                        st.divider()
    else:
        st.info("Aguardando gravação de áudio para iniciar o processo.")
