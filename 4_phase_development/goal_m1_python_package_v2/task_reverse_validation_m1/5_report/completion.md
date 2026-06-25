# Completion — T-051 reverse_validation_m1

## Verdict

**PASS — 42/42 checks passed.**

The M1 reverse query implementation (T-060/T-044) is validated as functionally correct against the T-042 contract. All positive demo, no-hit/error, ranking, and CLI checks produce expected outputs.

## Steps Executed

| Step | Description | Result |
|------|-------------|--------|
| 1 | Package provenance — inspected symlink, recorded resolved path, version | PASS |
| 2 | Fixture loading via M1FixtureLoader — confirmed xpr shape (15×9), target columns, A549 | PASS |
| 3 | Positive demo — reverse_query(activate=APOPTOSIS, suppress=MYC_TARGETS_V1, cell=A549, top_n=3) — output matches reference | PASS |
| 4 | No-hit/error cases — NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, empty-target no-hit | PASS |
| 5 | Ranking comparison — observed top-3 sig_ids/similarity/order match reference JSON and CSV | PASS |
| 6 | CLI smoke — `info` and `reverse` commands run, correct exit codes, correct JSON output | PASS |
| 7 | Validation report written — structured JSON with per-check pass/fail, explicit verdict | PASS |
| 8 | Artifact registry written | PASS |

## Traceability

| Attribute | Value |
|-----------|-------|
| Package version | 0.1.0 |
| Package code path | `1_asset/reverse_query_package_code` (symlink) |
| Resolved symlink target | `task_package_skeleton_m1/4_artifact/1_package/pxfquery` (T-044) |
| Loader | `pxfquery.data.m1_loader.M1FixtureLoader` |
| Manifest ID | `reverse_repair_manifest_m1_1` |
| Fixture | `reverse_repair_fixture_m1_1` (xpr: 15×9) |
| Ranking/scoring method | Cosine similarity (target vector +1 activate / -1 suppress) |
| Sort keys | similarity desc, cmap_name asc, cell_iname asc, sig_id asc |

## Deliverables

| Deliverable | Path | Required |
|---|---|---|
| Validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | yes |
| Comparison table (CSV) | `4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | recommended |
| Validation report (HTML) | `4_artifact/3_document/validation_report_v20260624_055812.html` | recommended |
| Smoke logs & evidence | `3_execution/` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Caveats

- The package code is a symlink to T-044 (`task_package_skeleton_m1`), not a self-contained local copy. This is a known structural observation (recorded in T-060 delivery_qa) but does not affect functional correctness.
- The ranking comparison checked top-3 against reference (matching the `top_n=3` protocol parameter). The full reference has 10 candidates; the first 3 match exactly.
