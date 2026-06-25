# AI Handoff: T-061 legacy_source_digest_repair_m1

## Task Goal
Create a clean replacement legacy source digest for the M1 Python-package milestone using T-007 as the trusted source map and only the registered migrated PxFquery package-source path. T-041 is failed historical context only.

## What Was Delivered
T-061 delivered a bounded static source digest, a module reuse matrix, a downstream reference-boundary YAML, and two human-readable HTML reports. The work stayed inside task outputs and did not run package workflows, write implementation code, read raw matrices, read the historical source root, or use web search.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Main concise digest of inspected legacy package modules, entry points, risks, and reuse classifications. | Read first for M1/M1.1 planning and cite as the bounded T-061 source interpretation. |
| D-002 | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | Module/file-level reuse matrix with recommended downstream actions. | Use to choose which legacy modules to reuse, adapt, isolate, or avoid. |
| D-003 | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Machine-readable rules for allowed citation/adaptation boundaries. | Use as the guardrail before any downstream task cites or adapts T-061 findings. |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html`: execution method and bounded-inspection audit.
- `4_artifact/3_document/result_report_v20260624.html`: human-facing result summary.
- `3_execution/a002_file_inventory_20260624.txt`: task-local inventory evidence.
- `3_execution/a002_python_symbol_index_20260624.txt`, `a002_definitions_20260624.txt`, `a002_ast_structure_20260624.txt`, `a002_risk_pattern_index_20260624.txt`: task-local static-inspection support files.

## Downstream Use
Use D-001 through D-003 as the authoritative T-061 package-source digestion package for future M1/M1.1 configuration, check, and execution tasks. Treat the outputs as planning and boundary evidence, not as runtime validation.

## Known Limits / Risks
This task did not execute the legacy package, rebuild indexes, inspect raw h5ad matrices, validate biological outputs, or prove that any legacy module runs in the current environment. Downstream implementation tasks must register runtime assets and run deterministic tests before treating legacy logic as operational.

## Do Not Read / Do Not Reuse
Do not use T-041 artifacts as authority. Do not use this task as permission to read the historical source root, broad `2_project_asset/` paths, raw matrices, notebooks, caches, or generated reports. Do not treat `3_execution/` support files as final reusable deliverables unless auditing T-061.

## Recommended Next Reads
1. `4_artifact/2_persist/legacy_source_digest_repair_m1.md`
2. `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`
3. `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`
