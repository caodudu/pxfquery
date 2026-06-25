# task_function_index_pack_v1

## Orchestration Input

- This waiting task should consume T-026/T-027 outputs and T-013 gap evidence. T-023 is not a predecessor for this v1 DAG.
- Produce a validated `function_index.json` pack as `pxfquery-T-028`; do not assume the old migrated package index is complete or correctly named.
- Acceptance requires machine-readable validation showing the function index can be loaded and mapped to the matrix var terms used by the loader.
- If a scoped mismatch is found, repair it inside this task output and preserve lineage.
