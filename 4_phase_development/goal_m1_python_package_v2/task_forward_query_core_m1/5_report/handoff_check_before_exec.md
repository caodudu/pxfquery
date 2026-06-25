# Check Handoff Before Exec: T-048 forward_query_core_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories, `1_project_init/`, `2_project_asset/`, `/Users/dudu/Documents/3_Project/8_functional_query/`
- Required registry: `1_asset/registration.yaml`
- Must stop if: a required registered asset cannot be read through the task-local symlink/registered path; T-046 loader API cannot expose the needed fixture data; implementation would require direct parsing of fixture internals, raw project assets, or legacy roots; T-042 contract and T-046 loader behavior are mutually incompatible.

## Objective Restatement
Implement the M1 forward query core as reusable package code for the current task. The implementation must follow the T-042 API/demo/no-hit contract exactly and must use the T-046 fixture loader API for all fixture data access. The task must produce code plus structured JSON demo evidence, no-hit evidence, an assertion summary table, reports, artifact registry, completion report, and downstream handoff. It must not implement reverse query, resolver/LLM behavior, plotting, production-scale ranking claims, or private ad hoc loaders.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | Authoritative M1 API, CLI, output JSON shape, no-hit/error contract, and pass/fail expectations. | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | Exact forward demo case and no-hit variants that must be exercised in structured evidence. | ok |
| A-003 | `1_asset/m1_contract_summary.md` | Optional human-readable orientation; secondary to A-001 and A-002. | ok |
| A-004 | `1_asset/m1_fixture_loader_code.py` | Required T-046 loader implementation; all fixture access must go through this API. | ok |
| A-005 | `1_asset/m1_loader_api_documentation.md` | Required loader API reference for correct use of `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. | ok |
| A-006 | `1_asset/m1_loader_smoke_evidence.csv` | Optional context for prior loader readiness. | ok |

## Execution Strategy
1. Read A-001 and A-002 first, extracting the public API/CLI names, accepted input fields, required output JSON fields, ranking fields, no-hit/error behavior, and assertion criteria. Expected output: a short implementation checklist under `3_execution/` or embedded in the smoke script comments.
2. Read A-005 and inspect A-004 only enough to use the T-046 loader correctly. Expected output: confirmed import path, loader construction pattern, returned fixture object shape, and available data access methods.
3. Build a minimal smoke/demo script in `3_execution/` that imports the loader and verifies the registered fixture can be loaded without any direct fixture parsing. Expected output: a small pass/fail loader smoke result before implementing query logic.
4. Implement task-local forward query code during development under `3_execution/`, then copy or package the accepted reusable modules under `4_artifact/1_package/pxfquery/`. Expected output: public API behavior matching A-001, backed only by loader-provided data.
5. Implement no-hit behavior as part of the query function and CLI path, not only in reports. Expected output: structured no-hit response matching A-001/A-002 contract.
6. Run demo and no-hit cases from A-002 through the implemented API/CLI. Expected output: `4_artifact/2_persist/forward_query_demo_evidence_v20260624.json` and `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json`.
7. Compare observed outputs against contract assertions from A-001/A-002. Expected output: `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` with explicit pass/fail rows.
8. Write reports and registration files. Expected output: execution/result HTML reports, `4_artifact/registry.yaml`, `5_report/completion.md`, and `5_report/handoff_ai_use.md` documenting implementation, evidence, limitations, and downstream use.

## Conservative Execution Advice
- Start with: a loader-only smoke check using A-004/A-005 before writing forward query logic.
- Smoke/demo command or method: use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` from the task root to run the `3_execution/` smoke/demo script against the registered assets.
- Full run only after: A-001/A-002 contract fields are mapped to concrete loader-provided fields and the loader-only smoke check passes.
- Cost/time risk: low local compute; no web search, network, API calls, large raw assets, or production-scale data scans should be used.
- Checkpoint advice: after loader smoke and after first demo JSON generation, inspect the output shape before generating all reports. If direct fixture parsing seems tempting, stop and report the missing loader interface instead.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Forward query package code | `4_artifact/1_package/pxfquery/` | Reusable code exists and implements the T-042 forward API/CLI using only the T-046 loader API. |
| Demo/smoke script | `3_execution/` | Script can be rerun with the `pxfquery` conda environment and regenerates the evidence files. |
| Forward demo JSON evidence | `4_artifact/2_persist/forward_query_demo_evidence_v20260624.json` | JSON matches the T-042 expected shape and demo assertions pass. |
| No-hit JSON evidence | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | JSON shows required no-hit behavior from the T-042 contract. |
| Contract assertion summary | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Table lists contract assertions with observed values and pass/fail status. |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Human-readable description of commands, inputs, implementation path, and evidence generation. |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Human-readable summary of demo/no-hit results and contract status. |
| Artifact registry | `4_artifact/registry.yaml` | Registers created artifacts with paths, types, provenance, and status. |
| Completion report | `5_report/completion.md` | States task outcome, acceptance status, commands run, and limitations. |
| Downstream AI handoff | `5_report/handoff_ai_use.md` | Gives downstream tasks enough API, evidence, and limitation context without requiring rediscovery. |

## Failure / Stop Conditions
- Stop if A-001, A-002, A-004, or A-005 is unreadable from the registered task asset path.
- Stop if the loader cannot be imported or cannot expose required fixture data without direct file parsing.
- Stop if matching the T-042 contract requires changing the contract silently.
- Stop if implementation would require reading `2_project_asset/`, predecessor raw assets, arbitrary predecessor folders, or `/Users/dudu/Documents/3_Project/8_functional_query/`.
- Stop if expected demo/no-hit behavior cannot be expressed with the fixture data available through the loader; document the exact missing interface or data field.
- Stop before any web search, external API call, production-scale data run, or dependency installation unless a missing local dependency is truly required and is recorded in the task output.

## Notes For Delivery QA
- Confirm the final reusable implementation is under `4_artifact/1_package/`, not only under `3_execution/`.
- Confirm no direct CSV/TSV/manifest/matrix parsing was introduced outside the T-046 loader API.
- Confirm no-hit behavior is tested with structured JSON evidence and included in the assertion summary.
- Confirm reports do not overclaim production readiness, reverse query support, resolver behavior, LLM interpretation, or use of full LINCS/raw assets.
- Confirm task status is not marked done automatically by execution AI; human/CyHex delivery flow should handle acceptance separately.
