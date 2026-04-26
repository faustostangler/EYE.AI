# Ubiquitous Language Glossary

This document serves as the Single Source of Truth for the Domain's Ubiquitous Language, as required by our DDD and Clean Architecture standards. It eliminates translation errors between business experts and engineers.

## Core Domain: Clinical Analytics
* **PEP (Prontuário Eletrônico do Paciente):** The Electronic Health Record. The upstream system from which raw clinical data is ingested.
* **Conduct Analysis (Análise de Conduta):** The final output of the system. A structured AI-generated medical evaluation based on the patient's retrieved medical history and the current clinical question.
* **RAG Prompt:** The final, anonymized string of text constructed by the Use Case, containing the instructions and the retrieved clinical context, ready to be sent to the LLM.

## Ingestion & Anti-Corruption Layer (ACL)
* **Ingestion Adapter:** The entry point port/adapter that receives data from the external PEP API.
* **PII Scrubber (Anonymizer):** The service within the ACL responsible for identifying and masking Protected Health Information (PHI) and Personally Identifiable Information (PII) to comply with LGPD before data enters the Core Domain.
* **Raw Payload:** The unvalidated, potentially sensitive JSON data received directly from the PEP API.
* **Scrubbed Payload:** The sanitized data where sensitive entities (like names, ages, locations) have been replaced with tokens (e.g., `[NAME_1]`).

## Infrastructure & Observability
* **TraceID:** A unique identifier for a single inference request lifecycle, used across Prometheus and Grafana Loki.
* **VectorID:** The unique identifier of a specific embedded chunk of the patient's medical history stored in the Qdrant database.
* **Graceful Degradation:** The system's ability to maintain availability even when hardware limits (6GB VRAM) are exceeded, specifically by offloading LLM layers to system RAM via `llama.cpp` instead of crashing with an Out-Of-Memory (OOM) error.
