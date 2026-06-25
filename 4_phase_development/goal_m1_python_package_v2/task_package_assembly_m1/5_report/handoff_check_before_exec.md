# Check Handoff Before Exec: T-052 package_assembly_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, T-024–T-040, T-048/T-049, predecessor task directories (read-only), `2_protocol/` (non-modifiable)
- Required registry: `4_artifact/registry.yaml` must be updated on completion
- Must stop if: fixture h5ad incompatible with M1FixtureLoader/anndata; manifest path references non-existent files; `func2pert` wiring reveals missing interface in `query/reverse.py`; missing dependencies cannot be installed

## Objective Restatement
Assemble the M1 pxfquery package from T-044 skeleton (CLI wiring) + T-059 (forward + reverse query logic, core pattern, data/index/llm/viz modules, fixtures) + T-060 (reverse fixture). Deliver an installable `src/pxfquery/` package with working `import pxfquery`, CLI with forward/reverse/info subcommands, and demo output for both query directions. Wiring/integration only — no reimplementation of query logic.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/pxfquery_pyproject_base.toml` | Base pyproject.toml (name, version, build) | ok |
| A-015 | `1_asset/forward_package_pyproject_cli.toml` | pyproject.toml with `[project.scripts]` entry | ok |
| A-002 | `1_asset/pxfquery_cli_init.py` | CLI wiring (forward/reverse/info subcommands) | ok |
| A-003 | `1_asset/pxfquery_cli_main_module.py` | `python -m pxfquery` entry | ok |
| A-004 | `1_asset/forward_query_impl.py` | Forward query implementation | ok |
| A-005 | `1_asset/reverse_query_impl.py` | Reverse query implementation | ok |
| A-010 | `1_asset/forward_package_core_module.py` | Reference PxFquery class (func2pert needs rewiring) | ok |
| A-006 | `1_asset/forward_package_data_modules` | Data loader (M1FixtureLoader) | ok |
| A-011 | `1_asset/forward_repair_fixture` | Forward demo fixture (synthetic EGFR/A549/xpr) | ok |
| A-012 | `1_asset/forward_repair_manifest.yaml` | Forward repair manifest | ok |
| A-013 | `1_asset/reverse_repair_fixture` | Reverse demo fixture (synthetic HALLMARK_MYC_TARGETS_V1/A549) | ok |
| A-014 | `1_asset/reverse_repair_manifest.yaml` | Reverse repair manifest | ok |
| A-007† | `1_asset/forward_package_index_modules` | Index modules | ok |
| A-008† | `1_asset/forward_package_llm_modules` | LLM prompt module | ok |
| A-009† | `1_asset/forward_package_viz_modules` | Visualization module | ok |

† = optional but included for completeness per protocol step 3.

## Execution Strategy
1. **Create package directory** — `4_artifact/1_package/src/pxfquery/`
2. **Establish pyproject.toml** — merge A-015 (scripts entry) with A-001 (base config); note: A-015 already has all fields, so A-001 is fallback reference
3. **Assemble module tree** — copy from T-059 via A-004–A-009 into `src/pxfquery/{query,data,index,llm,viz,__init__.py}`
4. **Wire core.py** — copy A-010 as base, then rewrite `func2pert()` to delegate to `query/reverse.reverse_query()` (import `from pxfquery.query.reverse import reverse_query`; call `reverse_query(self.matrix, ...)`)
5. **Wire CLI** — copy A-002 (T-044 `cli/__init__.py`) and A-003 (`cli/__main__.py`) into `src/pxfquery/cli/` (NOT T-059's partial CLI which lacks reverse/info)
6. **Wire `__init__.py`** — export `PxFquery` and `__version__` (already in T-059's init pattern)
7. **Install** — `pip install -e .` from task root; if missing deps (numpy, anndata, pyyaml), install them
8. **Smoke test** — `import pxfquery`; `pxfquery info`; `pxfquery --help`; `pxfquery forward --help`; `pxfquery reverse --help`
9. **Forward demo** — `pxfquery forward --perturbation EGFR --cell-line A549 --manifest 1_asset/forward_repair_manifest.yaml --fixture-root 1_asset/forward_repair_fixture`
10. **Reverse demo** — `pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --manifest 1_asset/reverse_repair_manifest.yaml --fixture-root 1_asset/reverse_repair_fixture`
11. **Collect evidence** — save smoke output, forward JSON, reverse JSON, CLI help to `4_artifact/`
12. **Register artifacts** — update `4_artifact/registry.yaml`
13. **Write reports** — execution report, result report, completion.md

## Conservative Execution Advice
- Start with: step 7–8 (pip install + smoke). If install fails, fix pyproject.toml or missing deps first.
- Smoke/demo command: `pxfquery info` (no matrix loading needed — pure CLI test)
- Full run only after: smoke passes AND `import pxfquery` works AND `pxfquery forward --help` shows correct options
- Cost/time risk: Low — all local, no API calls, no network. ~5 min execution.
- Checkpoint advice: Save `4_artifact/` progress after each evidence capture. If a demo fails, save partial logs before diagnosing.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Assembled package source | `4_artifact/1_package/` | `pip install -e .` succeeds |
| Import smoke evidence | `4_artifact/2_import_smoke/smoke_test_v20260624.txt` | `import pxfquery`; `pxfquery.info` returns valid JSON |
| Forward demo JSON | `4_artifact/2_persist/forward_demo_v20260624.json` | `found: true` with top_activated/suppressed for EGFR/A549/xpr |
| Reverse demo JSON | `4_artifact/2_persist/reverse_demo_v20260624.json` | `found: true` with top_candidates for MYC_TARGETS_V1/A549 |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | File exists with structured content |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | File exists with structured content |
| CLI help text | `4_artifact/2_persist/cli_help_v20260624.txt` | Shows forward/reverse/info subcommands |

## Failure / Stop Conditions
- T-059/T-060 fixture h5ad files incompatible with M1FixtureLoader or anndata → stop, report asset loading gap
- T-060 fixture manifest path references non-existent files → stop, report
- Missing deps (numpy, anndata, pyyaml) → install; if core logic requires rewriting → stop, report
- `func2pert` wiring reveals missing interface in `query/reverse.py` → stop, report integration gap; do not modify query/reverse.py
- `pip install -e .` fails structurally (not dep-related) → stop, report packaging gap

## Notes For Delivery QA
- T-059 `core.py`'s `func2pert()` returns NotImplemented — **this MUST be rewired** in step 4 to delegate to `query/reverse.reverse_query()`. This is the single most important wiring change.
- T-044 CLI (A-002) is the correct CLI source; T-059 has its own CLI at `src/pxfquery/cli/` but it only has `forward` subcommand (no reverse/info). Use A-002/A-003.
- The registered asset `1_asset/reverse_repair_manifest.yaml` is correctly `.yaml` (the prompt display truncation showing `.yam` was a display artifact only).
- Meta.yaml notes mention "T-048/T-049" but the constraint supplement and protocol correctly override to T-059/T-060.
- M1FixtureLoader expects well-known filenames under fixture_root: `{cp,sh,xpr}_func_fixture_m1.h5ad` + csv/json files. The manifest resource paths are metadata only.
- All demo commands use `1_asset/` symlinks — these resolve to predecessor task paths. No need to navigate to predecessor directories.
