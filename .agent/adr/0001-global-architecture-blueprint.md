# ADR 0001: Global Architecture Blueprint for Local Clinical RAG

## Status
Approved

## Context
The hospital requires a local Retrieval-Augmented Generation (RAG) system to ingest Electronic Health Records (PEP - Prontuário Eletrônico do Paciente) and generate conduct analysis using the Gemma 4 open-source LLM. To guarantee strict compliance with the General Data Protection Law (LGPD), the system must operate entirely on the local hospital network, with absolute zero cloud dependency (air-gapped environment). 

Hardware constraints:
* **Throughput:** 2 requests per minute.
* **Compute:** Single GPU NVIDIA RTX 2060 (6 GB VRAM).

Architectural constraints:
* Must be Microservice-Ready but operate as a Modular Monolith.
* Strict Domain-Driven Design (DDD) with Clean and Hexagonal Architecture.

## Options Considered

### Option 1: Distributed Microservices
* **Description:** Separate codebases and CI/CD pipelines for Ingestion, Core Analytics, and Inference.
* **Pros:** Strict physical boundaries, independent scaling.
* **Cons:** High operational overhead, violates KISS principle for the current volumetry, complex local orchestration.

### Option 2: SOTA Modular Monolith with Unified Deployment (Selected Strategy)
* **Description:** A single deployable unit built with DDD and Hexagonal Architecture. Bounded contexts are logically separated but housed in the same repository. A single `Dockerfile` acts as the Single Source of Truth, manifesting different roles (API, Worker, Inference Server) via environment variables and entrypoints.
* **Pros:** Operational simplicity, microservice-ready (easy to split in the future), cohesive testing, optimal resource sharing on limited hardware.
* **Cons:** Requires strict import hygiene to prevent boundary leakage (no `src.` imports).

## Decision
We will proceed with **Option 2 (SOTA Modular Monolith)** to satisfy the architectural blueprint and constraints.

### 1. Bounded Contexts & Hexagonal Flow
* **Ingestion Context (Adapter):** An Anti-Corruption Layer (ACL) connects to the PEP API. It validates incoming raw data using Pydantic V2 (fail-fast) into pure Value Objects (VOs) and Entities. The workload is decoupled from inference by enqueuing valid payloads into **Redis**.
* **Clinical Analytics (Core Domain):** Contains the Use Cases. It retrieves relevant medical history (via Qdrant adapter) to construct prompts, sends them to the local LLM via REST, and strictly formats the response into structured JSON validated by Pydantic.

### 2. Resource Allocation (Hardware Constraints)
Given the 6GB VRAM limit on the RTX 2060:
* **Embeddings & Vector Database:** Embeddings generation and **Qdrant** will run exclusively on **CPU**.
* **LLM Inference:** The GPU is fully dedicated to inference. We will use `llama.cpp` serving a quantized version of Gemma 4 via a local REST API. The container will enforce strict VRAM limits and cap the maximum context size to prevent KV cache exhaustion and OOM errors. (Future-proofed to migrate to vLLM in v2, as in ADR 0002).

### 3. Infrastructure & Deployment
* **Containerization:** Single `Dockerfile` using `python:3.12-slim-bookworm` with `uv` for fast dependency resolution.
* **Configuration:** Centralized `config.py` using `pydantic-settings`. Container roles (e.g., `role=api`, `role=worker`) are injected via entrypoints and `.env`.
* **Telemetry & Observability:** 
    * Prometheus metrics for the Four Golden Signals (Latency, Traffic, Errors, Saturation).
    * Grafana Loki for logs.
    * Strict tracing mapping `TraceID -> VectorID -> RAG Prompt` to ensure every AI prediction is explicitly linked to the exact embeddings/context that supported it.

## Consequences
* **Positive:** Complete LGPD compliance, maximum utilization of the 6GB VRAM for the LLM, guaranteed domain isolation via Hexagonal Architecture, and highly observable predictions.
* **Negative:** Strong reliance on strict quantization and context management; any configuration drift could result in GPU OOM errors. Requires discipline in maintaining the ACL to protect the core domain from PEP API changes.
