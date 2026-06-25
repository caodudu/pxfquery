# T-021 Step 5: Python Verification & Validation

**Generated:** 2026-06-23

## Results: 18/18 PASS (0 failures)

### Functional Matrices (h5ad float32)
| File | n_obs | n_vars | dtype | No NaN | No Inf | Range OK | Status |
|---|---|---|---|---|---|---|---|
| cp_func_ad.h5ad | 201,014 | 91 | float32 | ✓ | ✓ | ✓ | PASS |
| sh_func_ad.h5ad | 189,365 | 91 | float32 | ✓ | ✓ | ✓ | PASS |
| xpr_func_ad.h5ad | 132,464 | 91 | float32 | ✓ | ✓ | ✓ | PASS |

### Query Indexes (JSON)
| File | Structure | Non-empty | Status |
|---|---|---|---|
| cellline_index.json | dict | ✓ | PASS |
| cellline_neighbors.json | dict | ✓ | PASS |
| cellline_tree.json | dict | ✓ | PASS |
| drug_index.json | dict | ✓ | PASS |
| drug_neighbors.json | dict | ✓ | PASS |
| gene_index_simple.json | dict | ✓ | PASS |
| gene_neighbors_simple.json | dict | ✓ | PASS |
| gene_index.json | dict | ✓ | PASS |
| gene_neighbors.json | dict | ✓ | PASS |
| function_index.json | dict | ✓ | PASS |

### Metadata Tables (CSV)
| File | Required Columns | Status |
|---|---|---|
| cellline_meta_standard.csv | cell_iname, cell_lineage, primary_disease | PASS |
| cellline_info_standard.csv | cell_iname, cellosaurus_id, cell_lineage | PASS |
| compound_meta_standard.csv | drug, target, smiles | PASS |
| compound_info_standard.csv | pert_id, cmap_name, target | PASS |
| gene_info_standard.csv | gene_id, gene_symbol, ensembl_id | PASS |

## Verification Protocol

### H5AD checks:
1. File readable by `anndata.read_h5ad`
2. `X.dtype == float32`
3. `n_vars == 91`
4. All required obs columns present (sig_id, cell_iname, pert_id, cmap_name, project_code)
5. No NaN in X
6. No Inf in X
7. Score range within [-100, 100] (actual: [-10, 10])

### JSON checks:
1. File parsable by `json.load`
2. Top-level structure is dict (or list)
3. Non-empty

### CSV checks:
1. File readable by `pandas.read_csv`
2. Key columns present

See also: `4_artifact/2_persist/process_records/step5_verification_results.json`