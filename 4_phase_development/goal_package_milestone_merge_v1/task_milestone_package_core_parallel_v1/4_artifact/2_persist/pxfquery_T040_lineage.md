# T-040 Package-Core Lineage

Generated: 2026-06-23

## Purpose

T-040 creates `pxfquery-T-040`, a package-core milestone branch assembled independently from the T-038 parallel branch. T-039 is the only intended downstream aggregation point.

## Inputs Used

- T-024 `workspace_package_v1`: package base copied from `4_artifact/2_persist/workspace/` into `4_artifact/2_persist/pxfquery-T-040/`.
- T-026 `matrix_loader_v1`: loader behavior integrated into `src/pxfquery/resources.py`.
- T-029 `forward_query_engine_v1`: deterministic EGFR/A549 forward-query behavior used as the package-core positive-control target.
- T-031 `no_hit_guard_v1`: guard behavior integrated into `src/pxfquery/query/no_hit_guard.py`.

## T-040 Integration

- Package base: `4_artifact/2_persist/pxfquery-T-040/`
- New package-core facade: `src/pxfquery/package_core.py`
- Standard resource access: `src/pxfquery/resources.py`
- No-hit guard: `src/pxfquery/query/no_hit_guard.py`
- Public exports updated in `src/pxfquery/__init__.py`
- Workspace metadata updated in `pyproject.toml` and `README.md`

## Resource Handling

The T-021 standard resource bundle was opened by reference at:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources`

No H5AD, JSON index, or CSV metadata bytes were copied into T-040.

## Verification Evidence

Verification command:

`/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/05_run_verification/verify_package_core.py`

Evidence files:

- `4_artifact/5_table/pxfquery_T040_test_results.json`
- `4_artifact/5_table/pxfquery_T040_demo_summary.json`
- `4_artifact/5_table/pxfquery_T040_EGFR_A549_forward_result.csv`

Observed verification:

- Required predecessor paths resolved.
- T-040 package imported.
- T-040 package compiled.
- Loader smoke loaded 19/19 standard resource files.
- `xpr_func_ad.h5ad` loaded as `(132464, 91)` float32.
- EGFR/A549 forward query returned `found=true`, 20 activated terms, and 20 suppressed terms.
- `egfr_random` returned `found=false` through the no-hit guard.
- `NONSENSE_ZZZ999` returned `found=false`.

## T-038 Independence

T-040 did not read, consume, or wait for T-038. The T-040 protocol and asset rules explicitly forbid `../task_milestone_reverse_demo_reports_v1/`. The verification evidence records `t038_not_used=true`.

## Upstream Mutation

No predecessor task directory was modified. T-040-local edits are confined to this task's `3_execution/`, `4_artifact/`, and `5_report/`.
