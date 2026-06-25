# Check Handoff Before Exec: T-044 package_skeleton_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1
- Allowed write dirs: 3_execution/, 4_artifact/, 5_report/
- Forbidden dirs: predecessor task directories, 2_project_asset/, 1_project_init/, legacy source root
- Required registry: 4_artifact/registry.yaml (update with outputs after delivery)
- Must stop if:
  - T-007 reports indicate a different canonical package name than `pxfquery`
  - Any required T-007 artifact (A-001, A-002, A-003) cannot be read
  - pyproject.toml cannot be built

## Objective Restatement

Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence. Anchor package name `pxfquery` and module boundaries (`core`, `data`, `query`, `index`, `llm`, `viz`, `cli`) in T-007 development state report. Do not migrate legacy implementation code and do not implement query behavior beyond import-safe stubs. This skeleton is the bottom-layer asset that later tasks will populate with actual loader, query, CLI, and resolver logic.

## Selected Inputs

| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 (T-007/D-002) | .../T-007/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Anchors canonical package name (pxfquery), intended module boundaries (core/data/query/index/llm/viz), and component architecture | ok |
| A-002 (T-007/D-003) | .../T-007/4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Confirms per-module status: which are implemented vs incomplete/historical, guiding stub decisions | ok |
| A-003 (T-007/D-006) | .../T-007/4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Provides D001 package setup scope, acceptance criteria, and explicit do-not-do rules | ok |

## Execution Strategy

1. **Read T-007 artifacts (A-001, A-002)** to confirm canonical package name is `pxfquery` and module boundaries are `core`, `data`, `query`, `index`, `llm`, `viz`. Cross-check against A-003 handoff constraints. Stop if package name differs.
2. **Create `pyproject.toml`** at the task working directory with `[build-system]` (hatchling or setuptools), `[project]` (`name = "pxfquery"`, version `0.1.0`, Python `>=3.10`), and `src`-layout package discovery. No runtime dependencies.
3. **Create `src/pxfquery/` directory tree** with `__init__.py` (set `__version__ = "0.1.0"`), import-safe stub modules for `core.py` (class `PxFquery`), `data/loader.py` (class `DataLoader`), `query/forward.py` and `query/reverse.py`, `index/` subpackage, `llm/prompts.py`, `viz/plots.py`, and `cli/__init__.py`. All stubs must have empty method bodies and no external imports.
4. **Run import smoke test** using the pxfquery conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "import pxfquery; print(pxfquery.__version__)"` from the package root. Also verify `from pxfquery import PxFquery`.
5. **Record import smoke evidence** as a text file in `4_artifact/2_import_smoke/` with the command used, stdout, and exit code.
6. **Register deliverables** in `4_artifact/registry.yaml` with asset IDs, paths, types, and status.

## Conservative Execution Advice

- Start with: Read A-001 to confirm package name, then create only `pyproject.toml` and `src/pxfquery/__init__.py` first. Run the most minimal import test before creating all stub files.
- Smoke/demo command or method: `python -c "import pxfquery; print(pxfquery.__version__)"` — this validates the package can be found and the version string works before any subpackage imports.
- Full run only after: the minimal import succeeds, then create remaining stubs one subpackage at a time, testing after each.
- Cost/time risk: Negligible — no network calls, no large data reads, no legacy code migration. Expected runtime < 2 minutes.
- Checkpoint advice: After `pyproject.toml` creation, after first successful `import pxfquery`, after full skeleton import test. Save import smoke evidence immediately.

## Expected Deliverables

| Deliverable | Target path | Acceptance signal |
|---|---|---|
| pyproject.toml | task working directory/pyproject.toml | File exists with `name = "pxfquery"`, `requires-python = ">=3.10"`, `[build-system]` table, src-layout package discovery |
| Package skeleton | src/pxfquery/ with all subpackage `__init__.py` and stub modules | `import pxfquery` succeeds; `from pxfquery import PxFquery` succeeds; all subpackage imports succeed (even if stubs are empty) |
| Import smoke evidence | 4_artifact/2_import_smoke/ | File contains the import command output showing version string and successful import |
| Execution script/log | 3_execution/ | Script used to create and test the skeleton |
| Updated registry | 4_artifact/registry.yaml | All deliverables registered with correct paths |
| Completion report | 5_report/completion.md | Documents what was created, what was tested, and any deviations |

## Failure / Stop Conditions

- If A-001/A-002 indicate a canonical package name other than `pxfquery` → stop, request human clarification
- If any required T-007 artifact is unreadable → stop, report missing precondition
- If `pyproject.toml` build fails or `import pxfquery` fails → stop, diagnose and report
- If the pxfquery conda environment is not usable → stop, report environment issue
- Do NOT proceed if any legacy implementation code needs to be read — the task's scope is stubs only

## Notes For Delivery QA

- The T-007 handoff (A-003) recommends D001 "Copy or promote code/pxfquery_package/ into the development phase workspace," but T-044 intentionally scopes narrower: skeleton and stubs only. This is correct per the task's constraint notes. The broader D001 scope belongs to a later task.
- Protocol step 4 says `python -c "import pxfquery; print(pxfquery.__version__)"` — the `__init__.py` must define `__version__` for this to work. If using a different version access pattern, adjust the smoke command accordingly.
- Use the pxfquery conda environment specified in project protocol (`/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`).
- `3_execution/` is currently empty — expected for a pre-execution state. Execution AI should populate it with build scripts and logs.
- The module status matrix (A-002) confirms `cli` is not listed as an existing module but the protocol adds it as a placeholder — this is correct since it's a new skeleton subpackage for future CLI entry points.