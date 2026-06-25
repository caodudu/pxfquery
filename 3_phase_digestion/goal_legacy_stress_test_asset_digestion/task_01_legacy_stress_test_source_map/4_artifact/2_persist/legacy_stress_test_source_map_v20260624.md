# Legacy Stress Test Source Map

Generated: 2026-06-24
Task: T-055 01_legacy_stress_test_source_map

## 1. Scope and Approach

This source map catalogs migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. It covers all 7 high-priority directories in the flat asset library (`legacy_flat_asset_library_v20260614/`).

**Key constraints:**
- No legacy-root scanning (`/Users/dudu/Documents/3_Project/8_functional_query`)
- All scripts marked `runnable_claim: false` (not verified in current environment)
- Complements (does not duplicate) T-007 validation evidence index (15 entries)
- Missing/ambiguous leads explicitly documented

**Approach:** Each asset was inspected for content, stress-test relevance, and provenance. Assets are organized by stress-test relevance category with cross-references to the T-007 evidence index.

## 2. Categorized Inventory of Candidate Stress-Test Assets

### 2.1 Validation Scripts

These are Python scripts in `code/index_builders/` that directly validate resolver behavior, index correctness, or LLM stability. They are the strongest candidates for reuse in a current-project validation suite.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/index_builders/M-0387_test_resolver_smoke.py` | script | validation_script | Not in A-006 | Smoke test: resolver creation + direct forward/reverse query. Hardcoded legacy workspace paths. |
| `code/index_builders/M-0386_test_forward_matrix.py` | script | validation_script | V-005=V-006 | Deterministic 7/7 forward matrix test using mock hooks. Tests L1-L4 gene and drug hit levels. |
| `code/index_builders/M-0389_verify_resolver_cases.py` | script | validation_script | V-008 | Real LLM resolver verification (4 cases: exact genetic, disease context, drug query, drug generic). |
| `code/index_builders/M-0385_run_forward_question_suite.py` | script | validation_script | V-008,V-010,V-011 | Suite runner for 14 predefined forward questions. Supports --provider, --limit, --ids, --no-summary, --resolver-mode. |
| `code/index_builders/M-0388_validate_act1.py` | script | validation_script | V-007 | Act-1 real API validation (forward EGFR/A549 + reverse apoptosis/MYC/A549). |
| `code/index_builders/M-0377_check_llm_stability.py` | script | stability_check | V-009 | LLM stability check: 3 cases x 3 rounds via MiniMax API. |

### 2.2 Validation Reports

All 57 items in `reports/validation_reports/`. 15 are already indexed in T-007 (A-006). Below are the key categories:

**Resolver suite runs and matrix tests:**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0291_6_llm_resovler_forward_matrix.md` | report | validation_report | V-005 | Latest forward matrix test (7/7 pass, mock). Preferred over M-0257. |
| `reports/validation_reports/M-0257_6_llm_resovler_forward_matrix.md` | report | validation_report | V-006 | Older forward matrix test (7/7 pass). Superseded by M-0291. |
| `reports/validation_reports/M-0266_6_llm_resovler_forward_question_suite_minimax.md` | report | validation_report | V-008 | 12-question forward suite: mix of EXACT/PROXY_CELL/PROXY_PERT/NOT_FOUND. |
| `reports/validation_reports/M-0269_20260409_235852__6_llm_resovler_forward_question_suite_minimax.md` | report | validation_report | Not in A-006 | Timestamped duplicate of M-0266. |
| `reports/validation_reports/M-0275_20260410_110940__6_llm_resovler_forward_question_suite_minimax_quick3_fastv3.md` | report | validation_report | V-011 | hybrid_fast mode: 3 queries in 0.825s. Exact/proxy-cell found. Default demo candidate. |
| `reports/validation_reports/M-0277_20260410_113854__6_llm_resovler_forward_question_suite_minimax_llm_summary4_stats.md` | report | validation_report | V-010 | always_llm mode: 4 queries in 167.3s. Timing breakdown shows llm_parse_intent dominating (117s). |
| `reports/validation_reports/M-0276_20260410_112853__6_llm_resovler_forward_question_suite_minimax_llm_summary6.md` | report | validation_report | Not in A-006 | 6-question always_llm suite with summaries. Latency data. |
| `reports/validation_reports/M-0274_20260410_001641__6_llm_resovler_forward_question_suite_minimax_quick3_fastv2.md` | report | validation_report | Not in A-006 | hybrid_fast v2: 3 queries. Performance data point. |

