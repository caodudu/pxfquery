# Protocol: task_index_name_normalizer_v1

## Objective

Create a `pxfquery-T-027` runtime query index directory that contains resolver-compatible filenames symlinked from the T-021 standard resources bundle (D-004). Deliver the normalized index pack and a schema report mapping each source file to its normalized output.

The pxfquery `QueryResolver` (see `code/pxfquery_package/query/resolver.py`) expects 7 specific JSON filenames under `index_dir`:
- `cellline_index.json`, `cellline_neighbors.json`
- `gene_index_simple.json`, `gene_neighbors_simple.json`
- `drug_index.json`, `drug_neighbors.json`
- `function_index.json`

The T-021 bundle already uses these exact filenames for its JSON indexes (plus 3 extra JSONs: `cellline_tree.json`, `gene_index.json`, `gene_neighbors.json`). This task normalizes the directory so the resolver can point directly at the T-027 runtime index pack.

## Inputs

- A-001: T-021 standard_resources bundle (D-004) — 19-file bundle under `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`. Source of 10 JSON index files.
- A-002: T-025 resource manifest (D-006) — enumerates all 19 files with schema, category, and filenames. Used as the authoritative inventory.
- A-003: T-025 schema summary (D-007) — describes JSON index shapes. Used for cross-reference when producing the schema report.
- A-004: T-021 artifact registry — confirms D-004 identity and file inventory.

## Steps

### Step 1: Read and verify source files

Read A-001 (the T-021/D-004 bundle) and A-002 (T-025/D-006 manifest). Confirm:
- The 10 JSON files exist under the T-021 standard_resources directory.
- Filenames are: `cellline_index.json`, `cellline_neighbors.json`, `cellline_tree.json`, `drug_index.json`, `drug_neighbors.json`, `gene_index_simple.json`, `gene_neighbors_simple.json`, `gene_index.json`, `gene_neighbors.json`, `function_index.json`.
- The 7 resolver-required files are present.

Output: `3_execution/step1_file_inventory.json`.

### Step 2: Create normalized runtime index directory

Create `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` and populate it:

For each of the 7 resolver-required JSON files, create a symlink pointing to the corresponding file in the T-021/D-004 bundle:
- `cellline_index.json` → T-021 bundle `cellline_index.json`
- `cellline_neighbors.json` → T-021 bundle `cellline_neighbors.json`
- `gene_index_simple.json` → T-021 bundle `gene_index_simple.json`
- `gene_neighbors_simple.json` → T-021 bundle `gene_neighbors_simple.json`
- `drug_index.json` → T-021 bundle `drug_index.json`
- `drug_neighbors.json` → T-021 bundle `drug_neighbors.json`
- `function_index.json` → T-021 bundle `function_index.json`

No byte-level copying — symlinks preserve the single source of truth at D-004.

Optionally (not required by resolver but part of the complete index pack), also symlink the 3 supplementary JSON files (`cellline_tree.json`, `gene_index.json`, `gene_neighbors.json`).

Do NOT symlink H5AD matrices or CSV metadata — those are not query indexes and are handled by T-026 (matrix loader).

Output: `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` (directory of symlinks).

### Step 3: Validate normalized index pack

Write and run a Python script that:
1. Lists all symlinks in the normalized directory.
2. For each symlink, resolves and confirms the target file exists and is readable.
3. Loads each JSON file and verifies it is valid JSON.
4. Confirms all 7 resolver-required filenames are present.
5. Confirms a `QueryResolver` would accept this directory as `index_dir` (by inspecting the resolver's expected filenames against the directory contents).

Output: `3_execution/step3_validation.json`.

### Step 4: Write schema report

Write `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md` mapping:
- Each source index filename (in T-021/D-004) → normalized output filename in the T-027 runtime pack.
- Top-level JSON key shape for each file (from T-025/D-007 schema data).
- Resolution status for each file (symlinked, not symlinked, or missing).
- A summary table listing all 7 resolver-required files with pass/fail status from Step 3 validation.

Output: `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md`.

### Step 5: Register outputs and write completion

Register deliverables in `4_artifact/registry.yaml` and write `5_report/completion.md`.

### Required Bug-Repair Handling

- If any filename in T-021/D-004 differs from what the resolver expects, do not modify the upstream bundle. Instead, create the symlink with the resolver-compatible name in the T-027 output directory and record the name mapping in the schema report.
- If any required resolver file is missing from T-021/D-004, record the gap, assess whether it can be rebuilt from other T-021 bundle files, and proceed with what is available.

## Constraints

### Scoped Repair And Versioning

- Do not modify the T-021/D-004 bundle. It is read-only input.
- Do not byte-copy JSON files; use symlinks to preserve single source of truth.
- The normalized directory is `pxfquery_T027_runtime_query_index/` — this is the task's versioned output.
- Do not include H5AD or CSV files in the query index directory.
- No HTML reports are required for this configuration-derivation task — the normalized directory and schema report ARE the deliverable. Validation evidence is stored in `3_execution/`.
- If the execution AI's action prompt requires HTML reports per CyHex §3.3.4, produce minimal `execution_report_v{date}.html` and `result_report_v{date}.html` in `4_artifact/3_document/` reflecting the normalization work, and register them.

## Deliverables

1. `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` — normalized runtime index directory with resolver-compatible symlinks.
2. `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md` — source-to-output schema mapping report.
3. `3_execution/step1_file_inventory.json` — source file inventory evidence.
4. `3_execution/step3_validation.json` — Python validation evidence.
5. `4_artifact/registry.yaml` — updated with T-027 deliverables.
6. `5_report/completion.md` — completion report.
7. `4_artifact/3_document/execution_report_v{date}.html` — execution report (if required by CyHex action prompt).
8. `4_artifact/3_document/result_report_v{date}.html` — result report (if required by CyHex action prompt).

## Acceptance

- All 7 resolver-required filenames exist in the normalized directory.
- Each symlink resolves to a valid JSON file in T-021/D-004.
- All JSON files load as valid JSON.
- The schema report explains the source-to-output mapping for each file.
- No byte-level duplication of T-021 files occurs.
- The resolver's expected filenames are matched exactly.