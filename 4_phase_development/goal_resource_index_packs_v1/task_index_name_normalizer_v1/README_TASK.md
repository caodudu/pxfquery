# task_index_name_normalizer_v1

## Orchestration Input

- This waiting task should use T-021 standard indexes and T-025 manifest as source evidence. T-023 is not a predecessor for this v1 DAG.
- Produce a task-versioned normalized runtime index pack (`pxfquery-T-027`) with resolver-compatible names and a schema report.
- If index naming or schema mismatches are discovered, repair them inside this task's output asset and document source lineage, changed files, and downstream consumption guidance.
