# T-047 resource_loader_hardening_m1 — Protocol

## Objective

Harden the M1 Python-package resource loader against real full matrix/index resources and the fixture package, using T-043 manifest/fixture definitions and T-045 index health findings. Deliver enhanced loader behavior (real-path loading, schema-aware unwrap, field normalization), smoke results against both full resources and fixtures, and a clear gap/block list for anything that cannot be safely hardened. This is a reusable enhancement asset and must not block the M1 fixture-only path if real resources are incomplete.

## Position In Project

- G-005 `goal_m1_python_package_v2` — development phase, enhancement/reuse asset
- Hard inputs: T-043 data manifest & fixture package, T-045 index health check
- T-041 legacy source digest is not delivered — exclude from configuration; execution may not use it
- T-047 is NOT an M1 blocker — if real resources are incomplete, report gaps and continue with fixture-based path

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-043/D-001 | 4_artifact/2_persist/resource_manifest_m1.yaml | Entry point for full standard resource paths (h5ad, csv, json) and fixture resource paths; defines loader role, required keys/columns, expected shapes, validation rules |
| A-002 | T-043/D-003 | 4_artifact/5_table/expected_shapes_keys_columns_m1.csv | Acceptance evidence for expected shapes, keys, columns, and index semantics |
| A-003 | T-043/D-004 | 4_artifact/5_table/sample_records_m1.csv | Traceable sample rows and keys for smoke verification |
| A-004 | T-045/D-001 | 4_artifact/2_persist/index_health_summary.json | Machine-readable per-index schema status, key completeness, known gaps, patch recommendations |
| A-005 | T-045/D-002 | 4_artifact/2_persist/index_health_report.md | Human-readable index health overview with pass/warn/block per index and M1 readiness verdict |
| A-006 | T-045/D-003 | 4_artifact/3_document/gap_notes.md | Detailed gap severity, demo impact, and resolution paths |
| A-007 | T-043/D-002 | 4_artifact/2_persist/fixture_package_m1/ | Compact real-data fixture bundle for deterministic loader smoke/demo runs |
| A-008 | T-043/D-005 | 4_artifact/2_persist/data_manifest_fixture_m1_readme.md | Downstream usage notes and exclusions |

## Execution Steps

1. **Load and validate the resource manifest.** Read `resource_manifest_m1.yaml` (A-001) and confirm that all listed resource paths are resolvable and non-empty. Record any missing full-resource paths as a gap.
2. **Read index health summary.** Load `index_health_summary.json` (A-004) and extract per-index schema requirements, field mappings, known gaps, and patch recommendations. Cross-reference with `expected_shapes_keys_columns_m1.csv` (A-002).
3. **Implement or enhance the loader against real full resources.** For each resource type (h5ad matrices, csv metadata, json indexes), implement or enhance loader functions that:
   - Open real `.h5ad` matrices (cp_func_ad, sh_func_ad, xpr_func_ad) and validate obs columns, var_names, and shapes against manifest expectations.
   - Load real CSV metadata tables and validate key columns, row counts against manifest.
   - Load real JSON indexes and validate schema/top-level structure against manifest and T-045 health summary.
   - Handle the `function_index.json` non-standard dict structure (`meta/var_names/aliases`) — unwrap per T-045 handoff.
   - Normalize field names where T-045 reports discrepancies (e.g., `gene_index.json` uses `symbol` not `gene_symbol`; `cellline_tree.json` is flat with 3 keys only, not hierarchical).
4. **Run loader smoke tests with the fixture package.** Load all fixture resources from `fixture_package_m1/` (A-007) and verify:
   - Fixture matrices are readable, shapes match manifest, obs columns and var_names are present.
   - Fixture metadata CSV files match expected row counts and key columns.
   - Fixture JSON indexes are parsable and match expected top-level keys.
5. **Execute real full-resource loading where feasible.** Attempt to load full standard resources from paths defined in the manifest. For each resource:
   - If load succeeds: record shape, key presence, and any field normalizations applied.
   - If load fails or a resource is missing: document the specific gap (path, reason), assess whether fixture covers the gap, and classify as block/warn/note.
6. **Produce gap list.** Aggregate all gaps from steps 1–5 into a structured gap list with: resource ID, path, issue, severity (block/warn/info), whether fixture covers it, recommended action.
7. **Produce smoke results report.** Generate a machine-readable result summary (JSON) and a human-readable report (MD) with: per-resource load status, shape/key validation results, any field normalizations applied, gap list.
8. **Deliver artifacts.** Register all accepted outputs in `4_artifact/registry.yaml`. Write `5_report/completion.md`.

## Constraints

- This is an enhancement/reuse asset — do NOT block the M1 fixture-based path if real resources are incomplete.
- Do NOT mutate or overwrite authoritative full-resource indexes or standard resources under `t021_standard_resources_bundle/`.
- Prefer the fixture path as a deterministic fallback when real resource loading is blocked.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- T-041 legacy source digest is NOT available (still executing). Do not use it.
- Use the `pxfquery` conda environment for all Python execution: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.

## Forbidden

- Do not modify legacy source roots or authoritative index files.
- Do not read `2_project_asset/`.
- Do not depend on T-041 outputs.
- Do not block the M1 fixture-only path.

## Web Search Allowance

Allowed: no
Reason: All required inputs are provided by T-043 and T-045 predecessor handoffs. No external/current information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Loader module or enhancement script | `4_artifact/1_code/loader_hardening_m1.py` | yes |
| Machine-readable smoke result | `4_artifact/2_persist/loader_smoke_results_m1.json` | yes |
| Human-readable smoke report | `4_artifact/3_document/loader_smoke_report_m1.md` | yes |
| Gap list | `4_artifact/3_document/loader_gap_list_m1.md` | yes |
| Execution report (HTML) | `4_artifact/3_document/execution_report_v*.html` | yes |
| Result report (HTML) | `4_artifact/3_document/result_report_v*.html` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- Loader handles all resource types in the manifest: h5ad matrices, csv metadata, json indexes.
- Fixture smoke tests pass for all fixture resources.
- Real full-resource loading attempted for each resource; gaps documented with severity.
- `function_index.json` unwrap logic implemented per T-045 findings.
- Field name normalizations applied where T-045 reports discrepancies.
- Gap list is complete, honest, and actionable.
- No authoritative files mutated.

## Failure / Stop Rules

- If T-043 manifest cannot be parsed, stop and request a green_config re-run.
- If T-045 health summary cannot be read, stop and escalate.
- If the Python environment (`pxfquery` conda env) is missing required packages (anndata, pandas, etc.), install them and record in completion report rather than stopping.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.