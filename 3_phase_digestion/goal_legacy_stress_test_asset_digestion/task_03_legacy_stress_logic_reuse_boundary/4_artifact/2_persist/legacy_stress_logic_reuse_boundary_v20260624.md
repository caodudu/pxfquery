# Legacy Stress Logic Reuse Boundary Analysis

Generated: 2026-06-24
Task: T-057 03_legacy_stress_logic_reuse_boundary

## 1. Classification Criteria

Each asset was read or inspected and assigned one of:

| Category | Definition |
|---|---|
| **direct reference** | Content is valid, current, and usable as reference without modification. May contain old workspace paths that do not affect its meaning. |
| **rewrite needed** | Core logic, test cases, or patterns are valuable, but old workspace paths, imports, or API calls prevent immediate use. Must be ported/rewritten. |
| **historical evidence only** | Content documents a past state, is superseded by newer versions, or serves only as provenance. Not suitable for active development. |
| **not usable** | No actionable substance for current development. Runtime artifacts, empty shells, or content with zero reuse value. |
| **unknown** | Content could not be assessed (e.g., unreadable, corrupted, or too opaque for classification). |

### Authority rules applied

- **Source map priority**: Prefer T-007 source map (A-012) which gives highest authority to current project protocol, code + latest validation reports, and M-0239 latest reports index.
- **Not-migrated check**: All evaluated assets were confirmed present in the flat asset library; no unmigrated assets were classified.
- **Old workspace paths**: Noted where present but do not block `direct reference` unless they prevent comprehension.
- **Superseded detection**: When M-0239 or T-007 validation index marks a report as superseded, the newer version takes priority.
- **T-001 authority rule**: Old protocol shells, MOC files, and checkpoint templates are historical-only.

## 2. Assessment by Asset Category

### 2.1 Validation Reports — Primary Evidence

#### Direct reference (highest reuse value)

**M-0239_latest_reports_index.md** — The authoritative index for resolving which validation reports are current. Defines that suite_runs/ reports with complete statistics take priority, and that the act1 auth-failure path is not valid basis. Essential for any developer navigating the 57-report corpus.

**M-0291_6_llm_resovler_forward_matrix.md** — Most recent deterministic mock-based resolver matrix test. 7/7 pass across all hit levels (EXACT, PROXY_PERT, PROXY_CELL, PROXY_BOTH, exact drug, proxy drug). This is the single strongest piece of validation evidence in the entire corpus.

**M-0277_always_llm_summary4_stats.md** — Definitive latency and failure evidence for the always_llm mode: 167.3s for 4 queries, with `llm_parse_intent` consuming 117.142s. Q5 (EGFR inhibitor) got NOT_FOUND in this mode vs PROXY_PERT in hybrid_fast. This is the canonical evidence motivating hybrid_fast as the default mode.

**M-0275_hybrid_fast_no_summary.md** — Best evidence for the preferred hybrid_fast mode: 3 queries in 0.825s total, all found (EXACT + 2 PROXY_CELL). Demonstrates sub-second deterministic resolver performance.

**M-0267_llm_stability_check.md** — Only formal LLM stability test: 6/9 success rate across 3 rounds. Failures consistently on drug intent ("EGFR inhibitor") and occasional NSCLC context. Critical risk evidence showing LLM parsing is not stable enough for manuscript claims.

**M-0243_known_risks.md** — Compact risk catalog: LLM stability, always_llm latency, mode consistency, evidence explanation, asset organization, path drift. Directly usable as development acceptance criteria.

**M-0244_next_execution_order.md** — 5-step reproducible resolver execution guidance. Still relevant for designing future validation tasks.

**M-0290_todolist.md** — Detailed resolver development TODO with completed items (logger, caching, hybrid_fast, retry, suite archiving) and remaining items (consistency regression, explanation docs). Directly informs T-058 development priorities.

#### Historical evidence only (usable as provenance or design context)

