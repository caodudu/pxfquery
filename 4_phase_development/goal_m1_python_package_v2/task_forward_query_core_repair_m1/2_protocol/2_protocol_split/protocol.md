# T-059 forward_query_core_repair_m1 — Protocol

## Objective

Create a same-layer repair/replacement for T-048 `forward_query_core_m1`. T-048 is only a reference incident showing that the T-042 required forward demo case `EGFR/A549/xpr` cannot be satisfied by the currently selected T-046 fixture assets.

This task must deliver a working M1 forward query core plus a task-local repair substrate, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly supplies the missing positive demo case without modifying completed T-042, T-043, T-044, T-046, or T-047 outputs. The repair substrate must be labeled as synthetic/repair provenance, not as original raw data.

## Position In Project

T-059 replaces T-048 for downstream forward-query work. It does not reopen T-048, mark T-048 as successful, or alter upstream completed artifacts. Downstream tasks should consume T-059 outputs as the authoritative M1 forward-query core repair deliverable.

Because seven predecessor tasks are selected, execution should use the registered handoff-derived assets only. If the executor finds that more predecessor context is needed beyond the registered assets, stop and recommend an intermediate digestion/integration task instead of expanding into broad predecessor reading.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Contract authority for public API, CLI shape, JSON output, no-hit behavior, and error semantics. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Defines the exact required forward demo case and assertions, including `EGFR/A549/xpr`. |
| A-003 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml` | Baseline M1 resource/fixture manifest to preserve compatibility and describe existing substrate boundaries. |
| A-004 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/` | Existing deterministic fixture package that must remain unchanged and should be extended only through a task-local repair substrate. |
| A-005 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Fixture schema and expected structure reference for any repair supplement. |
| A-006 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv` | Traceable sample-record context and fixture content reference; useful for documenting the missing positive case. |
| A-007 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml` | Base package metadata and src-layout anchor. |
| A-008 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/` | Base package skeleton to extend with forward-query code. |
| A-009 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Prior import-smoke baseline to replicate after implementation. |
| A-010 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Loader implementation that forward query must use or remain compatible with. |
| A-011 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-012 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Evidence that baseline fixture loading worked before the repair. |
| A-013 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened loading behavior; not required to replace the T-046 API. |
| A-014 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap context if the executor needs to compare repair behavior with hardening results. |
| A-015 | T-048 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/completion.md` | Reference incident report documenting the EGFR/A549/xpr fixture gap and failed assertion. |

## Execution Steps

1. Stage a task-local working package in `3_execution/` from T-044 package metadata/skeleton, then integrate T-046 loader code or a compatibility-preserving copy of it.
2. Read the T-042 API/demo contract and identify the exact forward output fields, no-hit object, error behavior, and pass/fail assertions that must be satisfied.
3. Confirm from the registered T-043/T-046 context that the baseline fixture lacks the `EGFR/A549/xpr` positive case. Do not treat this confirmation as a reason to modify upstream fixture assets.
4. Create a task-local repair substrate under `4_artifact/2_persist/`, such as `forward_repair_manifest_m1_1.yaml` plus `forward_repair_fixture_m1_1/`, that adds the minimal positive demo case needed for T-042. Mark the substrate as `synthetic_repair` or equivalent provenance and explain that it is a contract bridge, not original raw data.
5. Implement the forward query core through the loader-compatible data access layer. Do not write a private ad hoc parser that bypasses the loader contract unless a clear compatibility wrapper is documented.
6. Implement required no-hit behavior and structured JSON output exactly as T-042 specifies.
7. Run the forward demo for the positive `EGFR/A549/xpr` case and at least one no-hit case. Save visible structured JSON evidence in `4_artifact/2_persist/`.
8. Produce an assertion table showing pass/fail for T-042 forward-demo requirements, package import smoke, loader compatibility, positive-hit behavior, no-hit behavior, and provenance labeling.
9. Write a concise provenance/report document explaining how T-059 replaces T-048, what was synthetic/repair, what remained upstream, and why no upstream completed artifacts were modified.

## Constraints

- Treat T-042 as the contract authority for forward API/demo behavior and JSON shape.
- Treat T-043/T-046 as the baseline fixture and loader boundary; extend through a task-local repair substrate only.
- Treat T-044 as the package skeleton source; keep package name `pxfquery` and src-layout conventions.
- T-047 may be used only as optional hardening reference.
- T-048 may be used only as a blocked incident reference; do not reuse its unaccepted code or evidence as authoritative deliverables.
- The repair substrate must clearly state synthetic/repair provenance and must not be represented as original LINCS/raw project data.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Use the configured Python environment unless a documented package/runtime issue requires a narrow exception: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.

## Forbidden

- Do not modify T-042, T-043, T-044, T-046, T-047, or T-048 task outputs.
- Do not mark T-048 done or green.
- Do not use T024-T040 blocked assets.
- Do not read or use project-level raw assets under `2_project_asset/`.
- Do not claim biological ranking validity or full-resource coverage from the minimal repair fixture.
- Do not perform web search for this task.

## Web Search Allowance

Allowed: no

Reason: The task is a local package repair and fixture-bridge implementation. All needed contract, fixture, skeleton, loader, and incident context is available from selected predecessor handoffs and registered artifacts.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Task-local package metadata and implemented package source | `4_artifact/1_package/` | yes |
| Repair fixture/manifest or contract-bridge supplement with synthetic/repair provenance | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` and/or `4_artifact/2_persist/forward_repair_fixture_m1_1/` | yes |
| Positive forward demo JSON evidence | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | yes |
| No-hit forward demo JSON evidence | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | yes |
| Contract assertion table | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | yes |
| Provenance and T-048 replacement report | `4_artifact/3_document/forward_query_core_repair_report_v20260624.md` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria

- The forward positive demo `perturbation=EGFR`, `cell_line=A549`, `matrix_type=xpr` runs and emits visible structured JSON conforming to T-042.
- The positive demo result reports `found=true` or the exact T-042 equivalent.
- At least one no-hit demo runs and emits the T-042 no-hit JSON shape without crashing.
- The implementation uses or preserves compatibility with the T-046 loader API.
- The repair substrate is task-local, registered as a reusable T-059 output, and labeled with synthetic/repair provenance.
- No upstream completed task artifacts are modified.
- T024-T040 blocked assets and `2_project_asset/` raw assets are not used.
- `4_artifact/registry.yaml` registers accepted/reusable outputs, including package code, repair substrate, JSON evidence, assertion table, and reports.

## Failure / Stop Rules

- Stop if the executor cannot create a transparent task-local repair substrate without reading forbidden raw assets.
- Stop if satisfying T-042 would require changing T-042, T-043, T-044, or T-046 outputs.
- Stop if the JSON shape required by T-042 is ambiguous after reading A-001 and A-002; report the exact ambiguity rather than guessing.
- Stop if more than the registered predecessor assets must be understood together; recommend an intermediate integration/digestion task.
- Stop if implementation would require using T024-T040 blocked assets.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
