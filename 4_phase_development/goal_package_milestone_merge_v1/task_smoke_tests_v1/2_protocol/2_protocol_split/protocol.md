# Protocol: smoke_tests_v1

## Objective
Create a `pxfquery-T-035` smoke/regression test suite that validates integration of the deterministic query engine chain by running each predecessor deliverable as a black-box smoke test and producing a single pass/fail evidence report with actual command execution output.

## Inputs
- **A-001**: T-029 forward query engine deliverable bundle — `forward_engine.py`, result tables, not-found JSON, validation JSON, completion report. Smoke-tested by re-running the engine script and comparing output against its own registered expectations.
- **A-002**: T-030 reverse query engine deliverable bundle — `run_reverse_demo.py`, candidate JSON, meta JSON, validation JSON, completion report. Smoke-tested by re-running the demo script. If no deliverable exists yet, the smoke test records that dependency is unmet and proceeds to the next smoke target.
- **A-003**: T-031 no-hit guard deliverable bundle — guard module, no-hit test script, positive-control test script, evidence JSONs, completion report. Smoke-tested by re-running both test scripts.
- **A-004**: T-032 reverse stability guard deliverable bundle — guard demo script, validation JSON, repaired workspace, warning JSONs, positive-control candidate JSON, completion report. Smoke-tested by re-running the `run_stability_guard.py` script.
- **A-005**: T-033 hybrid fast resolver deliverable bundle — resolver artifact if delivered. Smoke-tested only when artifacts exist; otherwise recorded as optional-skipped with evidence.
- **A-006**: Current project protocol — defines the pxfquery conda environment required for all test execution.

## Steps
1. Read each predecessor task's `4_artifact/registry.yaml` to inventory expected deliverables and their roles.
2. For each predecessor (T-029, T-030, T-031, T-032, T-033):
   - If the task's runnable script or demo exists, execute it inside the pxfquery conda environment and capture stdout, stderr, exit code, and elapsed time.
   - If a task has no deliverable yet, record it as `UNMET_DEPENDENCY` with a timestamp and move on.
   - Compare smoke output against the task's own acceptance criteria (e.g. `found=True` for EGFR/A549, `found=False` for nonsense queries, guard warnings fire, candidates contain finite scores).
3. Produce a consolidated smoke-test evidence JSON at `4_artifact/5_table/pxfquery_T035_smoke_results.json` with one record per predecessor containing: task_id, smoke_target, status (PASS/FAIL/UNMET_DEPENDENCY/SKIPPED), command, exit_code, stdout_summary, stderr_sample, elapsed_seconds, and a note.
4. If any predecessor test fails and the failure is a scoped integration issue fixable within T-035, repair it locally and record the fix in `5_report/repair_log.md` with lineage back to the predecessor task.
5. Produce CyHex-mandatory reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese HTML step-by-step execution record.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese HTML result report with pass/fail summary table and stderr excerpts.
6. Write `4_artifact/registry.yaml` registering all T-035 deliverables.
7. Write `5_report/completion.md` summarizing which predecessors passed smoke, which failed, which were unmet, and which downstream tasks should note the integration state.

### Required Bug-Repair Handling
- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-035`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning
- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read upstream versions and emit `pxfquery-T-035` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Smoke-Test Discipline
- All test execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- Smoke tests are black-box: re-run the predecessor's own script/demo, do not reimplement its logic inline.
- T-030 and T-033 may not have deliverables yet. Record them as UNMET_DEPENDENCY with clear evidence rather than marking the smoke suite as failed.
- T-033 resolver is optional: smoke it only if artifacts exist; otherwise mark SKIPPED.
- The consolidated smoke results JSON must include actual command output evidence, not just file-existence checks.

## Deliverables
- `4_artifact/5_table/pxfquery_T035_smoke_results.json` — Consolidated smoke-test pass/fail evidence with command output per predecessor.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex-mandatory Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex-mandatory Chinese result report.
- `4_artifact/registry.yaml` — T-035 artifact registry.
- `5_report/completion.md` — Completion report with integration state summary.
- `5_report/repair_log.md` — Only if scoped repairs were performed.

## Acceptance
- T-029 forward engine smoke: script re-runs and produces EGFR/A549 `found=True` with non-empty result table.
- T-030 reverse engine smoke: script re-runs if deliverable exists; otherwise UNMET_DEPENDENCY recorded.
- T-031 no-hit guard smoke: test scripts re-run, nonsense queries return `found=False`, positive control returns `found=True`.
- T-032 stability guard smoke: demo re-runs, guard warnings file is non-empty, positive-control candidates are finite.
- T-033 resolver smoke: run if deliverable exists; otherwise SKIPPED with evidence.
- Consolidated smoke results JSON contains actual stdout/stderr/exit_code per predecessor, not just a checklist.
- All Python execution uses the pxfquery conda environment.