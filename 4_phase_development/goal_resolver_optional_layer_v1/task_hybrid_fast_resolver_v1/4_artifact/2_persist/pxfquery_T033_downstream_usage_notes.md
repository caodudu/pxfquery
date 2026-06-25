# pxfquery-T-033 Downstream Usage Notes

`pxfquery-T-033` is an optional resolver metadata layer. It is not required by the deterministic milestone path, but it can be consumed by a demo or merge task when available.

## What It Does

- Loads T-027 runtime query indexes by reference.
- Loads the T-028 function index by reference.
- Resolves exact perturbation/cell queries.
- Resolves proxy cell or proxy perturbation queries when an index-supported proxy exists.
- Emits explicit `NOT_FOUND` for no-hit perturbations, preserving T-031 guard semantics.
- Includes T-032-style guard metadata samples for downstream stability reporting.

## Import

```python
from pxfquery_T033_hybrid_fast_resolver import HybridFastResolver

resolver = HybridFastResolver()
result = resolver.resolve("EGFR/A549/xpr")
print(result.to_dict())
```

Run from `3_execution/` or add that directory to `PYTHONPATH`.

## Verification Command

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/run_examples.py
```

The run writes:

- `4_artifact/5_table/pxfquery_T033_example_exact.json`
- `4_artifact/5_table/pxfquery_T033_example_proxy.json`
- `4_artifact/5_table/pxfquery_T033_example_not_found.json`
- `4_artifact/5_table/pxfquery_T033_examples_metadata.json`

## Current Validation

- Exact: `EGFR/A549/xpr` -> `found=true`, `hit_level=EXACT`.
- Proxy: `TP53/breast/xpr` -> `found=true`, `hit_level=PROXY_CELL`, `used_cell=BT20`.
- Not found: `NONSENSE_ZZZ999/UNKNOWN_CELL/xpr` -> `found=false`, `hit_level=NOT_FOUND`.

## Scope

This is a repaired T-033 local asset. It does not mutate T-027, T-028, T-031, T-032, or any upstream completed artifact.
