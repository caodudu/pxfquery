

I'll execute this T-042 CyHex task. Let me follow the execution strategy: read the primary assets first, then produce all 5 deliverables
Now let me read the optional cross-check assets:
Let me read key evidence shapes from the bundle:
Now let me write the API contract:
Now write the registry and completion report:
Let me verify all deliverables are in place:
T-042 execution complete. Here is the summary:

**All 5 deliverables produced under `4_artifact/` and `5_report/`:**

| Deliverable | Path |
|---|---|
| API + CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` |
| Demo cases | `4_artifact/2_persist/m1_demo_cases.yaml` |
| Contract summary | `4_artifact/3_document/m1_contract_summary.md` |
| Artifact registry | `4_artifact/registry.yaml` |
| Completion report | `5_report/completion.md` |

**What the M1 contract covers:**

- **(B, P, F) model**: `PxFquery` class with `pert2func` (forward) and `func2pert` (reverse) — deterministic only, no resolver/LLM
- **DEMO-001**: EGFR perturbation in A549 (xpr matrix) — exact forward hit from T-013 evidence
- **DEMO-002**: Apoptosis activation + MYC suppression in A549 — reverse ranking from T-013 evidence
- **Error/no-hit structures**: `PerturbationNotFound`, `ContextNotFound`, `ProgramNotFound`, `NoMatrixLoaded`, `AmbiguousQuery`, `UnsupportedQuery`, `LowConfidenceResult`
- **CLI**: `pxfquery forward`, `pxfquery reverse`, `pxfquery info` subcommands with JSON output and deterministic exit codes
- **Scope**: T024-T40 excluded; LLM/gated capabilities explicitly out of M1 scope; `function_index.json` gap noted as implementation task for T-048/T-049
