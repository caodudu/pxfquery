# Check Handoff Before Exec: T-061 legacy_source_digest_repair_m1

## Check Verdict
yellow_repair

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: T-041 task files, predecessor task directories, project protocol directories, registered project assets, historical source root `/Users/dudu/Documents/3_Project/8_functional_query`, and broad unregistered `2_project_asset/` paths outside A-002.
- Required registry: `1_asset/registration.yaml`
- Must stop if: A-001 or A-002 is missing, A-002 resolves outside the registered migrated package-source path, the digest would require reading T-041 outputs as authority, execution would need raw matrices/notebooks/binaries, or execution would need to modify legacy/project assets.

## Objective Restatement
Create a clean replacement digestion asset for the failed T-041 role. The execution AI should use T-007 as the trusted source map, inspect only the registered migrated PxFquery package-source directory, and produce a concise source digest, module reuse matrix, and downstream reference-boundary YAML for future M1/M1.1 development tasks. This task must not implement package code or promote outputs into final project deliverables.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Trusted T-007 source map for migrated package path and source-priority context. | ready; symlink resolves to existing file |
| A-002 | `1_asset/migrated_pxfquery_package_source` | Only raw legacy package-source directory allowed for bounded static inspection. | ready; symlink resolves to existing directory with about 30 files at max depth 2 |

## Execution Strategy
1. Confirm A-001 and A-002 still resolve to the paths registered in `1_asset/registration.yaml`; stop on mismatch.
2. Inventory A-002 filenames and sizes first, saving notes or helper output under `3_execution/`.
3. Inspect only Python/source files under A-002 with bounded windows. Prefer imports, classes, functions, constants, and entry-point behavior; do not dump whole large files.
4. Classify each relevant module/file as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 tasks.
5. Record data/index access assumptions, hard-coded paths, LLM/API coupling, missing runtime assets, and downstream risks.
6. Write the three required reusable outputs under `4_artifact/`, then write reports, registry, and completion note.

## Conservative Execution Advice
- Start with: `find 1_asset/migrated_pxfquery_package_source -maxdepth 2 -type f -print` plus file sizes.
- Smoke/demo command or method: inspect a small subset first, such as package entry points and query-related modules, then expand to all Python files.
- Full run only after: A-001 and A-002 resolve correctly and no forbidden path is needed.
- Cost/time risk: low to moderate; this is static source digestion, not code execution or matrix analysis.
- Checkpoint advice: if any file appears too large, inspect only targeted symbol windows and document the skipped regions.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Replacement source digest | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Names concrete modules/classes/functions and classifies reuse status. |
| Module reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | One row per relevant module/file with reuse status, downstream relevance, risks, and recommended action. |
| Legacy reference boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Machine-readable rules for what later tasks may cite, adapt, or must avoid. |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Explains bounded-read method and execution steps. |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Summarizes accepted findings and downstream use. |
| Artifact registry | `4_artifact/registry.yaml` | Registers all accepted outputs. |
| Completion note | `5_report/completion.md` | States what was produced and what was intentionally not done. |

## Failure / Stop Conditions
- A required asset is missing, empty, or resolves outside the registered boundary.
- Execution needs to read T-041 outputs as authoritative evidence.
- Execution needs unregistered project assets, historical source root files, raw h5ad matrices, notebooks, binaries, caches, or generated reports.
- Execution needs to run package workflows, rebuild indexes, perform biological analysis, perform web search, or write implementation code.
- The package-source inspection cannot be completed without dumping large files verbatim.

## Notes For Delivery QA
- Delivery QA should verify that outputs are fresh T-061 artifacts, not copied from T-041.
- Delivery QA should check that the digest documents the bounded-read method and the A-002 file inventory.
- Delivery QA should confirm the registry points only to T-061 outputs under `4_artifact/`.
- Delivery QA should treat this as a digestion/reference asset, not as a package milestone deliverable.
