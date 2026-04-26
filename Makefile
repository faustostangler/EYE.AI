# Configuration
COMPOSE_FILE := docker-compose.yml
ENV_FILE := env/compose.env
LOCAL_ENV := .env

.PHONY: help setup build up down logs ps test lint clean sync mutation

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

$(LOCAL_ENV): ## Generate local .env from compose.env for local tools (SSOT)
	@echo "Generating $(LOCAL_ENV) from $(ENV_FILE)..."
	@cp $(ENV_FILE) $(LOCAL_ENV)

setup: $(LOCAL_ENV) sync ## Setup local development environment

build: ## Build Docker images
	docker compose build

up: ## Start all services in the background
	docker compose up -d

down: ## Stop and remove all containers
	docker compose down

logs: ## View logs for all services
	docker compose logs -f

ps: ## Show status of all services
	docker compose ps

sync: ## Sync local dependencies using uv
	uv sync

test: ## Run full test suite (lint, format, pytest)
	uv run ruff check .
	uv run ruff format --check .
	uv run pytest tests/ -v

mutate: ## Run mutation testing
	@echo "🧬 Starting mutation testing with mutmut..."
	uv run mutmut run --paths-to-mutate src/

lint: ## Run ruff and mypy
	uv run ruff check .
	uv run mypy src

clean: ## Remove temporary files and containers
	docker compose down -v
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .coverage .mutmut-cache
