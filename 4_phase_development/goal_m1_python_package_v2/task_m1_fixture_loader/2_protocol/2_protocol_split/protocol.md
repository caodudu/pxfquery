# T-046 m1_fixture_loader — Protocol

## Objective
Implement the low-risk M1 fixture loader using T-043 as the hard source for the manifest, fixture package, expected shapes, keys, columns, and index semantics. Deliver reusable loader code plus smoke evidence showing that the M1 fixture can be loaded through stable matrix/index access APIs.

## Position In Project
This task is the small development bridge between the T-043 data substrate and downstream M1 query/demo tasks. T-048 and T-049 must be able to use the loader API without creating private fixture parsing or bypassing the T-043 fixture contract. This task is not responsible for production resource hardening, biological ranking validation, or full-resource loading.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml` | Hard source for M1 manifest schema and fixture/full-resource path discovery. |
| A-002 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/` | Deterministic fixture package that the loader must load. |
| A-003 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Acceptance reference for expected fixture shapes, keys, columns, validation rules, and index semantics. |

## Execution Steps
1. Inspect the registered T-043 manifest, fixture package, and expected-shapes table only as needed to implement the loader.
2. Locate the current Python package/module layout and add a minimal reusable M1 fixture loader in the existing code style.
3. Expose a stable loader API that reads the T-043 manifest/fixture contract and returns documented matrix/index access objects or mappings suitable for downstream T-048/T-049 use.
4. Keep validation limited to fixture existence, supported file formats, required keys/columns, expected shapes, and stable index/matrix access. Do not add full production resource hardening.
5. Create a small smoke script or test in `3_execution/` that loads the registered fixture through the public loader API and records observed shapes, keys, columns, and example index access.
6. Move accepted reusable outputs and evidence into `4_artifact/`, update `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints
- Use T-043 artifacts as the hard source for manifest and fixture behavior; do not invent alternative schemas.
- Keep the loader deliberately small, deterministic, and reliable.
- The API must be stable enough for T-048 and T-049 to call directly.
- Document the API surface and expected fixture contract in a reusable artifact or report.
- Use the project Python runtime unless the execution stage documents a concrete reason to do otherwise.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.

## Forbidden
- Do not read or use project-level raw assets under `2_project_asset/`.
- Do not scan unrelated tasks or legacy source roots.
- Do not use T024-T040 outputs as authority for the M1 route.
- Do not create private query logic, ranking logic, or biological interpretation.
- Do not claim the fixture validates full-resource coverage or biological ranking quality.
- Do not call downstream CyHex prompt endpoints.

## Web Search Allowance
Allowed: no
Reason: The task is fully scoped by project protocol, current task metadata, and selected T-043 predecessor artifacts. No current external evidence is needed.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Reusable M1 fixture loader code | Existing package/module path chosen by execution after inspecting code layout | Yes |
| Loader API documentation or concise usage note | `4_artifact/2_persist/` or `4_artifact/3_document/` | Yes |
| Loader smoke evidence with observed shapes/keys/index access | `4_artifact/5_table/` and/or `4_artifact/3_document/` | Yes |
| Execution logs or temporary smoke scripts | `3_execution/` | Yes |
| Artifact registry update | `4_artifact/registry.yaml` | Yes |
| Completion report | `5_report/completion.md` | Yes |

## Acceptance Criteria
- The loader reads the T-043 manifest and fixture package rather than hardcoding unrelated paths or schemas.
- The public API can load the fixture and expose stable matrix/index access needed by downstream query tasks.
- Smoke evidence records successful loading plus observed shapes, key names, columns, and at least one stable index/matrix access example.
- Observed fixture structure is checked against T-043 expected shapes/keys/columns.
- Scope remains limited to fixture loading and smoke evidence.
- Reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules
- Stop if the registered T-043 manifest, fixture package, or expected-shapes table is missing or internally inconsistent.
- Stop if implementation would require reading `2_project_asset/` raw assets or direct legacy roots.
- Stop if the current package layout cannot be identified without scanning outside the project/task boundary; report the blocker.
- Stop if the loader cannot follow the T-043 fixture contract without inventing a schema.

## Delivery Requirements
- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
