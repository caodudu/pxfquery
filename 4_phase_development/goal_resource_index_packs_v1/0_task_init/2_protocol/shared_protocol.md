# resource_index_packs_v1 — Shared Protocol

## Versioning And Repair Rule

- This v1 DAG is allowed to repair defects discovered during execution. A task is not limited to passive inspection when a local fix is required for its deliverable.
- Use the task id as the temporary package asset version, for example `pxfquery-T-025` for T-025 outputs. Do not overwrite upstream historical assets in place.
- Input assets and output deliverables may intentionally use different PxFquery versions. For example, a task may read a `pxfquery-T-025` resource manifest and produce a corrected `pxfquery-T-026` loader or `pxfquery-T-028` function-index pack; the milestone merge may then produce a later integrated package deliverable.
- Every repair or version split must record lineage: source task ids, changed files/assets, reason for divergence, validation evidence, and whether the downstream task should consume the new version.
- If an upstream asset is wrong but outside the task scope, create a corrected downstream asset and document the defect; do not mutate unrelated completed task artifacts unless explicitly required by the active task.
