# T-047 Loader Smoke Report — M1 Resource Hardening

**Generated:** 2026-06-24T05:03:39
**Elapsed:** 6.74s
**Standard bundle exists:** True

---

## Summary

| Metric | Count |
|---|---|
| Total resources | 36 |
| Loaded | 36 |
| Missing | 0 |
| Load errors | 0 |
| Not attempted | 0 |
| Unsupported type | 0 |
| Gaps identified | 6 |
| Normalizations applied | 4 |

---

## Per-Resource Results

| Resource ID | Type | Fixture | Status | Shape | Key Fields | Notes |
|---|---|---|---|---|---|---|
| m1_full_cp_matrix | h5ad | no | loaded | 201014 obs x 91 vars |  |
| m1_fixture_cp_matrix | h5ad | yes | loaded | 4 obs x 7 vars |  |
| m1_full_sh_matrix | h5ad | no | loaded | 189365 obs x 91 vars |  |
| m1_fixture_sh_matrix | h5ad | yes | loaded | 4 obs x 7 vars |  |
| m1_full_xpr_matrix | h5ad | no | loaded | 132464 obs x 91 vars |  |
| m1_fixture_xpr_matrix | h5ad | yes | loaded | 4 obs x 7 vars |  |
| m1_full_cellline_meta | csv | no | loaded | 240 rows x 8 cols |  |
| m1_full_cellline_info | csv | no | loaded | 240 rows x 20 cols |  |
| m1_full_compound_meta | csv | no | loaded | 6647 rows x 9 cols |  |
| m1_full_compound_info | csv | no | loaded | 39321 rows x 7 cols |  |
| m1_full_gene_info | csv | no | loaded | 12328 rows x 7 cols |  |
| m1_fixture_cellline_meta | csv | yes | loaded | 4 rows x 8 cols |  |
| m1_fixture_cellline_info | csv | yes | loaded | 4 rows x 20 cols |  |
| m1_fixture_compound_meta | csv | yes | loaded | 4 rows x 9 cols |  |
| m1_fixture_compound_info | csv | yes | loaded | 4 rows x 7 cols |  |
| m1_fixture_gene_info | csv | yes | loaded | 8 rows x 7 cols |  |
| m1_full_cellline_index | json | no | loaded |  | cellline_index_unwrap |
| m1_full_cellline_neighbors | json | no | loaded |  |  |
| m1_full_cellline_tree | json | no | loaded |  | cellline_tree_flat |
| m1_full_drug_index | json | no | loaded |  |  |
| m1_full_drug_neighbors | json | no | loaded |  |  |
| m1_full_gene_index_simple | json | no | loaded |  |  |
| m1_full_gene_neighbors_simple | json | no | loaded |  |  |
| m1_full_gene_index | json | no | loaded |  | norm: symbol->gene_symbol; gene_index_field_normalization |
| m1_full_gene_neighbors | json | no | loaded |  |  |
| m1_full_function_index | json | no | loaded |  | norm: category_from_source; function_index_unwrap |
| m1_fixture_cellline_index | json | yes | loaded |  | cellline_index_unwrap |
| m1_fixture_cellline_neighbors | json | yes | loaded |  |  |
| m1_fixture_cellline_tree | json | yes | loaded |  | cellline_tree_flat |
| m1_fixture_drug_index | json | yes | loaded |  |  |
| m1_fixture_drug_neighbors | json | yes | loaded |  |  |
| m1_fixture_gene_index_simple | json | yes | loaded |  |  |
| m1_fixture_gene_neighbors_simple | json | yes | loaded |  |  |
| m1_fixture_gene_index | json | yes | loaded |  | norm: symbol->gene_symbol; gene_index_field_normalization |
| m1_fixture_gene_neighbors | json | yes | loaded |  |  |
| m1_fixture_function_index | json | yes | loaded |  | norm: category_from_source; function_index_unwrap |

---

## Field Normalizations Applied

| Resource ID | Normalization |
|---|---|
| m1_full_gene_index | symbol->gene_symbol |
| m1_full_function_index | category_from_source |
| m1_fixture_gene_index | symbol->gene_symbol |
| m1_fixture_function_index | category_from_source |

---

## Gaps Identified

| Resource ID | Issue | Severity | Fixture Coverage | Recommended Action |
|---|---|---|---|---|
| index:function_index.json | Non-standard structure: dict{meta, var_names, aliases} | warning | yes | Handled: see normalizations applied |
| index:function_index.json | Hallmark vs 3CA MPS in 'source' field, not 'category' | warning | yes | Handled: see normalizations applied |
| index:gene_index.json | Field names: 'symbol' not 'gene_symbol', no 'ensembl_id' | warning | yes | Handled: see normalizations applied |
| index:cellline_index.json | Single wrapping key, not 1-to-1 cell line mapping | cosmetic | yes | Handled: see normalizations applied |
| index:drug_index.json | No reverse BRD->alias lookup | cosmetic | yes | Handled: see normalizations applied |
| index:cellline_tree.json | Flat 3-key structure, not hierarchical tree | warning | yes | Handled: see normalizations applied |

---

## M1 Readiness Verdict

- **Fixture path:** PASS
- **Full resources:** 18 loaded, 0 with issues
- **Gaps:** 6 total
- **Normalizations:** 4 applied

**Verdict: READY**