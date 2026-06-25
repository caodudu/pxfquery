# T-048 forward_query_core_m1 — Protocol

## Objective
Implement the M1 forward query core for PxFquery. The implementation must follow the T-042 API/demo contract exactly and must access all M1 fixture data through the T-046 loader API. Deliver reusable forward query code plus in-task structured JSON demo evidence, including the required no-hit behavior.

## Position In Project
T-048 is a development task in `goal_m1_python_package_v2`. It turns the accepted M1 contract from T-042 and the accepted fixture loader from T-046 into the first deterministic forward query implementation. This task is not a full production-data task, not a reverse-query task, and not a resolver/LLM task.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Authoritative API, CLI, JSON shape, and no-hit/error contract. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Exact forward demo case and pass/fail assertions, including no-hit variants. |
| A-003 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md` | Secondary human-readable orientation for scope and constraints. |
| A-004 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Loader implementation that must be used for all fixture data access. |
| A-005 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for correct use of `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-006 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Optional evidence that the loader passed fixture structure checks before this task. |

## Execution Steps
1. Read A-001 and A-002 first. Extract only the forward query contract, forward demo case, output JSON shape, pass/fail assertions, and no-hit/error requirements.
2. Read A-005 and inspect A-004 as needed to use the T-046 loader API correctly.
3. Create a task-local implementation of the M1 forward query core under `3_execution/` while developing, then place accepted reusable code under `4_artifact/1_package/`.
4. Implement deterministic forward query behavior for the T-042 forward contract. Data access must call the T-046 loader API; do not parse fixture files directly.
5. Implement required no-hit behavior from T-042 as first-class behavior, not as an afterthought or manual report note.
6. Run an in-task demo/smoke script that exercises the forward demo case and required no-hit case(s), writing structured JSON evidence under `4_artifact/2_persist/`.
7. Compare observed JSON against the T-042 expected shape and assertions. Record pass/fail status in a concise evidence table or JSON summary.
8. Write completion and human-facing report files that state what was implemented, which contract assertions passed, and any unresolved loader/API gaps.

## Constraints
- Follow T-042 exactly for public API names, input fields, output JSON shape, and no-hit/error behavior.
- Use T-046 loader API for all M1 fixture data access.
- Do not write a private ad hoc loader, fixture reader, manifest parser, CSV/TSV reader, or direct matrix/index parser.
- Do not treat mock data as a replacement for the T-046 fixture loader.
- Keep this task scoped to forward query core behavior. Reverse query, LLM interpretation, resolver logic, plotting, and production-scale resource hardening are out of scope.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- If the T-046 loader API is insufficient, document the precise missing interface and stop or degrade only with an explicit compatibility note; do not bypass the loader.

## Forbidden
- Reading or parsing `2_project_asset/`.
- Directly reading fixture package internals or predecessor raw assets instead of using the registered T-046 loader API.
- Using T024-T040 outputs, migrated raw code, or legacy project roots as authority for this task.
- Changing the T-042 contract silently.
- Implementing reverse query, resolver/LLM behavior, or full production-data ranking claims.

## Web Search Allowance
Allowed: no
Reason: This is a local development task fully configured from selected predecessor handoffs and accepted artifacts. No current external evidence is required.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Forward query package code | `4_artifact/1_package/pxfquery/` | yes |
| Demo/smoke script used to generate evidence | `3_execution/` | yes |
| Structured forward demo JSON evidence | `4_artifact/2_persist/forward_query_demo_evidence_v20260624.json` | yes |
| Structured no-hit JSON evidence | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | yes |
| Contract assertion summary | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | yes |
| Human-readable execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Human-readable result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| Completion report | `5_report/completion.md` | yes |
| AI handoff for downstream tasks | `5_report/handoff_ai_use.md` | yes |

## Acceptance Criteria
- Forward query implementation exists as reusable package code in `4_artifact/1_package/`.
- All fixture data access in the implementation goes through the T-046 loader API.
- The T-042 forward demo case runs and produces structured JSON matching the required output shape.
- Required no-hit behavior runs and produces structured JSON matching the T-042 no-hit/error contract.
- Contract assertion evidence clearly marks pass/fail status for the forward demo and no-hit behavior.
- No private ad hoc loader or direct fixture parser is introduced.
- All accepted/reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules
- Stop if implementing the forward query would require reading `2_project_asset/`.
- Stop if the T-046 loader cannot expose a required matrix/index/metadata object; report the exact missing loader interface instead of reading the data directly.
- Stop if T-042 and T-046 conflict in a way that prevents a contract-compliant forward demo.
- Stop if the task cannot produce structured JSON evidence for both hit and no-hit behavior.

## Delivery Requirements
- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
