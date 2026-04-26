# ADR 0004: Docker Compose Environment Parametrization

## Status
Proposed

## Context
To ensure consistency, portability, and "Single Source of Truth" (SSOT) across different environments (development, staging, production), all configuration values in `docker-compose.yml` must be parameterized using environment variables with sensible defaults.

## Decision
All values in `docker-compose.yml` (including image names, versions, container names, ports, and environment variables) MUST use the following format:
`${VARIABLE_NAME:-default_value}`

To maintain a clean and secure project structure, environment variables follow a **Separation of Concerns** strategy:
1. **Source of Truth:** Located in `env/` directory.
   - `env/compose.env` (Versioned): Orchestration and infrastructure metadata.
   - `env/creds.env` (Ignored): Sensitive secrets and API keys.
2. **Local Artifact:** The root `.env` file is considered a **Generated Artifact** for compatibility with local tools (IDEs, Pydantic, Pytest). It is created by concatenating the source files via `make setup` and must be ignored by Git.

## Implementation Rules
1. **Container Naming:** Use `${COMPOSE_PROJECT_NAME:-eye}_service_name`.
2. **Images:** Use `${IMAGE_NAME:-base}:${IMAGE_TAG:-latest}`.
3. **Ports:** Use `${BIND_IP:-127.0.0.1}:${EXTERNAL_PORT:-8000}:${INTERNAL_PORT:-8000}`.
4. **Environment Variables:** All `environment:` keys must also be parameterized.
5. **Orchestration:** Use `env_file:` in `docker-compose.yml` to load both source files.
6. **Local Setup:** Use `make setup` to synchronize the local `.env` artifact.

## Consequences
* **Positive:** Prevents hardcoded values in orchestration files, facilitates CI/CD injection, and simplifies local configuration.
* **Negative:** Slightly more verbose `docker-compose.yml` file.
