# PxFquery T-025 Standard Resource Usage Notes

Generated: 2026-06-23 | Source: T-021/D-004 standard_resources bundle

## 1. How to Load the Bundle

All files resolve from the T-021 bundle path (A-001 in T-025 registration):

```
goal_precomputed_data_exploration/task_standard_resources_optimal_formats/
  4_artifact/2_persist/standard_resources/
```

### H5AD matrices

```python
import anndata as ad
bundle = "path/to/standard_resources"
cp = ad.read_h5ad(f"{bundle}/cp_func_ad.h5ad")
sh = ad.read_h5ad(f"{bundle}/sh_func_ad.h5ad")
xpr = ad.read_h5ad(f"{bundle}/xpr_func_ad.h5ad")

# cp.obs  — perturbation metadata (sig_id, cell_iname, pert_id, cmap_name, ...)
# cp.var  — 91 function term names (index)
# cp.X    — float32 NES scores (dense, n_obs × 91)
```

### JSON indexes

```python
import json
with open(f"{bundle}/drug_index.json") as f:
    drug_index = json.load(f)   # {alias_lower: "BRD-..."}
with open(f"{bundle}/gene_index.json") as f:
    gene_index = json.load(f)   # {lowercase: {symbol, gene_type, in_matrix}}
```

### CSV metadata

```python
import pandas as pd
cellline = pd.read_csv(f"{bundle}/cellline_meta_standard.csv")
compound = pd.read_csv(f"{bundle}/compound_meta_standard.csv")
```

---

## 2. Bundle Reference Rules

- **The canonical bundle path IS** the T-021 bundle directory. This task produces only the manifest/reference files, not a copy of the data.
- **Always load bytes from A-001**, not from the manifest. The manifest is the inventory; the real bytes live at T-021/D-004.
- **Downstream tasks (T-026+) should register A-001 as their input asset**, not as a copy inside this task directory.
- **Relative paths**: from sibling tasks under `goal_resource_index_packs_v1/`, use `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`.

---

## 3. Verification Expectations

Any consumer of the bundle must confirm:

1. **Python-load** every file before relying on its schema.
2. **Matrix dimensions** must match the manifest claims: n_obs and n_vars=91.
3. **Total file count** must be 19.
4. **Total bundle size** must be approximately 323.5 MB (±5%).
5. **function_index.json** must have 91 var_names, 91 meta entries, and 91 aliases.

The manifest file `pxfquery_T025_standard_resource_manifest_v20260623.yaml` provides the authoritative record against which to validate.

---

## 4. Hard Rules

- **Do not split the bundle** — all 19 files ship together.
- **Do not move files** — keep the T-021 directory layout intact.
- **Do not copy bytes into your task directory** — reference A-001.
- **Do not modify** any file inside the T-021 bundle (read-only input).
- **Do not write** new data into the bundle directory (T-025 output goes to this task's `4_artifact/`).

---

## 5. Provenance

- **Bundle:** T-021/D-004, produced 2026-06-23
- **Guide:** T-021/D-001 (`pxfquery_standard_resource_guide_v20260623.md`) — detailed documentation per file
- **Float precision:** float64 → float32, verified lossless at rank correlation 1.000
- **Gap closure:** function_index.json rebuilt from 50 Hallmark + 41 3CA MPS terms