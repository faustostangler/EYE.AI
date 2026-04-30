# ADR 0006: Asynchronous Ingestion API and Compliance

## Status
Proposed

## Context
The system needs to ingest unstructured clinical records (PEP payload) and process them using a Local LLM (Llama 3.1 / Gemma) on a host with limited VRAM (6GB RTX 2060). LLM inference is a slow, compute-bound process. If the ingestion API were synchronous, the HTTP requests would timeout, and the system would be unable to handle concurrent ingestion requests without running Out Of Memory (OOM). Furthermore, these clinical records contain Protected Health Information (PHI) subject to LGPD.

## Decision
1. **Asynchronous Architecture:** The Ingestion API will be completely asynchronous. The HTTP endpoint will only receive the payload, generate a `task_id`, delegate the actual processing to a background worker queue, and immediately return a `202 Accepted` response.
2. **Message Broker:** We will use Redis as the message broker and `rq` (Redis Queue) as the task queue manager to decouple the API from the Inference Worker.
3. **Mandatory PII Scrubbing:** Before any clinical data is placed on the Redis queue (which represents a persistence boundary), it MUST pass through the `PIIScrubber`. No raw PHI/PII is allowed in the message broker or logs.

## Consequences
* **Positive:** The API remains highly responsive. GPU concurrency can be strictly controlled (e.g., concurrency=1) by the worker to prevent OOM errors. Strict adherence to LGPD by ensuring data is anonymized early in the pipeline.
* **Negative:** Increased architectural complexity (requires managing Redis and Worker processes). Clients must poll or rely on webhooks to get the final clinical extraction results.
