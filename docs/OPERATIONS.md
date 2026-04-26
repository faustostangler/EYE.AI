# 🛠 EYE.AI - Operations & Infrastructure Management Guide

This document describes the functions and commands required to maintain the lifecycle of the local EYE.AI ecosystem, adhering to the principles of Single Source of Truth (SSOT) and Fail-Fast.

## 0. Host Prerequisites (One-Time Setup)

### GPU Access for Docker (NVIDIA Container Toolkit)
The Inference Worker requires GPU access inside Docker. The host must have the NVIDIA Container Toolkit installed.

**Verify driver is working:**
```bash
nvidia-smi
```

**Install NVIDIA Container Toolkit (Ubuntu/Debian):**
```bash
# 1. Add NVIDIA repository
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

# 2. Install toolkit
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit

# 3. Configure Docker runtime and restart
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```

**Verify setup succeeded:**
```bash
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

> **WHY:** The Docker daemon does not have access to the GPU by default. The NVIDIA Container Toolkit injects the GPU device drivers into the container namespace at runtime. Without it, `deploy.resources.reservations.devices` in docker-compose.yml fails to resolve the "nvidia" driver.

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

## 3. Monitoring & Inspection

### Services Logs
Watch the heartbeats of the API and Inference Worker:
```bash
docker logs -f eye_api
docker logs -f eye_worker
```

### Data & Infrastructure
Check Redis keyspace (queues and states):
```bash
docker exec -it eye_redis redis-cli info keyspace
```

Access Qdrant Web Dashboard:
[http://localhost:6333/dashboard](http://localhost:6333/dashboard) (Default API port)

### Hardware Monitoring
Monitor the health and VRAM usage of your RTX 2060:
```bash
watch -n 1 nvidia-smi
```

### Container Shell Access
Inspect the source code or environment inside a running container:
```bash
docker exec -it eye_api sh
# Inside the container:
ls -R /app/src
exit
```

