# -*- coding: utf-8 -*-
"""
Auto-generated script from ingestion.ipynb
Hermes Clinical Consultant - RAG Pipeline
"""


# ========================================
# CELL ID: setup
# ========================================
# !uv pip install langchain langchain-community langchain-core langchain-chroma langchain-huggingface langchain-ollama sentence-transformers pypdf ipywidgets pydantic-settings

# ========================================
# CELL ID: imports
# ========================================
import os
import json
import warnings
import logging

# Silence transformers lazy-loading warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")
try:
    from transformers import logging as transformers_logging
    transformers_logging.set_verbosity_error()
except ImportError:
    pass

import ollama
from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings
from IPython.display import Markdown, display, JSON

import glob
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.document_transformers import LongContextReorder

# ========================================
# CELL ID: config
# ========================================
class Settings(BaseSettings):
    """Configurações centralizadas com fail-fast."""
    # Define base paths relative to this file
    _BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
    
    def get_db_path(self, kb_name: str) -> str:
        return os.path.join(self._BASE_DIR, f"chroma_db_{kb_name}")
        
    def get_docs_path(self, kb_name: str) -> str:
        return os.path.join(os.path.dirname(self._BASE_DIR), "docs", "rag", kb_name)
    
    MODEL_NAME: str = Field(default="gemma4:e4b", validation_alias="LLM_MODEL_PATH")
    EMBEDDING_MODEL_NAME: str = "nomic-embed-text"
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150
    RETRIEVAL_K: int = 10
    MAX_CONTEXT_TOKENS: int = 8192
    HISTORY_TOKEN_BUDGET: int = 3500
    
    model_config = {
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
print(f"[CONFIG] Modelo: {settings.MODEL_NAME}")


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for Portuguese text."""
    return len(text) // 4

# ========================================
# CELL ID: domain
# ========================================
class ClinicalResponse(BaseModel):
    """Entidade de Domínio para resposta clínica validada."""
    resposta_texto: str = Field(..., description="A resposta em texto livre baseada nos protocolos")
    fonte: List[str] = Field(..., description="Documentos que sustentam a resposta")
    alerta_alucinacao: bool = Field(default=False, description="True se a informação não foi encontrada no contexto")

    @classmethod
    def from_llm_output(cls, raw_text: str, docs: List) -> 'ClinicalResponse':
        # Heurística simples de alerta caso o LLM diga que não encontrou
        texto_lower = raw_text.lower()
        alerta = "não encontrei" in texto_lower or "não há informações" in texto_lower or "não menciona" in texto_lower
        fontes = list(set([os.path.basename(doc.metadata.get('source', 'Unknown')) for doc in docs]))
        return cls(
            resposta_texto=raw_text,
            fonte=fontes,
            alerta_alucinacao=alerta
        )

# ========================================
# CELL ID: infra_vector
# ========================================
class VectorDBAdapter:
    """Adapter de Infraestrutura para o banco vetorial ChromaDB."""
    def __init__(self, kb_name: str = "mock"):
        self.kb_name = kb_name
        self._embeddings = None
        self.db = None

    @property
    def embeddings(self):
        if self._embeddings is None:
            print(f"[DB] Inicializando OllamaEmbeddings ({settings.EMBEDDING_MODEL_NAME})...")
            self._embeddings = OllamaEmbeddings(model=settings.EMBEDDING_MODEL_NAME)
        return self._embeddings

    def load_or_create(self, force_reingest: bool = False) -> Chroma:
        db_path = settings.get_db_path(self.kb_name)
        if os.path.exists(db_path) and not force_reingest:
            print(f"[DB] Carregando banco persistente: {db_path}")
            self.db = Chroma(persist_directory=db_path, embedding_function=self.embeddings)
        else:
            self.db = self._ingest()
        return self.db

    def _ingest(self) -> Chroma:
        docs_dir = settings.get_docs_path(self.kb_name)
        db_path = settings.get_db_path(self.kb_name)
        print(f"[DB] Iniciando ingestão rápida de: {docs_dir}")
        
        # Fast Loading: glob + TextLoader (evita overhead do DirectoryLoader)
        docs_path = os.path.join(docs_dir, "**/*.md")
        files = glob.glob(docs_path, recursive=True)
        
        documentos = []
        for f in files:
            try:
                loader = TextLoader(f, encoding="utf-8")
                documentos.extend(loader.load())
            except Exception as e:
                print(f"[ERR] Falha ao carregar {f}: {e}")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE, 
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = splitter.split_documents(documentos)

        if os.path.exists(db_path):
            import shutil
            shutil.rmtree(db_path, ignore_errors=True)
            
        db = Chroma.from_documents(chunks, self.embeddings, persist_directory=db_path)
        print(f"[DB] Ingestão concluída ({len(chunks)} chunks).")
        return db

    def retrieve(self, query: str) -> List:
        if not self.db: self.load_or_create()
        
        # Busca os Top K
        retriever = self.db.as_retriever(search_kwargs={"k": settings.RETRIEVAL_K})
        docs_relevantes = retriever.invoke(query)
        
        # [ARQUITETURA] Scored Reorder para mitigar "Lost in the Middle"
        reorder = LongContextReorder()
        docs_reordenados = reorder.transform_documents(docs_relevantes)
        
        return docs_reordenados

# ========================================
# CELL ID: infra_llm
# ========================================
class ClinicalLLMAdapter:
    """Adapter para o motor de inferência Ollama."""
    def __init__(self):
        self._llm = None
        self._rewriter = None
        self.prompt_template = PromptTemplate.from_template("""
            Você é o Visio-Chat Hermes, um sistema de suporte à decisão clínica com RIGOR ABSOLUTO.
            Sua única fonte de verdade é o CONTEXTO INSTITUCIONAL fornecido abaixo.
            
            REGRAS CRÍTICAS:
            1. Se a resposta não estiver EXPLICITAMENTE em uma das fontes abaixo, diga CLARAMENTE "Não encontrei essa informação nos protocolos fornecidos".
            2. Se você encontrar a resposta, estruture-a de forma clara e direta e cite o nome da [FONTE] na sua resposta.
            3. IGNORE seu conhecimento médico prévio se ele não estiver suportado pelo texto fornecido.
            4. Não faça deduções heróicas. Se o texto diz "A causa B", responda exatamente isso.

            CONTEXTO INSTITUCIONAL:
            {contexto}

            HISTÓRICO DA CONVERSA:
            {historico}

            PERGUNTA DO MÉDICO:
            {pergunta}

            Responda em formato de texto claro e direto (pode usar Markdown para organizar a resposta, como tópicos ou negrito).
            """)

    @property
    def llm(self):
        if self._llm is None:
            print(f"[LLM] Inicializando motor {settings.MODEL_NAME}...")
            self._llm = OllamaLLM(model=settings.MODEL_NAME, temperature=0.0)
        return self._llm

    @property
    def rewriter(self):
        """Lazy-loaded LLM for query rewriting (no JSON format constraint)."""
        if self._rewriter is None:
            self._rewriter = OllamaLLM(model=settings.MODEL_NAME, temperature=0.0)
        return self._rewriter

    def rewrite_query(self, current_query: str, conversation_context: str) -> str:
        """Rewrites a vague follow-up into a self-contained query using conversation context."""
        if not conversation_context:
            return current_query
        rewrite_prompt = (
            "Dado o contexto da conversa anterior:\n"
            f"{conversation_context}\n\n"
            "Reescreva a seguinte pergunta para que seja auto-contida, "
            "incorporando informações relevantes do contexto. "
            "Retorne APENAS a pergunta reescrita, sem explicações.\n\n"
            f"Pergunta: {current_query}\n"
            "Pergunta reescrita:"
        )
        rewritten = self.rewriter.invoke(rewrite_prompt).strip()
        print(f"[REWRITE] '{current_query}' → '{rewritten}'")
        return rewritten

    def generate(self, pergunta: str, contexto: str, historico: str = "") -> str:
        chain = self.prompt_template | self.llm
        return chain.invoke({"contexto": contexto, "pergunta": pergunta, "historico": historico})

# ========================================
# CELL ID: application
# ========================================
class HermesClinicalConsultant:
    def __init__(self, kb_name: str = "mock"):
        self.kb_name = kb_name
        self.vector_db = VectorDBAdapter(kb_name=self.kb_name)
        self.llm = ClinicalLLMAdapter()

    def ask(self, pergunta: str, conversation_context: str = "") -> (ClinicalResponse, List):
        print(f"[HERMES] Analisando consulta: '{pergunta}'")
        
        # 1. Query Rewriting (contextualiza perguntas vagas usando histórico)
        search_query = self.llm.rewrite_query(pergunta, conversation_context)
        
        # 2. Recuperação (usa a query reescrita para melhor recall semântico)
        docs = self.vector_db.retrieve(search_query)
        
        # Formatação do contexto com metadados (Strict Grounding)
        contexto_formatado = []
        for doc in docs:
            fonte = os.path.basename(doc.metadata.get('source', 'Desconhecida'))
            contexto_formatado.append(f"[FONTE: {fonte}]\n{doc.page_content}")
        
        contexto = "\n\n---\n\n".join(contexto_formatado)
        
        # 3. Token budget check — trunca histórico antigo se necessário
        historico = conversation_context
        if estimate_tokens(historico) > settings.HISTORY_TOKEN_BUDGET:
            while estimate_tokens(historico) > settings.HISTORY_TOKEN_BUDGET and "\n" in historico:
                historico = historico.split("\n", 1)[1]
            print(f"[BUDGET] Histórico truncado para {settings.HISTORY_TOKEN_BUDGET} tokens")
        
        # 4. Geração com histórico
        raw_output = self.llm.generate(pergunta, contexto, historico)
        
        # 5. Validação de Domínio
        response = ClinicalResponse.from_llm_output(raw_output, docs)
        
        return response, docs

# ========================================
# CELL ID: human_readable_display
# ========================================
from IPython.display import Markdown, display, HTML

def renderizar_dashboard_hermes(pergunta: str, response: ClinicalResponse, docs_relevantes=None):
    """
    Renderiza um dashboard clínico elegante no Jupyter Notebook.
    """
    # Cores e Estilos
    alerta = response.alerta_alucinacao
    status_color = "#ef4444" if alerta else "#22c55e"
    status_text = "⚠️ ALERTA: DADOS NÃO ENCONTRADOS" if alerta else ""
    
    # Usamos markdown no jupyter também se tiver HTML
    html_header = f"""
    <div style="font-family: sans-serif; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; margin-bottom: 20px;">
        <div style="background-color: {status_color}; color: white; padding: 12px 20px; font-weight: bold; display: flex; justify-content: space-between;">
            <span>VISIO-CHAT HERMES | Suporte à Decisão</span>
            <span>{status_text}</span>
        </div>
        <div style="padding: 20px; background-color: #f9fafb;">
            <h3 style="margin-top: 0; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 8px;">❓ Pergunta do Médico</h3>
            <p style="font-size: 1.1em; color: #374151; font-weight: 500; line-height: 1.6;">{pergunta}</p>

            <h3 style="margin-top: 24px; color: #111827; border-bottom: 2px solid #e5e7eb; padding-bottom: 8px;">🎯 Resposta Clínica</h3>
            <div style="font-size: 1.1em; color: #374151; line-height: 1.6;">
                {response.resposta_texto}
            </div>
        </div>
    </div>
    """
    
    display(HTML(html_header))

    # Se houver documentos, mostrar as fontes de forma resumida
    if docs_relevantes:
        fontes_html = "<div style='font-family: sans-serif; padding: 0 10px;'><h4>📄 Fontes Institucionais Consultadas:</h4><ul style='color: #6b7280; font-size: 0.9em;'>"
        for fonte in response.fonte:
            fontes_html += f"<li>{fonte}</li>"
        
        fontes_html += "</ul></div>"
        display(HTML(fontes_html))

# ========================================
# CELL ID: main
# ========================================
# ==========================================
# EXECUÇÃO VIA FACHADA DE APLICAÇÃO
# ==========================================
if __name__ == "__main__":
    # Instancia o Consultor (Application Service)
    hermes = HermesClinicalConsultant(kb_name="mock")
    
    # Opcional: Forçar reingestão se houver novos arquivos
    # hermes.vector_db.load_or_create(force_reingest=False)

    # Consulta de Teste
    pergunta = "Paciente com baixa de visão e catarata, além de disúria. Qual pode ser o diagnóstico?"
    resposta, docs_originais = hermes.ask(pergunta)

    # Renderização
    renderizar_dashboard_hermes(pergunta, resposta, docs_originais)

# # ========================================
# # CELL ID: utility_inspector
# # ========================================
# import chromadb
# import pandas as pd

# def inspecionar_colecoes():
#     """Ferramenta de DX para visualizar o estado interno do banco de vetores."""
#     client = chromadb.PersistentClient(path=settings.VECTOR_DB_PATH)
#     collections = client.list_collections()
    
#     print(f"[INSPECTOR] Localizado: {settings.VECTOR_DB_PATH}")
#     for col in collections:
#         count = col.count()
#         print(f"\nColeção: '{col.name}' | Total de Chunks: {count}")
        
#         if count > 0:
#             dados = col.get(limit=5)
#             df = pd.DataFrame({
#                 'ID': dados['ids'],
#                 'Documento': [d[:150] + '...' for d in dados['documents']],
#                 'Metadata': dados['metadatas']
#             })
#             display(df)

# inspecionar_colecoes()
