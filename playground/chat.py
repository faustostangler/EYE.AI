# -*- coding: utf-8 -*-
"""
Hermes Clinical Chat — Streamlit Conversational Interface.

Reuses the RAG adapters from ingestion.py to provide a chat experience
over institutional clinical protocols.

Usage:
    cd playground && streamlit run chat.py
"""
import os
import sys
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

import streamlit as st

# Ensure playground/ is on sys.path for sibling imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ingestion import HermesClinicalConsultant, ClinicalResponse, settings, estimate_tokens


# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Hermes Clinical Chat",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Custom Theme (injected CSS)
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Global font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Chat message styling */
    .stChatMessage {
        border-radius: 12px;
        margin-bottom: 8px;
    }

    /* Grounding badge */
    .badge-grounded {
        background: linear-gradient(135deg, #059669, #10b981);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78em;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }
    .badge-hallucination {
        background: linear-gradient(135deg, #dc2626, #ef4444);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78em;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 8px;
    }

    /* Source cards */
    .source-chip {
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 4px 10px;
        font-size: 0.82em;
        color: #475569;
        display: inline-block;
        margin: 2px 4px 2px 0;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: #38bdf8 !important;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Session State Initialization
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "hermes" not in st.session_state:
    # Use st.status for a premium DX during initialization
    with st.status("🩺 Inicializando Hermes...", expanded=True) as status:
        st.write("Configurando adaptadores de IA...")
        hermes = HermesClinicalConsultant()
        
        # Check if ingestion is needed immediately (First Run fix)
        db_exists = os.path.exists(settings.VECTOR_DB_PATH)
        if not db_exists:
            st.write("📚 Base de protocolos não encontrada. Iniciando ingestão...")
            hermes.vector_db.load_or_create()
            st.write("✅ Ingestão concluída!")
        else:
            st.write("✅ Memória de protocolos carregada.")
            
        st.session_state.hermes = hermes
        status.update(label="🩺 Hermes pronto!", state="complete", expanded=False)

if "conversation_context" not in st.session_state:
    st.session_state.conversation_context = ""


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 🩺 Hermes")
    st.caption("Clinical Decision Support")
    st.divider()

    st.markdown(f"**Modelo LLM:** `{settings.MODEL_NAME}`")
    st.markdown(f"**Embeddings:** `{settings.EMBEDDING_MODEL_NAME}`")
    st.markdown(f"**Chunks (top-K):** `{settings.RETRIEVAL_K}`")
    st.markdown(f"**Chunk size:** `{settings.CHUNK_SIZE}`")
    st.divider()

    # Vector DB status
    db_exists = os.path.exists(settings.VECTOR_DB_PATH)
    if db_exists:
        st.success("🟢 Vector DB loaded", icon="✅")
    else:
        st.warning("🟡 Vector DB not found — will ingest on first query", icon="⚠️")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Re-ingest", use_container_width=True):
            with st.spinner("Ingesting documents..."):
                st.session_state.hermes.vector_db.load_or_create(force_reingest=True)
            st.success("Done!")
            st.rerun()
    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.conversation_context = ""
            st.rerun()

    st.divider()

    # Token usage DX metric
    ctx_tokens = estimate_tokens(st.session_state.conversation_context)
    budget = settings.HISTORY_TOKEN_BUDGET
    pct = min(int((ctx_tokens / budget) * 100), 100) if budget else 0
    st.markdown(f"🧠 **Memory:** `{ctx_tokens}/{budget}` tokens ({pct}%)")
    st.progress(pct / 100)

    st.divider()
    st.caption("Playground · EYE.AI")


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────
def format_response_markdown(response: ClinicalResponse, docs: list) -> str:
    """Formats a ClinicalResponse into a rich markdown string for the chat."""
    # Grounding badge
    if response.alerta_alucinacao:
        badge = '<span class="badge-hallucination">⚠️ ALERTA: Dados não encontrados nos protocolos</span>'
    else:
        badge = '<span class="badge-grounded">✅ Grounded — Baseado nos protocolos</span>'

    # Source chips
    fontes = response.fonte if isinstance(response.fonte, list) else [response.fonte]
    source_chips = " ".join(
        f'<span class="source-chip">📄 {f}</span>' for f in fontes
    )

    md = f"""{badge}

{response.resposta_texto}

### 📄 Fontes
{source_chips}
"""
    return md


def get_source_details(docs: list) -> str:
    """Extracts unique source filenames and preview from retrieved documents."""
    details = []
    seen = set()
    for doc in docs:
        source = os.path.basename(doc.metadata.get("source", "Unknown"))
        if source not in seen:
            seen.add(source)
            preview = doc.page_content[:200].replace("\n", " ")
            details.append(f"**{source}**\n> {preview}...")
    return "\n\n".join(details)


# ─────────────────────────────────────────────
# Chat History Rendering
# ─────────────────────────────────────────────
st.markdown("## 🩺 Hermes Clinical Chat")
st.caption("Converse com os protocolos clínicos institucionais")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑‍⚕️" if msg["role"] == "user" else "🩺"):
        if msg["role"] == "assistant":
            st.markdown(msg["content"], unsafe_allow_html=True)
            if msg.get("sources"):
                with st.expander("📚 Detalhes das fontes consultadas"):
                    st.markdown(msg["sources"])
        else:
            st.markdown(msg["content"])


# ─────────────────────────────────────────────
# Chat Input & Processing
# ─────────────────────────────────────────────
if prompt := st.chat_input("Descreva o caso clínico..."):
    # Render user message immediately
    with st.chat_message("user", avatar="🧑‍⚕️"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process with Hermes (passing rolling conversation context)
    with st.chat_message("assistant", avatar="🩺"):
        with st.spinner("Consultando protocolos..."):
            response, docs = st.session_state.hermes.ask(
                prompt,
                conversation_context=st.session_state.conversation_context,
            )

        formatted = format_response_markdown(response, docs)
        source_details = get_source_details(docs)

        st.markdown(formatted, unsafe_allow_html=True)

        with st.expander("📚 Detalhes das fontes consultadas"):
            st.markdown(source_details)

    # Update rolling conversation context (compact rewrite, zero LLM cost)
    preview = response.resposta_texto[:100].replace('\n', ' ')
    turn_summary = f"Médico: {prompt} \u2192 Hermes: {preview}..."
    if st.session_state.conversation_context:
        st.session_state.conversation_context += f"\n{turn_summary}"
    else:
        st.session_state.conversation_context = turn_summary

    # Persist to session
    st.session_state.messages.append({
        "role": "assistant",
        "content": formatted,
        "sources": source_details,
    })
