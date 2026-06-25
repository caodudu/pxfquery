# task_matrix_loader_v1

## Orchestration Input

- This waiting task should use T-021 standard resources and T-025 manifest as its source of truth. Do not hard-code matrix schema from this planning note; read the T-021 bundle and record the observed file paths, matrix shapes, obs columns, var count, dtype, and load behavior.
- T-023 is not a predecessor for this v1 DAG. Treat T-013 as the gap/capability evidence and T-021/T-025 as the data-resource evidence.
- The deliverable must include runnable loader code plus a validation script that actually opens xpr/sh/cp resources and prints or writes a visible validation record. File existence alone is not enough for green acceptance.
- If a scoped bug prevents loading, fix it inside this task's `pxfquery-T-026` asset and document lineage, changed files, and validation evidence.
