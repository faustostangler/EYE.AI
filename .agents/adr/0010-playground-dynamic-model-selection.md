# ADR 0010: Dynamic Model Selection in Playground UI

## Status
Proposed

## Context
The EYE.AI Playground currently relies on the `LLM_MODEL_PATH` environment variable to define the active LLM. Switching models requires manual editing of the `.env` file or restarting the Streamlit application. For a better developer experience (DX) and clinical testing, it is necessary to allow users to switch between available models (e.g., `phi3:mini`, `qwen3.5:4b`, `gemma4:e4b`) directly from the sidebar.

## Decision
We will implement a model selector in the Streamlit interface.
1. The list of available models will be derived from the local Ollama installation via `ollama.list()`.
2. **Layout Placement**: In the Visio-Scribe Jonathan flow, the selector will be positioned exactly between the Whisper transcription expander and the EHR extraction expander.
3. **Benchmarking**: Each extraction will be timed, and results (model, duration) will be stored in `st.session_state.inference_history` to allow side-by-side comparison.
4. **Caching**: `get_llm(model_name)` will be updated to be parameterized and cached by `st.cache_resource`.
5. **VRAM Management**: Selecting a new model will trigger a cache refresh for the LLM component.

## Consequences
- **Positive**: Improved comparison of model accuracy vs. speed (latency). Faster iteration as audio doesn't need re-transcription.
- **Negative**: UI becomes slightly more complex with a benchmarking section.
- **Risks**: VRAM exhaustion if Ollama doesn't unload quickly, but current settings (50 layers) should be safe for one model at a time.
