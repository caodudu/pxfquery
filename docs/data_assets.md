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

Standard resource folder shape:

```text
standard_resources/
  cp_func_ad.h5ad
  sh_func_ad.h5ad
  xpr_func_ad.h5ad
  cellline_index.json
  cellline_neighbors.json
  cellline_tree.json
  drug_index.json
  drug_neighbors.json
  function_index.json
  gene_index.json
  gene_index_simple.json
  gene_neighbors.json
  gene_neighbors_simple.json
  cellline_info_standard.csv
  cellline_meta_standard.csv
  compound_info_standard.csv
  compound_meta_standard.csv
  gene_info_standard.csv
  data_description.yaml
```

Minimum manifest example for that flat folder:

```yaml
root: /path/to/standard_resources
assets:
  matrix.cp_func_ad:
    path: cp_func_ad.h5ad
    role: compound perturbation function matrix
  matrix.sh_func_ad:
    path: sh_func_ad.h5ad
    role: shRNA perturbation function matrix
  matrix.xpr_func_ad:
    path: xpr_func_ad.h5ad
    role: overexpression perturbation function matrix
  metadata.cellline_info:
    path: cellline_info_standard.csv
    role: extended cell line metadata
  metadata.cellline_meta:
    path: cellline_meta_standard.csv
    role: standard cell line metadata
  metadata.compound_info:
    path: compound_info_standard.csv
    role: compound target/MOA metadata
  metadata.compound_meta:
    path: compound_meta_standard.csv
    role: standard compound metadata
  metadata.gene_info:
    path: gene_info_standard.csv
    role: gene metadata
  index.drug_index:
    path: drug_index.json
    role: drug lookup index
  index.gene_index:
    path: gene_index.json
    role: gene lookup index
  index.gene_index_simple:
    path: gene_index_simple.json
    role: simple gene lookup index
  index.cellline_index:
    path: cellline_index.json
    role: cell line lookup index
  index.drug_neighbors:
    path: drug_neighbors.json
    role: drug proxy neighbor index
  index.gene_neighbors:
    path: gene_neighbors.json
    role: gene proxy neighbor index
  index.gene_neighbors_simple:
    path: gene_neighbors_simple.json
    role: simple gene proxy neighbor index
  index.cellline_neighbors:
    path: cellline_neighbors.json
    role: cell line proxy neighbor index
  index.cellline_tree:
    path: cellline_tree.json
    role: cell line lineage tree
  index.function_index:
    path: function_index.json
    role: function lookup index
  provenance.data_description:
    path: data_description.yaml
    role: data provenance description
```

## Expected Runtime Assets

The package should prefer curated runtime assets over raw working directories when available.

| Registry key | Asset | Purpose |
| --- | --- | --- |
| `matrix.cp_func_ad` | `cp_func_ad.h5ad` | compound perturbation function matrix |
| `matrix.sh_func_ad` | `sh_func_ad.h5ad` | shRNA perturbation function matrix |
| `matrix.xpr_func_ad` | `xpr_func_ad.h5ad` | overexpression perturbation function matrix |
| `metadata.cellline_info` | `cellline_info_standard.csv` | extended cell line metadata |
| `metadata.cellline_meta` | `cellline_meta_standard.csv` | standard cell line metadata |
| `metadata.compound_info` | `compound_info_standard.csv` | compound target/MOA metadata |
| `metadata.compound_meta` | `compound_meta_standard.csv` | standard compound metadata |
| `metadata.gene_info` | `gene_info_standard.csv` | gene metadata |
| `index.drug_index` | `drug_index.json` | drug lookup |
| `index.gene_index` | `gene_index.json` | gene lookup |
| `index.gene_index_simple` | `gene_index_simple.json` | simple gene lookup |
| `index.cellline_index` | `cellline_index.json` | cell line lookup |
| `index.drug_neighbors` | `drug_neighbors.json` | drug proxy neighbors |
| `index.gene_neighbors` | `gene_neighbors.json` | gene proxy neighbors |
| `index.gene_neighbors_simple` | `gene_neighbors_simple.json` | simple gene proxy neighbors |
| `index.cellline_neighbors` | `cellline_neighbors.json` | cell line proxy neighbors |
| `index.cellline_tree` | `cellline_tree.json` | cell line lineage tree |
| `index.function_index` | `function_index.json` | function term lookup |
| `provenance.data_description` | `data_description.yaml` | data provenance description |

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
