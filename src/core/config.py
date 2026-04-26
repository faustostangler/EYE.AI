from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class SystemSettings(BaseSettings):
    """
    Centralized configuration for the Clinical Analysis context.
    Follows fail-fast principles by requiring critical environment variables.
    """

    # Environment Identity
    env: str = Field(default="production", validation_alias="ENV")

    # PEP (Prontuário Eletrônico do Paciente) ACL Settings
    pep_api_url: str = Field(..., validation_alias="PEP_API_URL")
    pep_api_key: SecretStr = Field(..., validation_alias="PEP_API_KEY")

    # LLM Boundaries (Strict safeguards for 6GB VRAM)
    llm_model_path: str = Field(..., validation_alias="LLM_MODEL_PATH")
    llm_max_context_tokens: int = Field(
        default=2048, validation_alias="LLM_MAX_CONTEXT_TOKENS"
    )
    llm_gpu_layers: int = Field(default=30, validation_alias="LLM_GPU_LAYERS")

    # Infrastructure
    redis_dsn: str = Field(
        default="redis://localhost:6379/0", validation_alias="REDIS_DSN"
    )
    qdrant_url: str = Field(
        default="http://localhost:6333", validation_alias="QDRANT_URL"
    )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
