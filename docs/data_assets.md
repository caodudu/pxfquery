# Data Assets

PxFquery is a data-query package. The current private GitHub repository contains package source, API docs, and tests; large digital assets are registered at runtime from a user-provided root or manifest.

The package must not invent demo data when local digital assets already exist.
It must also not hard-code one developer's workspace path.

User code should register data assets before parsing or routing:

```python
pxf.register_assets(root="/path/to/standard_resources")
```

or:

```python
pxf.register_assets(manifest="assets.yaml")
```

The manifest path is the stable contract when files move.

## Asset Registration Contract

PxFquery accepts either a standard resource root or a manifest. Prefer a manifest for portable projects, because it survives file moves and arbitrary directory layouts.

Minimum manifest example:

```yaml
root: /path/to/pxfquery_assets
assets:
  matrix.cp_func_ad:
    path: matrices/cp_func_ad.h5ad
    role: compound perturbation function matrix
  matrix.sh_func_ad:
    path: matrices/sh_func_ad.h5ad
    role: shRNA perturbation function matrix
  matrix.xpr_func_ad:
    path: matrices/xpr_func_ad.h5ad
    role: overexpression perturbation function matrix
  index.drug_index:
    path: indexes/drug_index.json
    role: drug lookup index
  index.gene_index:
    path: indexes/gene_index.json
    role: gene lookup index
  index.cellline_index:
    path: indexes/cellline_index.json
    role: cell line lookup index
  index.function_index:
    path: indexes/function_index.json
    role: function lookup index
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

## Expected Runtime Assets

The package should prefer curated runtime assets over raw working directories when available.

| Registry key | Asset | Purpose |
| --- | --- | --- |
| `matrix.cp_func_ad` | `cp_func_ad.h5ad` | compound perturbation function matrix |
| `matrix.sh_func_ad` | `sh_func_ad.h5ad` | shRNA perturbation function matrix |
| `matrix.xpr_func_ad` | `xpr_func_ad.h5ad` | overexpression perturbation function matrix |
| `index.drug_index` | `drug_index.json` | drug lookup |
| `index.gene_index` | `gene_index.json` | gene lookup |
| `index.cellline_index` | `cellline_index.json` | cell line lookup |
| `index.function_index` | `function_index.json` | function term lookup |

Observed development matrix validation:

| Matrix | Shape | Role |
| --- | --- | --- |
| `cp_func_ad.h5ad` | `201014 x 91` | compound perturbation function matrix |
| `sh_func_ad.h5ad` | `189365 x 91` | shRNA perturbation function matrix |
| `xpr_func_ad.h5ad` | `132464 x 91` | overexpression perturbation function matrix |

Observed development function index:

- 91 function terms
- includes Hallmark functions and MP1-MP41 programs
- validated against all three H5AD matrix `var_names`

## Required Runtime Direction

Future query execution must expose which assets were touched, for example:

```text
index.drug_index      source=assets:index.drug_index
index.cellline_index  source=assets:index.cellline_index
index.function_index  source=assets:index.function_index
matrix.cp_func_ad     source=assets:matrix.cp_func_ad
matrix.sh_func_ad     source=assets:matrix.sh_func_ad
matrix.xpr_func_ad    source=assets:matrix.xpr_func_ad
```

The GitHub repository should document these asset dependencies, but should not commit large local `.h5ad` matrices unless a separate packaging/data-distribution task explicitly approves that policy.
