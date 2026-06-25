# Protocol: matrix_loader_v1

## Objective
Create the `pxfquery-T-026` matrix/resource loader from T-021 standard resources (xpr/sh/cp float32 H5AD matrices, JSON indexes, CSV metadata) and T-025 manifest. The loader must discover and validate the actual resource structure at runtime — it must not hard-code matrix shape, obs/var columns, or file paths based on planning notes — and must produce reproducible load evidence with no byte-level copies of upstream files.

## Inputs
- A-001: T-025 resource manifest (D-006) — YAML inventory of all 19 files in T-021/D-004; located at `1_asset/T-025 resource manifest (D-006).yaml` (symlink to `task_resource_manifest_v1/4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml`). Used to enumerate matrix/index/metadata files and verify expected schema categories.
- A-002: T-025 schema summary (D-007) — human-readable schema reference at `1_asset/T-025 schema summary (D-007).md`. Cross-reference during loader validation.
- A-003: T-025 usage notes (D-008) — Python loading snippets and consumption rules at `1_asset/T-025 usage notes (D-008).md`. Reference for validation script approach.
- A-004: T-021 standard_resources bundle (D-004) — canonical 19-file bundle at `1_asset/T-021 standard_resources bundle (D-004)` (symlink to `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`). The actual data loader must load and validate.
- A-005: T-021 standard resource guide (D-001) — detailed documentation covering every file. Reference for expected schemas.
- A-006/A-007: T-021 HTML execution/result reports — reference only.
- A-008: T-021 process records (D-005) — audit/profiling/validation records. Reference for float32 precision evidence.
- A-009: T-021 artifact registry — confirms D-004 bundle identity.

## Steps
1. Read T-025 manifest (A-001) to discover matrix/index/metadata filenames; do not rely on hard-coded shape or column lists from planning notes.
2. Implement a `pxfquery-T-026` loader package at `3_execution/loader/` that:
   - Accepts a bundle root directory as input (default: A-004 bundle path).
   - For each H5AD matrix file (`cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`), opens it with `anndata.read_h5ad` and records: resolved path, shape `(n_obs, n_var)`, `obs.columns`, `var.shape`, `X.dtype`, and basic load timing in seconds.
   - For each JSON index file, opens it with `json.load` and records: resolved path, top-level keys, item count (or recursive stats), and load timing.
   - For each CSV metadata file, opens it with `pandas.read_csv` and records: resolved path, columns, row count, and load timing.
   - For `data_description.yaml`, opens it with `yaml.safe_load` and records top-level keys.
   - Exposes a `load_bundle(bundle_root)` function returning a structured `dict` per file category plus a top-level summary.
   - Exposes a per-file load function `load_matrix(name) -> AnnData`, `load_index(name) -> dict`, `load_metadata(name) -> DataFrame`.
3. Implement a validation script `3_execution/validate_loader.py` that:
   - Invokes `load_bundle` against A-004 bundle root.
   - Writes a machine-readable validation record to `3_execution/loader_validation.json` capturing per-file observed path, shape/keys/columns/row counts, dtype, load time, and any non-fatal warnings.
   - Writes a short readable summary to `3_execution/loader_validation_summary.md`.
   - Runs inside the `pxfquery` conda environment using `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
   - Does not rely on file-existence checks alone — every file must actually be opened and inspected.
4. If loading fails because of a scoped package/path/schema issue (e.g. unexpected dtype, missing column, malformed JSON), repair it inside this task scope by producing a corrected local version of the failing resource at `4_artifact/2_persist/pxfquery_T-026_<name>_repaired.<ext>`. Record what was fixed, source asset id, changed files, validation evidence, and the downstream task that should consume the repaired version in `5_report/repair_log.md`.
5. Register loader source files at `4_artifact/2_persist/loader/` (copies, not symlinks) and produce a Chinese HTML execution report plus a Chinese HTML result report under `4_artifact/3_document/`. Register every new artefact in `4_artifact/registry.yaml`.
6. Write `5_report/completion.md` summarizing load evidence, repaired issues (if any), and downstream consumption guidance for the next task.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, e.g. `pxfquery-T-026`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-026` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Loader Discipline

- The loader must NOT hard-code the matrix shape, obs columns, var count, or any column names from planning notes. It must discover them by reading the actual H5AD files at runtime.
- The loader must NOT copy the T-021 bundle bytes into this task. All loads are by reference (open-from-path).
- The loader must run inside the `pxfquery` conda environment. Use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`. Verify the environment can import `anndata`, `pandas`, `numpy`, `yaml`, `json` before running the loader.
- Schema validation in the loader is permissive: schema is recorded, not asserted. The validation script may report warnings if rows/columns look abnormal, but must not abort the run.

## Deliverables
- `3_execution/loader/` — pxfquery-T-026 loader package source code (Python).
- `3_execution/validate_loader.py` — validation driver script.
- `3_execution/loader_validation.json` — machine-readable load record (path/shape/columns/dtype/timing per file).
- `3_execution/loader_validation_summary.md` — short readable summary.
- `4_artifact/2_persist/loader/` — copy of loader source registered as a deliverable.
- `4_artifact/registry.yaml` — T-026 deliverable registry.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex-mandatory execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex-mandatory result report.
- `5_report/completion.md` — completion report.
- `5_report/repair_log.md` — present only if a bug was repaired inside this task; otherwise omitted.

## Acceptance
- Validation script actually opens all 3 H5AD matrices (`cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`) from A-004 and reports observed `(n_obs, n_var)`, `obs.columns`, `X.dtype`.
- Validation script actually opens every JSON index and CSV metadata file from A-004 and reports observed top-level keys / columns / row counts.
- Loader does not rely on file-existence checks alone — every file must be opened with the corresponding Python library.
- `loader_validation.json` exists, is non-empty, and contains one entry per file actually loaded.
- T-023 is not required; A-001 (T-025 manifest) + A-004 (T-021 bundle) are sufficient sources for this v1 task.
- If a repair was performed, `5_report/repair_log.md` explains source asset, changed files, validation evidence, and downstream consumer guidance.