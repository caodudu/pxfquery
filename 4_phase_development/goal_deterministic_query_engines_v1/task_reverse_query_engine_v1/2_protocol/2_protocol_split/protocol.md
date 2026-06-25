# Protocol: reverse_query_engine_v1

## Objective
Create a `pxfquery-T-030` reverse query engine deliverable that runs a deterministic reverse query demo (apoptosis activation / MYC suppression style candidate ranking) producing serializable, ranked candidate outputs and validation reports. The deliverable reuses the T-024 workspace package and T-026 loader/outputs, and must produce fresh runnable evidence — not an in-place repair of upstream artifacts.

## Inputs
- A-001: T-024 workspace package (pxfquery-T-024) — `4_artifact/2_persist/workspace/` with src/-layout, editable install support, pyproject.toml, and the complete reverse.py/ForwardQuery/ReverseQuery module tree. Installed as editable into the `pxfquery` conda env for demo execution.
- A-002: T-026 loader outputs (pxfquery-T-026) — `4_artifact/2_persist/loader/` loader package (`load_bundle`, `load_matrix`), validation JSON (`loader_validation.json`) recording observed matrix shapes/dtypes/obs columns, and completion report listing 19/19 loads succeeded. Provides the `load_matrix` function to open T-021/D-004 matrices without hard-coding schema.
- A-003: T-021 standard resources bundle (D-004) — canonical 19-file float32 H5AD matrices (cp/sh/xpr), JSON indexes, CSV metadata. The actual data consumed by the reverse demo via A-002 loader.
- A-004: T-013 MVP capability review deliverables — capability status matrix (D-003) and failure/missing capability list (D-005). Used to understand what already passed/failed in the legacy reverse query path and to position the T-030 reverse demo as a scoped v1 repair+delivery, not a re-review.
- A-005: Current project protocol — defines conda environment, workspace boundaries, and legacy asset non-modification rules.

## Steps
1. Read and understand the T-024 workspace reverse query code (`query/reverse.py`, `core.py`, `utils.py`, `data/loader.py`) to know the existing `ReverseQuery` class API, `ReverseResult` schema, `build_target_vector`, `cosine_similarity_matrix`, and fuzzy match helpers.
2. Read T-026 `loader_validation.json` or completion report to confirm matrix shapes, obs columns (`pert_id`, `cmap_name`, `cell_iname`), functional term var_names, and dtype (float32). Also confirm which bundle path contains the three H5AD files.
3. Implement a reverse query demo script `3_execution/run_reverse_demo.py` that:
   - Installs/imports pxfquery from the T-024 workspace (editable install) in the `pxfquery` conda environment.
   - Uses `data.loader.DataLoader` or `core.PxFquery.load_data_dir()` to load at least one perturbation type matrix (prefer `cp` for compound coverage) from the A-003 bundle path.
   - Runs a reverse query targeting apoptosis activation and MYC suppression: `activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"]`, optionally filtered to a relevant cell line (e.g., MCF7).
   - Serializes the ranked candidates as a structured JSON file `4_artifact/2_persist/pxfquery_T-030_reverse_demo_candidates.json` (one record per row: rank, cmap_name, cell_iname, similarity, driving_terms).
   - Serializes the full `ReverseResult` metadata (activate, suppress, cell_line, note) into a separate JSON `4_artifact/2_persist/pxfquery_T-030_reverse_demo_meta.json`.
   - Runs entirely inside `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
4. If the demo script encounters a runtime bug (e.g. import error, column mismatch, dtype issue, missing dependency), repair it within this task scope:
   - Apply minimal fixes to a local copy of the affected workspace module(s) under `3_execution/pxfquery_T-030_repaired/`, not in the T-024 workspace.
   - Record what was fixed, which source asset (T-024), the changed file(s), and validation evidence in `5_report/repair_log.md`.
   - The repaired code should be registered as a deliverable and versioned as `pxfquery-T-030`.
5. Write a machine-readable validation record `3_execution/demo_validation.json` capturing: exact command executed, environment (python version, key package versions), matrices loaded, query parameters, candidate count, top-5 candidates with scores, and any warnings.
6. Write Chinese HTML reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — step-by-step execution record.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — human-readable result report showing ranked candidate table, query parameters, and matrix schema summary.
7. Write `5_report/completion.md` summarizing what was built, run evidence, repaired issues (if any), and downstream consumption guidance.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-030`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-030` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Execution Discipline

- All Python execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- The T-024 workspace must be installed as editable (`pip install -e .`) in the `pxfquery` conda env before running the demo.
- Do not copy T-021/D-004 matrix bytes into this task; load by reference through the T-024 workspace data loader or T-026 loader.
- Do not hard-code matrix shapes, column names, or file paths from planning notes — discover them at runtime.
- The demo must actually run and produce non-empty candidate outputs. File existence alone is not acceptable.

## Deliverables
- `3_execution/run_reverse_demo.py` — reverse query demo script.
- `3_execution/demo_validation.json` — machine-readable validation record.
- `4_artifact/2_persist/pxfquery_T-030_reverse_demo_candidates.json` — ranked candidate output (array of {rank, cmap_name, cell_iname, similarity, driving_terms}).
- `4_artifact/2_persist/pxfquery_T-030_reverse_demo_meta.json` — query metadata (activate, suppress, cell_line, note).
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — T-030 artifact registry.
- `5_report/completion.md` — completion report.
- `5_report/repair_log.md` — only if repairs were performed.

## Acceptance
- The reverse demo script actually runs and produces visible, structured candidate results in JSON format.
- Top candidates show meaningful compound/drug names with similarity scores and driving pathway terms.
- Validation JSON is non-empty and captures the exact run parameters and evidence.
- If a T-024 workspace bug blocked the demo, the repair log records the fix with lineage back to T-024.
- T-023 is not required; T-013 provides the gap/capability reference for this v1 task.