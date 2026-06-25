# AI Handoff: T-043 data_manifest_fixture_m1

## Task Goal
Produce the stable M1 data manifest and a small deterministic real-data fixture package for downstream loader, forward-query, reverse-query, validation, and package-assembly tasks.

## What Was Delivered
T-043 delivered a resource manifest, a fixture package, expected shape/key/column tables, sample records, validation evidence, registry metadata, and human-readable execution/result reports. The fixture package is intentionally small and is meant for deterministic smoke/demo wiring, not biological ranking-performance claims.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Entry point for full-resource and fixture-resource paths. | T046/T047 should read this first to discover M1 resource paths. |
| D-002 | `4_artifact/2_persist/fixture_package_m1/` | Compact real-data fixture bundle for fast deterministic tests. | T046/T048/T049/T050/T051 may use it for smoke/demo runs. |
| D-003 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Documents expected shapes, keys, columns, and validation rules. | Loader and validation tasks should use it as acceptance evidence. |
| D-004 | `4_artifact/5_table/sample_records_m1.csv` | Traceable sample rows and keys used by the fixture package. | Query-core tasks should use it to select concrete demo inputs. |

## Supporting Artifacts
- `4_artifact/2_persist/data_manifest_fixture_m1_readme.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `3_execution/validation_log_m1.json`
- `4_artifact/registry.yaml`

## Downstream Use
T046 should implement the minimal fixture loader against D-001 and D-002. T047 may harden resource loading using D-001 and D-003. T048 and T049 should use D-004 only for bounded demo-case selection, and must still follow the API/demo contract from T042 once T042 is done.

## Known Limits / Risks
The fixture is deliberately small. It validates file format, path wiring, loader behavior, and smoke-test mechanics only. It must not be used to claim biological ranking quality or full-resource coverage.

## Do Not Read / Do Not Reuse
Do not use historical T024-T040 outputs as authority for this M1 route. Do not substitute this fixture for full-resource validation when the task explicitly requires full standard resources.

## Recommended Next Reads
1. `4_artifact/2_persist/resource_manifest_m1.yaml`
2. `4_artifact/5_table/expected_shapes_keys_columns_m1.csv`
3. `4_artifact/5_table/sample_records_m1.csv`
4. `5_report/completion.md`
