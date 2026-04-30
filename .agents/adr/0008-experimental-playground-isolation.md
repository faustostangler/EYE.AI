# ADR 0008: Isolation of Experimental Playground

## Status
Proposed (2026-04-30)

## Context
As the project evolves, developers require a space for "dirty" coding, rapid prototyping, and experimental data science spikes (e.g., Jupyter Notebooks for RAG ingestion tuning) that do not yet meet the high standards of Domain-Driven Design (DDD), Hexagonal Architecture, or Test-Driven Development (TDD) enforced in the `src/` directory.

Historically, allowing such experiments in production folders leads to architectural pollution and "Module Identity Mismatches" during pattern matching if relative imports leak.

## Decision
We establish a root-level `playground/` directory as a designated **Dark Folder**. This folder is governed by the following rules:

1.  **Logical Isolation**: Code in `playground/` is NOT part of the official project domain and is excluded from ADR-based design requirements.
2.  **Import Barrier**: Production code in `src/` MUST NEVER import from `playground/`. This is enforced by automated infrastructure tests (`tests/infrastructure/test_playground_isolation.py`).
3.  **Experimental Freedom**: Code within this folder is exempt from strict TDD, Hexagonal layering, and standard docstring requirements.
4.  **No ADR Overhead**: Changes within `playground/` do not require new ADRs or updates to existing ones.
5.  **Transition Protocol**: Any logic proven in the playground that is intended for production must be fully re-implemented in `src/` following the Akita Method (Plan -> Red -> Green -> Refactor).

## Consequences
- **Positive**: Increases developer velocity for exploration.
- **Positive**: Protects the core domain from experimental "noise."
- **Negative**: Risk of "copy-paste" debt if not properly re-implemented when moving to `src/`.
- **Negative**: Potential for duplicate logic between playground spikes and domain services.

## Ubiquitous Language Definition
- **Playground**: A non-production directory for spikes and experimental scratchpads.
- **Dark Folder**: A directory structure that exists within the repository for developer utility but is ignored by architectural integrity checks and production runtime.
