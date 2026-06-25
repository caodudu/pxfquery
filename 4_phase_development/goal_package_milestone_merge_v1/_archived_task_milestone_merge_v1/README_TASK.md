# task_milestone_merge_v1

## Orchestration Input

- This waiting task is the milestone package handoff. It should select the best validated upstream task-versioned assets and produce its own integrated deliverable version (`pxfquery-T-037` or a clearly named successor under this task).
- Core milestone dependencies are deterministic: workspace, resource manifest/loader/index/function-index, forward query, reverse query, guards, smoke tests, and demo. Optional LLM/resolver assets may be included only if validated and must not block the core milestone.
- Acceptance requires runnable package handoff evidence, test evidence, demo evidence, and a lineage report mapping each selected upstream task asset to the final deliverable.
- If merge reveals a scoped package bug, repair inside this task output and document lineage. Do not overwrite unrelated completed upstream artifacts.

## Upstream Reference Map

- Original intent and constraints: T-007, T-013, T-021.
- Core package/resource chain: T-024, T-025, T-026, T-027, T-028.
- Core query chain: T-029, T-030, T-031, T-032.
- Milestone validation chain: T-035 smoke tests and T-036 demo CLI.
- Non-blocking side branches: T-033 resolver and T-034 LLM adapter may be included only when validated and must not block the deterministic milestone.
