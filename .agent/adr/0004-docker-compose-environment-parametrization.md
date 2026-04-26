# ADR 0004: Docker Compose Environment Parametrization

## Status
Proposed

## Context
To ensure consistency, portability, and "Single Source of Truth" (SSOT) across different environments (development, staging, production), all configuration values in `docker-compose.yml` must be parameterized using environment variables with sensible defaults.

## Decision
All values in `docker-compose.yml` (including image names, versions, container names, ports, and environment variables) MUST use the following format:
`${VARIABLE_NAME:-default_value}`

To maintain a clean project structure, all environment variables for orchestration will be stored in `env/compose.env`. This file acts as the primary SSOT for the Docker ecosystem.

## Implementation Rules
1. **Container Naming:** Use `${COMPOSE_PROJECT_NAME:-eye}_service_name`.
2. **Images:** Use `${IMAGE_NAME:-base}:${IMAGE_TAG:-latest}`.
3. **Ports:** Use `${BIND_IP:-127.0.0.1}:${EXTERNAL_PORT:-8000}:${INTERNAL_PORT:-8000}`.
4. **Environment Variables:** All `environment:` keys must also be parameterized.
5. **File Location:** Use `env_file: - env/compose.env` in `docker-compose.yml`.

## Consequences
* **Positive:** Prevents hardcoded values in orchestration files, facilitates CI/CD injection, and simplifies local configuration.
* **Negative:** Slightly more verbose `docker-compose.yml` file.
