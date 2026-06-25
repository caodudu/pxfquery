# Handoff Check Before Exec

## Check Conclusion
green_check

## Task Path
`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1`

## Allowed Write Directories
- `3_execution/`
- `4_artifact/`
- `5_report/`

## Forbidden / Read-Only Areas
- Do not modify T-024, T-026, T-021, T-029, or T-013 upstream artifacts.
- Do not broaden the task into resolver, natural-language, or LLM behavior.
- Do not claim full reverse-query or package milestone completion from this task.

## Objective Restatement
Create a scoped no-hit safety guard for the forward query path so unsupported perturbation names return explicit `found=False` behavior instead of fuzzy false positives.

## Selected Inputs And Precheck State
- T-029 forward query artifacts: positive-control baseline and result evidence.
- T-024 workspace package: source of legacy `ForwardQuery` behavior.
- T-026 loader and T-021 resources: used for validation data access.
- T-013 capability evidence: identifies CAP-05 false-positive risk.

## Execution Strategy
1. Reproduce false-positive behavior with unguarded `ForwardQuery`.
2. Implement `NoHitGuardForwardQuery` as a task-local wrapper.
3. Run negative no-hit tests against nonsense perturbation names.
4. Run positive-control tests against EGFR/A549 and TP53/MCF7.
5. Persist evidence JSON files under `4_artifact/5_table/`.
6. Register guard module, tests, evidence, reports, and completion.

## Smoke / Validation Signal
- Command: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/test_no_hit_guard.py`
- Latest observed result: 11/11 negative queries return `found=False`.
- Command: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/test_positive_control.py`
- Latest observed result: 2/2 positive controls return `found=True` with activated and suppressed terms.

## Expected Deliverables
- `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py`
- `3_execution/test_no_hit_guard.py`
- `3_execution/test_positive_control.py`
- `4_artifact/5_table/pxfquery_T031_false_positive_reproduced.json`
- `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json`
- `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json`
- `4_artifact/3_document/execution_report_v20260623.html`
- `4_artifact/3_document/result_report_v20260623.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Delivery QA Notes
- This task is safe as a downstream reference asset for no-hit behavior.
- It is a scoped guard only; it does not certify resolver, reverse query, LLM, or final package completion.
- Downstream tasks should consume the guard module and evidence JSON directly, not infer broader milestone status.
