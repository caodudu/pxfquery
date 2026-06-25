# task_hybrid_fast_resolver_v1

## Orchestration Input

- This waiting task is an optional resolver layer, but it may feed the demo if it validates cleanly.
- Consume T-027/T-028/T-031/T-032 outputs and produce `pxfquery-T-033` resolver assets with exact, proxy, and not-found examples.
- Acceptance requires runnable resolver examples with visible metadata, not only index files.
- If resolver bugs are scoped to this layer, repair them inside this task output and document lineage. Do not block the deterministic milestone if the optional layer cannot be validated.

## Upstream Reference Map

- Core context: T-007 for PxFquery intent, T-013 for resolver/gap evidence, T-021 for standard resource provenance.
- Direct inputs: T-027 normalized indexes, T-028 function index, T-031 no-hit guard, T-032 reverse stability guard.
- Non-blocking role: T-033 is a side-branch asset. It can be consumed by later demo/merge only when validated.
