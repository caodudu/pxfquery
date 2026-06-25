# PxFquery T-025 Standard Resource Schema Summary

Generated: 2026-06-23 | Source: T-021/D-004 standard_resources bundle (19 files, 323.47 MB)

## 1. Functional Matrices (H5AD, float32)

Three perturbation-type functional score matrices. All share the same structure:

| Property | Value |
|----------|-------|
| Format | AnnData H5AD |
| X dtype | float32 |
| n_vars | 91 (50 Hallmark + 41 3CA MPS gene sets) |
| obs columns | sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time |
| Score meaning | NES × -log10(FDR+1e-10); positive = activation, negative = inhibition |
| Precision | float64→float32, verified lossless by T-021 (rank correlation=1.000 across all 91 functions) |

| File | Perturbation type | n_obs | Size (MB) |
|------|------------------|-------|-----------|
| cp_func_ad.h5ad | Compound (drug) | 201,014 | 105.11 |
| sh_func_ad.h5ad | shRNA knockdown | 189,365 | 95.52 |
| xpr_func_ad.h5ad | CRISPR/ORF | 132,464 | 64.22 |

**Loading:** `anndata.read_h5ad(path)`

The 91 function terms are listed in `function_index.json` under `var_names`.

---

## 2. Query Indexes (JSON)

### 2.1 Cell Line Indexes

| File | Shape | Size | Purpose |
|------|-------|------|---------|
| cellline_index.json | `{valid_cells: [...]}` (243 cell names) | 3.5 KB | Valid cell line name list |
| cellline_neighbors.json | `{lineage: {disease: {subtype: [cells]}}}` (19 lineages) | 6.6 KB | Cell neighbor groups by lineage hierarchy |
| cellline_tree.json | `{tree, cell_index, meta}` | 50 KB | Full hierarchical cell lineage tree |

### 2.2 Drug Indexes

| File | Shape | Size | Purpose |
|------|-------|------|---------|
| drug_index.json | `{alias_lower: "BRD-..."}` (5,958 keys) | 172 KB | Drug alias → BRD-ID lookup |
| drug_neighbors.json | `{BRD_suffix: [[neighbor, cosine_int], ...]}` (5,312 keys) | 4.38 MB | Drug neighbor similarity graph |

### 2.3 Gene Indexes

| File | Shape | Size | Purpose |
|------|-------|------|---------|
| gene_index.json | `{lowercase: {symbol, gene_type, in_matrix}}` (78,061 keys) | 6.12 MB | Full gene symbol lookup (case-insensitive) |
| gene_index_simple.json | `{SYMBOL: "type_code"}` (25,036 keys) | 348 KB | Gene type lookup (simpler subset) |
| gene_neighbors.json | `{symbol: [[neighbor, cosine_int], ...]}` (33,791 keys) | 21.76 MB | Full gene neighbor similarity graph |
| gene_neighbors_simple.json | `{symbol: [[neighbor, cosine_int], ...]}` (30,319 keys) | 19.50 MB | Simpler gene neighbor graph |

### 2.4 Function Index

| File | Shape | Size | Purpose |
|------|-------|------|---------|
| function_index.json | `{var_names, meta, aliases}` (91 terms) | 17 KB | Function term metadata and aliases (rebuilt by T-021) |

**Loading:** `json.load(open(path))`

---

## 3. Metadata Tables (CSV)

| File | Key Columns | Rows | Size | Purpose |
|------|------------|------|------|---------|
| cellline_meta_standard.csv | cell_iname, cell_lineage, primary_disease, subtype, cell_alias | 240 | 15 KB | Canonical cell line metadata |
| cellline_info_standard.csv | cell_iname, cell_type, donor_sex, cell_lineage, primary_disease, subtype | 240 | 35 KB | Extended cell metadata (Cellosaurus) |
| compound_meta_standard.csv | drug, target, moa, aliases, query_name | 6,647 | 926 KB | Canonical compound metadata |
| compound_info_standard.csv | pert_id, cmap_name, target, moa, canonical_smiles, compound_aliases | 39,321 | 4.19 MB | Full compound information |
| gene_info_standard.csv | gene_id, gene_symbol, ensembl_id, gene_title, gene_type, src | 12,328 | 1.09 MB | Gene annotation metadata |

**Loading:** `pandas.read_csv(path)`

---

## 4. Data Description

| File | Size | Purpose |
|------|------|---------|
| data_description.yaml | 5 KB | Legacy-style asset registry describing 9 upstream source entries (genePT embeddings, CMAP matrices, metadata tables). Uses id/name/path/format/dimensions/key_fields conventions. Preserved as provenance record; not authoritative for manifest entries. |

---

## Provenance

- **Source:** T-021/D-004 standard_resources bundle (`goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`)
- **Validated:** T-021 Python verification (18/18 files pass), float32 precision lossless
- **Related:** T-021/D-001 standard resource guide (`pxfquery_standard_resource_guide_v20260623.md`)