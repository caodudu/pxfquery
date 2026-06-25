# deterministic_query_engines_v1 — Shared Protocol

## Versioning And Repair Rule

- This v1 DAG is allowed to repair defects discovered during execution. A task is not limited to passive inspection when a local fix is required for its deliverable.
- Use the task id as the temporary package asset version, for example `pxfquery-T-029` or `pxfquery-T-030` for query-engine outputs. Do not overwrite upstream historical assets in place.
- Input assets and output deliverables may intentionally use different PxFquery versions. For example, forward query, reverse query, no-hit guard, and reverse-stability guard may each produce their own corrected task-versioned assets before the milestone merge selects and integrates them.
- Every repair or version split must record lineage: source task ids, changed files/assets, reason for divergence, validation evidence, and whether the downstream task should consume the new version.
- If an upstream asset is wrong but outside the task scope, create a corrected downstream asset and document the defect; do not mutate unrelated completed task artifacts unless explicitly required by the active task.
