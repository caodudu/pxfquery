# task_smoke_tests_v1

## Orchestration Input

- This waiting task is integration validation, not the first place where forward/reverse functionality should be discovered broken.
- Consume T-029/T-030/T-031/T-032 outputs that already include their own runnable demos and guard evidence.
- Deliver `pxfquery-T-035` smoke/regression tests covering import, resource load, forward demo, reverse demo, no-hit guard, reverse stability guard, and optional resolver when available.
- If integration exposes a scoped package bug, repair inside this task output and document lineage. Do not silently accept file-only success.

## Upstream Reference Map

- Core context: T-007 for product intent, T-013 for MVP gaps/capabilities, T-021/T-025 for standard resource provenance.
- Package/resource lineage: T-024 workspace, T-026 loader, T-027 normalized indexes, T-028 function index.
- Direct functional inputs: T-029 forward demo, T-030 reverse demo, T-031 no-hit guard, T-032 reverse stability guard.
- Side branch: T-033 resolver evidence may be included only if validated; T-034 must not be required for deterministic smoke tests.
