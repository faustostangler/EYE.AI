# ADR 0002: LLM Engine Strategy for 6GB VRAM Constraints

## Status
Approved

## Context
The environment has a strict physical constraint: a single NVIDIA RTX 2060 GPU with 6GB of VRAM. This is a highly constrained and hostile environment for running Large Language Models (LLMs). A model like Gemma (even in smaller versions like 2B or 7B) will need to be highly quantized (e.g., Q4_K_M or Q5_K_M). 

Furthermore, besides the model's weight, the KV Cache grows linearly with the context size, which poses a severe risk of Out-Of-Memory (OOM) errors in a 6GB VRAM environment.

## Options Considered

### Option 1: vLLM
* **Description:** A high-throughput and memory-efficient LLM serving engine using PagedAttention.
* **Pros:** Excellent for high concurrency and batching.
* **Cons:** Allocates large blocks of VRAM upfront and has a very high overhead for small GPUs. With an expected volumetry of 2 requests per minute, throughput (Traffic) is not the bottleneck, but rather Latency and VRAM Saturation.

### Option 2: llama.cpp (Selected Strategy)
* **Description:** A lightweight, C/C++ based LLM inference engine supporting GGUF quantization.
* **Pros:** Allows granular control of the context limit (`--ctx-size`) and performs intelligent offloading of layers to system RAM if VRAM is exhausted (Graceful Degradation).
* **Cons:** Lower theoretical maximum throughput compared to vLLM in highly concurrent environments (which is irrelevant for our 2 req/min use case).

## Decision
We will use **llama.cpp** exclusively as the LLM Inference Engine in version 1. 

The idea to start with `llama.cpp` and migrate to `vLLM` in "version 2" has been reviewed and discarded for this specific hardware profile., and will be postponed untill better bare metal GPUs are available. `vLLM`'s upfront VRAM allocation is detrimental to our current 6GB VRAM limit. 

## Consequences
* **Positive:** Granular control over the context window and memory footprint. We achieve "Graceful Degradation"; if the context size accidentally spikes, `llama.cpp` will offload to system RAM instead of immediately crashing the container with an OOM error.
* **Negative:** Inference latency will increase if layers are forced to offload to system RAM, but this is an acceptable trade-off to ensure system stability and API availability.
