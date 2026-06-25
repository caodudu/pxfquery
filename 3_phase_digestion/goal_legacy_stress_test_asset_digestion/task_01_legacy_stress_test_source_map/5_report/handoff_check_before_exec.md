# Check Handoff Before Exec: T-055 01_legacy_stress_test_source_map

## Check Verdict
green_check

## CyHex Boundaries
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map
- Allowed write dirs: 3_execution/, 4_artifact/, 5_report/
- Forbidden dirs: /Users/dudu/Documents/3_Project/8_functional_query, 1_project_init/, predecessor task folders (T-001, T-002, T-007 contents under 3_phase_digestion/)
- Required registry: 1_asset/registration.yaml (all 9 assets preflight ok)
- Must stop if: flat asset library inaccessible, >10% of referenced files not found in flat library, any predecessor artifact (A-003~A-009) unreadable (note the limitation but proceed)

## Objective Restatement
Create a source map of migrated legacy materials related to PxFquery stress testing, complex queries, resolver validation, edge cases, and old validation scripts/reports. This is a candidate catalog--not execution, not validation. Deliverables: a structured markdown guide and a CSV index for later task use.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for migrated stress-test/validation materials | ok |
| A-002 | T-002 migration_manifest_v20260614.json | Trace migrated/excluded files and original paths | ok |
| A-003 | T-001 old_asset_structure_report.md | Legacy source structure context | ok |
| A-004 | T-001 project_background_extraction_report.md | Why stress-test assets were created | ok |
| A-005 | T-007 pxfquery_development_state_report_v20260617.md | Current development state and known validation gaps | ok |
| A-006 | T-007 pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence (15 entries) to avoid duplication | ok |
| A-007 | T-007 pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps/risks for cross-reference | ok |
| A-008 | T-002 flat_asset_library_structure_zh_v20260615.md | Structure explanation for navigating flat library | ok |
| A-009 | T-002 not_migrated_assets_report_zh_v20260616.md | Explicitly excluded assets that may contain stress-test content | ok |

## Execution Strategy
1. Read A-005, A-006, A-007 to establish the known validation landscape and identify gaps that stress-test sourcing should fill.
2. Read A-002 and A-009 to map stress-test-related entries (filter manifest for keywords: stress, test, validate, smoke, edge, stability, suite) and record not-migrated items.
3. Browse A-001 high-priority directories (reports/validation_reports/ 57 items, code/index_builders/ 19 items, code/pxfquery_package/query/ 5 items, data/query_indexes/ 9 items, reports/digested_context/ 9 items, code/analysis_scripts/ 55 items, results/gsea_tables/ 6 items). Read README files and key scripts/reports to classify relevance.
4. For each candidate asset, record: migrated path, original path, asset type, stress-test relevance category, assessment, runnable_claim (always false), and T-007 cross-reference where applicable.
5. Write legacy_stress_test_source_map_vYYYYMMDD.md: summary, categorized inventory tables per category, cross-reference with A-006, missing/ambiguous leads, guidance for later tasks.
6. Write stress_test_candidate_asset_index_vYYYYMMDD.csv: one row per candidate with columns category, migrated_path, original_path, asset_type, relevance, runnable_claim, T-007_cross_ref, notes.
7. Register both deliverables in 4_artifact/registry.yaml, write 5_report/completion.md.

## Conservative Execution Advice
- Start with: read A-006 (validation evidence index, only 15 rows) and A-002 (migration manifest) to establish a baseline before any directory browsing.
- Smoke/demo command or method: do a single directory scan (reports/validation_reports/) and produce 2-3 candidate rows before committing to full scan of all 7 directories.
- Full run only after: the first 2-3 rows match the expected schema and relevance categories.
- Cost/time risk: low. No API calls, no computation, no network access. Pure file-system read-and-catalog work. The flat library has ~160 files total across target directories; browsing is fast.
- Checkpoint advice: after completing the validation_reports/ scan (largest directory), checkpoint the partial CSV to avoid data loss.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Legacy stress test source map | 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md | Covers all 7 target directories; has categorized inventory tables; cross-references A-006; documents missing leads |
| Stress test candidate asset index | 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv | One row per candidate; all 8 columns present; machine-readable; no legacy-root paths |

## Failure / Stop Conditions
- Flat asset library inaccessible or empty: immediate stop, write 5_report/blocked.md.
- More than ~10% of validation-report-referenced files not found in flat library: flag as systematic migration gap but continue.
- Predecessor artifact (A-003~A-009) unreadable: document limitation and proceed.
- Migration manifest missing critical path mapping: note gap and proceed.

## Notes For Delivery QA
- All 9 assets preflight ok; all symlinks resolve. Flat library target directories all exist with substantial content (57+9+19+5+9+55+6 items).
- The T-007 validation evidence index has 15 entries covering validation_reports/; the source map should complement, not duplicate, these 15 entries. Focus on scripts, indexes, GSEA tables, and any validation reports NOT already in A-006.
- The meta.yaml shows sub_status: check_failed from a prior cycle. This green_check should allow the executing AI to proceed.
- This task is digestion-phase, so 2_project_asset/ browsing is permitted. No legacy-root access needed.
- runnable_claim must always be false for all entries.