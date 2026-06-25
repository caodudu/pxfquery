# PxFquery Standard Resources — Optimal Format Guide

**Task:** T-021 standard_resources_optimal_formats
**Generated:** 2026-06-23
**Status:** Python-verified, ready for downstream development and testing

---

## 目录 / Table of Contents

1. [Overview](#overview)
2. [Total Footprint](#total-footprint)
3. [Functional Matrices](#functional-matrices)
4. [Query Indexes](#query-indexes)
5. [Metadata Tables](#metadata-tables)
6. [Format Decisions](#format-decisions)
7. [Float Precision Trade-off](#float-precision-trade-off)
8. [Function Index](#function-index)
9. [Python Verification Results](#python-verification-results)
10. [Usage in pxfquery](#usage-in-pxfquery)

---

## Overview

This guide documents the standard built-in resources for PxFquery derived from the legacy precomputed data. All resources have been:

1. **Evaluated** for optimal format and precision
2. **Produced** in the best format for pxfquery compatibility and file-size efficiency
3. **Python-verified** for schema correctness, data integrity, and loadability
4. **Consolidated** — duplicates removed, canonical versions selected

All standard resources are located under:
```
4_artifact/2_persist/standard_resources/
```

---

## Total Footprint

| Category | Files | Size (MB) | Notes |
|---|---|---|---|
| Functional matrices (h5ad f32) | 3 | 264.85 | cp: 105.11, sh: 95.52, xpr: 64.22 |
| Query indexes (JSON) | 10 | 58.25 | includes rebuilt function_index.json |
| Metadata tables (CSV) | 5 | 6.24 | consolidated, deduplicated |
| Misc (yaml) | 1 | 0.01 | data_description.yaml |
| **Total** | **19** | **329.35** | |

**Original legacy footprint (h5ad f64 only):** 1,472.98 MB
**Savings:** 1,143.63 MB (77.6%)

---

## Functional Matrices

### Overview

The three functional score matrices are the core query substrate for PxFquery. Each contains perturbation observations × 91 functional term scores.

| File | Perturbation | n_obs | n_vars | dtype | Size (MB) |
|---|---|---|---|---|---|
| `cp_func_ad.h5ad` | Compound (drug) | 201,014 | 91 | float32 | 105.11 |
| `sh_func_ad.h5ad` | shRNA knockdown | 189,365 | 91 | float32 | 95.52 |
| `xpr_func_ad.h5ad` | ORF overexpression | 132,464 | 91 | float32 | 64.22 |

### Schema

**obs (rows — perturbation experiments):**
| Column | Type | Description |
|---|---|---|
| sig_id | string | Unique signature identifier (e.g., ABY001_A375_XH:BRD-...) |
| project_code | string | Project code (e.g., ABY, CGS, XPR) |
| cell_iname | string | Cell line name (e.g., A375, BICR6, ES2) |
| pert_id | string | Perturbation ID (e.g., BRD-A90490067, CGS001-2) |
| cmap_name | string | Common name (e.g., fulvestrant, A2M, STAC) |
| pert_dose | float | Dose value |
| pert_time | float | Time point |

**var (columns — functional terms):**
- 50 MSigDB HALLMARK gene sets (e.g., HALLMARK_ADIPOGENESIS, HALLMARK_APOPTOSIS)
- 41 3CA MPS programs (e.g., MP39 Metal-response, MP40 PDAC-related)

**X (scores):**
- dtype: float32 (converted from float64)
- Range: [-10.0, 10.0]
- Dense matrix, no sparsity (nonzero fraction ≈ 1.0)
- Score semantics: signed numeric functional score

### Source

Converted from canonical legacy files:
- M-0105_cp_func_ad.h5ad → cp_func_ad.h5ad
- M-0106_sh_func_ad.h5ad → sh_func_ad.h5ad
- M-0107_xpr_func_ad.h5ad → xpr_func_ad.h5ad

M-0199~M-0201 are byte-identical duplicates (confirmed by MD5) and were not used.

---

## Query Indexes

### Overview

Ten JSON files that provide runtime exact-match and neighbor lookup for the pxfquery resolver pipeline.

| File | Role | Size (MB) | Schema |
|---|---|---|---|
| `cellline_index.json` | Valid cell line names | 0.003 | `{"valid_cells": [...]}` |
| `cellline_neighbors.json` | Lineage-based cell grouping | 0.006 | `{lineage: {disease: {subtype: [cells]}}}` |
| `cellline_tree.json` | Full cell line ontology tree | 0.048 | `{tree, cell_index, meta}` |
| `drug_index.json` | Drug alias → BRD-id | 0.172 | `{"alias_lower": "BRD-..."}` |
| `drug_neighbors.json` | Drug similarity neighbors | 4.40 | `{id_no_prefix: [[id, t_int], ...]}` |
| `gene_index_simple.json` | Gene symbol → type | 0.348 | `{"SYMBOL_UPPER": "type_code"}` |
| `gene_neighbors_simple.json` | Gene semantic neighbors | 19.50 | `{symbol: [[neighbor, cosine_int], ...]}` |
| `gene_index.json` | Full gene lookup | 6.10 | `{lowercase: {symbol, gene_type, in_matrix}}` |
| `gene_neighbors.json` | Full gene neighbors | 21.80 | Same shape as simple version |
| `function_index.json` | Function term catalog | 0.017 | `{var_names, meta, aliases}` |

### Compactness Invariants

- **Drug neighbors:** BRD- prefix stripped from keys and values; Tanimoto similarity stored as `int = round(t × 100)`
- **Gene neighbors:** Cosine similarity stored as `int = round(cosine × 100)`; lists sorted descending
- **Function index:** Rebuilt from matrix var_names (was missing in legacy migration)

### Source

All index files copied from `legacy_flat_asset_library_v20260614/data/query_indexes/`, with `function_index.json` rebuilt from scratch.

---

## Metadata Tables

### Overview

Consolidated CSV metadata tables for cell lines, compounds, and genes. Duplicate vintage pairs have been deduplicated; enriched versions are selected as canonical.

| File | Rows | Columns | Size (MB) | Source |
|---|---|---|---|---|
| `cellline_meta_standard.csv` | 240 | 8 | 0.015 | M-0234 (enriched, deduplicated from M-0093/M-0184) |
| `cellline_info_standard.csv` | 240 | 20 | 0.035 | M-0185 (detailed beta annotations) |
| `compound_meta_standard.csv` | 6,647 | 9 | 0.948 | M-0235 (enriched, deduplicated from M-0099/M-0188) |
| `compound_info_standard.csv` | 39,321 | 7 | 4.19 | M-0186 (detailed beta annotations) |
| `gene_info_standard.csv` | 12,328 | 7 | 1.09 | M-0187 (gene annotations) |

### Key Deduplication Decisions

- **Cell line metadata:** M-0093 and M-0184 are byte-identical duplicates. Selected M-0234 (enriched) as canonical.
- **Compound metadata:** M-0099 and M-0188 are byte-identical duplicates. Selected M-0235 (enriched) as canonical.
- **Beta info files** (M-0185, M-0186, M-0187) located under `cmap_ad_matrices/` — consolidated into standard CSV files.

---

## Format Decisions

| Decision | Rationale | Evidence |
|---|---|---|
| **h5ad float32** (not float64) | Perfect rank preservation, 82% size reduction | Rank corr = 1.00000 across all 91 functions; Top 5% overlap = 100% |
| **h5ad** (not parquet/feather/table-split) | pxfquery package uses `anndata.read_h5ad` exclusively; h5ad f32 is 105 MB (vs 66 MB feather but zero compatibility) | Package code inspection: `DataLoader.load_local` only calls `ad.read_h5ad` |
| **JSON** for indexes | Already compact and directly compatible with pxfquery index loaders; no benefit from format conversion | Integer-coded similarity values, prefix-stripped keys |
| **CSV** for metadata | Human-readable, pandas-compatible, small (< 5 MB each) | All metadata files under 5 MB |

---

## Float Precision Trade-off

### Test Protocol

For each functional matrix (cp/sh/xpr × 91 functions = 273 column tests):
1. Convert X from float64 to float32 and back to float64
2. Measure: max absolute difference, rank correlation, top/bottom 5% rank overlap

### Results

| Metric | cp | sh | xpr |
|---|---|---|---|
| Rank correlation (per-function mean) | 1.000000 | 1.000000 | 1.000000 |
| Rank correlation (per-function min) | 1.000000 | 1.000000 | 1.000000 |
| Top 5% rank overlap (mean) | 100.0% | 100.0% | 100.0% |
| Top 5% rank overlap (min) | 100.0% | 100.0% | 100.0% |
| Bottom 5% rank overlap (mean) | 100.0% | 100.0% | 100.0% |
| Bottom 5% rank overlap (min) | 100.0% | 100.0% | 100.0% |
| Max absolute difference | ~0.00025 | ~0.00025 | ~0.00025 |
| Mean absolute difference | ~3×10⁻⁶ | ~3×10⁻⁶ | ~3×10⁻⁶ |

### Conclusion

**float32 conversion is lossless for practical purposes.** At a score scale of [-10, 10], the maximum error of 0.00025 is equivalent to 0.00125% of the value range. Rank ordering (the primary retrieval signal for forward/reverse queries) is perfectly preserved. No downstream query result is affected.

**Decision:** All standard functional matrices use **float32**.

---

## Function Index

The `function_index.json` was **missing** from the legacy migration (identified by T-007 and confirmed by T-014). T-021 has rebuilt it.

### Rebuilt Schema

```json
{
  "var_names": ["HALLMARK_ADIPOGENESIS", ..., "MP41 Unassigned"],
  "meta": {
    "HALLMARK_ADIPOGENESIS": {"source": "hallmark", "label": "Adipogenesis"},
    "MP39 Metal-response": {"source": "3ca_mps", "label": "Metal-response", "mp_id": 39},
    ...
  },
  "aliases": {
    "hallmark_adipogenesis": "HALLMARK_ADIPOGENESIS",
    "mp39_metal-response": "MP39 Metal-response",
    ...
  }
}
```

- 50 HALLMARK terms with source "hallmark"
- 41 3CA MPS programs with source "3ca_mps" and mp_id
- Case-insensitive aliases for all 91 terms
- Compatible with `FunctionIndex` from pxfquery package (index/function_index.py)

---

## Python Verification Results

| Category | Files tested | Pass | Fail |
|---|---|---|---|
| Functional matrices (h5ad) | 3 | 3 | 0 |
| Query indexes (JSON) | 9 + 1 rebuilt = 10 | 10 | 0 |
| Metadata tables (CSV) | 5 | 5 | 0 |
| **Total** | **18** | **18** | **0** |

### Verification Checklist (per file type)

**h5ad matrices:**
- [x] File exists and readable by `anndata.read_h5ad`
- [x] `X.dtype == float32`
- [x] `n_vars == 91`
- [x] obs columns include sig_id, cell_iname, pert_id, cmap_name, project_code
- [x] No NaN or Inf in X
- [x] Score range within [-10, 10]
- [x] Var names start with HALLMARK_ or MP prefix

**JSON indexes:**
- [x] File exists and parsable by `json.load`
- [x] Contains expected top-level structure (dict or list)
- [x] Non-empty

**CSV metadata:**
- [x] File exists and readable by `pandas.read_csv`
- [x] Required key columns present

---

## Usage in pxfquery

### Loading Standard Resources

```python
from pathlib import Path
import anndata as ad

RESOURCES = Path("4_artifact/2_persist/standard_resources/")

# Load functional matrices
cp_adata = ad.read_h5ad(RESOURCES / "cp_func_ad.h5ad")
sh_adata = ad.read_h5ad(RESOURCES / "sh_func_ad.h5ad")
xpr_adata = ad.read_h5ad(RESOURCES / "xpr_func_ad.h5ad")

# Or use PxFquery DataLoader
from pxfquery.data.loader import DataLoader
loader = DataLoader()
loader.load_all_local(str(RESOURCES))

# Load indexes (for QueryResolver)
import json
with open(RESOURCES / "function_index.json") as f:
    func_idx = json.load(f)
```

### Package Compatibility

All standard resources match the pxfquery package expectations:

| Package component | Expected format | Standard resource | Match |
|---|---|---|---|
| `DataLoader.load_local()` | `.h5ad` via `anndata.read_h5ad` | `{cp,sh,xpr}_func_ad.h5ad` | Yes |
| `CellLineIndex` | `cellline_index.json` + `cellline_neighbors.json` | Same | Yes |
| `DrugIndex` | `drug_index.json` + `drug_neighbors.json` | Same | Yes |
| `GeneIndex` | `gene_index_simple.json` + `gene_neighbors_simple.json` | Same | Yes |
| `FunctionIndex` | `function_index.json` | Rebuilt, schema-compatible | Yes |
| `QueryResolver` | `output/store/query_index/` (all 9+1 JSONs) | All present | Yes |

### Known Gaps

| Gap | Status | Notes |
|---|---|---|
| 5 CMAP upstream H5ADs | Corrupt in legacy migration (truncated HDF5) | Cannot be recovered from migrated assets. Not needed for pxfquery; needed only for provenance trace. |
| `function_index.json` | **Rebuilt by T-021** | Was missing from legacy migration; now 91 functions in correct format |
| GSEA result artifacts | Available as provenance only | Not included in standard resources; historical evidence, not runtime dependency |
| GenePT embeddings (867 MB) | Not included | Optional gene proxy resource; too large for standard resource set |

---

## Files Produced

All under `4_artifact/2_persist/standard_resources/`:

1. `cp_func_ad.h5ad` — Compound functional matrix (float32, 105.11 MB)
2. `sh_func_ad.h5ad` — shRNA functional matrix (float32, 95.52 MB)
3. `xpr_func_ad.h5ad` — ORF functional matrix (float32, 64.22 MB)
4. `cellline_index.json` — Valid cell line names
5. `cellline_neighbors.json` — Lineage-based cell grouping
6. `cellline_tree.json` — Cell line ontology tree
7. `drug_index.json` — Drug alias → BRD-id
8. `drug_neighbors.json` — Drug similarity neighbors
9. `gene_index_simple.json` — Gene symbol → type
10. `gene_neighbors_simple.json` — Gene semantic neighbors
11. `gene_index.json` — Full gene lookup
12. `gene_neighbors.json` — Full gene neighbors
13. `function_index.json` — Function term catalog (rebuilt)
14. `cellline_meta_standard.csv` — Cell line metadata (enriched)
15. `cellline_info_standard.csv` — Cell line annotations (beta)
16. `compound_meta_standard.csv` — Compound metadata (enriched)
17. `compound_info_standard.csv` — Compound annotations (beta)
18. `gene_info_standard.csv` — Gene annotations (beta)
19. `data_description.yaml` — Asset description reference

**Total: 19 files, ~329 MB**

