# Handoff Check Before Exec

## Check Conclusion
green_check

## Task Path
`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_resource_manifest_v1`

## Allowed Write Directories
- `3_execution/`
- `4_artifact/`
- `5_report/`

## Forbidden / Read-Only Areas
- Do not modify the upstream T-021 standard resource bundle.
- Do not copy H5AD, JSON index, or CSV metadata bytes from upstream resources.
- Do not modify unrelated completed task artifacts.

## Objective Restatement
Create the T-025 standard resource manifest from the T-021 `standard_resources` bundle, with schema summary, usage notes, validation evidence, registry, and reports.

## Selected Inputs And Precheck State
- T-021 standard resources bundle: resolved and used by reference.
- T-021 standard resource guide and reports: reference context only.
- Asset path issue found during the original run was repaired before execution; the final validation evidence reports 19/19 files matched and present.

## Execution Strategy
1. Enumerate the 19-file upstream bundle without copying file bytes.
2. Derive matrix, JSON index, metadata, and description schemas from real files.
3. Write a single YAML manifest under `4_artifact/2_persist/`.
4. Write self-contained schema summary and usage notes.
5. Validate filename parity, file existence, bundle size, and `data_description.yaml` inclusion.
6. Register manifest, support documents, validation evidence, and reports.

## Smoke / Validation Signal
- `3_execution/step6_validation.json` records PASS for file count, exact filename match, all files present, description included, and bundle-size agreement.
- `5_report/process_record.yaml` confirms config/check/execute sessions reached done; one stopped manual config attempt is historical and does not supersede the later done config/check/execute path.

## Expected Deliverables
- `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml`
- `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md`
- `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md`
- `3_execution/step6_validation.json`
- `4_artifact/3_document/execution_report_v20260623.html`
- `4_artifact/3_document/result_report_v20260623.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Delivery QA Notes
- This task is safe as a downstream reference asset for resource inventory.
- It is a manifest/schema task, not a package or query engine task.
- Downstream tasks should consume T-025 as a resource map, not as copied data.
