# T-052 package_assembly_m1 — Protocol

## Objective

Assemble the runnable M1 package surface from predecessor deliverables T-044 (package skeleton), T-059 (forward query core repair), and T-060 (reverse query core repair). Deliver an installable `pxfquery` package under `src/pxfquery/`, import evidence, CLI command wiring with forward/reverse/info subcommands, and demo command output for forward and reverse queries. Wiring and integration only — do not reimplement query logic or replace validation evidence from T-050/T-051.

## Position In Project

Bottom-layer M1 package assembly. Consumes T-044 skeleton structure and CLI wiring, T-059 forward+reverse query implementations, and T-060 reverse repair fixture. The assembled package becomes the single installable surface consumed by downstream M1 validation and demo tasks.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-044/D-001 | `4_artifact/1_package/pyproject.toml` | Base build config (name=pxfquery, hatchling, src-layout) |
| A-015 | T-059/D-001 | `4_artifact/1_package/pyproject.toml` | pyproject.toml with `[project.scripts]` entry |
| A-002 | T-044/D-002 | `pxfquery/cli/__init__.py` | CLI wiring with forward+reverse+info subcommands |
| A-003 | T-044/D-002 | `pxfquery/cli/__main__.py` | `python -m pxfquery` entry |
| A-004 | T-059/D-001 | `src/pxfquery/query/forward.py` | Forward query implementation |
| A-005 | T-059/D-001 | `src/pxfquery/query/reverse.py` | Reverse query implementation |
| A-010 | T-059/D-001 | `src/pxfquery/core.py` | Reference PxFquery class (func2pert needs rewiring) |
| A-006 | T-059/D-001 | `src/pxfquery/data/` | M1FixtureLoader + base loader |
| A-011 | T-059/D-003 | `forward_repair_fixture_m1_1/` | Forward demo fixture (EGFR/A549/xpr) |
| A-012 | T-059/D-002 | `forward_repair_manifest_m1_1.yaml` | Forward repair manifest |
| A-013 | T-060/D-002 | `reverse_repair_fixture_m1_1/` | Reverse demo fixture (HALLMARK_MYC_TARGETS_V1) |
| A-014 | T-060/D-003 | `reverse_repair_manifest_m1_1.yaml` | Reverse repair manifest |

## Execution Steps

1. **Create task-local package directory** at `4_artifact/1_package/` with `src/pxfquery/` layout.
2. **Establish pyproject.toml** — use T-059 version (A-015) with `[project.scripts]` entry; preserve name, version, build config from T-044 (A-001).
3. **Assemble module tree** — copy from T-059 forward package (A-004, A-005, A-006, A-007, A-008, A-009) into `src/pxfquery/`:
   - `query/forward.py` — forward query logic
   - `query/reverse.py` — reverse query logic
   - `data/` — loader modules
   - `index/` — index modules
   - `llm/` — prompt module
   - `viz/` — viz module
4. **Wire core.py** — create `src/pxfquery/core.py` with `PxFquery` class:
   - `pert2func()` delegates to `query/forward.forward_query()`
   - `func2pert()` delegates to `query/reverse.reverse_query()`
   - `load_data()`, `load_fixture()`, `query()` methods from T-059 pattern
   - This is wiring only — each query function already exists in the imported modules.
5. **Wire `__init__.py`** — export `PxFquery` class and `__version__`.
6. **Wire CLI** — copy T-044 `cli/__init__.py` (A-002) and `cli/__main__.py` (A-003); verify forward, reverse, info subcommands all resolve.
7. **Install package** — `pip install -e .` from the task working directory.
8. **Run import smoke** — verify `import pxfquery`, `from pxfquery.core import PxFquery`, `pxfquery --help`, `pxfquery info` all work.
9. **Run forward demo** — use T-059 repair fixture (A-011, A-012):
   ```
   pxfquery forward --perturbation EGFR --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
   ```
   Capture JSON output as evidence.
10. **Run reverse demo** — use T-060 repair fixture (A-013, A-014):
    ```
    pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
    ```
    Capture JSON output as evidence.
11. **Collect evidence** — save import smoke evidence, forward demo JSON, reverse demo JSON, and CLI help text under `4_artifact/`.
12. **Register artifacts** — update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not reimplement forward or reverse query logic. All query functions already exist in predecessor modules; only wire them in `core.py`.
- Do not replace, re-validate, or modify validation evidence from T-050/T-051.
- Do not use T024-T040 blocked assets.
- Do not use T-048/T-049 failed predecessor outputs. Use T-059/T-060 replacement outputs only.
- Do not read project-level raw assets under `2_project_asset/`.
- T-060/D-001 (package code) is a symlink to T-044 and is not accepted as standalone reverse implementation. Use T-059 `query/reverse.py` (A-005) as the authoritative reverse query source.
- Preserve `synthetic_repair` provenance labels when using T-059/T-060 fixtures.
- Do not modify predecessor task artifacts.

## Forbidden

- Reimplementing `forward_query()`, `reverse_query()`, or any query logic
- Reading or referencing T-048/T-049 artifacts
- Reading T024-T040 blocked assets
- Reading `2_project_asset/`
- Modifying predecessor task outputs
- Stripping `synthetic_repair` provenance from fixture usage

## Web Search Allowance

Allowed: no
Reason: All required inputs are available from selected predecessor tasks. No external/current information is needed for package assembly.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Assembled package source | `4_artifact/1_package/` | yes |
| Import smoke evidence | `4_artifact/2_import_smoke/smoke_test_v20260624.txt` | yes |
| Forward demo JSON | `4_artifact/2_persist/forward_demo_v20260624.json` | yes |
| Reverse demo JSON | `4_artifact/2_persist/reverse_demo_v20260624.json` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| CLI help text | `4_artifact/2_persist/cli_help_v20260624.txt` | optional |

## Acceptance Criteria

- `pip install -e .` succeeds in the task working directory.
- `python -c "import pxfquery; print(pxfquery.__version__)"` returns `0.1.0`.
- `pxfquery info` returns valid JSON with package name and version.
- `pxfquery forward --help` and `pxfquery reverse --help` show subcommand options.
- Forward demo with T-059 fixture returns `found: true` for EGFR/A549/xpr.
- Reverse demo with T-060 fixture returns `found: true` for HALLMARK_MYC_TARGETS_V1 + A549.
- All output JSON is well-formed and structured per T-042 contract shape.
- No query logic was reimplemented — verify all query functions come from predecessor modules via import.

## Failure / Stop Rules

- If T-059/T-060 fixture h5ad files are incompatible with `M1FixtureLoader` or `anndata`, stop and report asset loading gap. Do not re-create fixtures.
- If T-060 fixture manifest path references non-existent files, stop and report.
- If `pyproject.toml` dependencies (e.g., `numpy`, `anndata`) are missing in the conda environment, install missing packages and record the additions. If core query logic would require rewriting because of interface mismatch, stop and report.
- If `func2pert` wiring in `core.py` reveals a missing interface in `query/reverse.py`, stop and report the integration gap; do not modify `query/reverse.py`.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
