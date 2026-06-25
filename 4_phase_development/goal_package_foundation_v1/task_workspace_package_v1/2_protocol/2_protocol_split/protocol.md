# Protocol: workspace_package_v1

## Objective
Create a current `pxfquery` package workspace under this task's `4_artifact/` using the migrated legacy package code as a read-only source. Deliver a `pyproject.toml` + `src/` layout that can pass `import pxfquery` and basic smoke checks in the project Python environment, without modifying any legacy assets.

## Inputs
- A-001: Legacy PxFquery package code — Read-only source for all `.py` modules, `pyproject.toml`, and package structure to replicate as a `src/`-layout workspace.
- A-002: T-013 MVP capability review deliverables — Reference for what already passed/failed in the legacy package; guides which smoke tests are realistic and which are expected to fail.
- A-003: Current project protocol — Defines the active runtime environment (`pxfquery` conda env), path boundaries, and non-modification rules for legacy assets.

## Steps
1. Read the legacy package `pyproject.toml`, `__init__.py`, and module tree (data, index, llm, prompt, query, viz) from the migrated asset library to understand the current flat package shape, dependencies, and public API.
2. Create a `src/pxfquery/` directory under `4_artifact/2_persist/workspace/` with the same module tree, copying source `.py` files and preserving all subpackage `__init__.py` files. Place `pyproject.toml`, `README.md`, and any root-level `.py` files (excluding `__pycache__`) in `src/pxfquery/`, adjusting imports if needed for the new package root.
3. Produce a workspace-level `pyproject.toml` at `4_artifact/2_persist/workspace/pyproject.toml` with `[tool.setuptools.packages.find]` configured for `where = ["src"]` and dependencies matching the legacy package.
4. In the `pxfquery` conda environment, run a package install from the workspace directory and test `python -c "from pxfquery import PxFquery; print('import OK')"`. Log the exact command, environment, and stdout/stderr output.
5. Run compile-smoke checks on all migrated `.py` modules using `python -m py_compile` or equivalent, recording which modules pass and which fail. Failures should be triaged. If a scoped package fix is required for this task deliverable to run, implement the fix inside this task workspace and record the lineage and validation evidence.
6. Write a workspace summary, an import/compile smoke evidence log, and register all outputs.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-024`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-024` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.
- Do not modify any file inside `2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/`.
- Do not edit legacy source, regenerate indexes, rebuild matrices, or change package APIs.
- The workspace should live entirely under `4_artifact/2_persist/workspace/`.
- Use the project default conda environment (`/Users/dudu/Softwares/miniconda/envs/pxfquery`) for any Python execution.
- `__pycache__` directories in the legacy source must not be copied.
- Legacy `main.py` is a historical placeholder; include it in the workspace for traceability but it need not pass import or smoke checks as a standalone module.
- If `py_compile` fails on a module, record the failure with the error message and fix scoped package issues when the fix is required for the task deliverable to run. Keep fixes inside this task workspace and document lineage.

## Deliverables
- Workspace root: `4_artifact/2_persist/workspace/`
- Compiled package tree: `4_artifact/2_persist/workspace/src/pxfquery/`
- Workspace `pyproject.toml`: `4_artifact/2_persist/workspace/pyproject.toml`
- Workspace `README.md`: `4_artifact/2_persist/workspace/README.md`
- Import/compile smoke evidence log: `4_artifact/2_persist/pxfquery_t024_smoke_evidence_v20260623.md`
- Workspace summary: `4_artifact/3_document/pxfquery_t024_workspace_summary_v20260623.html`
- Execution report: `4_artifact/3_document/execution_report_v20260623.html`
- Result report: `4_artifact/3_document/result_report_v20260623.html`

## Acceptance
- `4_artifact/2_persist/workspace/src/pxfquery/__init__.py` exists and is byte-identical to the legacy source.
- `import pxfquery` succeeds in the `pxfquery` conda environment after local `pip install -e .` from the workspace directory.
- Smoke evidence log documents the exact commands and their output.
- Legacy assets in `2_project_asset/` remain unmodified.