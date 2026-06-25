# AI Handoff: T-055 01_legacy_stress_test_source_map

## Task Goal
Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. This is a candidate catalog only -- no execution, no validation.

## What Was Delivered
- `legacy_stress_test_source_map_v20260624.md`: Categorized inventory of ~160 candidate stress-test assets across 7 target directories in the flat asset library. Includes cross-reference to T-007 validation evidence index, missing/ambiguous leads, and guidance for later tasks.
- `stress_test_candidate_asset_index_v20260624.csv`: Machine-readable index with one row per candidate asset (8 columns).

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Primary catalog of all stress-test candidates with relevance categories and T-007 cross-ref | Read first to identify which assets to use for validation suite design |
| D-002 | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Queryable machine-readable index for filtering by category, type, or cross-ref | Load as DataFrame for filtering/analysis |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html` — execution process summary
- `4_artifact/3_document/result_report_v20260624.html` — result summary for human review

## Downstream Use
1. **Validation suite design**: Use section 2.1 (validation scripts) and section 5 guidance to build a current-environment validation suite.
2. **Gap remediation**: Rebuild `function_index.json` via M-0373_build_function_index.py.
3. **Baseline comparison**: Use M-0386 (test_forward_matrix.py) as primary regression test.
4. **Performance characterization**: Reference M-0277 (timing) and M-0275 (hybrid_fast v3) for expectations.
5. **LLM risk assessment**: Reference M-0377 and M-0267 (6/9 success rate) for conservative claims.

## Known Limits / Risks
- All scripts marked `runnable_claim: false` — none are directly runnable in current environment.
- `function_index.json` is missing from migrated query indexes (must be rebuilt).
- GSEA eval scripts have HPC-specific dependencies (SLURM, scanpy, gseapy).
- GSEA tables in results/gsea_tables/ are symlink placeholders (244-372MB each).
- Duplicate script pairs exist (M-013x vs M-034x/035x series).
- Suite run variants require deduplication.

## Do Not Read / Do Not Reuse
- Legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`) — not registered for task access.
- Predecessor task folders (T-001, T-002, T-007) — outputs are already consumed via asset registry.
- `1_project_init/` — not needed for stress-test source map consumption.
- Flat asset library (`2_project_asset/`) — read-only; do not modify.

## Recommended Next Reads
1. `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` — full catalog
2. `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` — machine index
3. `5_report/completion.md` — execution summary
