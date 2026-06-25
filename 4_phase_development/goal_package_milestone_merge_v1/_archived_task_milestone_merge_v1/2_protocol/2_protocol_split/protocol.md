# Protocol: milestone_merge_v1

## Objective
Create `pxfquery-T-037`, a slim runnable package core milestone assembled only from the minimum upstream assets required for a working package foundation: package workspace, loader/resource access, deterministic forward query, no-hit guard, and minimal package tests. Reverse/stability demo is moved to T-038, and final aggregation is moved to T-039.

## Inputs
- A-001: T-024 pxfquery workspace package — base src-layout package and pyproject foundation.
- A-002: T-021 standard resources bundle — canonical runtime resource files available through the loader lineage; use only the minimum files needed for local validation.
- A-003: T-025 standard resource manifest — optional resource inventory reference; do not make it a hard execution dependency.
- A-004: T-026 matrix/resource loader package — loader implementation and validation evidence to merge into the package.
- A-005: T-027 runtime query index directory — optional runtime-index reference only. Do not require it for T-037 package-core completion.
- A-006: T-028 function index pack — optional function-index reference only. Do not require it for T-037 package-core completion.
- A-007: T-029 forward query engine artifacts — runnable deterministic forward path and canonical result/evidence files.
- A-008: T-031 no-hit guard artifacts — false-positive guard module and no-hit/positive-control evidence.
- A-009: T-032 reverse stability guard artifacts and repaired package — optional reference only in T-037; T-038 consumes this as a hard input.
- A-010: T-035 integration smoke test artifacts — optional reference only in T-037; T-038 consumes this as a hard input.
- A-011: T-030 reverse query task record — lineage context only; its direct artifact registry is empty and must not block T-037.
- A-012: T-036 demo CLI task record — lineage context only; it must not block T-037 because T-037 produces its own final demo.
- A-013: Current project protocol — runtime environment and workspace-boundary reference.

## Steps
1. Verify only the T-037 required assets: A-001, A-002, A-004, A-007, A-008, and A-013. Treat A-003/A-005/A-006/A-009/A-010/A-011/A-012 as optional lineage/reference context and read them only if a specific missing detail is needed.
2. Create the T-037 package workspace under `4_artifact/2_persist/pxfquery-T-037/` from A-001, then merge loader/resource access, deterministic forward query evidence, and no-hit guard behavior into a coherent runnable package layout.
3. Vendor or reference only the minimum resource files needed for deterministic demo/test execution under the T-037 package artifact. Preserve upstream resources as read-only; if copying, keep checksums or file-size evidence in the lineage report.
4. Implement package entry points or scripts for deterministic forward and no-hit modes only. Do not require reverse/stability, optional resolver, LLM success, T-030 direct reverse artifacts, or T-036 demo artifacts.
5. Run focused checks in the project `pxfquery` conda environment: install/import smoke, compile checks, resource-loader check, forward demo, and no-hit negative demo.
6. If a bug blocks a runnable T-037 milestone, repair it inside the T-037 package artifact only. Do not overwrite upstream task artifacts. Record repaired files, source asset, validation evidence, and downstream consumption guidance.
7. Produce deliverables: merged package, test/demo logs and JSON/CSV outputs, package handoff notes, lineage report, artifact registry, completion report, and the two required Chinese HTML reports.

## Constraints
- This task configures and later executes a merged package milestone; it must not promote outputs into `6_project_deliverable/`.
- Do not modify upstream predecessor task artifacts, project raw assets, or the historical source root.
- Use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` for Python execution unless the executor documents a specific blocker.
- T-030 direct reverse output is missing and is outside T-037 package-core scope.
- T-036 demo output is not a hard input and is outside T-037 package-core scope.
- T-032/T-035 are handled by T-038, and final aggregation is handled by T-039; do not pull them back into T-037 as hard requirements.
- Config, check, and execute must be launched as separate fresh CLI sessions. Do not resume a previous long Codex thread for later stages.
- Optional resolver/LLM assets are outside the required milestone path and must not block completion.
- Large matrices and resource files should be inspected by manifest/schema/sample or loader validation rather than dumped into reports.

## Deliverables
- `4_artifact/2_persist/pxfquery-T-037/` — merged runnable Python package milestone.
- `4_artifact/2_persist/pxfquery_T037_handoff.md` — package-core handoff and usage notes for T-038.
- `4_artifact/2_persist/pxfquery_T037_lineage.md` — upstream asset-to-package lineage report for T-037 required inputs.
- `4_artifact/5_table/pxfquery_T037_test_results.json` — final test and smoke evidence.
- `4_artifact/5_table/pxfquery_T037_demo_summary.json` — forward/no-hit package-core demo evidence.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — output artifact registry.
- `5_report/completion.md` — completion and remaining-risk report.
- `5_report/repair_log.md` — only if scoped package repairs were needed.

## Acceptance
- The T-037 package installs or imports successfully in the `pxfquery` conda environment.
- Final tests include actual commands, exit status, and output files for import/compile, resource loading, forward query, no-hit guard, and reverse/stability demo behavior.
- The deterministic demo produces readable forward and no-hit outputs without requiring reverse/stability, optional resolver, or LLM assets.
- The lineage report maps every consumed upstream asset to the package core and explicitly states that reverse/stability and final demo/report completion moved to T-038.
- Required Chinese HTML reports exist under `4_artifact/3_document/`.
