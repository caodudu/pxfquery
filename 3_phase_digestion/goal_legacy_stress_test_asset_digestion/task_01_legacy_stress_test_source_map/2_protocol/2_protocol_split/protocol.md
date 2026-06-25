# T-055 01_legacy_stress_test_source_map — Protocol

## Objective

Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. The source map must be a structured guide that later tasks can use to locate, assess, and reuse these materials without directly scanning the unregistered legacy root.

## Position In Project

This is a digestion-phase task under G-005 (legacy stress test asset digestion). It follows T-001 (legacy semantic digestion), T-002 (flat asset migration), and T-007 (development state digestion). This task does not execute, run, or validate any old script. It produces a candidate map only, enabling later assessment tasks to proceed without legacy-root access.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|----------|-------------|------|------------|
| A-001 | T-002 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for all migrated legacy materials that may contain stress-test/validation content |
| A-002 | T-002/D-002 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json | Full migration manifest to trace which stress-test files were migrated, their source paths, and any not-migrated items |
| A-003 | T-001/D-003 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md | Understanding legacy source structure and identification of operational vs archive layers |
| A-004 | T-001/D-004 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md | Project background context for understanding why certain stress-test assets were created |
| A-005 | T-007/D-002 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development state summary to understand which validation gaps are already documented |
| A-006 | T-007/D-004 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence index to avoid redundant cataloging and identify gaps |
| A-007 | T-007/D-005 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps and risks to cross-reference against discovered stress-test materials |
| A-008 | T-002/D-005 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Chinese structure explanation for the flat library navigation |
| A-009 | T-002/D-007 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Record of intentionally not-migrated assets; may contain stress-test content that was explicitly excluded |

## Execution Steps

1. Read A-001 (flat asset library) structure to understand available directories.
2. Read A-005, A-006, A-007 (T-007 handoff) to understand already-documented validation landscape.
3. Read A-002 (migration manifest) and A-009 (not-migrated report) to identify stress-test-related entries.
4. Browse the following high-priority directories within A-001 for stress-test/validation content:
   - `reports/validation_reports/` — resolver validation, suite runs, stability checks, known risks
   - `code/index_builders/` — test scripts (test_resolver_smoke, test_forward_matrix, verify_resolver_cases, run_forward_question_suite, validate_act1, check_llm_stability)
   - `code/pxfquery_package/query/` — resolver pipeline source with forward search policy (L1-L4 logic)
   - `data/query_indexes/` — index files used by the resolver for query resolution
   - `reports/digested_context/` — any context reports mentioning validation outcomes
   - `code/analysis_scripts/` — GSEA evaluation scripts (cp_gsea_eval, sh_gsea_eval, xpr_gsea_eval) and analysis notebooks
   - `results/gsea_tables/` — GSEA result tables used as validation baselines
5. For each candidate asset found, record:
   - Migrated path within flat library (or explicit not-migrated status)
   - Original legacy source path (from manifest or A-003/A-008 context)
   - Asset type: script, report, data, index, result, design_doc
   - Stress-test relevance category: complex_query, resolver_edge_case, validation_script, validation_report, stability_check, GSEA_evaluation, performance, edge_case_input, known_risk
   - Brief assessment of what it tests or validates
   - Caveat if the asset is not directly runnable or has ambiguous provenance
6. Produce `4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md` with:
   - Summary of scope and approach
   - Categorized inventory of candidate stress-test assets
   - For each category, a table with asset path, type, relevance, and notes
   - Cross-reference to T-007 validation evidence index to show overlap and gaps
   - Honest record of missing or ambiguous leads (e.g., "suite run output referenced but not found")
   - Guidance for later tasks on how to use this map
7. Produce `4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv` with:
   - One row per candidate asset
   - Columns: category, migrated_path, original_path (if known), asset_type, relevance, runnable_claim, T-007_cross_ref, notes

## Constraints

- Do not scan the unregistered legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`). Use only the flat asset library and predecessor artifacts.
- Do not claim any old script is runnable in the current environment. Mark all scripts with `runnable_claim: false` unless explicitly verified.
- Record missing or ambiguous leads honestly. If a validation report references a file not found in the flat library, note the discrepancy.
- Date format for deliverables: `vYYYYMMDD` using the execution date.

## Forbidden

- No execution or modification of legacy scripts.
- No modification of files in the flat asset library.
- No modification of predecessor task artifacts.
- No creation of symlinks or directory copies outside `4_artifact/`.
- No comparison with external databases or web sources.

## Web Search Allowance

Allowed: no
Reason: All required source material is available in migrated project assets and predecessor artifacts.

## Deliverables

| Expected output | Target path | Required |
|-----------------|-------------|----------|
| Legacy stress test source map | 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md | yes |
| Stress test candidate asset index | 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv | yes |

## Acceptance Criteria

- Source map covers all validation_reports/, index_builders/ test scripts, query/resolver code, and GSEA evaluation scripts.
- Each candidate asset has a clear relevance category and provenance.
- Missing or ambiguous leads are explicitly documented, not silently omitted.
- CSV index is machine-readable with consistent columns.
- No legacy-root paths appear in the deliverables (use migrated paths or explicit "not migrated" notation).
- The deliverables reference and complement, not duplicate, the T-007 validation evidence index.

## Failure / Stop Rules

- If the flat asset library is not accessible or is empty, stop and report the precondition failure.
- If the migration manifest is missing critical path mapping, note the gap and proceed with available information.
- If more than 10% of referenced files in validation reports cannot be located in the flat library, flag this as a systematic migration gap.
- If a predecessor artifact (A-003 through A-009) cannot be read, proceed without it and document the limitation.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results (optional for this task; use markdown if sufficient).
