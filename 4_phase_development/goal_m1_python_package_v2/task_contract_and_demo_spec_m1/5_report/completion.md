# T-042 contract_and_demo_spec_m1 — Completion Report

## Summary

T-042 delivered the M1 API/CLI contract for the PxFquery Python package. All required deliverables are produced and registered.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Structured API + CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | accepted |
| Forward + reverse demo cases with assertions | `4_artifact/2_persist/m1_demo_cases.yaml` | accepted |
| Human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | accepted |
| Artifact registry | `4_artifact/registry.yaml` | accepted |
| Completion note | `5_report/completion.md` | (this file) |

## Evidence Traceability

- **A-001 (T-007 source map)**: Used for package identity, asset boundary, and source priority rules.
- **A-002 (T-007 state report)**: Extracted `(B,P,F)` model, `pert2func`/`func2pert` intent, component readiness, index inventory, and validated examples.
- **A-004 (T-013 capability contract)**: Used for M1 scope (deterministic forward/reverse only), gated capabilities (resolver/LLM), and unsafe-claim boundaries.
- **A-005 (T-013 failure list)**: Provided negative cases (CAP-03 index naming gap, CAP-05 no-hit false-positive risk, CAP-06 numerical warnings) — all incorporated as contract-level error structures.
- **A-003 / A-006 / A-007**: Used as targeted cross-checks for risk validation and output JSON shape reference.

## Key Decisions And Assumptions

1. **function_index.json gap**: The contract defines `pert2func` and `func2pert` as operating directly on functional score matrices (h5ad). The missing `function_index.json` is noted as an implementation gap that T-048/T-049 must resolve; it does not block the contract.

2. **No-hit behavior**: Defined as structured JSON error objects, not exceptions. The `PerturbationNotFound` / `ContextNotFound` / `ProgramNotFound` / `NoMatrixLoaded` error types are deterministic and carry all identifying fields.

3. **Low-confidence detection**: Not hardcoded in the contract. A validation requirement is stated in `m1_demo_cases.yaml`: the implementation task should define a threshold (e.g. `max(|similarity|) < 0.05`).

4. **Reverse query numerical warnings**: The contract accepts warnings in the `warnings` field of `reverse_result`. Implementation must guarantee all top_candidate similarity values are finite.

5. **M1 scope**: Deterministic forward and reverse only. LLM, resolver, proxy retrieval, fuzzy matching, multi-matrix merge, plotting, and Zenodo download are explicitly out of scope.

## Assets Used

All 7 registered assets (A-001 through A-007) were read. Primary extraction used A-001, A-002, A-004, A-005. Cross-checks used A-003, A-006, A-007.

## Forbidden Paths Compliance

- Did not read `2_project_asset/`.
- Did not read `/Users/dudu/Documents/3_Project/8_functional_query`.
- Did not read or cite T024-T040 outputs.
- Did not implement code, analyze matrices, run tests, or produce package artifacts.

## Handoff For Downstream Tasks

- **T-048 / T-049 (M1 implementation)**: Follow `m1_api_contract.yaml` for exact class, method, parameter, return, and error structures. Rebuild or mock `function_index.json` as needed. Do not add resolver/LLM modes.
- **T-052 (M1 validation)**: Use `m1_demo_cases.yaml` DEMO-001 and DEMO-002 pass/fail criteria. Verify no-hit variants and error structures.
- Counter-indications: Do not rely on the old `main.py` entry point. Do not use migrated index JSON files as-is without name-prefix stripping.
