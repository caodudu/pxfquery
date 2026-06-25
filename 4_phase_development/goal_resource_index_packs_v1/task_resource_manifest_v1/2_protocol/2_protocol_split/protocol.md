# task_resource_manifest_v1 — Protocol

## Objective

Build the `pxfquery-T025` standard resource manifest from the T-021 `standard_resources` bundle (D-004). This task is a configuration/derivation step: its deliverables are a manifest file, a schema summary, and usage notes — no new data is produced.

The manifest is the formal, machine-readable record of every file in the T-021 bundle and must be reusable by:

1. The CyHex task graph (as the registered output asset for T-025).
2. Downstream development and testing tasks that need to know exactly which files exist, where they live, what each file's role is, and what schema/integrity expectations apply.
3. Future release / packaging tasks that will vendor the bundle.

## Inputs

- A-001: T-021 standard_resources bundle (D-004) — the 19-file bundle under `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`. The bundle is the source of truth for every entry in the manifest.
- A-002: T-021 standard resource guide (D-001) — cross-reference document explaining each file; reused (not copied) to derive usage notes.
- A-003/A-004: T-021 HTML reports — historical record, optional reference.
- A-005: T-021 process records — optional audit trail for precision / format decisions.
- A-006: T-021 artifact registry — confirms D-004 identity and core status.

## Steps

### Step 1: Enumerate bundle contents

List every file under `goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` (relative path from this task: `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources`). Record 19 files: 3 H5AD matrices, 10 JSON indexes, 5 CSV metadata tables, 1 YAML data description. For each entry record: filename, format, file size in bytes (rounded MB), and SHA-style identifier when present inside the bundle (e.g. data_description.yaml ids).

Output: inline table inside the manifest draft.

### Step 2: Derive schema summary

For each file classify schema into one of three categories:

1. **Tabular matrix (H5AD)** — `obs` columns (sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time, plus dtype-specific extras), `var` names (91 function terms), `X` dtype (float32), `X` shape. The manifest captures obs columns verbatim and var count; it does not duplicate the 91 function names (those belong to `function_index.json`).
2. **JSON index** — store the top-level key shape (e.g. cellline_index.json → `{valid_cells: [...]}`; cellline_neighbors.json → `{bone: {bone cancer: {ewing's sarcoma: [...]}}}` lineage tree; drug_neighbors.json → `{BRD-suffix: [[neighbor, sim_int]]}`).
3. **CSV metadata** — column names and row counts (from T-021 verification: cellline ~240 rows, compound ~6,647 / ~39,321, gene ~12,328).

For `data_description.yaml`: capture only its `id / name / path / format / dimensions / key_fields` conventions; do not copy its full asset entries.

Output: schema inventory embedded in the manifest.

### Step 3: Build manifest YAML

Write `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` with this minimal structure:

```yaml
manifest_version: 1
task_id: T-025
name: pxfquery-T025 standard resource manifest
generated: 2026-06-23
source_bundle:
  identity: T-021/D-004
  path: ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/
  file_count: 19
  total_size_estimate_mb: <measured at execution time>
files:
  - id: SRM-001
    filename: cp_func_ad.h5ad
    category: matrix
    format: h5ad
    role: compound (cp) perturbation functional score matrix
    obs_columns: [...]
    var_columns_count: 91
    notes: float32; dimensions 201014x91
  - ... (one entry per file)
```

Each entry carries: `id`, `filename`, `category` (matrix/index/metadata/description), `format`, `role`, `notes`. Matrix entries also carry `obs_columns` and `var_count`. Index entries carry `top_level_keys`. Metadata entries carry `row_count_estimate` and `key_columns`.

Place this in `4_artifact/2_persist/` so it lives next to the T-025 schema summary and usage notes.

Output: `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml`.

### Step 4: Write schema summary

Write `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` as a human-readable Markdown reference. One section per file category:

1. **Functional matrices (H5AD)** — common obs schema, var=91 functions, float32, score semantics.
2. **Query indexes (JSON)** — purpose of each: cell/drug/gene lookup, neighbor graphs, function index, cell-line lineage tree. Brief shape description per file.
3. **Metadata tables (CSV)** — purpose of each, key columns, row counts.
4. **data_description.yaml** — convention-only; entries inside are descriptive sub-records of the bundle.

Output: `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md`.

### Step 5: Write usage notes

Write `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` describing:

1. How to load the bundle (suggested Python snippets for h5ad via `anndata.read_h5ad`, JSON via `json.load`, CSV via `pandas.read_csv`).
2. How downstream tasks should reference the bundle path: the canonical path is the T-021 bundle path; the manifest is the declared inventory but the bytes always come from A-001.
3. Verification expectations: any consumer of the bundle must Python-load every file before relying on its schema; matrix dimensions must match the manifest claims.
4. Provenance pointer back to T-021/D-004 and T-021/D-001 guide.
5. Hard rules: do not split the bundle; do not move files; do not duplicate into this task's own directory.

Output: `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md`.

### Step 6: Validate manifest

Run a Python check that:

1. Lists the bundle directory and confirms the manifest's `files:` list has exactly the same filenames as `os.listdir(bundle_path)`.
2. Confirms the file count in the manifest matches `len(os.listdir(bundle_path))`.
3. Confirms each manifest entry's filename points to an existing file.
4. Confirms `data_description.yaml` is referenced and exists.
5. Records total bundle size in MB and writes it into the manifest header.

Save the validation output to `3_execution/step6_validation.json`.

Output: validation JSON + a one-line confirmation in completion.md.

### Step 7: Register outputs and write completion

Register the three artefact files in `4_artifact/registry.yaml` (D-006 manifest, D-007 schema summary, D-008 usage notes, D-009 validation record) and the manifest is added as an input-side asset for future tasks by writing `1_asset/registration.yaml` updates for any consumer-facing entries. Write `5_report/completion.md` summarising what was produced and what was intentionally not produced (no new data, no byte-level copies).

Output: registry update + completion.md.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-025`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-025` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

- Do not modify the T-021 bundle. It is read-only input.
- Do not copy any bundle bytes into this task directory. The manifest is the inventory; the actual data lives at A-001.
- Manifest must be single-file and parseable as YAML (no anchors to cross-task files).
- Do not duplicate the 91 function names verbatim inside the manifest; reference `function_index.json` instead.
- Schema summary and usage notes may cite external paths but must remain readable on their own.
- No HTML reports are required for this configuration task — manifest, schema summary, and usage notes ARE the deliverable. Loading/validation evidence is captured in `3_execution/` plus `5_report/completion.md`.

## Deliverables

1. `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` — the manifest.
2. `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` — schema summary.
3. `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` — usage notes.
4. `4_artifact/registry.yaml` — updated with T-025 artefacts.
5. `3_execution/step6_validation.json` — Python validation evidence.
6. `5_report/completion.md` — completion report.

## Acceptance

- Manifest lists exactly the 19 files in the T-021 bundle (binary byte-for-byte equality between manifest `files[]` filenames and `os.listdir(bundle_path)`).
- Each matrix entry records `obs` columns and a 91-var count consistent with T-021.
- Each JSON index entry records its top-level key shape.
- Each CSV entry records key columns and approximate row count.
- Total bundle size in the manifest is within ±5% of the actual `os.path.getsize` sum.
- `data_description.yaml` is included and labelled as `description`.
- No byte-level duplication of bundle files occurs in this task directory.
- Schema summary and usage notes are self-contained Markdown files that a developer can read independently of T-021/D-001.
- `4_artifact/registry.yaml` lists every new artefact with a stable `identity: T-025/D-006..009`.
