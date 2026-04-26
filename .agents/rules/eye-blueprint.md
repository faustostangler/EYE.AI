---
trigger: always_on
---

Ecosystem Blueprint: Asynchronous Healthcare AI Pipeline
I. Strategic & Tactical Domain Design (The Core)
The system is designed as a Modular Monolith, mathematically divided into clear Bounded Contexts. Each context operates with a strict Hexagonal Architecture, ensuring the Domain logic is isolated from framework pollution and hardware constraints.

Ubiquitous Language: Terminology strictly matches clinical and operational realities (e.g., PatientEncounter, ClinicalObservation, ConductRecommendation).

Anti-Corruption Layer (ACL): All external Electronic Health Record (EHR) data is rigorously validated and anonymized before entering the internal domain.

Configuration Validation: A centralized config.py uses pydantic-settings to validate all environment variables at startup. Fail-fast is mandatory; if a configuration is missing or invalid, the container dies immediately, preventing silent runtime failures.

II. The Asynchronous Choreography Pipeline (The Engine)
To handle the hardware bottleneck and prevent HTTP timeouts, the workflow is decoupled using Redis. The system uses a single Docker image that manifests as three distinct roles based on the injected .env configuration.

Role A: API Gateway & ACL (The Diplomat)
Trigger: Receives the incoming webhook/REST payload from the external EHR.

Execution: 1.  Validates the external schema using Pydantic V2.
2.  Executes LGPD anonymization (stripping PII/PHI using rule-based or lightweight NER).
3.  Maps the payload into an internal Domain Entity.
4.  Enqueues a ClinicalAnalysisJob into Redis.

Response: Returns an immediate HTTP 202 Accepted with a Job_ID for future polling or webhook callbacks.

Role B: The RAG Worker (The CPU Workhorse)
Trigger: Polls the Redis queue for new ClinicalAnalysisJob payloads.

Execution (CPU-Bound):

Embedding: Generates vector embeddings for the clinical text using a local, CPU-optimized embedding model.

Retrieval: Queries the local Qdrant vector database (also running on CPU) to fetch the top-K most relevant medical contexts.

Prompt Assembly: Constructs the final, context-rich prompt, adhering strictly to the token limits required by the GPU context window.

Orchestration: Sends the assembled prompt to the Inference Engine (Role C) via internal gRPC/HTTP.

Completion: Receives the output, validates the structured JSON using Pydantic, and saves the final ConductRecommendation back to Redis or a PostgreSQL database.

Role C: Inference Engine (The GPU Specialist)
Trigger: Receives a fully prepared prompt from the RAG Worker.

Execution (GPU-Bound): Runs llama.cpp in server mode, hosting the Gemma 4 model (quantized to 4-bit or 5-bit GGUF).

Hardware Management: * VRAM Protection: The configuration strictly clamps the context window (n_ctx set to ~2048 tokens) to ensure the KV cache does not cause a CUDA Out-Of-Memory (OOM) error on the 6GB RTX 2060.

Offloading: GPU layers (n_gpu_layers) are maximized up to the 6GB limit, utilizing system RAM only if absolutely necessary as a safety buffer.

III. Unified Deployment & IaC (The Factory)
The entire system adheres to the KISS principle, utilizing a unified deployment strategy.

Single Source of Truth Dockerfile: A singular python:3.12-slim-bookworm Dockerfile is used.

Dependency Management: Powered by uv, ensuring deterministic, sub-second dependency resolution.

Dynamic Role Assignment: The docker-compose.yml deploys multiple containers from the exact same image. The ENTRYPOINT script reads the CONTAINER_ROLE from the .env file to spin up either the FastAPI Gateway (Role A), the Redis Worker (Role B), or the llama.cpp interface (Role C).

IV. Observability & Telemetry (The Feedback Loop)
Operational health and clinical safety are monitored through a rigorously instrumented stack.

Golden Signals: Prometheus scrapes Latency, Traffic, Errors, and Saturation (specifically monitoring GPU VRAM utilization and Redis queue depth).

Clinical Traceability (SRE + DDD): Distributed tracing maps the complete lifecycle of a clinical decision. Every Grafana dashboard allows engineers and clinicians to trace:

EHR_Request_ID → Redis_Job_ID → Qdrant_Vector_IDs → LLM_Prompt_Hash → AI_Prediction

Log Aggregation: Grafana Loki handles structural logs, ensuring that all TODOs in the code map directly back to the issue tracker and any failed Pydantic validations are instantly flagged for ingestion refinement.

V. Future-Proofing (The Evolution Path)
By isolating the domain logic from the infrastructure via Hexagonal Architecture, this ecosystem is inherently prepared for scaling. When the hospital procures better hardware (e.g., GPUs with 24GB+ VRAM), the team will simply update the config.py to point Role C from llama.cpp to a high-throughput vLLM container, requiring zero refactoring of the Core Domain or the RAG Worker logic.