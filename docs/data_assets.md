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

Download/cache use:

```python
pxf.resources.download()
```

In `0.4.0`, download/cache is not implemented. Users provide a local resource pack with `pxf.resources.use(...)`.

## Internal Pack Layout

The resource pack currently uses the `standard_resources/` layout produced by the project preprocessing pipeline. That file layout is an internal validation concern, not a user-facing setup contract.

Observed development matrix shapes:

| Matrix | Shape | Role |
| --- | --- | --- |
| `cp_func_ad.h5ad` | `201014 x 91` | compound perturbation function matrix |
| `sh_func_ad.h5ad` | `189365 x 91` | shRNA perturbation function matrix |
| `xpr_func_ad.h5ad` | `132464 x 91` | overexpression perturbation function matrix |

The package source must not hard-code a developer's local resource path.

## Runtime Direction

The query engine should report resource-pack evidence in biological terms first, with file-level diagnostics available only in structured output.
