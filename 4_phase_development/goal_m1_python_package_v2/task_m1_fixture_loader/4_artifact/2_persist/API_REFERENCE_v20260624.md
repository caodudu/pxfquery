# M1FixtureLoader — API Reference

## Overview

`M1FixtureLoader` is a minimal, deterministic loader for M1 fixture resources defined by T-043. It reads a `resource_manifest_m1.yaml` manifest and a `fixture_package_m1/` directory (containing H5AD matrices, CSV metadata tables, and JSON index files), validates file existence and supported formats, and returns stable matrix/index access objects.

## Public API

### `pxfquery.data.m1_loader.M1FixtureLoader`

```python
class M1FixtureLoader:
    def __init__(self, manifest_path: str, fixture_root: Optional[str] = None)
```

**Parameters:**
- `manifest_path` — Absolute or relative path to the YAML manifest (e.g. `resource_manifest_m1.yaml`).
- `fixture_root` — Path to the directory containing fixture files. If `None`, derived as the sibling `fixture_package_m1/` of the manifest directory.

**Properties:**
- `manifest` → `M1Manifest` — Parsed manifest with `.resources` (list of resource dicts), `.fixture_resources()`, and `.resource_by_id(id)`.
- `fixture` → `M1Fixture` — Loaded fixture data (lazy; loaded on first access).

### `pxfquery.data.m1_loader.M1Fixture`

```python
@dataclass
class M1Fixture:
    cp: anndata.AnnData          # Compound functional matrix (4x7)
    sh: anndata.AnnData          # shRNA functional matrix (4x7)
    xpr: anndata.AnnData         # ORF overexpression matrix (4x7)
    cellline_meta: pd.DataFrame   # Cell metadata (4x8)
    cellline_info: pd.DataFrame   # Cell detailed info (4x20)
    compound_meta: pd.DataFrame   # Compound metadata (4x9)
    compound_info: pd.DataFrame   # Compound annotations (4x7)
    gene_info: pd.DataFrame       # Gene annotations (8x7)
    # JSON indices as dict:
    cellline_index, cellline_neighbors, cellline_tree
    drug_index, drug_neighbors
    gene_index_simple, gene_neighbors_simple
    gene_index, gene_neighbors
    function_index
```

**Convenience methods:**
- `matrix_shape(name)` → `(n_obs, n_vars)` — Shape of matrix `'cp'`, `'sh'`, or `'xpr'`.
- `matrix_obs_columns(name)` → `list[str]` — Column names of `.obs`.
- `matrix_var_names(name)` → `list[str]` — Variable (function term) names.
- `get_sig_ids(name)` → `list[str]` — All signature IDs.
- `get_matrix_row(name, sig_id)` → `pd.Series` — Single row as a pandas Series indexed by var names.

### `pxfquery.data.m1_loader.M1Manifest`

```python
@dataclass
class M1Manifest:
    raw: dict
    resources: list[dict]
```

- `fixture_resources()` → `list[dict]` — Resources whose `resource_id` starts with `"m1_fixture_"`.
- `resource_by_id(resource_id)` → `dict | None`

## Scope Limits

- Validates: file existence, supported formats (`.h5ad`, `.csv`, `.json`), shape matching against expected values from A-003.
- Does NOT add: full production resource hardening, private query/ranking logic, biological interpretation, or raw project-asset access.
- All fixture data is loaded into memory (small — under 1 MB total).

## Example Usage

```python
from pxfquery.data.m1_loader import M1FixtureLoader

loader = M1FixtureLoader("path/to/resource_manifest_m1.yaml")
fxt = loader.fixture

# Access matrix
cp = fxt.cp
print(cp.shape)                     # (4, 7)
print(cp.obs["sig_id"].tolist())    # list of signature IDs
print(fxt.get_matrix_row("cp", "ABY001_A375_XH:BRD-K66175015:10:24"))

# Access metadata
print(fxt.cellline_meta.columns.tolist())
print(fxt.drug_index.keys())        # 4 drug aliases
```