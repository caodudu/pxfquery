# T-047 Loader Gap List — M1 Resource Hardening

**Generated:** 2026-06-24T05:03:39

---

## Gap Summary

| Severity | Count |
|---------|-------|
| block | 0 |
| warn | 4 |
| info | 2 |

---

## Detailed Gap List

| # | Resource ID | Path | Issue | Severity | Fixture Covers | Recommended Action |
|---|---|---|---|---|---|---|
| 1 | index:function_index.json | standard_bundle/function_index.json | Non-standard structure: dict{meta, var_names, aliases} | warning | yes | Handled: see normalizations applied |
| 2 | index:function_index.json | standard_bundle/function_index.json | Hallmark vs 3CA MPS in 'source' field, not 'category' | warning | yes | Handled: see normalizations applied |
| 3 | index:gene_index.json | standard_bundle/gene_index.json | Field names: 'symbol' not 'gene_symbol', no 'ensembl_id' | warning | yes | Handled: see normalizations applied |
| 4 | index:cellline_index.json | standard_bundle/cellline_index.json | Single wrapping key, not 1-to-1 cell line mapping | cosmetic | yes | Handled: see normalizations applied |
| 5 | index:drug_index.json | standard_bundle/drug_index.json | No reverse BRD->alias lookup | cosmetic | yes | Handled: see normalizations applied |
| 6 | index:cellline_tree.json | standard_bundle/cellline_tree.json | Flat 3-key structure, not hierarchical tree | warning | yes | Handled: see normalizations applied |

---

## Known T-045 Health Gaps (Addressed by Loader)

The following T-045 known gaps were handled by loader logic:

1. **function_index.json non-standard structure** — unwrap via `meta` key extraction implemented
2. **function_index.json missing category** — category derived from `source` field (Hallmark / 3CA MPS)
3. **gene_index.json field names** — `symbol` mapped to canonical `gene_symbol`
4. **cellline_tree.json flat** — documented as flat structure; no rebuild attempted
5. **cellline_index.json wrapper** — unwrapped: `valid_cells` key extracted
6. **drug_index.json no reverse** — cosmetic, not handled (not needed for M1)
