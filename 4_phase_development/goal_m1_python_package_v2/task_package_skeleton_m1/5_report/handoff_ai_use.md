# AI Handoff: T-044 package_skeleton_m1

## Task Goal
Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence.

## What Was Delivered
- `pyproject.toml` with name=pxfquery, version=0.1.0, hatchling build, Python>=3.10, src-layout
- `src/pxfquery/` package skeleton with 8 subpackages (core, data, query, index, llm, viz, cli) and import-safe stubs
- Import smoke test results — all imports pass
- Execution script, HTML execution report, HTML result report

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_package/pyproject.toml` | Build configuration anchoring package name & version | Copy to task root or reference as canonical package metadata |
| D-002 | `4_artifact/1_package/pxfquery/` | Package skeleton with all stub modules | Copy into new task's working directory; populate stubs with implementation |
| D-003 | `4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Evidence that the skeleton is import-safe | Run same tests after modifying skeleton to verify no regressions |

## Supporting Artifacts
| ID | Path | Type | Stars |
|---|---|---|---|
| D-004 | `3_execution/create_skeleton.sh` | script | 2 |
| D-005 | `4_artifact/3_document/execution_report_v20260624.html` | report | 3 |
| D-006 | `4_artifact/3_document/result_report_v20260624.html` | report | 3 |

## Downstream Use
The skeleton is the bottom-layer asset for all later M1 development tasks. Downstream tasks should:
- Copy `4_artifact/1_package/pyproject.toml` and `4_artifact/1_package/pxfquery/` into their working directory
- Extend stubs with actual loader, query, index, LLM, viz, and CLI logic
- Do NOT modify the skeleton's package name (`pxfquery`) or src-layout

## Known Limits / Risks
- No runtime dependencies are declared yet (numpy, pandas, anndata, etc. will be needed by later tasks)
- Stubs have empty method bodies — they are not functional
- `pyproject.toml` references `README_TASK.md` which does not exist at the project root (only relevant for `pip install -e .` outside the task directory)

## Do Not Read / Do Not Reuse
- Legacy implementation code under `2_project_asset/` or legacy source root — intentionally excluded from skeleton scope
- `main.py` — identified as historical/incomplete by T-007

## Recommended Next Reads
1. `4_artifact/1_package/pyproject.toml` — canonical package metadata
2. `4_artifact/1_package/pxfquery/__init__.py` — version and top-level exports
3. `4_artifact/2_import_smoke/smoke_test_v20260624.txt` — import test patterns to replicate