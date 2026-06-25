# Check Handoff Before Exec: T-059 forward_query_core_repair_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1`
- Allowed write dirs: task-local `3_execution/`, `4_artifact/`, and `5_report/`
- Forbidden dirs: predecessor task output directories; `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/`; T024-T040 blocked assets; T-048 `4_artifact/`; any future-stage prompt files under `2_protocol/0_prompt/`
- Required registry: `1_asset/registration.yaml`; accepted reusable outputs must also be registered in `4_artifact/registry.yaml`
- Must stop if: T-042 JSON/API semantics are ambiguous after reading A-001/A-002; satisfying the contract requires mutating T-042/T-043/T-044/T-046/T-047/T-048 outputs; raw `2_project_asset/` or T024-T040 inputs are needed; the repair substrate cannot be transparently labeled synthetic/repair; more broad predecessor context is needed than the registered assets provide

## Objective Restatement
Deliver the same-layer replacement that T-048 failed to deliver: a working M1 forward-query package plus a task-local repair substrate that fills the required `EGFR/A549/xpr` positive demo case. T-048 is only an incident reference. The repair must preserve upstream completed artifacts, use or remain compatible with the T-046 loader boundary, emit T-042-shaped structured JSON for both positive-hit and no-hit cases, and document the synthetic/repair provenance clearly.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | T-042 authority for API, CLI, JSON shape, no-hit behavior, and errors | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | T-042 forward demo case and assertions, including `EGFR/A549/xpr` | ok |
| A-003 | `1_asset/resource_manifest_m1.yaml` | Baseline M1 resource/fixture boundary | ok |
| A-004 | `1_asset/fixture_package_m1` | Existing deterministic fixture package to preserve and bridge without mutation | ok |
| A-005 | `1_asset/expected_shapes_keys_columns_m1.csv` | Schema/shape reference for repair fixture compatibility | ok |
| A-006 | `1_asset/sample_records_m1.csv` | Baseline fixture sample-record context | ok |
| A-007 | `1_asset/package_skeleton_pyproject.toml` | Base package metadata and src-layout anchor | ok |
| A-008 | `1_asset/package_skeleton_src` | Package skeleton to extend with forward-query implementation | ok |
| A-009 | `1_asset/import_smoke_evidence.txt` | Prior import-smoke baseline to replicate | ok |
| A-010 | `1_asset/m1_fixture_loader_code.py` | T-046 loader implementation for compatible data access | ok |
| A-011 | `1_asset/m1_loader_api_documentation.md` | Loader API reference for integration | ok |
| A-012 | `1_asset/smoke_evidence_table.csv` | Baseline loader smoke evidence | ok |
| A-013 | `1_asset/loader_hardening_m1_code.py` | Optional T-047 hardening reference only | ok |
| A-014 | `1_asset/loader_gap_list.md` | Optional T-047 known-gap context only | ok |
| A-015 | `1_asset/t048_blocked_completion_report.md` | T-048 incident reference for the missing positive case | ok |

## Execution Strategy
1. Stage a working package in `3_execution/` from A-007/A-008 and add the T-046 loader code or a compatibility-preserving copy from A-010, guided by A-011.
2. Read A-001/A-002 first and extract the exact forward-query callable/CLI contract, JSON fields, no-hit shape, and pass/fail assertions.
3. Confirm the baseline fixture boundary from A-003/A-004/A-005/A-006/A-012 and the T-048 incident from A-015, only enough to justify the missing `EGFR/A549/xpr` repair case.
4. Create a task-local repair substrate in `4_artifact/2_persist/`, preferably `forward_repair_manifest_m1_1.yaml` plus `forward_repair_fixture_m1_1/`, labeled as `synthetic_repair` or equivalent and explicitly not original LINCS/raw data.
5. Implement forward-query package code in the staged package, preserving T-046 loader API compatibility and avoiding private ad hoc parsing unless wrapped and documented as compatibility-preserving.
6. Run a conservative smoke sequence: import smoke, loader compatibility check, positive `EGFR/A549/xpr` demo, and one no-hit demo.
7. Save visible JSON evidence and assertion evidence into `4_artifact/` only after the demo outputs satisfy T-042 shape and behavior.
8. Write provenance/report documents and `4_artifact/registry.yaml`, making clear that T-059 replaces T-048 for downstream use without modifying upstream artifacts.

## Conservative Execution Advice
- Start with: a read-only contract extraction from A-001/A-002 and a minimal import/loader smoke in `3_execution/`
- Smoke/demo command or method: use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`; first import `pxfquery`, then invoke the forward demo for `perturbation=EGFR`, `cell_line=A549`, `matrix_type=xpr`, then run one deliberately unmatched no-hit query
- Full run only after: the staged package imports, the loader-compatible fixture objects can be loaded, and the repair manifest/fixture provenance is explicit
- Cost/time risk: low local CPU/runtime cost; no network or web search is allowed; avoid broad predecessor scanning because it is the main scope risk
- Checkpoint advice: keep temporary scripts/logs in `3_execution/`; only copy accepted package, fixture, evidence, tables, reports, and registry into `4_artifact/`

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Implemented package metadata/source | `4_artifact/1_package/` | Package imports and forward-query API/CLI behavior match T-042 |
| Repair substrate manifest | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Documents minimal `EGFR/A549/xpr` bridge and synthetic/repair provenance |
| Repair fixture package | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Loader-compatible supplement present and not represented as original raw data |
| Positive demo JSON | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Visible structured JSON conforms to T-042 and reports found/positive result |
| No-hit demo JSON | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Visible structured JSON conforms to T-042 no-hit behavior without crash |
| Contract assertion table | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Pass/fail rows cover import, loader compatibility, positive hit, no-hit, JSON shape, and provenance |
| Provenance/replacement report | `4_artifact/3_document/forward_query_core_repair_report_v20260624.md` | Explains T-059 replacement role, T-048 incident use, repair provenance, and untouched upstream artifacts |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Human-readable execution record exists |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Human-readable result summary exists |
| Artifact registry | `4_artifact/registry.yaml` | Registers accepted/reusable T-059 outputs |
| Completion report | `5_report/completion.md` | Summarizes execution, evidence, limitations, and acceptance status |

## Failure / Stop Conditions
- Stop if A-001/A-002 do not define enough JSON/API detail to implement without guessing.
- Stop if the only way to satisfy `EGFR/A549/xpr` is to modify upstream T-042/T-043/T-044/T-046/T-047/T-048 artifacts.
- Stop if the executor needs `2_project_asset/`, T024-T040, web search, or arbitrary predecessor folder scans.
- Stop if T-048 code/evidence is needed as an authority rather than only its completion report as an incident reference.
- Stop if the repair substrate cannot be honestly labeled synthetic/repair or if it would be misleading to downstream users.
- Stop if outputs can only be made to pass by claiming biological ranking validity or full-resource coverage beyond the minimal fixture bridge.

## Notes For Delivery QA
- Confirm no upstream predecessor files were modified.
- Confirm T-048 remains a blocked/incident reference and is not marked successful.
- Confirm A-013/A-014 are treated as optional hardening context, not mandatory contract authority.
- Confirm JSON evidence is visible, structured, and contract-shaped rather than only embedded in logs.
- Confirm `4_artifact/registry.yaml` includes the package code, repair substrate, JSON evidence, assertion table, reports, and provenance document.
