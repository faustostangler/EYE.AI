# 🛠 EYE.AI - Operations & Infrastructure Management Guide

This document describes the functions and commands required to maintain the lifecycle of the local EYE.AI ecosystem, adhering to the principles of Single Source of Truth (SSOT) and Fail-Fast.

## 1. Native Docker Commands (Low-Level Management)

| Function | Command |
| :--- | :--- |
| List active containers | `docker ps` |
| List all containers (including errors) | `docker ps -a` |
| View logs in real-time | `docker logs -f <container_name>` |
| Stop a specific container | `docker stop <name_or_id>` |
| Stop all active containers | `docker stop $$(docker ps -q)` |
| Remove all stopped containers | `docker container prune` |
| Clean orphan volumes and images | `docker system prune -a --volumes` |

## 2. Makefile Commands (Architectural Abstraction)

These commands utilize `docker-compose.yml` and `uv` to ensure the integrity of the Shared Kernel.

| Function | Command |
| :--- | :--- |
| Start ecosystem (API, Worker, Redis, Qdrant) | `make up` |
| Tear down and clean infrastructure | `make down` |
| Execute all tests (TDD Mirrored) | `make test` |
| Run Linter and Formatter (Ruff) | `make lint` |
| Mutation Testing | `make mutate` |
| Sync dependencies | `make sync` |
| Setup local environment (.env & sync) | `make setup` |

## 3. Conflict Resolution (Troubleshooting)

### Port Conflict (e.g., Port 6379 occupied)
If the system fails to start Redis because the port is already allocated on the host:

1. **Identify the invading process:**
   ```bash
   sudo lsof -i :6379
   ```

2. **Disable native service (Recommended for SSOT):**
   ```bash
   sudo systemctl stop redis-server
   sudo systemctl disable redis-server
   ```

3. **Restart the EYE.AI environment:**
   ```bash
   make down && make up
   ```
