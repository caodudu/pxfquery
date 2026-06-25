# Orchestration Resolution: T-049 reverse_query_core_m1

Resolved: 2026-06-24

## Internal Finding

T-049 is not a transport/session failure. Its config, check, and execute sessions all completed, and the task correctly discovered a real input/contract mismatch:

- T-042 required the reverse demo suppress target `HALLMARK_MYC_TARGETS_V1`.
- The selected T-049/T-046 assets did not include `resource_manifest_m1.yaml` or `fixture_package_m1/`.
- Registered loader smoke evidence did not include `HALLMARK_MYC_TARGETS_V1`.
- Completing the task honestly would require registering different fixture assets, revising the completed demo contract, or fabricating private data. All are outside T-049 scope.

## Replacement Path

T-060 `reverse_query_core_repair_m1` was created as the same-layer bypass repair for this exact gap.

T-060 is complete and provides:

- a reverse implementation package,
- a task-local repair fixture/manifest,
- positive reverse demo evidence,
- no-hit/error evidence,
- ranking evidence,
- CLI smoke output,
- reports and registry.

The task graph already demotes T-049 downstream edges to `may` and makes T-060 the `must` replacement for reverse validation and package assembly.

## Resolution

Do not force T-049 to pass. Keep its artifacts as failure evidence and mark the task archived/blocked because the work was superseded by T-060.

T-049 should not be used as an authoritative implementation input. Downstream tasks should consume T-060.
