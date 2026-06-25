# pxfquery-T-040

T-040 package-core milestone build of PxFquery. This branch assembles the T-024 package workspace, the T-026 standard-resource loader behavior, the T-029 deterministic forward-query path, and the T-031 no-hit guard into one importable package-core artifact.

## Lineage

- Package base: T-024 `4_artifact/2_persist/workspace/`
- Resource access: T-026 loader behavior, vendored in `pxfquery.resources`
- Forward query: T-024 `ForwardQuery` with T-029 deterministic demo expectations
- No-hit guard: T-031 guard behavior, integrated as `pxfquery.query.no_hit_guard.NoHitGuardForwardQuery`
- Data access: standard resources are opened by reference from the existing T-021 bundle; H5AD/JSON/CSV bytes are not copied into T-040.
- Downstream: T-039 may consume this workspace as `pxfquery-T-040`.
