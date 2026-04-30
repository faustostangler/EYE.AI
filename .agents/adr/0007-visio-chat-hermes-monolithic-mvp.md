# ADR 0007: Visio-Chat Hermes Monolithic MVP

## Status
Proposed

## Context
The organization requires a clinical decision support system, **Visio-Chat Hermes**, acting as a Medical Preceptor. Strict LGPD compliance mandates a local-first approach to ensure patient data privacy. To support structured medical EHRs and future Model Context Protocol (MCP) integrations, the preceptor must provide strictly formatted JSON outputs without hallucinations. 
For a fast validation loop (KISS principle), we need a monolithic proof of concept (MVP) that demonstrates full local RAG capabilities before committing to a fully decoupled Hexagonal/DDD integration.

## Decision
1. **Temporary Monolith:** We will build a temporary, isolated monolithic RAG engine inside the `MVP/` folder. 
2. **Local-First Technology Stack:** 
   - **Ollama** as the physical inference backend using `gemma:2b` or `gemma:7b` for generation and `nomic-embed-text` for embeddings.
   - **ChromaDB** for local, serverless vector persistence.
   - **LangChain** to orchestrate parsing, embedding, retrieval, and prompt management.
3. **Deterministic JSON Output:** Leverage Ollama's native `format="json"` capability linked with Pydantic/schema enforcement to guarantee structured payloads matching internal medical decision formats.

## Consequences
* **Positive:** Rapid local evaluation of Gemma's clinical capabilities; Zero data leaves the local environment (LGPD-safe); Standardized output formats.
* **Negative:** Highly coupled implementation lacking hexagonal boundary controls. It must NOT be pushed into production domains without architectural refactoring.
