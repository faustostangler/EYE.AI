# ADR 0005: Documentation Strategy - Operations and Infrastructure Management

## Status
Proposed

## Context
As a Modular Monolith with multiple infrastructure dependencies (Redis, Qdrant, Workers), the operational complexity for local development and CI/CD can increase. We need a standardized way to document how to manage, monitor, and troubleshoot the ecosystem.

## Decision
We will maintain an `OPERATIONS.md` file located in the `docs/` directory that serves as the "Runbook" for the project.

## Requirements
1. **SSOT focus:** All commands must prioritize the `Makefile` as the primary interface.
2. **Native Fallbacks:** Include low-level Docker commands for deep debugging.
3. **Troubleshooting:** Must include a section for common environmental conflicts (ports, permissions, VRAM).
4. **Hardware Specifics:** Document safeguards for the RTX 2060 (6GB VRAM) context.

## Consequences
* **Positive:** Reduces onboarding time, ensures environment parity, and centralizes "institutional knowledge" about infra quirks.
* **Negative:** Requires manual updates when the infrastructure changes.