**Act-1 validation:**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0255_6_llm_resovler_act1_validation_minimax.md` | report | validation_report | V-007 | Real API validation: forward EGFR/A549 EXACT, reverse apoptosis/MYC/A549 found candidates. Mixed authority per latest report index. |
| `reports/validation_reports/M-0258_6_llm_resovler_cellline_stepwise_demo.md` | report | validation_report | Not in A-006 | Cell line stepwise resolution demo. Proxy-cell logic walkthrough. |
| `reports/validation_reports/M-0259_6_llm_resovler_external_api_demo.md` | report | validation_report | Not in A-006 | External API (PubChem/Cellosaurus) demo report. |

**LLM stability and risk:**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0267_6_llm_resovler_llm_stability_check.md` | report | stability_check | V-009 | LLM stability: 6/9 success rate. EGFR inhibitor and NSCLC-like queries failed. |
| `reports/validation_reports/M-0243_known_risks.md` | report | known_risk | V-012 | 6 known risks: LLM stability, always-LLM latency, mode consistency, evidence explanation, asset organization, path drift. |
| `reports/validation_reports/M-0244_next_execution_order.md` | report | known_risk | V-013 | 5-step execution guidance. Read latest index first, run both modes, document NOT_FOUND/PROXY_*. |
| `reports/validation_reports/M-0245_obsolete_and_legacy_list.md` | report | known_risk | V-014 | Cleanup guidance for legacy report folders and compatibility paths. |

**Index build reports (validation of index construction):**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0246_2_cp_index.md` | report | validation_report | V-002 | Drug index build: exit 0, 6647 named drugs, 5314 PubChem SMILES hits. |
| `reports/validation_reports/M-0247_2_cp_index.log` | report | validation_report | Not in A-006 | Build log for drug index. |
| `reports/validation_reports/M-0248_3_gene_index.md` | report | validation_report | V-003 | Gene index build: 78061 full entries, 25036 simple. Biological sanity checks pass. |
| `reports/validation_reports/M-0249_3_gene_index_demo.log` | report | validation_report | Not in A-006 | Gene index demo log. |
| `reports/validation_reports/M-0250_3_gene_index.log` | report | validation_report | Not in A-006 | Gene index build log. |
| `reports/validation_reports/M-0252_5_function_index.md` | report | validation_report | V-004 | Function index build: 91 functions, 243 aliases, 11 lookup tests pass. |
| `reports/validation_reports/M-0253_5_function_index.log` | report | validation_report | Not in A-006 | Function index build log. |

**Suite run variants (same question suite, different modes):**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0260_6_llm_resovler_forward_question_suite_minimax_quick3_fastv2.md` | report | validation_report | Not in A-006 | hybrid_fast v2: 3 queries. |
| `reports/validation_reports/M-0261_6_llm_resovler_forward_question_suite_minimax_quick3.md` | report | validation_report | Not in A-006 | 3-question always_llm suite. |
| `reports/validation_reports/M-0262_6_llm_resovler_forward_question_suite_minimax_single_budgeted.md` | report | validation_report | Not in A-006 | Single budgeted query. |
| `reports/validation_reports/M-0263_6_llm_resovler_forward_question_suite_minimax_single_fastcheck.md` | report | validation_report | Not in A-006 | Single fast-check query. |
| `reports/validation_reports/M-0264_6_llm_resovler_forward_question_suite_minimax_single.md` | report | validation_report | Not in A-006 | Single always_llm query. |
| `reports/validation_reports/M-0265_6_llm_resovler_forward_question_suite_minimax_summary_check.md` | report | validation_report | Not in A-006 | Summary quality check. |
| `reports/validation_reports/M-0270_20260410_000136__6_llm_resovler_forward_question_suite_minimax_single.md` | report | validation_report | Not in A-006 | Timestamped single always_llm. |
| `reports/validation_reports/M-0271_20260410_000233__6_llm_resovler_forward_question_suite_minimax_single_fastcheck.md` | report | validation_report | Not in A-006 | Timestamped single fast-check. |
| `reports/validation_reports/M-0272_20260410_000531__6_llm_resovler_forward_question_suite_minimax_quick3.md` | report | validation_report | Not in A-006 | Timestamped 3-question always_llm. |
| `reports/validation_reports/M-0273_20260410_000631__6_llm_resovler_forward_question_suite_minimax_single_budgeted.md` | report | validation_report | Not in A-006 | Timestamped single budgeted. |

