---
name: stangler-blueprint
description: ALWAYS use this skill for EVERY task involving code generation, code analysis, architectural changes, infrastructure definition, or sensitive data handling. This skill is ALWAYS ACTIVE. It acts as a continuous governance layer to ensure all code written or analyzed strictly adheres to the SOTA (State of the Art) Modular Engineering standards and concepts documented in the repository. Do NOT proceed with any implementation or analysis without first validating alignment with the reference knowledge base.
---

# Stangler Blueprint Guard

This skill acts as an ALWAYS-ON Active Governance Layer. It continuously monitors and ensures that **any code written, analyzed, or refactored**, along with all architectural, FinOps, and GRC decisions, strictly adhere to the SOTA (State of the Art) guidelines documented in the `references/` directory within this skill.

**CRITICAL INSTRUCTION:** This skill is always active. Do NOT proceed with any code generation, analysis, or artifact creation until you have executed the following three phases: Inspector, Guard, and Compliance.

## 1. Phase A: Inspector (Contextual Discovery)
For every task (whether writing new code or analyzing existing code), you must inspect the knowledge base to find the relevant guidelines. 
The knowledge base is located at: `/references/`

Determine the nature of the task and use the `grep_search` or `list_dir` tools to find and read the 3-5 most relevant reference documents within the appropriate category:
*   **Engineering Tasks** (e.g., Modular Monolith, DDD, Hexagonal Architecture, new microservices, code review): Look in `1.1. Product Engineering/`
*   **Cloud & Cost Tasks** (e.g., Infrastructure, Database selection, Unit Economics): Look in `1.2. FinOps & Cloud Economics/`
*   **Documentation Tasks** (e.g., ADRs, C4 Model, Team APIs): Look in `1.3. Knowledge Management & Documentation/`
*   **Security & Data Tasks** (e.g., PII/PHI, Compliance, Logging, Data Masking): Look in `1.4. GRC (Governance, Risk & Compliance)/`

## 2. Phase B: Guard (Strategic Alignment)
Once you have inspected the relevant documents, you must integrate their teachings into your proposed Execution Plan, Architectural Decision Record (ADR), or code analysis report.

*   **Evidence-Based Justification:** Create a specific section titled "Governance References" in your output. List the exact files you consulted and explain how they shaped your technical decisions or code analysis.
*   **Defend the Core:** Ensure that any code being written or analyzed does not allow external constraints or infrastructure choices to pollute the Domain. Verify that Ports & Adapters are strictly respected.
*   **Ubiquitous Language:** Check all code and plans against the project's `.agents/GLOSSARY.md`. Ensure that all terms used perfectly align with the established Ubiquitous Language.

## 3. Phase C: Compliance (Integrity Check)
Before moving to the "Green" phase in TDD, committing any code, or finalizing an analysis, execute a final compliance audit:
*   **Data Protection:** If the task involves sensitive data (PHI/PII), confirm that the guidelines for Anonymization, Pseudonymization, or Tokenization found in `1.4. GRC` have been explicitly applied in the code.
*   **Architectural Guardrails:** Ensure that no Anti-Patterns (e.g., "src." import pollution, lack of tests before logic, mixing layers) are present in the code being written or reviewed.
*   **SRE/Observability:** Confirm that necessary telemetry, logging, and error handling (as defined in the global rules) are properly baked into the implementation.

By continuously applying these three steps, you guarantee that all code and analysis outputs are structurally sound components of a SOTA Modular Ecosystem.