**M-0255_act1_validation.md** — Contains valuable forward EGFR/A549 EXACT result with functional scores and a reverse apoptosis/MYC example. However, the latest report index explicitly warns that the act1 auth-failure path is NOT a valid result basis. **Mixed authority**: content is useful but must be cited with the priority rule caveat.

**M-0257_6_llm_resovler_forward_matrix.md** — Identical 7/7 results to M-0291 but older. Superseded; use M-0291.

**M-0266_forward_question_suite.md** — Full 12-question suite with detailed resolver_meta. Rich behavioral evidence but superseded by timestamped suite_runs/ versions.

**M-0246_2_cp_index.md** — Drug index build evidence (4.1h, 6647 drugs, 5314 PubChem SMILES hits). Index JSONs already migrated; report is provenance-only.

**M-0248_3_gene_index.md** — Gene index build evidence (78061 entries, biological sanity checks pass). Index JSONs already migrated.

**M-0252_5_function_index.md** — Function index build evidence (91 functions, 243 aliases, 11/11 tests). Confirms function_index.json was built, but the runtime JSON is missing from migrated assets. Use as spec for rebuilding.

**M-0245_obsolete_and_legacy_list.md** — Documents old report folders and compatibility paths. Low direct reuse value but prevents duplicate-report confusion.

**M-0258_cellline_stepwise_demo.md**, **M-0259_external_api_demo.md** — Demo reports with old workspace paths. Use as design reference only.

**Timestamped suite runs** (M-0260 through M-0276, except M-0266, M-0275, M-0277 already classified above, and M-0269 through M-0274 below) — Historical intermediate runs superseded by the latest suite_runs/ reports.

**README and log files** (M-0254, M-0278, M-0279, M-0289, M-0292, M-0293, M-0240, M-0042) — Navigation shells and log indexes. No substantive evidence.

**Logger demo files** (M-0281 through M-0286) — Logger demonstration artifacts. Logging is already implemented in the current resolver.

#### Not usable

**GSEA log files** (M-0117 through M-0127, .err and .out files) — Runtime output artifacts from GSEA and UMAP runs. Zero analytical value for current development.

### 2.2 Legacy Test/Verify Scripts

All scripts in `code/index_builders/` reference old workspace paths (e.g., `Path(__file__).resolve().parents[3]`, `workspace/script`, `output/store/gsea_anndata`, `output/store/query_index`). None are runnable as-is in the current project. However, their core test logic and patterns are valuable.

#### Rewrite needed (high priority for future development)

**M-0386_test_forward_matrix.py** — Deterministic mock-based forward matrix test with the 7 canonical test cases (EXACT through PROXY_BOTH). The mock hook pattern (`query_intents`, `parse_intent_hook`, `map_cell_hook`) is the right approach for deterministic resolver testing. Should be the first test ported after resolver package migration.

**M-0387_test_resolver_smoke.py** — Minimal smoke test checking resolver creation, forward query, and reverse query. Simple pattern suitable as the first verification step after package setup.

**M-0389_verify_resolver_cases.py** — Integration test with real LLM backend, flexible hit-level expectations, and timing. Valuable as a template for regression testing.

**M-0385_run_forward_question_suite.py** — Full-featured 14-question suite runner with dual-mode support (always_llm/hybrid_fast), timing diagnostics, and output archiving. The 14-question bank covers good scenario diversity.

**M-0388_validate_act1.py** — Act-1 forward/reverse validation script. Useful after resolver migration.

**M-0377_check_llm_stability.py** — LLM stability checker with 3-round repeated queries. Valuable for future LLM evaluation.

**M-0381_demo_resolver.py** — General resolver demo. Use as integration demo template.

#### Rewrite needed (conditional — only if index rebuild is required)

**M-0373_build_function_index.py** — HIGH PRIORITY for rewrite: this is the only path to restore the missing `function_index.json` runtime asset. Needs access to functional matrix h5ad files.

**M-0365_build_drug_index.py** — Drug index builder. 4.1h runtime with PubChem API. Only needed if drug index must be rebuilt.

**M-0367_build_gene_index.py** — Gene index builder. Requires large GenePT embedding files. Only needed if gene index must be rebuilt.