**Logger and development reports:**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0281_logger_capabilities_demo.md` | report | validation_report | Not in A-006 | Logger capabilities demo report. |
| `reports/validation_reports/M-0282_loggerdemo_01_normal_technical_2026-04-10.log` | report | validation_report | Not in A-006 | Logger demo output (normal technical). |
| `reports/validation_reports/M-0283_loggerdemo_02_quiet_minimal_2026-04-10.log` | report | validation_report | Not in A-006 | Logger demo output (quiet). |
| `reports/validation_reports/M-0284_loggerdemo_03_debug_with_io_2026-04-10.log` | report | validation_report | Not in A-006 | Logger demo output (debug with IO). |
| `reports/validation_reports/M-0285_loggerdemo_04_normal_human_2026-04-10.log` | report | validation_report | Not in A-006 | Logger demo output (human-readable). |
| `reports/validation_reports/M-0286_loggerdemo_05_live_llm_2026-04-10.log` | report | validation_report | Not in A-006 | Logger demo output (live LLM). |
| `reports/validation_reports/M-0290_todolist.md` | report | known_risk | V-015 | Resolver TODO: completed items (logger, caching, hybrid_fast, retry, suite archiving) and remaining work (consistency, explanation docs). |

**GSEA execution logs (in validation_reports/):**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0117_cp_gsea.err` | report | GSEA_evaluation | Not in A-006 | cp GSEA stderr (timing/errors). |
| `reports/validation_reports/M-0118_cp_gsea.out` | report | GSEA_evaluation | Not in A-006 | cp GSEA stdout. |
| `reports/validation_reports/M-0119_cp_umap.err` | report | GSEA_evaluation | Not in A-006 | cp UMAP stderr. |
| `reports/validation_reports/M-0121_sh_gsea.err` | report | GSEA_evaluation | Not in A-006 | sh GSEA stderr. 3.4MB. |
| `reports/validation_reports/M-0122_sh_gsea.out` | report | GSEA_evaluation | Not in A-006 | sh GSEA stdout. |
| `reports/validation_reports/M-0123_sh_umap.err` | report | GSEA_evaluation | Not in A-006 | sh UMAP stderr. |
| `reports/validation_reports/M-0125_xpr_gsea.err` | report | GSEA_evaluation | Not in A-006 | xpr GSEA stderr. 9.8MB. |
| `reports/validation_reports/M-0126_xpr_gsea.out` | report | GSEA_evaluation | Not in A-006 | xpr GSEA stdout. |
| `reports/validation_reports/M-0127_xpr_umap.err` | report | GSEA_evaluation | Not in A-006 | xpr UMAP stderr. |

**README and index files:**

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/validation_reports/M-0239_latest_reports_index.md` | report | known_risk | V-001 | Latest report authority index. Prioritize suite_runs/ and statistics-complete reports. |
| `reports/validation_reports/M-0240_log_files_index.md` | report | known_risk | Not in A-006 | Log files index. |
| `reports/validation_reports/M-0254_README.md` | report | known_risk | Not in A-006 | README for validation reports directory. |
| `reports/validation_reports/M-0278_README.md` | report | known_risk | Not in A-006 | README for suite run reports. |
| `reports/validation_reports/M-0279_README.md` | report | known_risk | Not in A-006 | README for resolver demo outputs. |
| `reports/validation_reports/M-0289_README.md` | report | known_risk | Not in A-006 | README for logger demo. |
| `reports/validation_reports/M-0292_README.md` | report | known_risk | Not in A-006 | README for stability check. |
| `reports/validation_reports/M-0293_README.md` | report | known_risk | Not in A-006 | README for run_forward_question_suite. |
| `reports/validation_reports/M-0042_latest_reports_index.md` | report | known_risk | Not in A-006 | Legacy report index (65 bytes, likely obsolete pointer). |

### 2.3 Resolver Pipeline Source

The resolver source code itself is a stress-test candidate because it implements the L1-L4 forward search policy and edge-case handling logic.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/pxfquery_package/query/resolver.py` | design_doc | resolver_edge_case | Not in A-006 (code) | Core resolver: L1 EXACT, L2 PROXY_PERT, L3 PROXY_CELL, L4 PROXY_BOTH. Contains edge-case handling for unknown cells, nonexistent genes, generic drug descriptions. 1072 lines. |
| `code/pxfquery_package/query/forward.py` | design_doc | resolver_edge_case | Not in A-006 (code) | ForwardQuery and ForwardResult. Used by all forward validation scripts. |
| `code/pxfquery_package/query/reverse.py` | design_doc | resolver_edge_case | Not in A-006 (code) | ReverseQuery and ReverseResult. Validated in Act-1 report only. |
| `code/pxfquery_package/query/__init__.py` | design_doc | resolver_edge_case | Not in A-006 (code) | Package init. |
| `code/pxfquery_package/query/__pycache__/` | data | resolver_edge_case | Not in A-006 (code) | Compiled bytecode cache (not meaningful as evidence). |

