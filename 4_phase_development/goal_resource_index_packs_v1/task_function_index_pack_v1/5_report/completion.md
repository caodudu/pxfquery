# T-028 Completion: function_index_pack_v1

Generated: 2026-06-23  
CyHex 1.2.19 compatibility supplement added: 2026-06-24

## Result Summary

T-028 produced `pxfquery-T-028`, a validated function-index pack containing exactly the 91 function terms observed in the upstream H5AD matrices.

Core artifact:

- `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json`

## Validation Summary

Latest validation command:

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/validate_function_index.py
```

Result: 7/7 checks pass.

Validation checks:

- `JSON_loads_ok`: T-028 `function_index.json` loads as valid JSON.
- `top_level_keys_present`: 7/7 required keys found.
- `n_functions_equals_91`: `n_functions=91`.
- `var_names_match_matrix`: T-028 `var_names` match matrix-observed `var_names`.
- `var_set_match_all_matrices`: cp/sh/xpr all match.
- `aliases_covers_all_terms`: aliases cover 91/91 terms.
- `alias_nonnull_self_first`: 91/91 terms have a non-null alias list with self first.

## Deliverables

- `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` — core function index pack.
- `4_artifact/5_table/pxfquery_t028_function_index_validation.csv` — 91-row validation table.
- `3_execution/01_verify/01_var_names.json` — matrix var-name evidence.
- `3_execution/02_inspect/02_upstream_function_index.json` — upstream function-index inspection record.
- `3_execution/05_validate/03_validation.json` — machine-readable validation record.
- `3_execution/05_validate/03_validation_summary.md` — readable validation summary.
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md` — English usage notes.
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md` — Chinese usage notes.
- `4_artifact/3_document/execution_report_v20260623.html` — Chinese execution report.
- `4_artifact/3_document/result_report_v20260623.html` — Chinese result report.
- `4_artifact/registry.yaml` — artifact registry.
- `5_report/process_record.yaml` — CyHex process record refreshed by API.
- `5_report/handoff_check_before_exec.md` — execution handoff for newer CyHex prompts.

## Scope And Integrity

No upstream T-021, T-026, T-027, or T-013 artifact was modified. T-028 is a derived, task-versioned index pack. It is safe to use as a downstream reference asset for function terms and aliases, but it is not a resolver, query engine, or package milestone.

## Downstream Use

Downstream tasks should read:

- `var_names` for the canonical ordered 91-term function list.
- `aliases` for term matching/proxy matching.
- `4_artifact/5_table/pxfquery_t028_function_index_validation.csv` when human-readable per-term audit is needed.

Avoid treating this task as evidence that resolver or LLM functionality is complete.
