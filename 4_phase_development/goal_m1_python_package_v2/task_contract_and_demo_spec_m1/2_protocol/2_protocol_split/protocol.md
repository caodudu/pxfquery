# T-042 contract_and_demo_spec_m1 — Protocol

## Objective

Define the single minimal M1 contract for the PxFquery Python package. The execution task must produce a compact API contract, CLI contract, forward demo case, reverse demo case, output JSON schema, no-hit/error behavior, and pass/fail criteria for downstream M1 implementation tasks.

This is a specification task only. It must not implement package code, run package tests, rebuild indexes, analyze raw data, or rewrite the full product design.

## Position In Project

T-042 sits at the start of `goal_m1_python_package_v2`. It translates the authoritative T-007 development-state digestion and T-013 MVP run-through review into a small M1 contract that later implementation and validation tasks can follow without inventing names, argument shapes, output schemas, demo inputs, or acceptance rules.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Anchor source authority, package identity, and safe carry-forward boundaries. |
| A-002 | T-007/D-002 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Keep the M1 contract faithful to the actual PxFquery tool and known component readiness. |
| A-003 | T-007/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Cross-check unsafe claims, scope boundaries, and no-hit/error behavior. |
| A-004 | T-013/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Primary authority for M1 required capabilities, gate capabilities, out-of-scope items, and prohibited claims. |
| A-005 | T-013/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Define negative cases and capabilities M1 must not claim. |
| A-006 | T-013/D-003 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Optional compact cross-check for pass/fail criteria. |
| A-007 | T-013/D-004 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/6_archive/pxfquery_t013_run_evidence_bundle_v20260618/` | Optional evidence-shape reference for prior forward, reverse, and no-hit examples; do not treat as current implementation output. |

## Execution Steps

1. Read A-001, A-002, A-004, and A-005 first; use A-003, A-006, and A-007 only as targeted cross-checks.
2. Extract only M1-relevant facts: package purpose, `(B, P, F)` model, forward query intent, reverse query intent, biological context fields, deterministic evidence boundaries, known missing capabilities, and unsafe claims to avoid.
3. Define a compact Python API contract with exact function names, required parameters, optional parameters, return JSON-like structures, and error/no-hit structures.
4. Define a compact CLI contract with exact command names, required flags, demo commands, output mode, exit behavior, and nonzero/error behavior.
5. Define exactly one forward demo case and exactly one reverse demo case. Each case must include exact input fields, expected output JSON shape, minimum required semantic content, and pass/fail assertions.
6. Define no-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior as deterministic contract-level outputs rather than uncaught crashes.
7. Write only the expected contract deliverables under `4_artifact/`, register them in `4_artifact/registry.yaml`, and summarize completion in `5_report/completion.md`.

## Constraints

- Do not implement code, run package tests, rebuild indexes, analyze raw matrices, or create package release artifacts.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not read the historical source root directly.
- Do not use T024-T040 outputs as authoritative inputs.
- Keep the contract small, deterministic, and directly actionable for T048, T049, and T052.
- M1 acceptance must not depend on LLM resolver success.
- Any uncertain biological or data-specific detail must be expressed as a validation requirement for later M1 implementation or validation tasks, not guessed here.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading `/Users/dudu/Documents/3_Project/8_functional_query`.
- Reading or citing failed/polluted T024-T040 task outputs as authorities.
- Expanding the task into full product design, manuscript strategy, package implementation, or algorithm repair.
- Calling downstream CyHex prompt endpoints from this configuration or execution task.

## Web Search Allowance

Allowed: no

Reason: The M1 contract must be derived from local authoritative predecessor outputs T-007 and T-013. No current external or web evidence is needed to define API, CLI, demo cases, no-hit/error behavior, or pass/fail criteria.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Structured API and CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | yes |
| Exact forward and reverse demo cases with assertions | `4_artifact/2_persist/m1_demo_cases.yaml` | yes |
| Short human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | yes |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion note | `5_report/completion.md` | yes |

## Acceptance Criteria

- The API and CLI contracts specify exact names, argument fields, optional fields, output schema, and error/no-hit schema.
- The forward demo case and reverse demo case are concrete, traceable to T-007/T-013 context, and include pass/fail assertions.
- No-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior are specified without requiring LLM availability.
- The contract states that deterministic forward and reverse behavior is M1 scope, while natural-language resolver success and broad biological generalization are out of scope unless later validated.
- T024-T040 are excluded as authorities.
- All accepted/reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop if execution cannot define the M1 contract without reading raw project assets or the legacy source root.
- Stop if T-007 and T-013 artifacts are missing or too contradictory to support a deterministic contract.
- Stop if the work would require implementation, package repair, matrix analysis, index rebuilding, or web evidence.
- Stop if demo-case details cannot be made traceable to T-007/T-013 without guessing; record the missing precondition in `5_report/completion.md`.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