### 2.4 Query Indexes

Index files used by the resolver for query resolution. These are the runtime data that the resolver validates against.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `data/query_indexes/M-0202_cellline_index.json` | index | edge_case_input | Not in A-006 | Cell line index. Used by resolver for cell resolution. |
| `data/query_indexes/M-0203_cellline_neighbors.json` | index | edge_case_input | Not in A-006 | Cell line neighbors for proxy cell lookup. |
| `data/query_indexes/M-0204_drug_index.json` | index | edge_case_input | V-002 | Drug index: 5958 alias entries. |
| `data/query_indexes/M-0205_drug_neighbors.json` | index | edge_case_input | Not in A-006 | Drug neighbors: 5312 entries. 4.6MB. |
| `data/query_indexes/M-0207_gene_index_simple.json` | index | edge_case_input | Not in A-006 | Simplified gene index: 25036 entries. |
| `data/query_indexes/M-0208_gene_neighbors_simple.json` | index | edge_case_input | Not in A-006 | Simplified gene neighbors: 30319 entries. 20MB. |
| `data/query_indexes/M-0209_cellline_tree.json` | index | edge_case_input | Not in A-006 | Cell line tree with hierarchy metadata. |
| `data/query_indexes/M-0210_gene_index.json` | index | edge_case_input | V-003 | Full gene index: 78061 entries. 6.4MB. |
| `data/query_indexes/M-0211_gene_neighbors.json` | index | edge_case_input | Not in A-006 | Full gene neighbors. 23MB. |

**Notable gap:** No `function_index.json` was found in the migrated query indexes. V-004 flags this as a known gap. The function index must be rebuilt from `M-0373_build_function_index.py` or recovered from the legacy root.

### 2.5 GSEA Evaluation Scripts and Analysis Scripts

