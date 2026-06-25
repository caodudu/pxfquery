# T-061 legacy_source_digest_repair_m1 — Protocol

## Objective

Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and inspect only the explicitly registered migrated PxFquery package-source directory. Treat T-041 as a failed historical attempt and do not reuse its outputs as authoritative evidence.

This is a digestion task. It must not write implementation code, run package workflows, modify legacy files, modify completed task artifacts, or promote outputs into project deliverables.

## Position In Project

T-061 replaces the failed/unsafe dependency role that T-041 was intended to serve. Its outputs should give later M1/M1.1 development tasks a concise, bounded, and auditable reference for which legacy package modules can be reused, adapted, or avoided.

T-007 remains the authority for the migrated package-source path and overall development-state source map. T-041 may be mentioned only to explain why a replacement digest was needed.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map identifying the migrated PxFquery package-source path and relevant source-priority rules. |
| A-002 | project_asset via T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/` | The only raw legacy package-source directory allowed for bounded static inspection in this task. |

## Execution Steps

1. Confirm the registered A-001 source map and A-002 package-source directory are available; stop if A-002 resolves outside the registered migrated package path.
2. Inventory A-002 filenames and file sizes first. Do not recursively read caches, notebooks, binaries, generated reports, matrix/data files, or `__pycache__`.
3. For each Python source file under A-002, inspect imports, classes, functions, key constants, and entry-point behavior using bounded windows. Prefer no more than 200 source lines per file unless a specific symbol requires a targeted extra window.
4. Identify concrete reusable, adaptable/risky, incomplete, and forbidden pieces for M1/M1.1 development. Name modules, classes, and functions where possible.
5. Record data/index access patterns, hard-coded path assumptions, LLM/API coupling, missing runtime assets, and other downstream risks without executing package code.
6. Write a concise markdown source digest to `4_artifact/2_persist/legacy_source_digest_repair_m1.md`.
7. Write a CSV module reuse matrix to `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`.
8. Write a machine-readable downstream reference-boundary YAML to `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`.
9. Create execution/result reports, update `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints

- Use T-007/D-001 as the source authority for the package-source path.
- Inspect only A-002 as raw legacy source.
- Use bounded static inspection; do not dump large files verbatim.
- Document the bounded-read method in the digest or execution report.
- Keep all generated analysis notes, scripts, and temporary logs in `3_execution/`.
- Put reusable accepted outputs only under `4_artifact/`.
- Preserve provenance for every conclusion that depends on A-001 or A-002.

## Forbidden

- Do not use T-041 outputs as authoritative inputs.
- Do not mark T-041 complete, repair T-041, or modify any T-041 file.
- Do not scan the whole `2_project_asset/` tree.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not read raw h5ad matrices, notebooks, binary data, caches, `__pycache__`, or generated reports inside package/source-adjacent paths.
- Do not run package workflows, rebuild indexes, perform biological analysis, perform web search, or write implementation code.
- Do not modify project protocol, predecessor task directories, completed artifacts, or legacy asset files.

## Web Search Allowance

Allowed: no

Reason: The task is a local digestion repair based on T-007 and a registered migrated package-source path. No current external or web evidence is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Replacement source digest | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | yes |
| Module reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | yes |
| Legacy reference boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The digest names concrete modules, classes, functions, and entry points inspected from A-002.
- The digest clearly classifies legacy pieces as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 use.
- The CSV matrix contains one row per relevant module/file with reuse status, downstream relevance, risks, and recommended action.
- The boundary YAML states exact downstream reference rules, including what later tasks may cite, adapt, or must avoid.
- T-041 is described only as failed/context and none of its artifacts are used as authority.
- The bounded-read method is documented, including filename/size inventory and per-file inspection limits.
- No implementation code, old-root reads, broad project-asset scans, raw data reads, or web searches are performed.

## Failure / Stop Rules

- Stop if A-001 or A-002 is unavailable or resolves to an unexpected path.
- Stop if completing the digest requires reading outside A-002 or outside the allowed predecessor context.
- Stop if package files are too large to inspect safely with bounded static windows; report the limitation instead of dumping contents.
- Stop if execution would require running package code, rebuilding indexes, reading matrices, or using T-041 outputs as authority.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
