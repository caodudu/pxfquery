# Check Handoff Before Exec: T-050 forward_validation_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories, T-048 `4_artifact/`
- Required registry: `1_asset/registration.yaml` (all 6 assets preflighted ok)
- Must stop if: package import fails (precondition failure), fixture cannot be loaded (compatibility failure)
- Also stop if T-059 is not installed, then install it first

## Objective Restatement
Independently validate T-059's M1 forward query by re-running the T-042 EGFR/A549/xpr demo against the T-059 package + repair fixture, recording traceability (package version, loader, manifest, reference evidence), and producing pass/fail against contract assertions. No core logic repair — only validation harness files may be touched.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/forward_query_package_m1_repair` → T-059 `4_artifact/1_package/` | M1 forward query package under test | ok |
| A-002 | `1_asset/forward_repair_fixture_m1_1` → T-059 `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Fixture with synthetic EGFR/A549/xpr row (5 obs x 7 vars) | ok |
| A-003 | `1_asset/forward_repair_manifest_m1_1.yaml` | Manifest with `provenance_label: synthetic_repair`, loader boundary info | ok |
| A-004 | `1_asset/forward_query_positive_demo_evidence.json` | Reference positive output for structural comparison | ok (optional) |
| A-005 | `1_asset/forward_query_no_hit_evidence.json` | Reference no-hit output for structural comparison | ok (optional) |
| A-006 | `1_asset/forward_query_contract_assertions.csv` | Reference contract checks already passed by T-059 | ok (optional) |

## Execution Strategy
1. **Install T-059 package.** `pip install -e 1_asset/forward_query_package_m1_repair` in pxfquery conda env. Record version from `pip show pxfquery`.
2. **Fixture loading smoke test.** Use `PxFquery(manifest_path=A-003, fixture_root=A-002)` or `M1FixtureLoader` directly. Assert `xpr` matrix shape is (5, 7). Record loader class = `M1FixtureLoader`.
3. **Positive forward demo.** Call `PxFquery.pert2func("EGFR", "A549", matrix_type="xpr")`. Verify `found=true`, `perturbation=EGFR`, `cell_line=A549`, `n_obs` positive int, `top_activated` and `top_suppressed` non-empty numeric dicts, input echo matches.
4. **No-hit forward demo.** Call `pert2func("UNKNOWN_GENE_XYZ999", "A549")`. Verify structured `{"error": "PerturbationNotFound", ...}`, no raw traceback, error message and suggestions present.
5. **Compare with reference (A-004/A-005).** Structural key match only — numerical values may differ.
6. **CLI smoke test.** `pxfquery forward --manifest <A-003 path> --fixture-root <A-002 path> --perturbation EGFR --cell-line A549`. Assert exit 0, stdout valid JSON.
7. **Record traceability.** Package version, loader identity, manifest path, synthetic_repair label, reference paths, all output JSON.
8. **Compile pass/fail table.** One CSV row per check (import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo), each PASS/FAIL.

## Conservative Execution Advice
- Start with: Step 1 (install) + Step 2 (fixture smoke test) — if either fails, stop and report precondition failure.
- Smoke/demo command: `python -c "from pxfquery.core import PxFquery; q=PxFquery(manifest_path='<A-003>', fixture_root='<A-002>'); print(q.loader.fixture.xpr.shape)"` → expected `(5, 7)`
- Full run only after: Step 2 passes (fixture loads, shape matches manifest).
- Cost/time risk: Low — local execution, no API calls, small fixture (5 obs x 7 vars), ~1 min total.
- Checkpoint advice: Save output JSON after step 3 and step 4 before proceeding to comparison.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Smoke execution log | `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | File exists, contains install + fixture load output |
| Re-run positive forward JSON | `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | Valid JSON with `found: true`, `perturbation: EGFR`, `cell_line: A549` |
| Re-run no-hit forward JSON | `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | Valid JSON with `error: PerturbationNotFound` |
| Validation results table | `4_artifact/5_table/forward_validation_results_v20260624.csv` | ≥6 rows, each PASS/FAIL with evidence path |
| Validation report (MD) | `4_artifact/3_document/forward_validation_report_v20260624.md` | Documents all steps, traceability, and overall pass/fail |
| Execution report (HTML) | `4_artifact/3_document/execution_report_v20260624.html` | HTML rendering of smoke log + outputs |
| Result report (HTML) | `4_artifact/3_document/result_report_v20260624.html` | HTML rendering of validation results table |

## Failure / Stop Conditions
- Package cannot be imported → mark import FAIL, stop.
- Fixture cannot be loaded by `M1FixtureLoader` or `PxFquery.load_fixture()` → mark fixture load FAIL, stop.
- Positive demo returns `found=false` or error → mark positive demo FAIL, continue to collect evidence (do not repair).
- No-hit demo returns raw traceback instead of structured error → mark no-hit FAIL, collect traceback as evidence, continue.
- CLI returns non-zero exit or invalid JSON → mark CLI FAIL, continue.
- Zero failures → overall PASS. One or more → overall FAIL.

## Notes For Delivery QA
- The protocol references T-048 in meta.yaml but actually uses T-059 artifacts. The clarification note at the top of protocol.md resolves this. All assets come from T-059.
- Do NOT strip or rename the `synthetic_repair` provenance label.
- Do NOT modify T-059 package code, fixtures, manifests, or evidence.
- Reference JSON files (A-004, A-005) are for structural comparison only — numerical scores may differ due to floating-point or platform differences.
- The package uses hatchling build backend; `pip install -e` from the symlink path works.
