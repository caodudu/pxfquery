# T-050 Forward Validation M1 — Validation Report

**Generated:** 2026-06-24  
**Task:** T-050 forward_validation_m1  
**Objective:** Independently validate the M1 forward query implementation delivered by T-059

## Overall Verdict: **PASS**

All 11 checks passed. Zero failures.

---

## Traceability Record

| Attribute | Value |
|---|---|
| Package version | 0.1.0 (pxfquery) |
| Loader class | `pxfquery.data.m1_loader.M1FixtureLoader` |
| Manifest path | `1_asset/forward_repair_manifest_m1_1.yaml` |
| Fixture root | `1_asset/forward_repair_fixture_m1_1` |
| Provenance label | `synthetic_repair` |
| Reference positive evidence | `1_asset/forward_query_positive_demo_evidence.json` |
| Reference no-hit evidence | `1_asset/forward_query_no_hit_evidence.json` |
| Reference assertions | `1_asset/forward_query_contract_assertions.csv` |

## Execution Summary

### Step 1: Package Install & Import (PASS)
- `pxfquery` v0.1.0 installed from T-059 package (local copy under `3_execution/`)
- Import of `PxFquery` and `M1FixtureLoader` successful

### Step 2: Fixture Loading Smoke Test (PASS)
- Repair fixture loaded via `M1FixtureLoader` without error
- xpr matrix shape: (5, 7) — matches manifest expected shape
- Provenance label: `synthetic_repair`

### Step 3: Positive Forward Demo (PASS)
- `pert2func("EGFR", "A549", matrix_type="xpr")` returned:
  - `found: true`
  - `perturbation: "EGFR"`
  - `cell_line: "A549"`
  - `n_obs: 1` (positive integer)
  - `top_activated`: 4 entries, all numeric
  - `top_suppressed`: 3 entries, all numeric
  - Input echo matches

### Step 4: No-hit Forward Demo (PASS)
- `pert2func("UNKNOWN_GENE_XYZ999", "A549", matrix_type="xpr")` returned:
  - Structured `{"error": "PerturbationNotFound", ...}`
  - No raw Python traceback
  - Error message and suggestions present

### Step 5: Reference Comparison (PASS)
- Positive re-run: all structural keys match (minus `_evidence` field which is T-059 harness-specific)
- No-hit re-run: all structural keys match (minus `_evidence`)
- `found`, `perturbation`, `cell_line` values identical

### Step 6: CLI Smoke Test (PASS)
- `pxfquery forward --perturbation EGFR --cell-line A549 --manifest <path> --fixture-root <path>`
- Exit code: 0
- Stdout: valid JSON with `found: true`, correct perturbation/cell_line

## Validation Results

| check_id | requirement | status | evidence |
|---|---|---|---|
| SMOKE-001 | package import succeeds | PASS | pxfquery v0.1.0 imported successfully |
| SMOKE-002 | T-046 compatible repair fixture loads | PASS | xpr shape=(5, 7) as expected |
| FORWARD-001 | positive EGFR/A549/xpr found=true | PASS | found: true, perturbation: EGFR, cell_line: A549, n_obs: 1 |
| FORWARD-002 | top_activated non-empty numeric dict | PASS | 4 entries, all numeric |
| FORWARD-003 | top_suppressed non-empty numeric dict | PASS | 3 entries, all numeric |
| FORWARD-004 | input echo matches contract | PASS | EGFR/A549 matches requested |
| NOHIT-001 | unknown perturbation returns structured no-hit | PASS | error: PerturbationNotFound |
| NOHIT-002 | no raw Python traceback | PASS | Output is valid JSON dict |
| JSON-001 | positive re-run matches reference structurally | PASS | Keys match (no _evidence) |
| JSON-002 | no-hit re-run matches reference structurally | PASS | Keys match (no _evidence) |
| CLI-001 | CLI exit code 0 with valid JSON | PASS | exit code=0 |

## Deliverables

| Path | Status |
|---|---|
| `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | Produced |
| `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | Produced |
| `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | Produced |
| `4_artifact/5_table/forward_validation_results_v20260624.csv` | Produced |
| `4_artifact/3_document/forward_validation_report_v20260624.md` | Produced |
| `4_artifact/3_document/execution_report_v20260624.html` | Produced |
| `4_artifact/3_document/result_report_v20260624.html` | Produced |
