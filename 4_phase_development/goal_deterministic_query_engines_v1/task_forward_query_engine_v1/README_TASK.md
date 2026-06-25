# task_forward_query_engine_v1

## Orchestration Input

- This waiting task should consume the task-versioned package workspace and matrix loader outputs, then produce a forward query engine asset (`pxfquery-T-029`).
- Acceptance requires an actual runnable forward demo, not only files. Use an EGFR/A549/xpr-style query or the nearest valid equivalent discovered from T-013/T-021, and write visible result output with a reasonable table/schema.
- T-023 is not a predecessor for this v1 DAG. Use T-013 as capability/gap evidence.
- If the query cannot run because of a scoped package or loader bug, repair it inside this task output and document lineage, changed files, and validation evidence.
