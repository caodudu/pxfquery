# Check Handoff Before Exec: T-060 reverse_query_core_repair_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1`
- Allowed write dirs: task-local `3_execution/`, `4_artifact/`, and `5_report/`.
- Forbidden dirs: predecessor task directories, `1_project_init/`, `2_project_asset/`, legacy/raw asset roots, and T024-T040 blocked assets.
- Required registry: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/1_asset/registration.yaml`
- Must stop if: satisfying the T-042 reverse positive demo requires forbidden raw project assets, blocked T024-T040 assets, editing upstream completed artifacts, silently changing the T-042 contract, or presenting synthetic/repair content as original raw LINCS/CMAP data.

## Objective Restatement
T-060 is a same-layer replacement for failed T-049 reverse-query core delivery. Execution must use T-049 only as an incident reference, create a task-local synthetic/repair reverse substrate that honestly supports the T-042 positive reverse demo including `HALLMARK_MYC_TARGETS_V1`, then implement and verify the M1 reverse query core with deterministic scoring/ranking, structured JSON output, no-hit/error behavior, runnable demo evidence, provenance reporting, and registered reusable outputs.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | Authoritative reverse demo case and pass/fail assertions. | ok |
| A-003 | `1_asset/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. | ok |
| A-004 | `1_asset/fixture_package_m1` | Original small M1 fixture package for registered fixture inspection and repair-substrate bridging. | ok |
| A-005 | `1_asset/expected_shapes_keys_columns_m1.csv` | Expected shapes, columns, keys, and validation rules. | ok |
| A-006 | `1_asset/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. | ok |
| A-007 | `1_asset/package_skeleton_pyproject.toml` | Canonical package metadata and editable package shape. | ok |
| A-008 | `1_asset/package_skeleton_src` | Base package skeleton to extend with reverse-query implementation. | ok |
| A-009 | `1_asset/m1_fixture_loader_code.py` | Accepted M1 fixture loader implementation. | ok |
| A-010 | `1_asset/m1_loader_api_reference.md` | Loader API reference for compatible reverse-core implementation. | ok |
| A-011 | `1_asset/m1_loader_smoke_evidence.csv` | Accepted fixture-loader smoke evidence and coverage boundary. | ok |
| A-012 | `1_asset/index_health_summary.json` | Optional known index health and schema-gap context. | ok |
| A-013 | `1_asset/loader_hardening_m1_code.py` | Optional hardened loader implementation reference. | ok |
| A-014 | `1_asset/loader_gap_list_m1.md` | Optional known loader/index gap reference. | ok |
| A-015 | `1_asset/t049_completion_incident_reference.md` | Reference incident explaining why T-049 did not satisfy the reverse demo. | ok |

## Execution Strategy
1. Read A-001 and A-002 first; extract the exact reverse API/CLI contract, JSON fields, expected positive demo, ranking assertions, and no-hit/error conventions. Output an implementation checklist in `3_execution/`.
2. Read A-003 through A-011 through the registered task-local links; verify the selected fixture/manifest gap for `HALLMARK_MYC_TARGETS_V1` and loader compatibility. Use A-012 through A-014 only if they reduce ambiguity about index shape or loader hardening.
3. Create a minimal task-local reverse repair substrate in `4_artifact/2_persist/`, with a manifest and fixture/supplement sufficient for the T-042 reverse positive case. Explicitly label copied predecessor-derived material versus synthetic/repair records.
4. Build package code under `4_artifact/1_package/pxfquery/` from the T-044 skeleton and T-046 loader API. Keep the ranking finite, deterministic, and stable under ties with documented sort keys.
5. Implement contract-compatible no-hit and error handling for missing program, missing context, empty or low-confidence results, and invalid/no-matrix cases required by A-001/A-002.
6. Run import/compile checks and the reverse positive demo in `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`; save visible structured JSON evidence and command provenance.
7. Run repeatability and no-hit/error smoke cases; compare JSON shape and ranking stability against the T-042 contract.
8. Register reusable outputs in `4_artifact/registry.yaml`, write provenance/result/execution reports, and write `5_report/completion.md` only after the evidence is present.

## Conservative Execution Advice
- Start with: a small contract extraction and loader smoke check against registered fixture paths before creating or copying any reusable output.
- Smoke/demo command or method: run package import/compile checks, then a single reverse positive demo command in the `pxfquery` conda environment against the task-local repair manifest; repeat once to verify stable ranking.
- Full run only after: the repair substrate loads through the accepted loader path or a documented compatible bridge, and the first JSON output matches T-042 field names and success/no-hit/error conventions.
- Cost/time risk: expected low compute and no network; highest risk is schema mismatch between repair substrate, T-042 contract, and T-046 loader behavior.
- Checkpoint advice: preserve intermediate command logs or scripts in `3_execution/`, but copy only accepted reusable artifacts into `4_artifact/`.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reverse query package code | `4_artifact/1_package/pxfquery/` | Imports/compiles and exposes contract-compatible reverse query behavior. |
| Reverse repair fixture package or supplement | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Contains enough task-local synthetic/repair support for the T-042 positive reverse demo. |
| Reverse repair manifest | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Loads or bridges through the accepted fixture semantics without modifying upstream assets. |
| Repair provenance report | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | Clearly separates copied predecessor material from synthetic/repair content and states it is not raw LINCS/CMAP data. |
| Reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Visible structured JSON includes `HALLMARK_MYC_TARGETS_V1` case and satisfies T-042 assertions. |
| Reverse no-hit/error JSON evidence | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | No-hit/error cases are structured JSON, not uncaught tracebacks. |
| Ranking/scoring evidence | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Documents deterministic scores, rank order, finite filtering, and tie-break keys. |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Records commands, environment, checks, and observed outcomes. |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Summarizes final behavior, limitations, and downstream use guidance. |
| Artifact registry | `4_artifact/registry.yaml` | Registers all reusable task outputs with provenance and status. |
| Completion report | `5_report/completion.md` | States final status, evidence paths, and any limitations without marking T-049 complete. |

## Failure / Stop Conditions
- Stop if the T-042 reverse positive demo cannot be satisfied from registered inputs plus a task-local synthetic/repair substrate.
- Stop if execution would need `2_project_asset/`, raw project assets, or T024-T040 blocked assets.
- Stop if upstream completed artifacts would need to be edited.
- Stop if the only way to pass is to change or weaken the T-042 API/demo contract without explicit compatibility documentation.
- Stop if repair records cannot be honestly labeled as synthetic/repair support.
- Stop if JSON evidence cannot be produced in the `pxfquery` conda environment.

## Notes For Delivery QA
- QA should verify that all accepted outputs are in `4_artifact/`, not only in `3_execution/`.
- QA should inspect JSON evidence for T-042 field compatibility, stable ranking across repeated runs, visible no-hit/error handling, and inclusion of `HALLMARK_MYC_TARGETS_V1`.
- QA should confirm the provenance report does not overclaim repair fixture content as original raw data.
- QA should confirm T-049 remains only a reference incident and is not marked complete or modified.
- QA should confirm no web search or external data acquisition was used.