These scripts in `code/analysis_scripts/` perform GSEA evaluation (the core functional scoring that the resolver queries). They are stress-test candidates because they validate the functional matrix pipeline.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/analysis_scripts/M-0137_cp_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | Compound perturbation GSEA evaluation. HPC paths hardcoded. Requires scanpy/gseapy. |
| `code/analysis_scripts/M-0138_cp_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job script for cp GSEA. HPC-specific. |
| `code/analysis_scripts/M-0139_sh_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | shRNA GSEA evaluation. HPC paths. |
| `code/analysis_scripts/M-0140_sh_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job for sh GSEA. |
| `code/analysis_scripts/M-0141_xpr_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | Expression (overexpression) GSEA evaluation. |
| `code/analysis_scripts/M-0142_xpr_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job for xpr GSEA. |
| `code/analysis_scripts/M-0143_cp_umap.py` | script | GSEA_evaluation | Not in A-006 | cp UMAP embedding generation. HPC paths. |
| `code/analysis_scripts/M-0144_cp_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job for cp UMAP. |
| `code/analysis_scripts/M-0145_sh_umap.py` | script | GSEA_evaluation | Not in A-006 | sh UMAP embedding. |
| `code/analysis_scripts/M-0146_sh_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job for sh UMAP. |
| `code/analysis_scripts/M-0147_xpr_umap.py` | script | GSEA_evaluation | Not in A-006 | xpr UMAP embedding. |
| `code/analysis_scripts/M-0148_xpr_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job for xpr UMAP. |
| `code/analysis_scripts/M-0351_cp_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0137 (archive/restructure version). Same HPC paths. |
| `code/analysis_scripts/M-0352_cp_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0353_sh_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0139. |
| `code/analysis_scripts/M-0354_sh_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0355_xpr_gsea_eval.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0141. |
| `code/analysis_scripts/M-0356_xpr_gsea_eval.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0357_cp_umap.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0143. |
| `code/analysis_scripts/M-0358_cp_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0359_sh_umap.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0145. |
| `code/analysis_scripts/M-0360_sh_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0361_xpr_umap.py` | script | GSEA_evaluation | Not in A-006 | Duplicate of M-0147. |
| `code/analysis_scripts/M-0362_xpr_umap.sh` | script | GSEA_evaluation | Not in A-006 | SLURM job duplicate. |
| `code/analysis_scripts/M-0062_1_statistic.ipynb` | script | GSEA_evaluation | Not in A-006 | Jupyter notebook (159KB). Data statistics. |
| `code/analysis_scripts/M-0131_2_dataset.ipynb` | script | GSEA_evaluation | Not in A-006 | Dataset exploration notebook (400KB). |
| `code/analysis_scripts/M-0132_3_genesets.ipynb` | script | GSEA_evaluation | Not in A-006 | Gene set analysis notebook (1.8MB). |
| `code/analysis_scripts/M-0134_5_beam_search.ipynb` | script | GSEA_evaluation | Not in A-006 | Beam search notebook (23KB). |
| `code/analysis_scripts/M-0135_6_forward_example.ipynb` | script | GSEA_evaluation | Not in A-006 | Forward query example notebook. |
| `code/analysis_scripts/M-0136_7_reverse_example.ipynb` | script | GSEA_evaluation | Not in A-006 | Reverse query example notebook. |
| Additional M-0130 design notebook, M-0133 LLM notebook, M-0298 main.py, M-0302 check_link.py | script | GSEA_evaluation | Not in A-006 | Ancillary analysis scripts. |

### 2.6 GSEA Result Tables

Large CSV files in `results/gsea_tables/` used as validation baselines for the resolver.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `results/gsea_tables/M-0114_cp_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | cp GSEA top 100 terms. 372MB symlink placeholder. |
| `results/gsea_tables/M-0115_sh_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | sh GSEA top 100 terms. 349MB symlink placeholder. |
| `results/gsea_tables/M-0116_xpr_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | xpr GSEA top 100 terms. 244MB symlink placeholder. |
| `results/gsea_tables/M-0236_cp_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | cp GSEA top 100 terms duplicate. 372MB symlink. |
| `results/gsea_tables/M-0237_sh_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | sh GSEA top 100 terms duplicate. 349MB symlink. |
| `results/gsea_tables/M-0238_xpr_gsea_100terms.csv` | result | GSEA_evaluation | Not in A-006 | xpr GSEA top 100 terms duplicate. 244MB symlink. |

### 2.7 Index Builder Scripts (non-test)

These scripts build the indexes that the resolver depends on. They are relevant as validation baselines and rebuild candidates.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/index_builders/M-0365_build_drug_index.py` | script | validation_script | V-002 | Drug index builder. 13.6KB. Builds drug_index.json and drug_neighbors.json. |
| `code/index_builders/M-0367_build_gene_index.py` | script | validation_script | V-003 | Gene index builder. 19.5KB. Builds gene_index.json and gene_neighbors.json. |
| `code/index_builders/M-0372_build_cellline_tree.py` | script | validation_script | Not in A-006 | Cell line tree builder. 5.1KB. |
| `code/index_builders/M-0370_build_cellline_index.py` | script | validation_script | Not in A-006 | Cell line index builder. 7.8KB. |
| `code/index_builders/M-0369_build_cellline_enrich.py` | script | validation_script | Not in A-006 | Cell line enrichment builder. 5.6KB. |
| `code/index_builders/M-0373_build_function_index.py` | script | validation_script | V-004 | Function index builder. 12.8KB. Can rebuild the missing function_index.json. |
| `code/index_builders/M-0363_1_install.md` | design_doc | validation_script | Not in A-006 | Install instructions for index builders. |

### 2.8 Demo Scripts

These demo scripts exercise the resolver with real LLM calls and demonstrate edge-case handling.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/index_builders/M-0381_demo_resolver.py` | script | complex_query | Not in A-006 | Simple resolver demo with --query arg. Uses legacy workspace paths. |
| `code/index_builders/M-0378_demo_cellline_stepwise.py` | script | complex_query | Not in A-006 | Cell line stepwise resolution demo. 4.6KB. |
| `code/index_builders/M-0379_demo_external_apis.py` | script | complex_query | Not in A-006 | PubChem/Cellosaurus API demo. 3.4KB. |
| `code/index_builders/M-0380_demo_logger_capabilities.py` | script | complex_query | Not in A-006 | Logger capabilities demo. 9.9KB. |
| `code/index_builders/M-0383_Resolver_Forward_Demo_Clean.ipynb` | script | complex_query | Not in A-006 | Jupyter notebook: clean forward resolver demo. |
| `code/index_builders/M-0384_Resolver_Workbench.ipynb` | script | complex_query | Not in A-006 | Jupyter notebook: resolver workbench for block-by-block validation. |

