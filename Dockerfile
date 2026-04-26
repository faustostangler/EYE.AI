# Stage 1: Build & Sync Dependencies using `uv`
FROM python:3.12-slim-bookworm AS builder

# Install build dependencies required for llama-cpp-python
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copy dependency files first to leverage Docker cache
COPY pyproject.toml .
COPY README.md .

# Install dependencies into the system environment to keep the final image clean
RUN uv pip install --system -e .

# Stage 2: Runtime Environment
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source code
COPY ./src ./src

# Set Python path to recognize the src directory
ENV PYTHONPATH=/app

# The command will be overridden by docker-compose for specific roles
CMD ["echo", "Specify a command (API or Worker) in docker-compose.yml"]
