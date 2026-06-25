# M1 PxFquery Package — Contract Summary

## Purpose

This contract defines the minimal viable M1 API, CLI, and acceptance criteria for the PxFquery Python package. It is derived from T-007 (development state and source authority) and T-013 (MVP capability contract and failure list). M1 covers deterministic forward and reverse queries over precomputed LINCS/CMAP functional score matrices **without** LLM, resolver, or natural-language dependencies.

## M1 Scope

| What | In scope | Out of scope |
|------|----------|--------------|
| Forward query | `(B, P) -> F` via exact matrix lookup | LLM parsing, proxy retrieval, fuzzy matching |
| Reverse query | `(B, F) -> P` via profile similarity | Function index rebuild, multi-matrix merge |
| Output format | JSON with `found`/`not-found` status | NL summaries, plots, manuscript reports |
| CLI | `forward`, `reverse`, `info` commands | Resolver, hybrid, or LLM modes |

## API (Python)

**Class:** `PxFquery` in `pxfquery.core`

| Method | Required params | Returns |
|--------|----------------|---------|
| `PxFquery.__init__` | `matrix_path: str` | instance |
| `pert2func` | `perturbation: str`, `cell_line: str` | `forward_result` dict |
| `func2pert` | `activate: list[str]`, `suppress: list[str]`, `cell_line: str` | `reverse_result` dict |

## CLI

```
pxfquery forward -p EGFR -c A549 -m matrix.h5ad
pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 -c A549 -m matrix.h5ad
pxfquery info
```

Output: JSON to stdout. Exit code 0 on success, 1-4 on errors.

## Demo Cases

| ID | Type | Input | Source |
|----|------|-------|--------|
| DEMO-001 | Forward | `perturbation=EGFR, cell_line=A549, metric=xpr` | T-013 run evidence (CAP-04 pass) |
| DEMO-002 | Reverse | `activate=[HALLMARK_APOPTOSIS], suppress=[HALLMARK_MYC_TARGETS_V1], cell_line=A549` | T-013 run evidence (CAP-06 partial) |

Each demo case includes pass/fail assertions, no-hit variants (PerturbationNotFound, ContextNotFound, ProgramNotFound, NoMatrixLoaded, AmbiguousQuery, LowConfidenceResult), and exact expected JSON shape.

## Error Structures

All errors are deterministic JSON objects (not exceptions). Defined error types: `FileNotFound`, `InvalidMatrix`, `NoMatrixLoaded`, `PerturbationNotFound`, `ContextNotFound`, `ProgramNotFound`, `AmbiguousQuery`, `UnsupportedQuery`, `LowConfidenceResult`, `NotImplemented`.

## M1 Constraints (from T-013)

- M1 acceptance must **not** depend on LLM resolver success.
- Natural-language platform claims are prohibited without further validation.
- `function_index.json` gap: M1 implementation must rebuild or handle its absence; not a blocker for the contract.
- Reverse query may produce numerical warnings; M1 must filter NaN/Inf similarities and surface warnings.
- Low-confidence detection is a validation requirement, not hardcoded.

## Downstream Task Handoff

- **T-048 / T-049**: Implement `PxFquery` class, matrix loader, `pert2func`, `func2pert` per this contract.
- **T-052**: Validate the implementation against DEMO-001 and DEMO-002 pass/fail criteria.
- T-042 does not impose API arguments or JSON shapes not defined in `m1_api_contract.yaml`.
