# T-044 package_skeleton_m1 — Protocol

## Objective

Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence. Anchor the package name and module boundaries in T-007 development state report. Do not migrate legacy implementation code and do not implement query behavior beyond import-safe stubs.

## Position In Project

This is the first development-phase task for `goal_m1_python_package_v2`. It delivers the bottom-layer Python package skeleton that later tasks will populate with actual loader, query, CLI, and resolver logic. The skeleton must remain reusable even if later implementation fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | .../4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Anchors intended package name (pxfquery), module structure (core/data/query/index/llm/viz), and component boundaries from legacy development state |
| A-002 | T-007/D-003 | .../4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Confirms per-module status: which modules are implemented/incomplete/historical, guiding what to stub and what to leave for later tasks |
| A-003 | T-007/D-006 | .../4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Provides recommended D001 package setup scope, acceptance criteria, and explicit do-not-do rules (do not copy main.py, do not edit flat assets) |

## Execution Steps

1. Read T-007 development state report and module status matrix to confirm the canonical package name (`pxfquery`) and intended subpackage boundaries: `core`, `data`, `query`, `index`, `llm`, `viz`.
2. Create `pyproject.toml` at the task's working directory with:
   - `[build-system]` using `setuptools` or `hatchling`
   - `[project]` with `name = "pxfquery"`, minimal metadata (version `0.1.0`, Python `>=3.10`), and no external dependencies beyond stubs
   - `[tool.setuptools.packages.find]` or equivalent pointing to `src`
3. Create the `src/pxfquery/` directory structure:
   - `src/pxfquery/__init__.py` — empty package marker
   - `src/pxfquery/core.py` — import-safe stub class `PxFquery` with `__init__` taking optional config dict, no functional methods
   - `src/pxfquery/data/__init__.py` — empty subpackage; stub `loader.py` with a `DataLoader` class placeholder
   - `src/pxfquery/query/__init__.py` — empty subpackage; stub `forward.py` and `reverse.py` with class placeholders
   - `src/pxfquery/index/__init__.py` — empty subpackage; stub `cellline_index.py`, `drug_index.py`, `gene_index.py`, `function_index.py` with class placeholders
   - `src/pxfquery/llm/__init__.py` — empty subpackage; stub `prompts.py` with function placeholders
   - `src/pxfquery/viz/__init__.py` — empty subpackage; stub `plots.py` with function placeholders
   - `src/pxfquery/cli/__init__.py` — empty subpackage for future CLI entry points
4. Run import smoke test: `python -c "import pxfquery; print(pxfquery.__version__)"` from the package root.
5. Record import smoke evidence as a file in `4_artifact/`.

## Constraints

- Use package name `pxfquery` as anchored by T-007 legacy codebase (`core.py` defines `PxFquery`, old package lives under `code/pxfquery_package/`).
- Use `src/pxfquery` layout (src-layout).
- All module stubs must be import-safe: no external imports that would fail, no filesystem operations, no network calls.
- Do not migrate, copy, or read legacy implementation code from `2_project_asset/` or the legacy source root.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep the skeleton dependency-free except for `setuptools`/`hatchling` build requirements.
- The `main.py` file identified by T-007 as historical/incomplete must not appear in this skeleton.

## Forbidden

- Do not copy legacy `code/pxfquery_package/` implementation or any migrated flat asset.
- Do not implement functional query, loader, resolver, index, LLM, or viz behavior.
- Do not install or require runtime dependencies (numpy, pandas, anndata, openai, etc.).
- Do not modify `2_project_asset/`, the migrated flat asset library, or the legacy source root.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| pyproject.toml | task working directory/ | yes |
| Package skeleton with stubs | src/pxfquery/ | yes |
| Import smoke evidence | 4_artifact/2_import_smoke/ | yes |
| Execution script/log | 3_execution/ | yes |
| Completion report | 5_report/completion.md | yes |

## Acceptance Criteria

- `pyproject.toml` exists with name `pxfquery`, minimum Python spec, and build-system declaration.
- `src/pxfquery/` layout exists with all subpackage `__init__.py` files and import-safe stub modules for `core`, `data/loader`, `query/forward`, `query/reverse`, `index/*`, `llm/prompts`, `viz/plots`, and `cli`.
- `python -c "from pxfquery import PxFquery"` succeeds without error.
- No legacy implementation code or flat asset content is present in the skeleton files.
- All outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- If T-007 reports indicate a different canonical package name, stop and request human clarification.
- If any required T-007 artifact cannot be read, stop and report the missing precondition.
- If `pyproject.toml` cannot be built, stop and report the build system constraint.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.