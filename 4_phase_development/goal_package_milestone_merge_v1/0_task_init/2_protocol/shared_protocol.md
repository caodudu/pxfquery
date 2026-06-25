# package_milestone_merge_v1 — Shared Protocol

## Versioning And Repair Rule

- This v1 DAG is allowed to repair defects discovered during execution. A task is not limited to passive inspection when a local fix is required for its deliverable.
- Use the task id as the temporary package asset version during intermediate work. The final milestone deliverable may be a later integrated version assembled from multiple task-versioned PxFquery assets.
- Input assets and output deliverables may intentionally use different PxFquery versions. The merge task should select the best validated upstream task-versioned assets and produce the runnable milestone package as its own deliverable version.
- Every repair or version split must record lineage: source task ids, changed files/assets, reason for divergence, validation evidence, and why each version was selected or rejected for the milestone.
- If an upstream asset is wrong but outside the task scope, create a corrected downstream asset and document the defect; do not mutate unrelated completed task artifacts unless explicitly required by the active task.