### 2.9 Digested Context Reports

Reports in `reports/digested_context/` that may mention validation outcomes. These are mostly navigation/context cards from the legacy workspace.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `reports/digested_context/M-0038_20_data_and_indexes.md` | report | known_risk | Not in A-006 | Context card: data and indexes (107 bytes, minimal content). |
| `reports/digested_context/M-0040_40_reports_and_evidence.md` | report | known_risk | Not in A-006 | Context card: reports and evidence (82 bytes, minimal). |
| `reports/digested_context/M-0041_50_risks_and_actions.md` | report | known_risk | Not in A-006 | Context card: risks and actions (81 bytes, minimal). |
| `reports/digested_context/M-0157_docs_map.md` | report | known_risk | Not in A-006 | Docs map for navigation. |
| `reports/digested_context/M-0176_INDEX.md` | report | known_risk | Not in A-006 | Legacy workspace index (L0/L1/L2 hierarchy). |
| `reports/digested_context/M-0178_20_data_and_indexes.md` | report | known_risk | Not in A-006 | Expanded data and indexes context. |
| `reports/digested_context/M-0180_40_reports_and_evidence.md` | report | known_risk | Not in A-006 | Expanded reports and evidence context. |
| `reports/digested_context/M-0181_50_risks_and_actions.md` | report | known_risk | Not in A-006 | Expanded risks and actions context. |
| `reports/digested_context/M-0183_project_audit.md` | report | known_risk | Not in A-006 | Project audit checklist. |

### 2.10 Background and Tutorial Scripts (in analysis_scripts/)

These are tutorial/learning scripts, less directly stress-test relevant but included for completeness.

