import pytest
from pydantic import ValidationError

# In TDD, we import the class we intend to create, even if it doesn't exist yet.
from src.core.config import SystemSettings


def test_config_fails_fast_when_missing_required_env_vars(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    Ensures the system cannot boot without critical infrastructure and domain parameters.
    """
    # Wipe the environment to simulate a raw container startup
    monkeypatch.delenv("PEP_API_URL", raising=False)
    monkeypatch.delenv("PEP_API_KEY", raising=False)
    monkeypatch.delenv("LLM_MODEL_PATH", raising=False)

    with pytest.raises(ValidationError) as exc_info:
        SystemSettings()

    errors = str(exc_info.value)
    assert "PEP_API_URL" in errors
    assert "PEP_API_KEY" in errors
    assert "LLM_MODEL_PATH" in errors


def test_config_loads_successfully_with_valid_env_vars(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """
    Ensures valid configurations are parsed and default VRAM safeguards are enforced.
    """
    # Inject valid required variables
    monkeypatch.setenv("PEP_API_URL", "https://api.hospital.local/v1/pep")
    monkeypatch.setenv("PEP_API_KEY", "mock-secure-key")
    monkeypatch.setenv("LLM_MODEL_PATH", "/models/gemma4-q4.gguf")

    # Initialize the Settings
    config = SystemSettings()

    # Verify explicitly set variables
    assert config.pep_api_url == "https://api.hospital.local/v1/pep"
    assert config.pep_api_key.get_secret_value() == "mock-secure-key"
    assert config.llm_model_path == "/models/gemma4-q4.gguf"

    # Verify Default Hardware Safeguards (CRITICAL for our 6GB RTX 2060)
    assert config.llm_max_context_tokens == 2048
    assert config.llm_gpu_layers == 30
