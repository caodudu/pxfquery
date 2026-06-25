# task_demo_cli_v1

## Orchestration Input

- This waiting task should build a user-facing demo CLI/script only after T-029/T-030 and T-035 provide runnable evidence.
- Deliver `pxfquery-T-036` demo outputs for both forward and reverse paths with readable visible result files.
- The demo may use optional resolver assets only if they validated; otherwise use deterministic inputs directly.
- If demo wiring exposes a scoped package bug, repair inside this task output and document lineage.

## Upstream Reference Map

- Core context: T-007 product intent and T-013 MVP evidence.
- Direct inputs: T-029 forward demo, T-030 reverse demo, T-035 integration smoke evidence.
- Supporting lineage: T-024 package workspace, T-026 loader, T-031/T-032 guards.
- Side branch: T-033 resolver may improve the demo only if validated; T-034 LLM adapter is not required for the deterministic demo.
