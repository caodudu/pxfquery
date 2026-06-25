# T-021 Step 1: Package Code Format Audit

**Generated:** 2026-06-23

## Findings

The pxfquery package code (in `code/pxfquery_package/`) was audited across all modules:

### Functional Matrices
- Format: **h5ad (AnnData on-disk)**
- Loader: `anndata.read_h5ad` via `DataLoader.load_local()` (data/loader.py)
- Expected naming: `{cp,sh,xpr}_func_ad.h5ad`
- obs schema (required): sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time
- var schema: 91 functional terms (50 HALLMARK + 41 3CA MPS)
- **No other formats supported** — no csv/parquet/feather/json support for primary matrices

### Query Indexes
- All loaded via `json.load()` from `output/store/query_index/`
- 10 expected index files; **function_index.json is MISSING** from legacy migration

### Key Code Paths
| Module | Class/Function | Input | Format |
|---|---|---|---|
| data/loader.py | DataLoader.load_local | per-type h5ad | anndata |
| index/cellline_index.py | CellLineIndex | 2 JSON | json |
| index/drug_index.py | DrugIndex | 2 JSON | json |
| index/gene_index.py | GeneIndex | 2 JSON | json |
| index/function_index.py | FunctionIndex | 1 JSON | json |
| query/resolver.py | QueryResolver | all 10 JSONs | json |

### Conclusion
PxFquery expects h5ad for data matrices and JSON for indexes. Table-split or alternative formats would require rewriting package code. The function_index.json is a critical missing resource that must be rebuilt.

See also: `4_artifact/2_persist/process_records/step1_package_format_audit.json`