**M-0369/M-0370/M-0372_build_cellline_*.py** — Cellline index builders. Only needed if cellline index must be rebuilt.

#### Historical evidence only

**M-0378_demo_cellline_stepwise.py**, **M-0379_demo_external_apis.py** — Demo scripts for educational purposes. Keep as design reference for resolver resolution patterns.

**M-0380_demo_logger_capabilities.py** — Logger already implemented in current resolver.

**M-0383_Resolver_Forward_Demo_Clean.ipynb**, **M-0384_Resolver_Workbench.ipynb** — Jupyter notebooks for interactive demos. Keep as reference for UI design.

**M-0363_1_install.md** — Old installation README. Superseded by conda pxfquery env.

### 2.3 Resolver Source Code and Design Docs

**resolver.py** (A-010) — **Direct reference**. The core resolver pipeline with forward-first proxy logic (L1-L4), evidence-aware retrieval with evidence budgets, genetic multi-source behavior, fast-path + LLM-path dual-mode architecture, and logging metadata. This is the canonical source that all stress-test scripts exercise. Contains a default `log_dir` with old workspace path and direct `openai` import — these should be updated during migration but do not affect its status as direct reference for understanding resolver logic.

**design_docs/** — **Direct reference**. Design documents explain resolver architecture and intent. Use to understand design rationale; cross-check against actual code for completeness.

### 2.4 Validation Traces

**M-0212_act1_validation_minimax.json** (A-011) — **Historical evidence only**. JSON trace of act1 forward/reverse cases. Content duplicates the M-0255 report. No additional analytical value beyond the report version. Prefer M-0255 for human readability (with the authority caveat noted in section 2.1).

## 3. Cross-Cutting Patterns

### 3.1 Old workspace paths are the primary barrier to direct reuse

Every script in `code/index_builders/` uses `Path(__file__).resolve().parents[3]` to locate the workspace root and constructs paths like `workspace/script`, `output/store/gsea_anndata`, and `output/store/query_index`. These paths do not exist in the current project structure. Reports reference `workspace/report/` paths that are also historical.

### 3.2 Validation evidence hierarchy is clear but requires compliance

The T-007 source map and M-0239 latest reports index together define a clear priority chain:
1. T-007 module status matrix (A-002) → component maturity
2. T-007 validation evidence index (A-003) → reuse classification for each report
3. M-0239 latest reports index → valid report routing
4. M-0245 obsolete list → files to avoid

All evidence in this assessment follows this priority chain.

### 3.3 Deterministic path is stronger than LLM path

The forward matrix test (7/7 deterministic) is the strongest evidence. The LLM stability check (6/9) shows real-user-facing reliability is insufficient. The always_llm latency (167.3s) makes it impractical. The hybrid_fast mode (0.825s for 3 queries) is the most defensible default.

### 3.4 Index builders are needed but not all are urgent

Most migrated index JSONs (drug, gene, cellline) are present and ready. The critical gap is `function_index.json` — its builder (M-0373) needs priority porting.

### 3.5 Test coverage is good for forward query, sparse for reverse

The 7-case deterministic matrix, 12-question suite, and stability check all focus on forward resolution. Only act1 validation provides reverse query evidence. Reverse testing should be expanded in future development.

## 4. Summary Statistics

| Category | Validation Reports | Scripts | Source/Design | Traces | **Total** |
|---|---|---|---|---|---|
| direct reference | 8 | 0 | 2 | 0 | **10** |
| rewrite needed | 0 | 11 | 0 | 0 | **11** |
| historical evidence only | 33 | 4 | 0 | 1 | **38** |
| not usable | 6 | 0 | 0 | 0 | **6** |
| unknown | 0 | 0 | 0 | 0 | **0** |

### Total assets classified: 65

- Validation reports: 47 (of 57 total; 10 GSEA log err/out files excluded as not individually classified)
- Scripts: 15 (of 19 total; M-0363 is README)
- Source/design: 2 (resolver.py + design_docs)
- Validation traces: 1 (JSON trace)