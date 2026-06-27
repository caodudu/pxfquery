# Data Assets And Resource Packs

PxFquery should expose data to users as one logical resource pack.

The resource pack contains perturbation-function matrices, entity indexes, metadata tables, and provenance. Those files are implementation details for validation and advanced debugging; they are not the normal user setup interface.

## User-Level Resource API

Current local-pack use:

```python
from pxfquery import PxFQuery

pxf = PxFQuery()
pxf.resources.use("/path/to/pxfquery_resource_pack")
status = pxf.resources.status()
```

Planned download/cache use:

```python
pxf.resources.download()
```

In `0.2.0`, download is a product-interface placeholder: it reports that official download is not configured yet. A later MS8 task will add archive download, cache location, manifest verification, and version checks.

## Compatibility API

The older registration API remains available:

```python
pxf.register_assets(root="/path/to/standard_resources")
pxf.register_assets(manifest="assets.yaml")
```

This is useful for local development, tests, and offline environments.

## Internal Pack Layout

The current resource pack content is the flat `standard_resources/` layout:

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

Observed development matrix shapes:

| Matrix | Shape | Role |
| --- | --- | --- |
| `cp_func_ad.h5ad` | `201014 x 91` | compound perturbation function matrix |
| `sh_func_ad.h5ad` | `189365 x 91` | shRNA perturbation function matrix |
| `xpr_func_ad.h5ad` | `132464 x 91` | overexpression perturbation function matrix |

The package source must not hard-code a developer's local resource path.

## Runtime Direction

Future resource-pack tasks should add:

- default cache directory
- official archive URL configuration
- manifest and hash verification
- resource-pack version reporting
- schema checks for JSON, CSV, and H5AD files
- readable missing-resource messages

The query engine should eventually report resource-pack evidence in biological terms first, with file-level diagnostics available only in structured output.
