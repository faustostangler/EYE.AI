# ADR 0003: LGPD Compliance and Observability (PII Scrubber)

## Status
Approved

## Context
In ADR 0001, we established a telemetry and tracing strategy that maps `TraceID -> VectorID -> RAG Prompt` in Grafana Loki to ensure complete observability of AI predictions. 

However, the raw prompts derived from the Electronic Health Records (PEP - Prontuário Eletrônico do Paciente) will inherently contain Protected Health Information (PHI) and Personally Identifiable Information (PII), such as patient names, ages, document numbers, and contact details. 
Storing this data in plain text within telemetry logs (like Loki or Prometheus) is a severe violation of the Brazilian General Data Protection Law (LGPD).

## Options Considered

### Option 1: Omit Prompts from Telemetry
* **Description:** Do not log the actual prompt text; only log the `TraceID` and `VectorID`.
* **Pros:** Guarantees no PII is leaked into the logs.
* **Cons:** Completely destroys the observability of the RAG pipeline. It makes debugging hallucinations, tracing poor retrieval, and auditing AI decisions practically impossible.

### Option 2: Implement a PII Scrubber/Anonymizer in the ACL (Selected Strategy)
* **Description:** Integrate a robust PII Scrubber (e.g., Microsoft Presidio or a local lightweight NER model) directly into the Anti-Corruption Layer (Adapter) during the ingestion phase. 
* **Pros:** Preserves the structural observability of the system. We can still read the logs and understand exactly what context the LLM received to make its decision, without exposing any patient identities.
* **Cons:** Introduces slight processing latency during ingestion and requires careful tuning to ensure it masks identities without destroying critical clinical context.

## Decision
We will proceed with **Option 2** and implement a **PII Scrubber/Anonymizer** in the Anti-Corruption Layer (ACL).

Before any data from the PEP API is validated by Pydantic and allowed into the Core Domain (or enqueued into Redis), it must pass through the anonymization process. 

The prompt sent to the LLM and subsequently logged in Loki must have sensitive entities masked. 
**Example Transformation:**
*   *Original:* "O paciente João da Silva, 45 anos, nascido em São Paulo, apresenta quadro de..."
*   *Scrubbed:* "O paciente [NAME_1], [AGE] anos, nascido em [LOCATION_1], apresenta quadro de..."

The `TraceID -> VectorID -> RAG Prompt` telemetry mapping remains fully functional, but the `RAG Prompt` logged will exclusively contain this scrubbed, LGPD-compliant text.

## Consequences
* **Positive:** Strict adherence to LGPD while maintaining the "Glass Box" observability required by SRE culture. Developers can debug traces securely without needing access to raw production patient data.
* **Negative:** The PII scrubber adds complexity to the Ingestion Adapter. If the Named Entity Recognition (NER) model is overly aggressive, it might mask relevant clinical data. If it is too lenient, it risks a privacy breach. It requires dedicated test coverage (Mutation Testing/Fuzzing) to ensure zero PII leakage.
