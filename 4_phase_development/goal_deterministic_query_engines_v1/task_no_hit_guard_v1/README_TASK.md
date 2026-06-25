# task_no_hit_guard_v1

## Orchestration Input

- This waiting task should consume the forward query engine output and T-013 failure evidence about fuzzy false positives.
- Deliver a guard asset (`pxfquery-T-031`) that returns an explicit not-found/no-hit result for unsupported perturbations instead of silently matching a wrong nearby entity.
- Acceptance requires a runnable negative test with visible output, plus a positive-control query that still works.
- If a scoped resolver/query bug blocks this behavior, repair it inside this task output and document lineage.
