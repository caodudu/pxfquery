# pxfquery-T-027 Runtime Query Index — Schema Report

**Generated:** 2026-06-23
**Task:** T-027 index_name_normalizer_v1
**Source bundle:** T-021/D-004 standard_resources
**Output directory:** `4_artifact/2_persist/pxfquery_T027_runtime_query_index/`

---

## 1. Purpose

Create a `pxfquery-T-027` runtime query index directory containing resolver-compatible filenames, populated by symlink from the canonical T-021 `standard_resources` bundle. This allows the pxfquery `QueryResolver` (see `code/pxfquery_package/query/resolver.py`) to point its `index_dir` argument directly at the T-027 directory without naming conflicts or file relocation.

The Resolver reads exactly 7 JSON filenames from `index_dir`:

| # | Filename | Resolver consumer |
|---|----------|--------------------|
| 1 | `cellline_index.json` | `CellLineIndex(...)` |
| 2 | `cellline_neighbors.json` | `CellLineIndex(...)` |
| 3 | `gene_index_simple.json` | `GeneIndex(...)` |
| 4 | `gene_neighbors_simple.json` | `GeneIndex(...)` |
| 5 | `drug_index.json` | `DrugIndex(...)` |
| 6 | `drug_neighbors.json` | `DrugIndex(...)` |
| 7 | `function_index.json` | `FunctionIndex(...)` |

The T-021 bundle already uses these exact filenames. This T-027 directory is therefore a thin wrapper that exposes only these 7 resolver-required files (plus 3 supplementary JSONs for full index coverage) as same-name symlinks, with byte-level fidelity preserved at the T-021 source.

---

## 2. Source → Output Mapping

All 7 resolver-required filenames and 3 supplementary JSON files in T-021/D-004 are exposed under the T-027 directory via symlink. Source filenames match output filenames; no renaming is required.

### 2.1 Filename Mapping Table

| T-021 source filename | T-027 output filename | Status | Resolver required | File size | Top-level shape (from Step 3) |
|-----------------------|------------------------|--------|-------------------|-----------|--------------------------------|
| `cellline_index.json` | `cellline_index.json` | symlinked | YES | 3,574 B | `{valid_cells: [...]}` top-level dict, 1 key |
| `cellline_neighbors.json` | `cellline_neighbors.json` | symlinked | YES | 6,610 B | top-level dict with 19 lineage keys (e.g. `bone`, `breast`, `lung`, ...) |
| `cellline_tree.json` | `cellline_tree.json` | symlinked | no (supplementary) | 50,548 B | `{tree, cell_index, meta}` dict, 3 keys |
| `drug_index.json` | `drug_index.json` | symlinked | YES | 180,301 B | `{alias_lowercase: BRD-id}` dict, ~5958 entries |
| `drug_neighbors.json` | `drug_neighbors.json` | symlinked | YES | 4,588,889 B | `{id_no_prefix: [[neighbor, tanimoto_int]]}` dict, ~5312 entries |
| `function_index.json` | `function_index.json` | symlinked | YES | 17,899 B | `{var_names, meta, aliases}` dict, 3 keys (rebuilt by T-021) |
| `gene_index.json` | `gene_index.json` | symlinked | no (supplementary) | 6,418,019 B | full gene index, lowercase symbol key, ~78061 entries |
| `gene_index_simple.json` | `gene_index_simple.json` | symlinked | YES | 364,484 B | `{SYMBOL_UPPER: type_code}` dict, ~25036 entries |
| `gene_neighbors.json` | `gene_neighbors.json` | symlinked | no (supplementary) | 22,815,738 B | full gene neighbor graph, ~33791 keys |
| `gene_neighbors_simple.json` | `gene_neighbors_simple.json` | symlinked | YES | 20,443,987 B | `{symbol: [[neighbor, cosine_int], ...]}` dict, ~30319 entries |

### 2.2 Verdict

| Check | Result |
|-------|--------|
| All 7 resolver-required filenames present in T-027 | **PASS** |
| All T-027 symlinks resolve to readable T-021 files | **PASS** |
| All T-027 JSON files load via `json.load` | **PASS** |
| T-021 source filenames match T-027 output filenames | **PASS** (no name remapping needed) |
| No byte-level duplication of T-021 files into T-027 | **PASS** (symlinks only) |

---

## 3. Source Provenance

- **Source bundle identity:** T-021/D-004 (standard_resources)
- **Manifest entry:** T-025/D-006 (YAML manifest of T-021 bundle, used for file enumeration)
- **Schema reference:** T-025/D-007 (top-level key shape descriptions cross-validated against Step 3 actual JSON load)
- **Resolver contract source:** `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py` lines 92-104

---

## 4. Symlink Resolution Table

| Name | Resolved absolute path |
|------|------------------------|
| `cellline_index.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_index.json` |
| `cellline_neighbors.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_neighbors.json` |
| `cellline_tree.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_tree.json` |
| `drug_index.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/drug_index.json` |
| `drug_neighbors.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/drug_neighbors.json` |
| `function_index.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/function_index.json` |
| `gene_index.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_index.json` |
| `gene_index_simple.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_index_simple.json` |
| `gene_neighbors.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_neighbors.json` |
| `gene_neighbors_simple.json` | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_neighbors_simple.json` |

---

## 5. Validation Results

`3_execution/03_validate/step3_validation.json` records:

| Check | Result |
|-------|--------|
| All 10 entries are symlinks | PASS |
| All 7 resolver-required filenames present | PASS |
| All 7 required symlinks resolve to readable files | PASS |
| All 10 JSON files load as valid JSON | PASS |
| Index directory would be accepted by `QueryResolver(index_dir=...)` | PASS (filename-level check; full runtime init not in scope) |

---

## 6. What Was Intentionally Not Produced

- No byte-level copies of T-021 JSON files in this task directory. All references are symlinks.
- No H5AD matrices or CSV metadata in this task directory — those are part of T-026 (matrix loader) scope and the standard_resources bundle, not runtime query indexes.
- No LLM-driven resolver instantiation test in Step 3 — resolver init requires an LLM client and loaded AnnData matrices, which is out of scope for the index normalization task. Acceptance is verified at the filename+JSON-load level.

---

## 7. Lineage

```
T-021/D-004 (standard_resources bundle, 19 files, 10 JSON indexes)
  └─ T-025/D-006 (YAML manifest enumerating 19 files)
  └─ T-025/D-007 (Schema summary describing JSON shapes)
       │
       └── T-027/4_artifact/2_persist/pxfquery_T027_runtime_query_index/
            └── 10 symlinks → T-021 JSON files (resolver-compatible names)
```
