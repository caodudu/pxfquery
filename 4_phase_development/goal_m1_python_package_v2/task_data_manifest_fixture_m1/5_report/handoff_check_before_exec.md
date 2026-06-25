# Check Handoff Before Exec: T-043 data_manifest_fixture_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories, `1_project_init/`, unrelated task outputs, failed T024-T040 outputs, and future-stage prompts under `2_protocol/0_prompt/`
- Required registry: `1_asset/registration.yaml`, with all six required assets preflighted as ready symlinks
- Must stop if: a required registered asset is unreadable or inconsistent, fixture records cannot be traced to A-001, downstream-ready examples require raw project assets or failed T024-T040 outputs, or execution would need to invent biological records, schema fields, identifiers, paths, or scores

## Objective Restatement
Prepare the stable M1 data substrate for later package development by producing a small, traceable resource manifest and fixture package derived only from registered T-014 and T-021 predecessor assets. The result should give downstream loader, forward-query, and reverse-query tasks enough concrete paths, schemas, shapes, columns, keys, and sample records to run demos without rediscovering broad legacy context.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t021_standard_resources_bundle` | Canonical standard resource bundle for concrete resource files, schemas, shapes, keys, columns, and real fixture records | ok |
| A-002 | `1_asset/t021_standard_resource_guide.md` | Authoritative guide for standard resource format decisions and expected usage | ok |
| A-003 | `1_asset/t021_process_records` | Validation and profiling records for cross-checking resource bundle boundaries | ok |
| A-004 | `1_asset/t014_precomputed_data_scope.md` | Precomputed-data scope and boundary authority for deciding the M1 substrate | ok |
| A-005 | `1_asset/t014_data_resource_inventory.csv` | Resource inventory for aligning manifest entries with predecessor interpretation | ok |
| A-006 | `1_asset/t014_matrix_schema_coverage.csv` | Matrix schema and coverage summary for expected shape and column/function checks | ok |

## Execution Strategy
1. Start with a narrow read of A-002, A-004, A-005, and A-006 to identify the resource categories, schema expectations, and matrix/index boundaries already approved by T-014/T-021; write only notes or scripts under `3_execution/`.
2. Inspect only the relevant files inside A-001 needed for the M1 loader, forward-query, and reverse-query substrate; do not scan unrelated project assets or predecessor directories outside the registered symlink.
3. Cross-check selected A-001 resources against A-003 process records and T-014 tables, then draft the manifest schema with stable resource IDs, relative bundle paths, file types, loader roles, keys, expected shapes, validation rules, and provenance.
4. Build a deterministic fixture package under `4_artifact/2_persist/fixture_package_m1/` from real A-001 records only, keeping enough linked rows/columns for loader smoke tests and one forward/reverse demo path.
5. Generate `expected_shapes_keys_columns_m1.csv` with one row per selected resource, including shape, key fields, required columns, index semantics, validation rule, and source/provenance.
6. Generate `sample_records_m1.csv` documenting exact source resource, row/key identifiers, selected fields, inclusion reason, and traceability back to source records.
7. Write `data_manifest_fixture_m1_readme.md`, `resource_manifest_m1.yaml`, and concise HTML execution/result reports explaining what is included, what is excluded from the full T-021 bundle, and how downstream tasks should consume the outputs.
8. Register all accepted outputs in `4_artifact/registry.yaml`; keep temporary scripts, logs, and validation snippets in `3_execution/`, not as final reusable outputs.

## Conservative Execution Advice
- Start with: a tiny schema/path survey of the six registered assets, especially A-002/A-004 for boundaries and A-005/A-006 for expected resource classes.
- Smoke/demo command or method: run a small local Python validation script from `3_execution/` using `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` to load only the chosen fixture files and verify declared shapes, keys, required columns, and sample IDs.
- Full run only after: the selected resources are traceable to A-001 and their inclusion is consistent with A-002/A-004/A-005/A-006 and, where applicable, A-003 validation records.
- Cost/time risk: expected cost is local file I/O only; no web, no downloads, no broad raw-asset scan, and no expensive recomputation should be needed.
- Checkpoint advice: before writing final artifacts, keep a `3_execution/` draft list of selected source files and sample identifiers; stop if the list cannot support both forward and reverse demo paths without synthetic data.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| M1 resource manifest | `4_artifact/2_persist/resource_manifest_m1.yaml` | YAML contains stable resource IDs, relative paths, file types, loader roles, required keys/columns, expected shapes, validation rules, and T-014/T-021 provenance |
| Minimal fixture package | `4_artifact/2_persist/fixture_package_m1/` | Small deterministic files copied/derived from real A-001 records, sufficient for loader smoke tests and one forward/reverse demo path |
| Expected shapes/keys/columns table | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | CSV lists selected resources with shape, keys, columns, index semantics, validation rule, and provenance |
| Sample records table | `4_artifact/5_table/sample_records_m1.csv` | CSV traces each sample/example record to exact source resource and identifiers with inclusion reason |
| Usage/readme document | `4_artifact/2_persist/data_manifest_fixture_m1_readme.md` | Markdown explains downstream use, fixture contents, known exclusions, and boundary rules |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | HTML summarizes method, inputs inspected, validation steps, and any limitations |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | HTML summarizes final outputs, acceptance checks, and downstream handoff notes |
| Artifact registry update | `4_artifact/registry.yaml` | Registry records all accepted outputs with paths, types, provenance, and status |

## Failure / Stop Conditions
- Stop if any registered required asset is missing, empty, unreadable, or materially inconsistent with the registry/preflight summary.
- Stop if the selected fixture cannot be built from real A-001 records with explicit provenance.
- Stop if a loader/forward/reverse demo path would require invented data, placeholder biological records, or unverifiable keys/scores.
- Stop if needed inputs appear to exist only under `2_project_asset/` or failed T024-T040 outputs.
- Stop if execution requires web search, external downloads, unrelated predecessor browsing, or modifying predecessor/project-protocol directories.
- Stop before expensive conversion or broad file scanning if a small sample survey cannot identify the minimal resources needed.

## Notes For Delivery QA
- Confirm final reusable outputs are in `4_artifact/`, not only in `3_execution/`.
- Confirm the fixture package is small and deterministic, with no synthetic biological content that could be mistaken for real data.
- Confirm all paths in the manifest are stable relative paths suitable for downstream package tasks.
- Confirm reports disclose exclusions from the full T-021 standard resource bundle and explain why the selected subset is enough for M1 demos.
- Confirm no downstream prompt generation endpoint was called during checking.
