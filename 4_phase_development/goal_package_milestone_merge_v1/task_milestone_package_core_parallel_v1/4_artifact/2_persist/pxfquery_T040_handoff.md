# T-040 Handoff For T-039

Generated: 2026-06-23

## What T-039 Should Consume

T-039 may consume T-040 as the package-core branch artifact:

- Package root: `4_artifact/2_persist/pxfquery-T-040/`
- Lineage: `4_artifact/2_persist/pxfquery_T040_lineage.md`
- Verification evidence: `4_artifact/5_table/pxfquery_T040_test_results.json`
- Demo summary: `4_artifact/5_table/pxfquery_T040_demo_summary.json`
- EGFR/A549 table: `4_artifact/5_table/pxfquery_T040_EGFR_A549_forward_result.csv`
- Reports: `4_artifact/3_document/execution_report_v20260623.html` and `4_artifact/3_document/result_report_v20260623.html`

## Package-Core Capabilities

- Importable `pxfquery` package from `pxfquery-T-040/src`.
- Standard resource loader exposed via `pxfquery.resources`.
- Guarded deterministic forward query exposed via `pxfquery.package_core.create_forward_engine`.
- No-hit guard exposed via `pxfquery.query.no_hit_guard.NoHitGuardForwardQuery`.
- Positive-control forward demo: EGFR/A549/xpr.
- Negative no-hit demos: `egfr_random` and `NONSENSE_ZZZ999`.

## Out Of Scope For T-040

- T-038 reverse-demo/report branch.
- T-030/T-032/T-035/T-036 reverse-query branch outputs.
- Resolver, natural-language, and LLM behavior.
- Promotion into `6_project_deliverable/`.
- Copying standard resource matrix/index/metadata bytes into the package.

## Downstream Notes

T-039 can aggregate this package-core branch without re-reading T-024/T-026/T-029/T-031 directly. If T-039 needs the standard resources, it should keep using the existing T-021 standard resource bundle by reference rather than copying data into the final aggregation task.
