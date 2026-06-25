# pxfquery-T-028 Function Index Pack — Downstream Usage Notes

## What this pack contains

`function_index.json` in `pxfquery_T028_function_index/` is a validated, task-versioned function index pack built by T-028 (`task_function_index_pack_v1`).

**Core data:**

| Field | Value |
|---|---|
| Version | `pxfquery-T-028` |
| Functions | 91 MSigDB Hallmark gene-set terms |
| Source | `var_names` of T-021 standard resources H5AD matrices (cp_func_ad, sh_func_ad, xpr_func_ad) |
| Aliases per term | 2–3 (self, lowercase, human-readable label) |
| Total alias entries | 273 |

**Structure:**
```json
{
  "version": "pxfquery-T-028",
  "n_functions": 91,
  "var_names": ["HALLMARK_ADIPOGENESIS", "HALLMARK_ALLOGRAFT_REJECTION", ...],
  "aliases": {
    "HALLMARK_ADIPOGENESIS": ["HALLMARK_ADIPOGENESIS", "hallmark_adipogenesis", "Adipogenesis"],
    ...
  },
  "meta": { ... }
}
```

## What changed vs upstream

| Aspect | Upstream (T-021/D-004) | T-028 (this pack) |
|---|---|---|
| `aliases` | lowercase→uppercase mapping (1:1 strings) | lists per term with [self, lowercase, label] |
| `meta` | per-term `{source, label}` dict | Task metadata (lineage, seed sources, notes) |
| Validation | None embedded | Machine-readable validation record included |
| Lineage | None | Task ID, matrix source, loader source recorded |

The upstream `function_index.json` from T-021 is present and well-formed; T-028 re-slices and augments it. The T-013 task flagged `function_index.json` as missing/incomplete in the **migrated** query index directory — this corrected local version closes that gap within T-028 scope.

## How query/resolver tasks should use it

```python
import json

with open("function_index.json") as f:
    fi = json.load(f)

# Iterate over all 91 function terms
for term in fi["var_names"]:
    aliases = fi["aliases"][term]  # [uppercase, lowercase, readable]
    primary = aliases[0]           # always the uppercase matrix var name

# Look up aliases for a specific term
aliases = fi["aliases"].get("HALLMARK_ADIPOGENESIS", ["HALLMARK_ADIPOGENESIS"])

# Resolve a user query (lowercase or partial) to a canonical term
def resolve_term(query: str, fi: dict) -> str | None:
    query_lower = query.lower()
    for term, alias_list in fi["aliases"].items():
        if any(query_lower in a.lower() for a in alias_list):
            return term
    return None
```

## Downstream consumers

This pack is intended for:
- Query/resolver tasks in the `goal_resource_index_packs_v1` DAG that need a validated 91-term function list
- Any task that needs to resolve function terms to matrix `var` columns
- Replaces T-021 `function_index.json` as the recommended runtime index for function-term lookups

**Do not** read the old T-021 `function_index.json` directly for runtime queries — prefer this `pxfquery-T-028` pack which carries explicit alias lists, validation evidence, and lineage.

## Validation evidence

- `function_index.json`: 7/7 checks pass (JSON loads, keys present, n=91, var_names match all 3 matrices, aliases cover all terms, self-first)
- `pxfquery_t028_function_index_validation.csv`: 91 rows, all status OK
- `03_validation.json`: Structured machine-readable validation record
- `03_validation_summary.md`: Human-readable summary