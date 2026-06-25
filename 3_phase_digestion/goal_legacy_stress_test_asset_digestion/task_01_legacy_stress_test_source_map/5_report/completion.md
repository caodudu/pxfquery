# Completion Report — T-055 01_legacy_stress_test_source_map

Generated: 2026-06-24

## Status
Completed.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Legacy stress test source map | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Accepted |
| Stress test candidate asset index | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Accepted |

## Coverage Summary

All 7 target directories were browsed and cataloged:
- `reports/validation_reports/` — 57 items (15 overlapped with T-007, ~42 newly cataloged)
- `code/index_builders/` — 19 items (6 validation scripts, 6 index builders, 6 demos, 1 install doc)
- `code/pxfquery_package/query/` — 5 items (resolver.py 1072 lines, forward.py, reverse.py, init, pycache)
- `data/query_indexes/` — 9 index files (function_index.json confirmed missing)
- `reports/digested_context/` — 9 items (minimal validation relevance)
- `code/analysis_scripts/` — 55 items (GSEA eval scripts, notebooks, duplicates)
- `results/gsea_tables/` — 6 large symlink items (244-372MB each)

Total candidate assets cataloged: ~160 entries in the CSV index.

## Key Findings

1. **Strongest validation baseline**: M-0386 (test_forward_matrix.py) with deterministic 7/7 pass rate.
2. **Critical gap**: `function_index.json` missing from migrated query indexes. Must be rebuilt via M-0373.
3. **LLM stability risk**: 6/9 success rate documented; conservative claims advised.
4. **Performance data**: always_LLM is ~200x slower than hybrid_fast (167.3s vs 0.825s for comparable queries).
5. **Script path assumptions**: All scripts use legacy workspace paths; none are directly runnable in current environment.
6. **Duplicate scripts**: M-013x and M-034x/035x series appear to be duplicates from different legacy versions.
7. **Systematic migration gap**: No GSEA table symlinks >10% of referenced files were unresolvable, but the function_index.json gap is significant.

## Notes

- `runnable_claim: false` set for all entries per protocol constraint.
- T-007 cross-reference documented in source map section 3.
- Missing/ambiguous leads documented in source map section 4.
- Guidance for later tasks provided in source map section 5.
- No legacy-root paths appear in deliverables.
- No modifications made to flat asset library or predecessor artifacts.
