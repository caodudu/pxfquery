# Index Health Report — T-045

**Generated:** 2026-06-24  
**Task:** T-045 index_health_check_m1  
**Scope:** 10 M1-relevant indexes from T-021 standard resources

---

## Core Indexes

### cellline_index.json — PASS (score: 90)
| Field | Value |
|---|---|
| Format | dict with list values (single key `valid_cells`) |
| File size | 3574 bytes |
| Cell lines | 240 names |
| Issues | Cosmetic: flat list wrapper, not 1-to-1 mapping |

### drug_index.json — PASS (score: 100)
| Field | Value |
|---|---|
| Format | dict, 5958 entries |
| File size | 180301 bytes |
| BRD values | 5870/5958 (98%) |
| Issues | Cosmetic: no reverse BRD->alias index |

### gene_index.json — PASS (score: 95)
| Field | Value |
|---|---|
| Format | dict, 78061 entries |
| File size | 6418019 bytes |
| Entry fields | symbol, gene_type, in_matrix |
| Gene types | 37 categories (protein_coding, lncRNA, miRNA, etc.) |
| Issues | Warning: field names differ from canonical (`symbol` not `gene_symbol`, no `ensembl_id`) |

### function_index.json — WARNING (score: 95)
| Field | Value |
|---|---|
| Format | dict with `meta`/`var_names`/`aliases` keys |
| File size | 17899 bytes |
| Terms | 91 (50 hallmark + 41 3ca_mps) |
| Issues | Structure requires unwrapping before use. No `category` field — Hallmark vs 3CA MPS in `source`. No `id`/`name` fields (uses `source`/`label`). |

### data_description.yaml — PASS
Provides field-level semantics. Top keys: ['assets']

---

## Optional Neighbor/Tree Indexes

### cellline_neighbors.json — PASS
19 lineage groups, 1-5 members each. No empty entries.

### cellline_tree.json — WARNING
3 flat keys (tissue, cell_line_category, valid_cells_ref). **Not a hierarchical tree** — cannot support ontology-based proxy matching without rebuild.

### drug_neighbors.json — PASS
5312 drugs, each with 50 neighbors. No empty entries.

### gene_neighbors.json — PASS
33791 genes, each with 50 neighbors. No empty entries.

### gene_neighbors_simple.json — PASS
30319 compact genes, each with 50 neighbors. No empty entries.

### gene_index_simple.json — PASS
25036 compact gene entries.

---

## Summary

| Metric | Count |
|---|---|
| Core indexes | 4/4 parseable and valid |
| Optional indexes | 6/6 parseable and valid |
| M1 blockers | **0** |
| Warnings | 4 (function_index structure, gene_index field names, cellline_tree flatness) |
| Cosmetic issues | 2 |

### Key Findings for T-047 (Loader Hardening)

1. **function_index.json** must be loaded with meta-unwrapping logic — not a flat list.
2. **gene_index.json** fields are `symbol`, `gene_type`, `in_matrix` — not canonical `gene_symbol`/`ensembl_id`.
3. **cellline_tree.json** is flat, not hierarchical; proxy expansion via ontology not available.
4. **drug_index.json** is alias→BRD only; no reverse mapping needed for M1.
5. All neighbor graphs have uniform 50-edge cardinality — good for proxy matching.

### M1 Readiness Verdict

    **Ready for M1 use.** All 10 indexes parse correctly. The 4 warnings are non-blocking and addressable during T-047 loader hardening. The fixture-only M1 path is not required — real indexes are M1-ready today.

The cellline_tree flatness is the only item that may require a decision: if proxy matching needs ontology-based cell line expansion, this index needs a rebuild pass.
