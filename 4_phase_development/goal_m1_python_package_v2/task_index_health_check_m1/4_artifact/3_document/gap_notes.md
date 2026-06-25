# Gap Notes — T-045 Index Health Check M1

**Generated:** 2026-06-24  
**Task:** T-045 index_health_check_m1  
**Scope:** Coverage gaps for M1 forward/reverse demo queries

---

## T-042 Dependency Note

T-042 (contract_and_demo_spec_m1) has **not been executed** — official M1 demo cases are not yet finalized. This analysis uses T-013 historical evidence (EGFR/A549 forward, Apoptosis+MYC/A549 reverse) as the best available proxy. Re-check against actual T-042 demo cases once they exist.

---

## Gap 1: function_index.json Non-Standard Structure

| Field | Value |
|---|---|
| Index | function_index.json |
| Severity | **warning** |
| Affected demo | Forward query (term lookup), Reverse query (term input) |
| Gap | Structure is `dict{meta, var_names, aliases}`, not a flat list of term objects |
| Resolution | Add loader unwrap logic in T-047 to extract `meta` entries |
| Fallback | If loader expects `function_index[i]['id']`, it will fail. If loader expects `function_index['meta']['HALLMARK_APOPTOSIS']`, it will work. |

---

## Gap 2: function_index.json Missing Category Field

| Field | Value |
|---|---|
| Index | function_index.json |
| Severity | **warning** |
| Affected demo | Forward query (category-based filtering, if used) |
| Gap | 91 terms present, but Hallmark (50) vs 3CA MPS (41) distinction is in `source` field not `category`. Terms have `source`/`label` fields, no `id`/`name`/`category`. |
| Resolution | Add `category` field during loader stage (derived from `source`: `hallmark` -> `Hallmark`, `$3ca$` -> `3CA MPS`) |
| Fallback | If query code does not use `category`, no impact |

---

## Gap 3: gene_index.json Field Name Mismatch

| Field | Value |
|---|---|
| Index | gene_index.json |
| Severity | **warning** |
| Affected demo | Forward query (gene perturbation lookup), Reverse query (gene candidate lookup) |
| Gap | Fields are `symbol`, `gene_type`, `in_matrix` — protocol expects `gene_symbol` and `ensembl_id` |
| Resolution | Update T-047 loader to use correct field names. No data loss — `symbol` contains the gene symbol |
| Fallback | Update demo case expected schema in T-042 to match actual field names |

---

## Gap 4: cellline_tree.json Not Hierarchical

| Field | Value |
|---|---|
| Index | cellline_tree.json |
| Severity | **warning** |
| Affected demo | Reverse query (context expansion via ontology), proxy matching |
| Gap | 3 flat top-level keys (tissue, cell_line_category, valid_cells_ref). Contains 3 entries total, but no nested children hierarchy |
| Resolution | Rebuild as proper tree with `children` nesting (data exists in flat structure — transformation only) |
| Fallback | Proxy matching can use cellline_neighbors.json (19 lineage groups) instead |

---

## Gap 5: cellline_index.json Flat Wrapper

| Field | Value |
|---|---|
| Index | cellline_index.json |
| Severity | **cosmetic** |
| Affected demo | Cell line validation in forward/reverse queries |
| Gap | 240 cell line names in list under key `valid_cells` |
| Resolution | Unwrap in loader: `cellline_index['valid_cells']` produces the list |
| Fallback | Not a real gap — no impact on query behavior |

---

## Gap 6: drug_index.json No Reverse Mapping

| Field | Value |
|---|---|
| Index | drug_index.json |
| Severity | **cosmetic** |
| Affected demo | Forward query (drug perturbation), Reverse query (drug candidate) |
| Gap | entries map alias->BRD only. No BRD->alias reverse index |
| Resolution | Not needed for M1 demo scope — add if reverse drug-name resolution required later |
| Fallback | Use alias keys as display names if needed |

---

## Summary

| Gap | Severity | Demo Impact | Resolution |
|---|---|---|---|
| function_index structure | warning | Term lookup | Loader unwrap (T-047) |
| function_index category | warning | Category filtering | Add derived field (T-047) |
| gene_index field names | warning | Gene lookup fields | Align field names (T-047) |
| cellline_tree flat | warning | Ontology expansion | Rebuild tree (post-M1) |
| cellline_index wrapper | cosmetic | None | Loader unwrap |
| drug_index no reverse | cosmetic | None | Future enhancement |

**Overall:** 0 blockers, 4 warnings, 2 cosmetic. All demo entities (EGFR, A549, HALLMARK_APOPTOSIS, HALLMARK_MYC_TARGETS_V1) are present in indexes. The T-021 standard resources are fully M1-ready.
