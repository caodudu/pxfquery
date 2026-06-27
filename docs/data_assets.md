# Data Assets

PxFquery is a data-query package. The current private GitHub repository contains package source, API docs, and tests; the large digital assets live in the local PxFquery workspace and are referenced by task/version lineage.

The package must not invent demo data when local digital assets already exist.

## Current Local Asset Sources

Primary local workspace:

```text
/Users/dudu/Documents/3_Project/12_PxFquery
```

Legacy migrated asset library:

```text
2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/data/
```

Important asset families:

| Asset family | Local examples | Purpose |
| --- | --- | --- |
| Functional matrices | `functional_matrices/*_func_ad.h5ad` | Function-level perturbation response matrices |
| CMAP/LINCS matrices | `cmap_ad_matrices/cmap_*_ad*.h5ad` | Underlying perturbation expression matrices |
| Query indexes | `query_indexes/*_index.json`, `*_neighbors.json` | Cell line, drug, and gene lookup/proxy routing |
| Metadata tables | `metadata_tables/*.csv` | Cell line, compound, and gene metadata |
| Gene embeddings | `genept_embeddings/*.npz`, `*.csv` | Gene similarity/proxy support |
| GSEA tables | `results/gsea_tables/*.csv` | Function enrichment tables |

## Task-Digested Runtime Assets

The package should prefer task-digested assets over raw legacy paths when available.

| CyHex task | Asset | Purpose |
| --- | --- | --- |
| T-025 | `pxfquery_T025_standard_resource_manifest_v20260623.yaml` | Manifest for the standard resource bundle |
| T-026 | matrix loader validation | Confirms matrix loading and shapes |
| T-027 | `pxfquery_T027_runtime_query_index/` | Normalized runtime query indexes |
| T-028 | `pxfquery_T028_function_index/function_index.json` | Validated 91-function index |

Observed T-026 matrix validation:

| Matrix | Shape | Role |
| --- | --- | --- |
| `cp_func_ad.h5ad` | `201014 x 91` | compound perturbation function matrix |
| `sh_func_ad.h5ad` | `189365 x 91` | shRNA perturbation function matrix |
| `xpr_func_ad.h5ad` | `132464 x 91` | overexpression perturbation function matrix |

Observed T-028 function index:

- 91 function terms
- includes Hallmark functions and MP1-MP41 programs
- validated against all three T-021 H5AD matrix `var_names`

## Required Runtime Direction

Future query execution must expose which assets were touched, for example:

```text
index.drug_index      source=T-027/runtime_query_index/drug_index.json
index.cellline_index  source=T-027/runtime_query_index/cellline_index.json
index.function_index  source=T-028/function_index.json
matrix.cp_func_ad     source=T-021/cp_func_ad.h5ad shape=201014x91
matrix.sh_func_ad     source=T-021/sh_func_ad.h5ad shape=189365x91
matrix.xpr_func_ad    source=T-021/xpr_func_ad.h5ad shape=132464x91
```

The GitHub repository should document these asset dependencies, but should not commit large local `.h5ad` matrices unless a separate packaging/data-distribution task explicitly approves that policy.
