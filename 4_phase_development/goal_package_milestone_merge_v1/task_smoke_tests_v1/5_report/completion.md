# T-035 smoke_tests_v1 — Completion Report

**Date:** 2026-06-23
**Task ID:** T-035
**Task name:** smoke_tests_v1 (goal: `goal_package_milestone_merge_v1`)
**Executor:** hybrid

## 1. What was produced

T-035 produced a black-box smoke / regression test suite that re-runs each
predecessor deliverable inside the project's default conda env
(`/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python`),
captures real stdout / stderr / exit_code / elapsed time, and emits a
consolidated JSON evidence file plus two CyHex-mandatory Chinese HTML
reports.

### Deliverables

| ID    | Path                                                            | Role                              |
|-------|-----------------------------------------------------------------|-----------------------------------|
| T035-D-001 | `3_execution/02_smoke_runs/run_smoke_suite.py`              | smoke orchestrator                |
| T035-D-002 | `4_artifact/5_table/pxfquery_T035_smoke_results.json`      | consolidated smoke evidence       |
| T035-D-003..006 | `3_execution/02_smoke_runs/*.txt`                       | per-target stdout smoke logs      |
| T035-D-007 | `4_artifact/3_document/execution_report_v20260623.html`    | execution report (Chinese HTML)   |
| T035-D-008 | `4_artifact/3_document/result_report_v20260623.html`       | result report (Chinese HTML)      |
| T035-D-009 | `4_artifact/registry.yaml`                                    | T-035 artifact registry           |
| T035-D-010 | `5_report/completion.md`                                       | this completion report            |

## 2. Summary of smoke runs

The smoke orchestrator `run_smoke_suite.py` invoked each predecessor's
executable entry point with cwd set to the predecessor's own task
directory (because each predecessor script hardcodes `TASK_ROOT =
Path(__file__).resolve().parents[1]`). All Python execution used the
project `pxfquery` conda environment.

| Task   | Smoke target                        | Status              | Exit | Elapsed | Evidence              |
|--------|-------------------------------------|---------------------|------|---------|------------------------|
| T-029  | `forward_engine.py`                 | PASS                | 0    | 2.14s   | all 5 acceptance flags True |
| T-030  | `run_reverse_demo.py`               | UNMET_DEPENDENCY    | —    | —       | script file missing         |
| T-031  | `test_no_hit_guard.py`              | PASS                | 0    | 1.72s   | 11/11 found=False           |
| T-031  | `test_positive_control.py`          | PASS                | 0    | 1.63s   | 2/2 found=True (20+20 each) |
| T-032  | `run_stability_guard.py`            | PASS                | 0    | 1.80s   | positive control + 6 B-cases + BC all pass |
| T-033  | (no executable resolver)            | SKIPPED             | —    | —       | optional layer              |

**Counts**

- PASS = 4
- FAIL = 0
- UNMET_DEPENDENCY = 1 (T-030 — explicit per protocol)
- SKIPPED = 1 (T-033 — explicit per protocol, optional layer)

## 3. Acceptance criteria status

- T-029 forward engine smoke: forward_engine.py re-run successfully and
  EGFR/A549 returned `found=True` with a non-empty (40-row) result table.
  TP53/MCF7 also returned `found=True` with 40 rows. NONEXISTENT_PERT_XYZ
  returned `found=False` without crashing. ✓ PASS
- T-030 reverse engine smoke: T-030 has not yet delivered an executable.
  Recorded as `UNMET_DEPENDENCY` per protocol — does **not** affect overall
  smoke status. ✓ handled
- T-031 no-hit guard smoke: nonsense queries return `found=False` (11/11),
  positive controls return `found=True` (2/2) with activated and
  suppressed terms. ✓ PASS
- T-032 stability guard smoke: scenarios A and B all pass; guard warnings
  fire; positive-control candidates are finite within [-1.0, 1.0];
  backward-compat within 1e-12. ✓ PASS
- T-033 resolver smoke: no resolver artifact exists; resolver is optional.
  Recorded as `SKIPPED` per protocol. ✓ handled
- Consolidated smoke results JSON contains actual stdout / stderr / exit_code
  per predecessor. ✓ yes
- All Python execution used the pxfquery conda environment. ✓ yes

## 4. Repairs performed

None. Every runnable predecessor passed with exit code 0 and satisfied its
own acceptance criteria. No scoped integration issue was encountered.

`5_report/repair_log.md` was not created because no repair was needed.

## 5. Integration state for downstream tasks

- **Forward query path (T-029)** is verified runnable in T-035. Downstream
  tasks can rely on `task_forward_query_engine_v1/4_artifact/` for actual
  results and trust the engine on xpr matrices.
- **Reverse query path (T-030)** is **not yet runnable** at smoke time. Any
  downstream task depending on T-030 reverse candidates should wait until
  T-030 completes development or should fall back to T-032 stability
  guard evidence.
- **No-hit guard (T-031)** is verified runnable. The `NoHitGuardForwardQuery`
  wrapper from T-031 is safe to consume and is preserved at
  `task_no_hit_guard_v1/4_artifact/2_persist/`.
- **Reverse stability guard (T-032)** is verified runnable. The repaired
  `pxfquery-T-032` workspace at
  `task_reverse_stability_guard_v1/3_execution/pxfquery_T-032_repaired/`
  is the recommended pxfquery package version for any reverse-query
  consumer.
- **Resolver (T-033)** is optional and not yet delivered; downstream
  consumers should treat resolver as deferred.

## 6. How to reproduce

```bash
export PXFQUERY_T035_TASK_ROOT="/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_smoke_tests_v1"
conda run -n pxfquery python 3_execution/02_smoke_runs/run_smoke_suite.py
```

Outputs:

- `4_artifact/5_table/pxfquery_T035_smoke_results.json` — consolidated
- `4_artifact/3_document/execution_report_v20260623.html`
- `4_artifact/3_document/result_report_v20260623.html`

## 7. Status

T-035 awaits human acceptance. Per CyHex workflow rules, the task is
**not** self-marked as `done`; that conversion happens after human
acceptance.

## Open items / follow-ups

- After T-030 (reverse query engine) is delivered by its own execute
  stage, re-run `run_smoke_suite.py` to convert that smoke row from
  `UNMET_DEPENDENCY` to `PASS`. No change to T-035 protocol needed.
- After T-033 resolver is delivered by its own execute stage, re-run
  `run_smoke_suite.py` and update the resolver smoke section in
  `run_smoke_suite.py` to invoke the resolver entry-point script.
