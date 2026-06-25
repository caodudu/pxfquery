# Handoff Check Before Exec

## Check Conclusion
green_check

## Task Path
`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1`

## Allowed Write Directories
- `3_execution/`
- `4_artifact/`
- `5_report/`

## Forbidden / Read-Only Areas
- Do not modify the upstream T-021 standard resource bundle.
- Do not overwrite T-026/T-027/T-013 predecessor artifacts.
- Do not guess or invent function terms beyond the matrix-observed 91 var names.

## Objective Restatement
Create the T-028 function index pack containing exactly the 91 function terms observed in the upstream H5AD matrices, with aliases, validation table, usage notes, reports, registry, and completion evidence.

## Selected Inputs And Precheck State
- T-026 loader and validation evidence: used to confirm matrix var-name source.
- T-027 runtime query index pack: used as resolver-compatible index context.
- T-021 standard resources bundle: used as read-only source for H5AD matrices and upstream `function_index.json`.
- T-013 MVP review evidence: reference context for the function-index gap.

## Execution Strategy
1. Read `cp_func_ad.h5ad`, `sh_func_ad.h5ad`, and `xpr_func_ad.h5ad` through the project Python environment.
2. Confirm all three matrices expose the same 91 `var_names`.
3. Inspect the upstream `function_index.json` and use it as an alias seed when valid.
4. Emit the versioned T-028 `function_index.json` under `4_artifact/2_persist/`.
5. Write a 91-row validation table and machine-readable validation JSON.
6. Write downstream usage notes and CyHex reports.
7. Register all reusable outputs.

## Smoke / Validation Signal
- Command: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/validate_function_index.py`
- Latest observed result: 7/7 checks pass.
- Required checks include JSON validity, top-level keys, `n_functions=91`, matrix var-name match, alias coverage for all 91 terms, and non-null self-first aliases.

## Expected Deliverables
- `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json`
- `4_artifact/5_table/pxfquery_t028_function_index_validation.csv`
- `3_execution/05_validate/03_validation.json`
- `3_execution/05_validate/03_validation_summary.md`
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md`
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md`
- `4_artifact/3_document/execution_report_v20260623.html`
- `4_artifact/3_document/result_report_v20260623.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Delivery QA Notes
- This task is safe as a downstream function-index reference.
- It should not be treated as a resolver implementation or query engine.
- The 91-term validation is the primary trust signal.
