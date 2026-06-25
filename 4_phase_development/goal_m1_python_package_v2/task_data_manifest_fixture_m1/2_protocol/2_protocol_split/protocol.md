# T-043 data_manifest_fixture_m1 — Protocol

## Objective

Prepare the stable M1 data substrate for downstream package development. The task must produce a reusable resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward-query, and reverse-query demos.

The execution must use T-014 and T-021 as the only predecessor authorities. It must confirm concrete paths and fixture contents from registered predecessor artifacts and must not invent data.

## Position In Project

This is a bottom-layer development task for `goal_m1_python_package_v2`. Its outputs define the reliable data boundary that later loader and query tasks can consume without rereading broad legacy/project raw assets.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle for concrete paths, schemas, shapes, keys, columns, and fixture records. |
| A-002 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Authoritative documentation for standard resource format decisions and expected usage. |
| A-003 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/` | Validation and profiling records for cross-checking the resource bundle. |
| A-004 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md` | Precomputed-data scope and boundaries for deciding the M1 substrate. |
| A-005 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv` | Resource inventory for aligning manifest entries with predecessor interpretation. |
| A-006 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv` | Matrix schema and coverage summary for expected shape and column/function checks. |

## Steps

1. Inspect only the registered input assets listed above, plus the current task's own writable folders.
2. Confirm the concrete standard resource paths and create `resource_manifest_m1.yaml` with stable resource IDs, relative bundle paths, file types, intended loader roles, required columns/keys, expected shapes, and provenance back to T-014/T-021.
3. Build a minimal fixture package from real records extracted from A-001. Include enough data for loader smoke tests, one forward-query demo path, and one reverse-query demo path. Keep fixture files small and deterministic.
4. Produce `expected_shapes_keys_columns_m1.csv` summarizing each selected resource's expected shape, key fields, columns, index semantics, and validation rule.
5. Produce `sample_records_m1.csv` or equivalent tabular summary showing the exact source resource, row/key identifiers, selected fields, and why each example is included.
6. Write a concise README explaining how downstream tasks should consume the manifest and fixture package, including any known exclusions from the full T-021 standard resource bundle.
7. Register all accepted outputs in `4_artifact/registry.yaml`, write completion reporting, and keep temporary scripts/logs in `3_execution/`.

## Constraints

- Use only T-014 and T-021 registered assets as authorities for input data and schema decisions.
- Do not invent rows, keys, columns, shapes, function names, drugs, genes, cell lines, or scores.
- Fixture records must be copied or derived from registered predecessor assets and must retain enough provenance to trace back to the source file and source identifier.
- Prefer small, deterministic fixtures over broad sampling.
- The fixture must be adequate for loader, forward-query, and reverse-query demonstrations, but it does not need to reproduce full query ranking performance.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not depend on T024-T040 outputs.
- Do not modify predecessor task directories or project protocol/state.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading unrelated task directories or outputs outside registered T-014/T-021 assets.
- Using outputs from failed T024-T040 tasks.
- Creating synthetic biological records or placeholder data that could be mistaken for real resources.
- Running external web search or downloading external data.

## Web Search Allowance

Allowed: no

Reason: The task is an internal data-substrate configuration and fixture task. The selected predecessor artifacts provide the needed authorities, and current/external information is not required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| M1 resource manifest | `4_artifact/2_persist/resource_manifest_m1.yaml` | Yes |
| Minimal fixture package | `4_artifact/2_persist/fixture_package_m1/` | Yes |
| Expected shapes/keys/columns table | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Yes |
| Sample records table | `4_artifact/5_table/sample_records_m1.csv` | Yes |
| Usage/readme document | `4_artifact/2_persist/data_manifest_fixture_m1_readme.md` | Yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Yes |
| Updated artifact registry | `4_artifact/registry.yaml` | Yes |
| Completion report | `5_report/completion.md` | Yes |

## Acceptance Criteria

- Manifest entries point to concrete, existing resources from the registered T-021 standard resource bundle or to fixture files generated in this task.
- Each manifest entry includes resource type, loader role, required keys/columns, expected shape or record count rule, provenance, and validation notes.
- Fixture files are small, deterministic, and contain only real data copied or boundedly extracted from registered assets.
- Expected shapes/keys/columns are explicitly documented for matrices, indexes, metadata tables, and fixture files used by loader/forward/reverse demos.
- Sample records are traceable to their source resource and include enough examples for downstream smoke tests.
- Outputs do not require project-level raw asset reads and do not reference T024-T040.

## Failure / Stop Rules

- Stop if registered predecessor assets are missing, unreadable, or insufficient to create real fixtures without guessing.
- Stop if execution appears to require `/2_project_asset/` or direct legacy source reads.
- Stop if no coherent minimal forward/reverse demo fixture can be extracted from registered resources.
- Stop if validation contradicts T-014/T-021 authority records in a way that changes the intended resource boundary.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
