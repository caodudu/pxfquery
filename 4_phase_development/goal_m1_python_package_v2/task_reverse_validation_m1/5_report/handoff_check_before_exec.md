# Check Handoff Before Exec: T-051 reverse_validation_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories (T-042, T-043, T-044, T-046, T-049, T-060)
- Required registry: `1_asset/registration.yaml` (6 assets, all ok)
- Must stop if: package code unresolvable, fixture cannot load, unhandled exception in any validation step

## Objective Restatement
Independently validate M1 reverse query (T-060/T-049) by re-running T-042 reverse demo against registered assets. Produce structured pass/fail report with full traceability. Do not hide instability or relax acceptance criteria.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/reverse_query_package_code` (symlink → T-044 pxfquery/) | Implementation under test | ok |
| A-002 | `1_asset/reverse_repair_fixture_m1_1/` | Fixture with A549 xpr matrix + HALLMARK targets | ok |
| A-003 | `1_asset/reverse_repair_manifest_m1_1.yaml` | Manifest for M1FixtureLoader | ok |
| A-004 | `1_asset/reverse_demo_evidence_reference.json` | Reference positive demo JSON | ok |
| A-005 | `1_asset/reverse_error_no_hit_evidence_reference.json` | Reference no-hit/error JSON | ok |
| A-006 | `1_asset/reverse_ranking_evidence_reference.csv` | Reference ranking CSV | ok |

## Execution Strategy
1. **Package provenance** — inspect symlink target, record resolved path and version.
2. **Load fixture via M1FixtureLoader** — must pass `fixture_root` explicitly (loader does not use manifest's `fixture_package_root` field). Confirm xpr matrix shape (15×9), target columns, A549 coverage.
3. **Positive demo** — `reverse_query(xpr, activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="A549", top_n=3)`. Record stdout/stderr/exit/elapsed, compare with A-004.
4. **No-hit/error cases** — test `NoMatrixLoaded` (None matrix), `ProgramNotFound` (bogus program), `ContextNotFound` (bogus cell line), `LowConfidenceResult`, empty-target no-hit. Compare with A-005.
5. **Ranking comparison** — compare CSV vs A-006 (order, similarity, candidate names). Report exact match or diff.
6. **CLI smoke** — run CLI reverse interface, confirm output matches documented format.
7. **Validation report** — write structured JSON with pass/fail per check (`4_artifact/2_persist/reverse_validation_report_v{date}.json`).
8. **Register outputs** in `4_artifact/registry.yaml`.

## Conservative Execution Advice
- **Start with:** Step 1 (symlink inspection) + Step 2 (loader test with explicit fixture_root). These confirm the substrate before any query runs.
- **Smoke/demo command:**
  ```python
  from data import M1FixtureLoader
  from query.reverse import reverse_query
  loader = M1FixtureLoader("1_asset/reverse_repair_manifest_m1_1.yaml", fixture_root="1_asset/reverse_repair_fixture_m1_1")
  fixture = loader.fixture
  result = reverse_query(fixture.xpr, activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="A549", top_n=3)
  ```
- **Full run only after:** Step 2 passes (fixture loads, shape correct).
- **Cost/time risk:** Negligible — local-only, small synthetic fixture (15 rows). All runs should complete under 60s.
- **Checkpoint advice:** Save intermediate JSON outputs in `3_execution/` after each step.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v{date}.json` | Structured pass/fail per check, explicit verdict |
| Smoke logs & evidence | `3_execution/` | stdout/stderr captures, exit codes |
| Comparison table (CSV) | `4_artifact/5_table/reverse_validation_comparison_v{date}.csv` | Rows match reference; differences explicit |
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | Rendered summary of all checks |
| Completion report | `5_report/completion.md` | Lists executed steps, verdict, traceability |
| Artifact registry | `4_artifact/registry.yaml` | All outputs registered |

## Failure / Stop Conditions
- **Package import error:** Stop, report full traceback. Do not fallback.
- **M1FixtureLoader failure:** Stop if `fixture_root` not accepted or manifest/h5ad unreadable.
- **Unhandled exception in any step:** Stop, record as failure. Do not skip.
- **Reference comparison mismatch:** Record difference explicitly; do not silently accept. Failure is valid evidence.
- **CLI missing or crashes:** Record as failure; do not fabricate CLI output.

## Notes For Delivery QA
- Package is a symlink to T-044 (`task_package_skeleton_m1/4_artifact/1_package/pxfquery`). The validation report must record this as a traceability observation.
- M1FixtureLoader does **not** use the manifest's `fixture_package_root` field. It derives root relative to manifest directory + `fixture_package_m1`, which is wrong for this task. The execution AI must pass `fixture_root` explicitly to `M1FixtureLoader(manifest_path, fixture_root=...)`.
- The reverse_query API signature is: `reverse_query(matrix, activate, suppress, cell_line, matrix_type="xpr", top_n=10, low_confidence_threshold=0.05)`.
- If validation produces failure results (e.g., scores differ from reference), that is valid output — do not relax thresholds to force pass.
