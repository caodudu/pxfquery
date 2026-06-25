# Minimal T-061 Execute Recovery Prompt

You are the CyHex execution AI for T-061 recovery.

The previous execute session already wrote the required T-061 artifacts but ended as interrupted before the session closed cleanly. Do not redo source digestion. Do not inspect A-002 source files again unless a required artifact is missing. Do not read or modify T-041.

Read only these T-061-local files:

- `5_report/handoff_check_before_exec.md`
- `5_report/completion.md`
- `4_artifact/registry.yaml`
- `4_artifact/2_persist/legacy_source_digest_repair_m1.md`
- `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`
- `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`

Perform only bounded validation:

1. Confirm all listed files exist and are non-empty.
2. Confirm the CSV has rows and includes at least `module_path`, `reuse_status`, `recommended_action`, and `provenance`.
3. Confirm the YAML files parse.
4. Confirm the completion note says T-041 outputs were not used as authority.
5. Write `5_report/execute_recovery_validation_20260624.md` with the validation result.

If validation passes, return a concise final completion summary. If validation fails, write `5_report/blocked.md` with the exact missing/invalid file. Do not mark the task done yourself. Do not call delivery prompt APIs.
