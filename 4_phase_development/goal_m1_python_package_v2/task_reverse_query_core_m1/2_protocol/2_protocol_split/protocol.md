# T-049 reverse_query_core_m1 — Protocol

## Objective

Implement the M1 reverse query core for PxFquery: given functional target intent and biological context, return candidate perturbations using the T-046 fixture loader and the exact T-042 M1 contract. The implementation must provide deterministic ranking/scoring behavior, structured JSON demo evidence, and clear stop reporting if the registered loader/index API cannot support a required contract behavior.

## Position In Project

This is a development task under `goal_m1_python_package_v2`. It follows the M1 contract/demo specification from T-042 and the fixture loader from T-046. It must produce reverse-query implementation evidence only; it must not broaden the product design, inspect raw legacy assets, or build a private data loading path.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 reverse API/CLI contract, JSON shape, errors, no-hit behavior, and scope. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Exact reverse demo case and pass/fail assertions for ranking/scoring evidence. |
| A-003 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md` | Optional orientation for contract boundaries and M1 scope. |
| A-004 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Required loader implementation; all reverse query data access must go through this API. |
| A-005 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for stable public methods and returned structures. |
| A-006 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Optional evidence for expected fixture structures when diagnosing assumptions. |

## Execution Steps

1. Read the registered T-042 contract and demo cases, then extract the reverse query function signature, accepted input fields, output JSON shape, no-hit/error objects, and required pass/fail assertions.
2. Read the T-046 loader API documentation and reusable loader code. Use the loader as the only access path to fixture matrices, indexes, and metadata.
3. Implement the reverse query core in task-local package code, preserving M1 contract names and return fields. Keep the method deterministic and fixture-focused.
4. Define a stable ranking/scoring procedure that can be reproduced from loaded fixture data. Record tie-breaking rules explicitly in code comments or evidence when needed.
5. Run an in-task reverse demo against the T-042 reverse demo case and emit structured JSON evidence under `4_artifact/2_persist/`.
6. Include no-hit/error behavior evidence if the T-042 contract requires it for reverse query.
7. If the loader or fixture index cannot support a required contract behavior, stop implementation at the precise gap and document the missing loader/index capability instead of inventing private data handling.

## Constraints

- Use T-042 as the contract authority for public API shape, CLI-facing behavior, JSON output, errors, and no-hit behavior.
- Use T-046 as the only fixture data access authority.
- Do not write a private ad hoc loader, private manifest reader, direct fixture parser, or direct raw asset reader.
- Ranking/scoring must be deterministic for identical inputs and fixture data.
- Keep the implementation M1-sized: reverse query core, contract compatibility, and demo evidence only.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep scripts, temporary logs, and exploratory notes in `3_execution/`; accepted reusable code/evidence belongs in `4_artifact/`.

## Forbidden

- Do not read `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Do not read or depend on failed T024-T040 assets.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not implement LLM resolver behavior, fuzzy biological interpretation, production resource hardening, plotting, or full-resource claims.
- Do not silently change T-042 contract fields or thresholds; document any unavoidable compatibility gap.

## Web Search Allowance

Allowed: no

Reason: This task can be configured from project protocol plus selected predecessor handoffs and accepted artifacts. No current external information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse query package code integrated with the M1 package structure | `4_artifact/1_package/` | yes |
| Structured reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Optional reverse no-hit/error evidence JSON if required by T-042 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | conditional |
| Concise execution/result report for human review | `4_artifact/3_document/` | yes |
| Optional ranking/scoring validation table | `4_artifact/5_table/` | optional |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- Reverse query code follows the T-042 contract for callable/API behavior and JSON output shape.
- All data access for fixture matrices/indexes/metadata goes through the T-046 loader API.
- The T-042 reverse demo case produces structured JSON evidence with required fields populated.
- Ranking and tie-breaking are deterministic and documented well enough for check-stage reproduction.
- Required no-hit/error behavior is implemented or a precise contract/loader gap is reported.
- No project-level raw assets, direct legacy roots, or T024-T040 assets are used.

## Failure / Stop Rules

- Stop and report a configuration or execution gap if the T-046 loader cannot expose data needed for the T-042 reverse contract.
- Stop rather than create hidden parsing logic if fixture data appear unavailable through the loader.
- Stop if satisfying the reverse query contract would require raw `2_project_asset/` data in this non-digestion task.
- Stop if the only available path depends on T024-T040 artifacts.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
