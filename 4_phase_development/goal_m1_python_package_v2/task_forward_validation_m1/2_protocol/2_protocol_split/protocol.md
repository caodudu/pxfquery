# T-050 forward_validation_m1 — Protocol

## Objective

Independently validate the M1 forward query implementation delivered by T-059 (same-layer replacement for T-048). Re-run the T-042 forward demo contract case (EGFR/A549/xpr positive hit + no-hit behavior) against the T-059 package and repair fixture, record traceability to package version, loader, fixture/manifest, and output JSON, and produce a pass/fail validation result. This task must not repair the implementation; failures must be reported as validation failures for same-layer repair/retry.

**Note on T-048 vs T-059:** The T-050 meta.yaml references T-048 as the implementation under test, but T-059 is the selected predecessor and is the accepted same-layer replacement for T-048. T-050 validates T-059's output, not T-048's. Use T-059 `4_artifact/1_package/` as the implementation under test.

## Position In Project

This task sits under `goal_m1_python_package_v2` in the development phase. T-059 has already delivered the forward query core package plus a synthetic repair fixture that bridges the T-042 EGFR/A549/xpr demo contract gap. T-050 independently re-runs that demo to confirm the implementation is reproducible and the contract assertions hold from an independent perspective.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-059/D-001 | `4_artifact/1_package/` | M1 forward query package under validation |
| A-002 | T-059/D-003 | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Fixture to re-run the positive demo |
| A-003 | T-059/D-002 | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Traceability to fixture provenance and loader boundary |
| A-004 (optional) | T-059/D-004 | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Reference positive output for comparison |
| A-005 (optional) | T-059/D-005 | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Reference no-hit output for comparison |
| A-006 (optional) | T-059/D-006 | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Reference assertion outcome table |

All asset paths are under the T-059 task directory at `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/`.

## Execution Steps

1. **Environment setup.** Install or configure the T-059 package from `A-001` into the pxfquery conda environment. Record the installed package version (`pip show pxfquery` or equivalent).
2. **Fixture loading smoke test.** Load the repair fixture `A-002` using the T-046-compatible `M1FixtureLoader` (or equivalent loader API in the package). Assert that the fixture loads without error and the xpr matrix has the expected shape (5 obs x 7 vars per the manifest). Record the loader class and path.
3. **Positive forward demo.** Run the EGFR/A549/xpr forward query against the loaded fixture. Collect the returned JSON/dict output. Verify:
   - `found` is `true`
   - `perturbation` is `EGFR`
   - `cell_line` is `A549`
   - `n_obs` is a positive integer
   - `top_activated` is a non-empty numeric dict
   - `top_suppressed` is a non-empty numeric dict
   - Input echo matches the requested perturbation and cell line
4. **No-hit forward demo.** Run a forward query for an unknown perturbation (e.g. `UNKNOWN_GENE_XYZ999`) against the same fixture. Verify:
   - Output is a structured error/no-hit object (e.g. `{"error": "PerturbationNotFound", ...}`)
   - No Python traceback leaks into the output
   - A relevant error message and suggestions are present
5. **Compare with reference.** Compare the re-run positive JSON (step 3) with the reference evidence `A-004`. Structural shape and key fields should match. Numerical values may differ — focus on structural consistency.
6. **CLI smoke test.** Invoke the forward query via CLI (`pxfquery forward ...`) for the positive case. Assert that stdout contains valid JSON and exit code is 0.
7. **Record traceability.** In the validation report, record:
   - Package version (from `pip show pxfquery` or `importlib.metadata`)
   - Loader class and path
   - Fixture manifest path and synthetic_repair provenance label
   - Reference evidence paths used for comparison
   - All re-run output JSON content
8. **Produce pass/fail result.** Compile a validation results table (CSV) with one row per check (import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo), each marked PASS/FAIL.

## Constraints

- Do not repair core logic — this is independent validation only.
- Do not modify T-059 artifacts or any predecessor task outputs.
- Failures must produce evidence for same-layer repair/retry, not silent workaround.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Preserve the `synthetic_repair` provenance label when referencing the repair fixture. Do not strip or rename it.

## Forbidden

- Modifying T-059 package code, fixture, manifest, or JSON evidence.
- Modifying any upstream completed task output.
- Introducing new synthetic data or bridging fixtures.
- Reading project-level raw assets under `2_project_asset/`.
- Using T-048 `4_artifact/` as accepted reference (use T-059 artifacts only).
- Using T024-T040 blocked assets.

## Web Search Allowance

Allowed: no
Reason: All required contract assertions and reference evidence are available from predecessor T-059.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Smoke execution log | `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | yes |
| Re-run positive forward JSON | `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | yes |
| Re-run no-hit forward JSON | `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | yes |
| Validation results table | `4_artifact/5_table/forward_validation_results_v20260624.csv` | yes |
| Validation report (MD) | `4_artifact/3_document/forward_validation_report_v20260624.md` | yes |
| Execution report (HTML) | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report (HTML) | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria

- All required deliverables exist under `4_artifact/` with correct paths.
- Validation results CSV records one PASS/FAIL per check (≥6 checks: import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo).
- All FAIL results include a clear reason and evidence path.
- Traceability record includes package version, loader identity, fixture manifest path, synthetic_repair provenance label, and reference evidence paths.
- Positive re-run output structurally matches the T-059 reference evidence (same key fields, same found=true).
- No-hit re-run output contains a structured error object, not a raw Python traceback.

## Failure / Stop Rules

- If the T-059 package cannot be imported or installed → mark import FAIL and stop. This is a precondition failure.
- If the repair fixture cannot be loaded by the package's loader → mark fixture load FAIL and stop. The fixture may be incompatible.
- If the positive demo returns found=false or errors → mark positive demo FAIL and continue to collect evidence. Do not repair.
- If the no-hit demo produces a raw traceback instead of a structured error → mark no-hit FAIL and continue. Collect the traceback as evidence.
- Zero FAIL results → overall verdict PASS. One or more FAIL results → overall verdict FAIL.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
