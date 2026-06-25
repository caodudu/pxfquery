# Check Handoff Before Exec: T-046 m1_fixture_loader

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/`, legacy source roots, unrelated task folders, downstream prompt endpoints
- Required registry: `1_asset/registration.yaml` with A-001 manifest, A-002 fixture package, and A-003 expected-shapes table; asset preflight reports all three as `ok`
- Must stop if: selected T-043 assets are missing or internally inconsistent, loader work requires raw `2_project_asset/` access or direct legacy-root reads, package layout cannot be identified within current project/task boundaries, or the T-043 fixture contract cannot be followed without inventing a schema

## Objective Restatement
Implement a deliberately small M1 fixture loader that uses the registered T-043 manifest and fixture package as the hard contract, exposes stable matrix/index access for downstream T-048/T-049, and proves that access with smoke evidence. The execution must avoid production resource hardening, private query/ranking logic, biological interpretation, raw asset reads, and any schema not grounded in T-043.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/resource_manifest_m1.yaml` | Hard source for M1 manifest schema and fixture/full-resource path discovery. | ok |
| A-002 | `1_asset/fixture_package_m1/` | Deterministic fixture package that the loader must load. | ok |
| A-003 | `1_asset/expected_shapes_keys_columns_m1.csv` | Acceptance reference for expected shapes, keys, columns, validation rules, and index semantics. | ok |

## Execution Strategy
1. Inspect only the registered task assets and the current package layout needed to place the loader; expected output is a short implementation target decision recorded in `3_execution/` notes or smoke logs.
2. Read A-001 and A-003 to identify the fixture contract: resource keys, relative paths, formats, required columns, expected shapes, and index semantics; expected output is a minimal contract summary used by implementation.
3. Add a compact public loader API in the existing Python package style that accepts a manifest path or fixture root and returns documented matrix/index access objects or mappings; expected output is reusable package code, not a task-local private parser.
4. Keep validation narrow: file existence, supported fixture file formats, required keys/columns, expected shapes, and stable matrix/index lookup; expected output is clear fixture-contract errors without full production hardening.
5. Create a smoke script or focused test under `3_execution/` that loads A-001/A-002 through the public loader API and compares observed structure against A-003; expected output is reproducible smoke evidence.
6. Run the smoke method in the project conda environment with `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`; expected output is successful loader execution or a precise stop reason.
7. Promote accepted documentation/evidence into `4_artifact/2_persist/`, `4_artifact/3_document/`, and/or `4_artifact/5_table/`, then update `4_artifact/registry.yaml`; expected output is no reusable result left only in `3_execution/`.
8. Write `5_report/completion.md` with API surface, smoke result, artifact list, scope limits, and any packages installed; expected output is a concise task completion record.

## Conservative Execution Advice
- Start with: a read-only smoke inspection of A-001 and A-003 plus a package-layout check before editing code.
- Smoke/demo command or method: run a small `3_execution/` Python smoke script through `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` that imports the public loader, loads `1_asset/resource_manifest_m1.yaml`, resolves `1_asset/fixture_package_m1/`, and emits observed keys/shapes/columns/index examples.
- Full run only after: the loader API can load the fixture without hardcoded predecessor paths beyond the registered task assets, and observed shapes/columns match A-003.
- Cost/time risk: low; this should be local file I/O and small fixture loading only. No web search, API calls, raw asset scans, full-resource loads, or biological ranking runs are expected.
- Checkpoint advice: after placing the loader API, run the smoke script before writing final artifacts; if validation fails, preserve the failure output in `3_execution/` and stop rather than widening scope.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reusable M1 fixture loader code | Existing package/module path selected after package-layout inspection | Public API loads the registered T-043 fixture and exposes stable matrix/index access without private downstream parsing. |
| Loader API documentation or usage note | `4_artifact/2_persist/` or `4_artifact/3_document/` | Documents function/class entry point, required manifest/fixture inputs, returned objects/mappings, and scope limits. |
| Loader smoke script/logs | `3_execution/` | Reproducible command and output show successful fixture loading through the public API. |
| Smoke evidence table/document | `4_artifact/5_table/` and/or `4_artifact/3_document/` | Records observed keys, shapes, columns, and at least one stable index/matrix access example checked against A-003. |
| Artifact registry update | `4_artifact/registry.yaml` | Registers accepted reusable code-reference documentation and smoke evidence artifacts. |
| Completion report | `5_report/completion.md` | Summarizes implementation, validation, artifacts, stop-rule compliance, and any environment changes. |

## Failure / Stop Conditions
- Stop if A-001, A-002, or A-003 is missing, unreadable, empty, or internally contradictory during content inspection.
- Stop if satisfying the loader contract requires reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/` or direct legacy roots.
- Stop if the package layout cannot be identified from the current project/task boundary.
- Stop if fixture files require unsupported formats or dependencies that cannot be justified for this small loader.
- Stop if the loader would need to invent query, ranking, interpretation, or schema behavior not present in T-043.
- Stop before any expensive, networked, full-resource, or downstream prompt-generation operation.

## Notes For Delivery QA
- Confirm the implementation stayed within fixture loading and did not add private query/ranking logic.
- Confirm downstream-facing API names and returned structure are documented clearly enough for T-048/T-049.
- Confirm smoke evidence includes both positive load success and contract comparison against A-003.
- Confirm no final reusable output remains only in `3_execution/`.
- Confirm `4_artifact/registry.yaml` and `5_report/completion.md` exist and match delivered artifacts.