| Migrated Path | Type | Relevance | T-007 Cross-Ref | Notes |
|---|---|---|---|---|
| `code/analysis_scripts/M-0065_1.1_local_ollama.md` | report | performance | Not in A-006 | Local Ollama setup doc (empty). |
| `code/analysis_scripts/M-0066_1.2_openai.md` | report | performance | Not in A-006 | OpenAI usage notes (23KB). |
| `code/analysis_scripts/M-0067_1.3_lietllm.md` | report | performance | Not in A-006 | LiteLLM usage (2KB). |
| `code/analysis_scripts/M-0068_2.1_internet.md` | report | performance | Not in A-006 | Internet access notes. |
| `code/analysis_scripts/M-0069_2.2_api.md` | report | performance | Not in A-006 | API usage notes. |
| `code/analysis_scripts/M-0070_2.3_MCP.md` | report | performance | Not in A-006 | MCP protocol notes (25KB). |
| `code/analysis_scripts/M-0071_2.4_MCP_important.md` | report | performance | Not in A-006 | MCP important notes (15KB). |
| `code/analysis_scripts/M-0072_3.1_single_langchain.md` | report | performance | Not in A-006 | LangChain notes (28KB). |
| `code/analysis_scripts/M-0073_3.2_openai_sdk.md` | report | performance | Not in A-006 | OpenAI SDK notes. |
| `code/analysis_scripts/M-0074_3.3_CrewAI.md` | report | performance | Not in A-006 | CrewAI notes. |
| `code/analysis_scripts/M-0075_3.4_AutoGen.md` | report | performance | Not in A-006 | AutoGen notes (empty). |
| `code/analysis_scripts/M-0076_4.1_opencode.md` | report | performance | Not in A-006 | OpenCode notes (14KB). |
| `code/analysis_scripts/M-0079_5.1.2_rag.md` | report | performance | Not in A-006 | RAG notes. |
| `code/analysis_scripts/M-0130_1_design.ipynb` | script | GSEA_evaluation | Not in A-006 | Design notebook. |
| `code/analysis_scripts/M-0133_4_llm.ipynb` | script | GSEA_evaluation | Not in A-006 | LLM notebook. |
| `code/analysis_scripts/M-0295___init__.py` | script | GSEA_evaluation | Not in A-006 | Package init. |
| `code/analysis_scripts/M-0298_main.py` | script | GSEA_evaluation | Not in A-006 | Old main.py with pxfquery class (legacy). |
| `code/analysis_scripts/M-0302_check_link.py` | script | GSEA_evaluation | Not in A-006 | Link checker utility. |
| `code/analysis_scripts/M-0344_1_design.ipynb` | script | GSEA_evaluation | Not in A-006 | Design notebook duplicate. |
| `code/analysis_scripts/M-0345_2_dataset.ipynb` | script | GSEA_evaluation | Not in A-006 | Dataset notebook duplicate. |
| `code/analysis_scripts/M-0346_3_genesets.ipynb` | script | GSEA_evaluation | Not in A-006 | Gene sets notebook duplicate. |
| `code/analysis_scripts/M-0347_4_llm.ipynb` | script | GSEA_evaluation | Not in A-006 | LLM notebook duplicate. |
| `code/analysis_scripts/M-0348_5_beam_search.ipynb` | script | GSEA_evaluation | Not in A-006 | Beam search notebook duplicate. |
| `code/analysis_scripts/M-0349_6_forward_example.ipynb` | script | GSEA_evaluation | Not in A-006 | Forward example notebook duplicate. |
| `code/analysis_scripts/M-0350_7_reverse_example.ipynb` | script | GSEA_evaluation | Not in A-006 | Reverse example notebook duplicate. |

## 3. Cross-Reference to T-007 Validation Evidence Index

The T-007 validation evidence index (A-006) contains 15 entries covering validation reports. This source map complements those entries by:

1. **Covering scripts, indexes, and source code** not in T-007: All validation scripts in `code/index_builders/`, all query indexes in `data/query_indexes/`, resolver pipeline source, GSEA evaluation scripts, and demo scripts.

2. **Covering validation reports not in T-007**: The T-007 index focused on canonical entries (15 total). This map adds ~30 additional validation reports (suite run variants, build logs, README files, logger demos) that may be useful for traceability.

3. **Covering GSEA evaluation materials**: All GSEA eval scripts and result tables (not covered by T-007 at all).

4. **Covering index builder scripts**: Build scripts for drug/gene/cellline/function indexes that T-007 does not catalog.

**Overlap with T-007 (15 entries):**

| T-007 ID | This Map Section | Notes |
|---|---|---|
| V-001 (M-0239 latest_reports_index) | 2.2 | Both reference as report authority guide |
| V-002 (M-0246 cp_index build) | 2.2 + 2.7 | V-002 covers report; map adds build script link |
| V-003 (M-0248 gene_index build) | 2.2 + 2.7 | Same pattern: report + builder script |
| V-004 (M-0252 function_index build) | 2.2 + 2.7 | Map flags missing function_index.json gap |
| V-005 (M-0291 forward_matrix) | 2.2 | Both reference; map adds context about supersession |
| V-006 (M-0257 forward_matrix) | 2.2 | Marked as superseded by V-005 |
| V-007 (M-0255 act1_validation) | 2.2 | Mixed authority noted in both |
| V-008 (M-0266 forward_suite) | 2.2 | Both reference 12-question suite results |
| V-009 (M-0267 llm_stability) | 2.2 + 2.1 | V-009 covers report; map adds check_llm_stability.py script |
| V-010 (M-0277 llm_summary4_stats) | 2.2 | Both reference timing data |
| V-011 (M-0275 hybrid_fast_v3) | 2.2 | Both reference hybrid_fast results |
| V-012 (M-0243 known_risks) | 2.2 | Both reference risk list |
| V-013 (M-0244 next_execution_order) | 2.2 | Both reference execution guidance |
| V-014 (M-0245 obsolete_list) | 2.2 | Both reference cleanup guidance |
| V-015 (M-0290 todolist) | 2.2 | Both reference resolver TODO |

