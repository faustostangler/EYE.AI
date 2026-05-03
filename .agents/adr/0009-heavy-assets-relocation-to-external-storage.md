# ADR 0009: Relocation of Heavy Playground Assets to External Storage

## Status
Accepted (Conditional to Host: Gamer)

## Context
The development environment on the `Gamer` host has a primary partition (`/`) with critical space constraints (~1.2GB available). 
Implementing SOTA Visual RAG (ColPali) and multimodal pipelines requires:
1. Large Python dependencies (PyTorch + CUDA wheels ~3GB+).
2. Heavy model weights (PaliGemma/Gemma ~2-5GB each).
3. Late Interaction indices (ColBERT/Byaldi ~15MB/page).

Additionally, **Python 3.13** (initial choice) proved unstable for the current ML stack, causing `uv` to fallback to ancient/broken library versions (e.g., `torchvision 0.1.6`) due to a lack of CUDA-enabled wheels for `cp313`.

The secondary disk `/mnt/gamer_d` provides high capacity and performance, suitable for these assets.

## Decision
We decided to offload all "heavy" playground assets to `/mnt/gamer_d/eye_ai_workspace/` and **downgrade the environment to Python 3.12** to ensure system stability and performance.

### Implementation Details:
1. **Python Version**: Downgraded to **3.12.3** to ensure full compatibility with PyTorch 2.5.1+ CUDA wheels.
2. **Virtual Environment**: The `.venv` is physically located at `/mnt/gamer_d/eye_ai_workspace/venvs/eye_ai_venv_312` and linked back to the project root via a symbolic link.
3. **UV Cache**: The `UV_CACHE_DIR` is redirected to `/mnt/gamer_d/eye_ai_workspace/uv_cache` during installation to prevent disk exhaustion during package downloads.
4. **Model Caches**: In the `playground/` notebooks, `HF_HOME` and `HF_HUB_CACHE` are explicitly set to `/mnt/gamer_d/huggingface_cache`.
5. **Byaldi Indices**: The `index_root` for Byaldi is explicitly directed to `/mnt/gamer_d/.byaldi`.
6. **Ollama**: Recommended reconfiguration of `OLLAMA_MODELS` to `/mnt/gamer_d/ollama/models`.

## Machine-Specific Constraint
**IMPORTANT**: This decision is strictly conditional to the current machine configuration (`Gamer` host).
* These paths (`/mnt/gamer_d/...`) are **NOT** portable. 
* Production and CI/CD pipelines must NOT use these hardcoded paths and should instead rely on standard containerized volumes or cloud storage as defined in the global architecture.
* The `.venv` symlink is a local developer experience (DX) hack to maintain standard IDE behavior while bypassing physical disk limits.

## Consequences
* **Positive**: Prevention of "Disk Full" crashes during heavy model experimentation.
* **Positive**: Preservation of the main OS partition for critical system tasks.
* **Negative**: Reduced portability of playground notebooks if shared with environments lacking `/mnt/gamer_d`.
* **Risk**: Accidental hardcoded path leak into `src/` (mitigated by ADR 0008 isolation tests).
