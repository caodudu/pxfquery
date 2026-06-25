# Check Handoff Before Exec: T-047 resource_loader_hardening_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories, legacy source root
- Required registry: `1_asset/registration.yaml` (A-001 through A-008)
- Must stop if: full resource loading would mutate authoritative indexes/standard resources; missing `t021_standard_resources_bundle/` dir prevents smoke verification path

## Objective Restatement
Harden M1 Python-package resource loader against real full matrix/index resources and the fixture package. Deliver enhanced loader code (real-path loading, schema-aware unwrap, field normalization), smoke results for both paths, and a structured gap list. This is a reusable enhancement asset — do not block if real resources are incomplete; fall back to fixture path and report gaps.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/resource_manifest_m1.yaml` | Entry point for all M1 resource paths, loader roles, expected shapes, validation rules | ok |
| A-002 | `1_asset/expected_shapes_keys_columns_m1.csv` | Acceptance evidence for expected shapes, keys, columns, index semantics | ok |
| A-003 | `1_asset/sample_records_m1.csv` | Traceable sample rows and keys for smoke verification | ok |
| A-004 | `1_asset/index_health_summary.json` | Per-index schema status, key completeness, known gaps, patch recommendations | ok |
| A-005 | `1_asset/index_health_report.md` | Human-readable index health overview with pass/warn/block verdicts | ok |
| A-006 | `1_asset/gap_notes.md` | Detailed gap severity, demo impact, and resolution paths for loader decisions | ok |
| A-007 | `1_asset/fixture_package_m1/` | Compact real-data fixture bundle for deterministic loader smoke/demo runs | ok |
| A-008 | `1_asset/data_manifest_fixture_m1_readme.md` | Downstream usage notes and known exclusions | ok |

## Execution Strategy
1. **Load manifest & health summary** — Parse A-001 and A-004; cross-reference resource types, expected shapes, known gaps. Establish fixture vs full-resource split.
2. **Implement/enhance loader functions** — Write `loader_hardening_m1.py` with per-type handlers:
   - h5ad: anndata read, validate obs columns, var_names, shape
   - CSV: pandas read, validate key columns, row count
   - JSON: parse, validate top-level schema, unwrap non-standard structures (function_index dict, cellline_index wrapper)
   - Field normalization: `symbol`→`gene_symbol`, category derivation from `source`
3. **Smoke test with fixture package** — Load all 18 fixture files, verify shapes/keys against A-002 manifest expectations.
4. **Attempt full resource loading** — Try loading full standard resources from `1_asset/t021_standard_resources_bundle/`. Record success/failure per resource.
5. **Aggregate gap list** — Collect all gaps (missing paths, schema mismatches, load failures) into structured list with severity and fixture coverage.
6. **Produce smoke results JSON** — Machine-readable per-resource load status, shape validation, normalizations applied, gap list.
7. **Produce smoke report MD** — Human-readable summary with markdown tables, gap assessment, recommendation for M1 fixture vs full path.
8. **Register artifacts & write completion** — Update `4_artifact/registry.yaml`, write `5_report/completion.md`.

## Conservative Execution Advice
- Start with: fixture-only smoke test (Step 3) — fastest feedback loop, no dependency on full bundle
- Smoke/demo command: `conda run -n pxfquery python 3_execution/0_smoke_fixtures.py` (to be created)
- Full run only after: fixture smoke passes and full bundle directory is confirmed non-empty
- Cost/time risk: Full h5ad matrices (cp: 201k obs, sh: 189k obs, xpr: 132k obs) may take ~30s each to load; JSON indexes (gene_index 6.4MB, gene_neighbors 22MB) may take memory/IO. Fixture loads are negligible (< 1MB total).
- Checkpoint advice: After fixture smoke passes, record intermediate results before attempting full-resource loads. If full bundle directory missing → skip to gap list, do not fabricate results.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Enhanced loader code | `4_artifact/1_code/loader_hardening_m1.py` | Loads all 18 fixture files, handles function_index unwrap, normalizes gene_index fields |
| Smoke results JSON | `4_artifact/2_persist/loader_smoke_results_m1.json` | Per-resource load status, shape validation, normalizations, gap list |
| Smoke report MD | `4_artifact/3_document/loader_smoke_report_m1.md` | Markdown tables with results, clear gap assessment, M1 readiness verdict |
| Gap list MD | `4_artifact/3_document/loader_gap_list_m1.md` | Resource ID, path, issue, severity, fixture coverage, recommended action |
| Execution report | `4_artifact/3_document/execution_report_v*.html` | Traceable execution log with commands, outputs, timestamps |
| Result report | `4_artifact/3_document/result_report_v*.html` | Formatted result summary with tables, gap classification, recommendations |

## Failure / Stop Conditions
- `t021_standard_resources_bundle/` missing or empty: skip full-resource loading, produce gap notice, complete via fixture path
- Fixture files corrupted/unreadable: stop and file block report — fixture integrity is prerequisite to any loader hardening
- Authentication/conda environment issues: fix environment first; if unresolved, document as environment blocker
- Any mutation of authoritative indexes: immediately stop and do not write modified files back to bundle

## Notes For Delivery QA
- Verify A-002 expected shapes CSV was used as ground truth, not guessed
- Verify loader code handles both fixture and full paths via configurable root
- Verify gap list distinguishes "not attempted" from "attempted and failed"
- Verify field normalization is explicit (logged/documented) not silent
- Do not commit modified indexes or bundle resources back to the repository