## 4. Missing or Ambiguous Leads

The following items are identified as gaps or ambiguities in the source map:

1. **Missing `function_index.json`**: The function index runtime file is absent from `data/query_indexes/`. The build report (M-0252) confirms a 91-function index was built, and `M-0373_build_function_index.py` exists to rebuild it, but no runtime JSON was found in the migrated flat library. This is a systematic migration gap for the function index runtime asset.

2. **Duplicate script pairs**: The `code/analysis_scripts/` directory contains two complete sets of GSEA eval scripts and notebooks (M-013x series and M-034x/035x series). They appear to be copies from different legacy workspace versions. The M-013x series is preferred (pre-restructure originals); the M-034x/035x series are archive copies.

3. **Legacy log file size**: Several GSEA err files are large (M-0121_sh_gsea.err: 3.4MB, M-0125_xpr_gsea.err: 9.8MB). Their content is execution diagnostics, not structured test results. A later task may want to parse them for timing or error patterns.

4. **GSEA tables as symlinks**: The 6 GSEA table CSVs in `results/gsea_tables/` are large file symlink placeholders (244-372MB each). They are not directly readable without resolving the symlink target. Their actual content should be verified before use as validation baselines.

5. **`function_index.json` not found**: V-004 in T-007 flags this as a known asset gap. Confirmed by this map. The function index is referenced by `FunctionIndex` class in the resolver but the runtime JSON is missing.

6. **Ambiguous script origins**: The GSEA eval scripts reference HPC paths (`/public/home/caojun/project/RUSH/`). These scripts were designed for SLURM cluster execution with specific environment assumptions. Their utility in the current macOS environment is limited without significant path and dependency adaptation.

7. **Suite run variant proliferation**: Multiple timestamped variants of the same forward question suite exist (M-0266 baseline + 6 timestamped duplicates in validation_reports/). A later reconciliation task should determine which variants contain unique results vs. exact duplicates.

8. **Old `main.py` (M-0298 in analysis_scripts/)**: Contains a legacy `pxfquery` class with many `pass` methods. Listed in T-007 gap #5 as conflicting with modern package entry. This file is historical and should not be used for validation.

## 5. Guidance for Later Tasks

### How to use this source map

1. **Validation suite design**: Start with the 6 validation scripts in `code/index_builders/` (section 2.1). Copy them into a current development task, update workspace paths, and run in the current environment with `mock` provider first.

2. **Baseline comparison**: Use the deterministic forward matrix test (M-0386) as the primary regression test. The expected 7/7 pass rate across all hit levels (EXACT, PROXY_PERT, PROXY_CELL, PROXY_BOTH) provides the strongest validation baseline.

3. **LLM stability risks**: Reference M-0377 (`check_llm_stability.py`) and M-0267 (stability report) to design LLM acceptance criteria. The 6/9 success rate should drive conservative LLM claims.

4. **Performance characterization**: Use M-0277 (timing stats) and M-0275 (hybrid_fast v3) to set performance expectations. Always-LLM mode is ~200x slower than hybrid_fast.

5. **Index gaps**: The missing `function_index.json` must be rebuilt or recovered before full resolver validation. Use M-0373_build_function_index.py in the flat library.

6. **GSEA baseline**: The 6 GSEA CSV tables in `results/gsea_tables/` can serve as validation baselines for resolver output, but they are large symlinks that need resolution first.

7. **T-007 complements**: This source map covers material outside T-007 scope. When designing validation tasks, reference both this map (for scripts/indexes/GSEA) and T-007 evidence index (for curated validation reports).

### Caveats

- All scripts contain legacy workspace path assumptions. Do not run in-place. Port into a current development task.
- The `function_index.json` gap is the most critical missing runtime asset.
- GSEA eval scripts have HPC-specific dependencies (SLURM, scanpy, gseapy). Local macOS equivalents may need different tooling.
- Suite run variants require deduplication before use as evidence.
