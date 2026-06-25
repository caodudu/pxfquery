# Stress Test Development Handoff Pack

Generated: 2026-06-24
Task: T-058 04_stress_test_development_handoff_pack
Phase: Digestion

This handoff pack integrates the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a structured bridge from the stress-test digestion goal to a future stress-test milestone in the development phase. It cross-references T-007 to align with current development state understanding.

---

## Section 1: Summary of Consolidated Digestion Findings

The three predecessor tasks collectively establish:

### What exists (from T-055)

Approximately 160 stress-test candidate assets across 7 directories in the flat asset library, spanning 10 categories:

| # | Category | Count | Key Assets |
|---|---|---|---|
| 1 | Validation scripts | 6 | M-0386 (7/7 matrix), M-0385 (14-question suite), M-0377 (stability check) |
| 2 | Validation reports | 57 | M-0291 (latest matrix), M-0275 (hybrid_fast), M-0277 (always_llm stats), M-0267 (stability 6/9) |
| 3 | Resolver pipeline source | 4 | resolver.py (1072 lines, L1-L4 policy), forward.py, reverse.py |
| 4 | Query indexes | 10 | drug_index (5958 entries), gene_index (78061 entries), cellline_index, neighbors |
| 5 | GSEA evaluation scripts | 24 | cp/sh/xpr GSEA eval + UMAP, plus 12 archive duplicates |
| 6 | GSEA result tables | 6 | cp/sh/xpr top 100 terms CSVs (244-372MB symlink placeholders each) |
| 7 | Index builder scripts | 7 | drug, gene, cellline (x3), function (M-0373) |
| 8 | Demo scripts | 6 | resolver demo, cellline stepwise, external APIs, logger, 2 Jupyter notebooks |
| 9 | Digested context reports | 9 | navigation cards, docs map, audit checklist (mostly minimal content) |
| 10 | Background/tutorial notes | 23 | LLM/SDK usage notes in analysis_scripts/ (not stress-test relevant) |

**8 documented gaps/missing leads from T-055:**
- GAP-1: function_index.json missing from migrated query indexes (critical)
- GAP-2: Duplicate script pairs in code/analysis_scripts/ (M-013x vs M-035x series)
- GAP-3: Large GSEA err files (M-0121: 3.4MB, M-0125: 9.8MB)
- GAP-4: GSEA table symlinks require resolution before use
- GAP-5: function_index.json confirmed absent (same as GAP-1, repeated)
- GAP-6: GSEA scripts have HPC path and SLURM assumptions
- GAP-7: Suite run variant proliferation (6+ timestamped duplicates of same suite)
- GAP-8: Obsolete main.py (M-0298) conflicting with modern package entry

### What to test (from T-056)

29 stress-test scenarios were derived across 9 query dimensions, all grounded in T-007 evidence:

| Dimension | Scenarios | Risk Profile |
|---|---|---|
| Complex queries (SC-001 to 003) | Multi-gene, multi-function, combined drug+gene | 3/3 marked FAIL (risk) |
| Strict queries (SC-004 to 006) | Exact gene, exact drug, strict reverse no-proxy | 3/3 marked PASS |
| Boundary queries (SC-007 to 010) | Unknown cell, fake drug, empty input, typo cell | 2 PASS, 1 FAIL, 1 PASS (all boundary-tested) |
| No-hit behavior (SC-011 to 013) | Generic drug desc, free-text context, impossible combo | 2 ambiguous (PASS/FAIL), 1 PASS |
| Overly broad results (SC-014 to 016) | Vehicle control, pan-cancer, common drug | 3/3 marked BORDERLINE |
| Proxy/exact matching (SC-017 to 020) | Exact gene, proxy cell, proxy both, proxy pert | 4/4 marked PASS |
| Difficult combos (SC-021 to 023) | Drug resistance, multi-drug multi-context, missing function | 1 BORDERLINE, 1 FAIL, 1 PASS |
| LLM mode cross-checks (SC-024 to 026) | Generic divergence, latency stress, mode consistency | 1 INCONSISTENT, 1 LATENCY, 1 PASS |
| Missing/partial index (SC-027 to 029) | Missing function_index, drug zero-neighbor, cell no-neighbor | 1 FAIL, 1 PASS, 1 BORDERLINE |

**Scenario risk summary:** 12/29 marked PASS, 6 marked FAIL (risk), 5 marked BORDERLINE, 4 ambiguous, 1 INCONSISTENT, 1 LATENCY_ISSUE. The risk-bearing scenarios cluster in complex queries, LLM mode cross-checks, and index gaps.

### What is reusable (from T-057)

65 assets were classified across 4 reuse categories:

| Reuse Decision | Count | Composition |
|---|---|---|
| Direct reference | 10 | 8 validation reports (M-0239, M-0291, M-0275, M-0267, M-0243, M-0244, M-0245, M-0290), 1 code base (resolver.py + design_docs), 1 trace (M-0212 JSON) |
| Rewrite needed | 11 | 8 test/verify scripts (M-0386, M-0387, M-0389, M-0385, M-0388, M-0377, M-0381), 1 index builder (M-0373 function_index, HIGH PRIORITY), 2 Jupyter notebooks (M-0383, M-0384) |
| Historical evidence only | 38 | 33 validation reports (superseded suites, READMEs, logs, legacy index builders), 4 demo scripts, 1 trace (M-0212 duplicate) |
| Not usable | 6 | 6 GSEA log files (M-0117-M-0127, err/out artifacts with zero analytical value) |

**Key reuse boundary findings:**
- The deterministic forward matrix test (M-0386, 7/7 pass) is the single strongest piece of validation evidence.
- hybrid_fast mode (0.825s/3 queries) is the defensible default; always_llm (167.3s/4 queries, 6/9 stability) is not manuscript-ready.
- Old workspace paths are the primary barrier: every script uses `Path(__file__).resolve().parents[3]` conventions.
- Validation evidence hierarchy is clear (M-0239 as report authority) but requires compliance.
- Forward query test coverage is good; reverse query sparse (only Act-1 provides reverse evidence).
- function_index.json is the critical missing runtime asset; M-0373 is the only rebuild path.

---

## Section 2: Asset-to-Scenario Cross-Walk

This section maps source assets (from T-055 and T-057) to the stress-test scenarios they support (from T-056).

### Validation Scripts

| Asset | Category | T-057 Decision | Supports Scenarios | Notes |
|---|---|---|---|---|
| M-0386 test_forward_matrix.py | validation_script | rewrite needed | SC-004, SC-005, SC-017, SC-018, SC-019, SC-020, SC-026 | 7-case deterministic matrix; covers all hit levels; primary regression test |
| M-0387 test_resolver_smoke.py | validation_script | rewrite needed | SC-004, SC-005, SC-017 | Minimal smoke test; creation + forward/reverse |
| M-0389 verify_resolver_cases.py | validation_script | rewrite needed | SC-004, SC-011, SC-024 | Real LLM 4-case verification; flexible hit-level expectations |
| M-0385 run_forward_question_suite.py | validation_script | rewrite needed | SC-004, SC-005, SC-011, SC-024, SC-025, SC-026 | 14-question suite; dual-mode support; timing diagnostics |
| M-0388 validate_act1.py | validation_script | rewrite needed | SC-002, SC-006, SC-017 | Act-1 forward/reverse; reverse query validation example |
| M-0377 check_llm_stability.py | validation_script | rewrite needed | SC-011, SC-012, SC-024 | 3-case/3-round stability checker |

### Direct-Reference Reports

| Asset | Category | T-057 Decision | Supports Scenarios | Notes |
|---|---|---|---|---|
| M-0239 latest_reports_index.md | known_risk | direct reference | All scenarios | Report routing authority; navigate validation evidence |
| M-0291 forward_matrix.md | validation_report | direct reference | SC-004, SC-005, SC-017–SC-020 | 7/7 deterministic pass; strongest validation evidence |
| M-0275 hybrid_fast_v3.md | validation_report | direct reference | SC-004, SC-005, SC-026 | 0.825s/3 queries; primary performance reference |
| M-0277 always_llm_stats.md | validation_report | historical evidence only | SC-011, SC-024, SC-025 | 167.3s/4 queries latency evidence; NOT_FOUND for generic drugs |
| M-0267 llm_stability.md | validation_report | direct reference | SC-011, SC-012, SC-024 | 6/9 success rate; critical risk evidence |
| M-0243 known_risks.md | validation_report | direct reference | All risk-bearing scenarios | 6 known risks as development acceptance criteria |
| M-0244 next_execution_order.md | validation_report | direct reference | SC-004–SC-006, SC-017–SC-020 | 5-step reproducible validation workflow |
| M-0290 todolist.md | validation_report | direct reference | All scenarios | Resolver TODO: completed vs remaining items |

### Query Indexes

| Asset | Category | T-057 Decision | Supports Scenarios | Notes |
|---|---|---|---|---|
| drug_index.json + neighbors | edge_case_input | N/A (runtime data) | SC-005, SC-008, SC-016, SC-020, SC-028 | 5958 aliases, 5312 neighbors; 2 drugs have 0 neighbors |
| gene_index.json + neighbors | edge_case_input | N/A (runtime data) | SC-001, SC-004, SC-017, SC-019 | 78061 full entries, 33791 neighbors |
| cellline_index.json + neighbors + tree | edge_case_input | N/A (runtime data) | SC-007, SC-010, SC-015, SC-018, SC-029 | Cell line resolution; neighbor coverage unknown at boundaries |
| function_index.json | edge_case_input | N/A (runtime data, MISSING) | SC-002, SC-006, SC-023, SC-027 | 91 functions in report; runtime JSON absent |

### GSEA Evaluation Materials

| Asset | Category | T-057 Decision | Supports Scenarios | Notes |
|---|---|---|---|---|
| GSEA eval scripts (M-013x series) | GSEA_evaluation | historical evidence only | SC-001–SC-003 (pipeline validation context) | HPC-specific; use as methodology reference only |
| GSEA tables (M-0114–M-0116) | GSEA_evaluation | N/A (result data) | All forward scenarios (baseline data) | 244-372MB symlink placeholders; resolve before use |
| Index builder scripts (M-0365–M-0373) | validation_script | rewrite needed (M-0373 HIGH PRIORITY) | SC-027, SC-028, SC-029 | M-0373 is only rebuild path for function_index.json |

---

## Section 3: Reuse-Ready Assets

The following 10 assets are classified as "direct reference" by T-057. They are valid, current, and usable without modification.

### 1. M-0239 latest_reports_index.md
**Path:** reports/validation_reports/M-0239_latest_reports_index.md
**Reuse value:** Defines report routing priority. Suite_runs/ reports with complete statistics take priority. Act-1 auth-failure path marked as non-valid basis. Essential entry point for navigating the 57-report corpus.
**Risk:** None — validated by T-007.
**Action:** Use as the entry point for all future validation-reading tasks.

### 2. M-0291 forward_matrix.md
**Path:** reports/validation_reports/M-0291_6_llm_resovler_forward_matrix.md
**Reuse value:** Deterministic mock-based resolver matrix test. 7/7 pass across EXACT, PROXY_PERT, PROXY_CELL, PROXY_BOTH, exact drug, proxy drug. Single strongest validation evidence in the entire corpus.
**Risk:** None — validated by T-007 as strongest resolver hit-level evidence.
**Action:** Reference for deterministic forward resolver behavior; supersedes M-0257.

### 3. M-0275 hybrid_fast_v3.md
**Path:** reports/validation_reports/M-0275_20260410_110940__6_llm_resovler_forward_question_suite_minimax_quick3_fastv3.md
**Reuse value:** 0.825s suite time for 3 queries with hybrid_fast/no-summary. All 3 found (EXACT + 2 PROXY_CELL). Best evidence for hybrid_fast viability.
**Risk:** None — best evidence for hybrid_fast viability.
**Action:** Use as primary performance reference for hybrid_fast mode.

### 4. M-0267 llm_stability_check.md
**Path:** reports/validation_reports/M-0267_6_llm_resovler_llm_stability_check.md
**Reuse value:** 6/9 success rate across 3 rounds with MiniMax-M2.7. Critical risk evidence for LLM mode decisions.
**Risk:** LLM stability is a known high-priority gap.
**Action:** Carry as acceptance-criteria evidence for LLM mode claims.

### 5. M-0243 known_risks.md
**Path:** reports/validation_reports/M-0243_known_risks.md
**Reuse value:** 6 documented risks: LLM stability, always-llm latency, mode consistency, evidence explanation, asset organization, path drift.
**Risk:** None — risk list is self-contained.
**Action:** Convert directly into development acceptance criteria.

### 6. M-0244 next_execution_order.md
**Path:** reports/validation_reports/M-0244_next_execution_order.md
**Reuse value:** 5-step reproducible validation workflow: read latest index, run both modes, document NOT_FOUND/PROXY_*.
**Risk:** None — process evidence only.
**Action:** Adapt for future validation task design.

### 7. M-0245 obsolete_and_legacy_list.md
**Path:** reports/validation_reports/M-0245_obsolete_and_legacy_list.md
**Reuse value:** Inventory of files to avoid re-reading or citing.
**Risk:** None — cleanup guidance only.
**Action:** Use to avoid duplicate-report confusion in future tasks.

### 8. M-0290 todolist.md
**Path:** reports/validation_reports/M-0290_todolist.md
**Reuse value:** Detailed resolver TODO: completed (logger, caching, hybrid_fast, retry, suite archiving), remaining (consistency regression, explanation docs).
**Risk:** None — handoff evidence.
**Action:** Use as handoff reference for next development phase priorities.

### 9. resolver.py + design_docs
**Path:** code/pxfquery_package/query/resolver.py
**Reuse value:** Core resolver pipeline (1072 lines): L1-L4 forward search policy, proxy evidence, genetic multi-source, budget-based collection, fast-path + LLM-path dual-mode architecture. Canonical implementation reference.
**Risk:** function_index.json runtime dependency missing; old log_dir path.
**Action:** Use as canonical resolver implementation reference for all future test design.

### 10. M-0252 function_index build report
**Path:** reports/validation_reports/M-0252_5_function_index.md
**Reuse value:** Documents 91 functions, 243 aliases, 11 lookup tests passed. Spec for rebuilding the missing function_index.json.
**Risk:** Runtime function_index.json is missing from migrated assets.
**Action:** Use to guide function index rebuild (with M-0373 builder script).

---

## Section 4: Rewrite-Required Assets and Risk Profile

11 assets classified as "rewrite needed" by T-057. All reference old workspace paths that prevent immediate use but contain valuable core logic.

### High-Priority Rewrite Candidates

**1. M-0386 test_forward_matrix.py**
- **Path:** code/index_builders/M-0386_test_forward_matrix.py
- **Core value:** 7-case deterministic mock test covering all hit levels (EXACT through PROXY_BOTH). Mock hook pattern is the right approach for isolation.
- **Rewrite barriers:** Old workspace paths via `Path(__file__).resolve().parents[3]`; accesses internal engine attributes (`_obs`, `_neighbors_raw`) that may change.
- **Risk profile:** LOW. Core logic is sound and deterministic; path updates are mechanical.
- **Priority:** First script to port after resolver package migration.

**2. M-0385 run_forward_question_suite.py**
- **Path:** code/index_builders/M-0385_run_forward_question_suite.py
- **Core value:** 14-question bank with dual-mode support (always_llm/hybrid_fast), timing diagnostics, output archiving.
- **Rewrite barriers:** Old output paths to `workspace/report/6_llm_resovler_suite_runs`; depends on old PxFquery package structure.
- **Risk profile:** LOW-MEDIUM. Question bank is valuable; mode switching needs verification in current environment.
- **Priority:** Port after M-0386; use hybrid_fast as default.

**3. M-0373 build_function_index.py — HIGH PRIORITY**
- **Path:** code/index_builders/M-0373_build_function_index.py
- **Core value:** Only path to restore missing function_index.json. Builds from functional matrix h5ad var_names.
- **Rewrite barriers:** Old workspace paths (`WORKSPACE=parent.parents[3]`); references `output/store/gsea_anndata/xpr_func_ad.h5ad`.
- **Risk profile:** HIGH. function_index.json is the most critical missing runtime asset. Without it, reverse query may fail, and function-mapped scenarios (SC-002, SC-006, SC-023, SC-027) cannot be validated.
- **Priority:** Port before any reverse-query validation work.

**4. M-0387 test_resolver_smoke.py**
- **Path:** code/index_builders/M-0387_test_resolver_smoke.py
- **Core value:** Minimal smoke test (resolver creation + forward/reverse query).
- **Rewrite barriers:** Old workspace paths; uses real LLM provider with no mock option.
- **Risk profile:** LOW. Simple pattern; mock provider substitution is straightforward.
- **Priority:** Port as minimal import/run check after package setup.

### Medium-Priority Rewrite Candidates

**5. M-0389 verify_resolver_cases.py**
- **Path:** code/index_builders/M-0389_verify_resolver_cases.py
- **Core value:** 4-case real LLM verification with pert_type/hit expectations.
- **Rewrite barriers:** Old paths; uses always_llm mode (not hybrid_fast); no output archiving.
- **Risk profile:** MEDIUM. Real LLM dependency makes it less deterministic.
- **Priority:** Port with hybrid_fast default toggle; add output archiving.

**6. M-0388 validate_act1.py**
- **Path:** code/index_builders/M-0388_validate_act1.py
- **Core value:** Act-1 forward/reverse validation with JSON/MD output.
- **Rewrite barriers:** Old paths; real LLM; old output directories.
- **Risk profile:** MEDIUM. Mixed authority per M-0239 (act1 auth-failure path).
- **Priority:** Register as optional smoke test; use mock provider.

**7. M-0377 check_llm_stability.py**
- **Path:** code/index_builders/M-0377_check_llm_stability.py
- **Core value:** 3-case/3-round LLM stability checker; produced key 6/9 evidence.
- **Rewrite barriers:** Old paths; real LLM only; no output archiving in script.
- **Risk profile:** MEDIUM. Real LLM dependency; stability outcome is non-deterministic.
- **Priority:** Port as optional external-dependency test; do not include in CI.

### Lower-Priority / Conditional Rewrite Candidates

**8. M-0381 demo_resolver.py**
- **Path:** code/index_builders/M-0381_demo_resolver.py
- **Core value:** Simple resolver demo with --query argument.
- **Rewrite barriers:** Old paths; stdout-only output.
- **Risk profile:** LOW. Replaceable with current-project demo script.
- **Priority:** Replace rather than port.

**9–10. Jupyter notebooks (M-0383, M-0384)**
- **Path:** code/index_builders/M-0383_Resolver_Forward_Demo_Clean.ipynb, M-0384_Resolver_Workbench.ipynb
- **Core value:** Interactive forward demo and block-by-block validation workbench.
- **Rewrite barriers:** Old paths; notebook dependencies on old project structure.
- **Risk profile:** LOW. Useful for interactive validation but not CI-critical.
- **Priority:** Port if needed for manuscript workflow demonstration.

**11. Index builder scripts (M-0365, M-0367, M-0369, M-0370, M-0372)**
- **Path:** code/index_builders/M-0365 through M-0372
- **Core value:** Drug/gene/cellline index rebuild. Proven with existing indexes.
- **Rewrite barriers:** Old paths; external dependencies (RDKit, PubChem, MyGene).
- **Risk profile:** LOW for drugs (indexes exist), HIGH for any missing index.
- **Priority:** Port selectively only if index rebuild is required.

---

## Section 5: Known Gaps and Missing Assets

This section consolidates gaps from three sources: T-055 missing leads, T-057 "not usable" assets, and T-007 gap/risk list (A-008).

### Critical Gaps

**GAP-1: function_index.json missing (T-055 GAP-1, T-055 GAP-5, T-057, T-007 GAP-2)**
- **Description:** The function_index.json runtime asset is absent from migrated data/query_indexes/. FunctionIndex class exists, build report (M-0252) confirms 91 functions were built, and builder script (M-0373) can rebuild. But no runtime JSON was found.
- **Impact:** Reverse query scenarios (SC-002, SC-006, SC-023, SC-027) cannot validate function mapping. resolver.py FunctionIndex class will fail to load.
- **Action:** Rebuild via M-0373_build_function_index.py in the current pxfquery conda environment using functional matrix h5ad var_names. Register rebuilt index as a current asset.
- **Source:** T-055 §4 gaps 1,5; T-057 §2.4; T-007 §High Priority Gap 2; A-001 §Notable gap

**GAP-2: Current-package runnable state not verified (T-007 GAP-1)**
- **Description:** Code is migrated under flat asset library; validation reports are legacy runs. No import/compile/smoke test has been run in the current workspace.
- **Impact:** Unknown import/path/environment drift may block all subsequent development.
- **Action:** T-007 D001 (package workspace establishment): copy package, install editable, run import tests.
- **Source:** T-007 §High Priority Gap 1

**GAP-3: Real LLM path unstable and slow (T-007 GAP-3)**
- **Description:** Stability check 6/9; always-LLM 167.3s/4 queries; llm_parse_intent dominates (117s). Generic drug queries oscillate between PROXY_PERT and NOT_FOUND.
- **Impact:** SC-011, SC-012, SC-024, SC-025 all expect inconsistent/failed behavior for generic and free-text queries. LLM mode cannot be the primary manuscript claim.
- **Action:** Use hybrid_fast as default; treat LLM as fallback/summary; deterministic tests as acceptance criteria.
- **Source:** T-007 §High Priority Gap 3; T-056 SC-011, SC-012, SC-024, SC-025; T-057 §3.3

### Operational Gaps

**GAP-4: Old workspace paths in all scripts (T-007 GAP-4)**
- **Description:** Every script in code/index_builders/ uses `Path(__file__).resolve().parents[3]` conventions and references `workspace/`, `output/store/`, `report/` paths that do not exist in the current project.
- **Impact:** No script can be run in-place; all 11 "rewrite needed" assets require path updates.
- **Action:** Port selected scripts into a clean development task; do not execute old scripts in-place.
- **Source:** T-007 §High Priority Gap 4; T-057 §3.1

**GAP-5: GSEA scripts have HPC assumptions (T-055 GAP-6)**
- **Description:** All GSEA eval scripts reference `/public/home/caojun/project/RUSH/` paths and are designed for SLURM cluster execution.
- **Impact:** Scripts cannot run in macOS environment without significant adaptation.
- **Action:** Use GSEA scripts as methodology reference only; do not attempt local execution.
- **Source:** T-055 §4 gap 6

**GAP-6: GSEA table symlinks unresolved (T-055 GAP-4)**
- **Description:** 6 GSEA result tables (cp/sh/xpr top 100 terms CSVs) are large symlink placeholders (244-372MB each). Actual content unverified.
- **Impact:** Cannot use migrated GSEA result tables as validation baselines without symlink resolution.
- **Action:** Resolve symlinks or locate source data before using as baseline.
- **Source:** T-055 §4 gap 4

**GAP-7: Reverse query less validated than forward (T-007 GAP-7)**
- **Description:** Only one reverse example exists in Act-1 (apoptosis/MYC/A549). 7-case matrix and 12-question suite are forward-only.
- **Impact:** Reverse-query manuscript claims weaker than forward. SC-002, SC-006, SC-023, SC-027 all involve reverse query.
- **Action:** Add deterministic reverse smoke cases after package setup and function index restoration.
- **Source:** T-007 §Medium Priority Gap 7; T-057 §3.5

**GAP-8: Drug generic-query behavior inconsistent (T-007 GAP-8)**
- **Description:** EGFR inhibitor and similar generic descriptions oscillate between PROXY_PERT and NOT_FOUND across runs.
- **Impact:** Natural-language drug examples may fail during demo (SC-011, SC-024).
- **Action:** Use exact drug-name examples for manuscript demos; stabilize fallback behavior before claiming natural-language drug support.
- **Source:** T-007 §Medium Priority Gap 8; T-056 SC-011, SC-024; T-057 §2.1 (M-0277 evidence)

### Deferred/Low-Priority Gaps

**GAP-9: main.py conflicts with modern package entry (T-007 GAP-5)** — Mark obsolete.
**GAP-10: Validation report naming conflicts (T-007 GAP-6)** — Keep canonical table; rerun smoke tests.
**GAP-11: Zenodo/download not implemented (T-007 GAP-9)** — Defer until local workflow passes.
**GAP-12: Figures not validated as manuscript-ready (T-007 GAP-10)** — Create figure task after query outputs stable.
**GAP-13: Large matrices/embeddings as raw migrated assets (T-007 GAP-11)** — Register only assets needed per task.
**GAP-14: Suite run variant proliferation (T-055 GAP-7)** — Deduplicate before use; T-057 already classified superseded variants as historical.
**GAP-15: Duplicate script pairs (T-055 GAP-2)** — Prefer M-013x series; treat M-034x/035x as archive copies.
**GAP-16: Not usable GSEA log files (T-057)** — 6 GSEA err/out files (M-0117 through M-0127) have zero analytical value.

---

## Section 6: Alignment with Current Development State

This section cross-references the handoff with T-007's development state understanding.

### T-007's 5-Step Development Interpretation

The handoff aligns with T-007's recommended development sequence:

| T-007 Step | Stress-Test Handoff Alignment |
|---|---|
| 1. Make package runnable in current workspace | GAP-2 covers this. All 11 rewrite-needed scripts depend on package setup first. Recommended milestone task T1 (package workspace) directly maps to D001. |
| 2. Restore/rebuild missing function_index.json | GAP-1 covers this. M-0373 is the rebuild path. Recommended milestone task T2 (index completeness) maps to D002. SC-027 and SC-023 depend on this. |
| 3. Verify deterministic query without LLM | The deterministic 7/7 matrix (M-0291/M-0386) and baseline exact scenarios (SC-004, SC-005, SC-017) support this. Recommended task T3 (deterministic smoke) maps to D003. |
| 4. Verify resolver in hybrid_fast mode | M-0275 (0.825s/3 queries) and SC-026 (mode consistency) support this. Recommended task T4 (hybrid_fast validation) maps to D004. |
| 5. LLM as optional convenience | M-0267 (6/9 stability), M-0277 (167.3s latency), and SC-024/SC-025 (mode cross-checks) all support the conclusion that LLM should be treated as fallback, not core. Recommended task T6 (LLM evaluation) provides guidance. |

### Mapping to T-007 Gap/Risk List

| T-007 Gap | Handoff Section | Recommended Task | Risk Level |
|---|---|---|---|
| GAP-1: Package runnability | §5 GAP-2 | Task T1 | HIGH |
| GAP-2: function_index.json | §5 GAP-1 | Task T2 | HIGH |
| GAP-3: LLM unstable/slow | §5 GAP-3 | Task T6 | MEDIUM |
| GAP-4: Old workspace paths | §5 GAP-4 | Tasks T1, T3, T4 | HIGH |
| GAP-5: main.py conflict | §5 GAP-9 | Task T1 (exclude during packaging) | LOW |
| GAP-6: Report naming conflicts | §5 GAP-10 | Task T3 (canonical evidence table) | MEDIUM |
| GAP-7: Reverse less validated | §5 GAP-7 | Task T3, T4 | MEDIUM |
| GAP-8: Drug generic inconsistent | §5 GAP-8 | Task T4, T6 | MEDIUM |

### T-007 Claims Alignment

**Claims to avoid (reinforced by handoff evidence):**
- "Stable broad AI-agent system" — contradicted by 6/9 stability and mode inconsistency (SC-024)
- "Natural-language performance stable across all domains" — contradicted by generic drug oscillation (SC-011) and free-text failure (SC-012)
- "Old validation reports are current-project validation" — legacy runs only; need fresh smoke tests (GAP-2)

**Safer claims (supported by handoff evidence):**
- "Deterministic LINCS/CMAP functional query core" — supported by 7/7 matrix (M-0291) and 4 exact/proxy pass scenarios (SC-017–SC-020)
- "Evidence-aware exact/proxy retrieval" — supported by L1-L4 resolver logic and cellline/gene/drug indexes
- "LLMs assist parsing/summarization, not scientific core" — supported by latency (167.3s) and stability (6/9) evidence

### T-007 Recommended Tasks Cross-Validation

| T-007 Task | Handoff Milestone Task | Alignment |
|---|---|---|
| D001: Establish Current Package Workspace | Task T1 | Direct alignment |
| D002: Restore Runtime Index Completeness | Task T2 | Direct alignment; adds function_index priority |
| D003: Deterministic Query Smoke Tests | Task T3 | Direct alignment |
| D004: Resolver Hybrid-Fast Validation | Task T4 | Direct alignment |
| D005: Genes-Style Case Study | Task T5 | Direct alignment |

The handoff adds stress-test-specific tasks (T6: LLM evaluation, T7: GSEA baseline, T8: suite deduplication) that are not in T-007's 5-task plan but are logical consequences of stress-test digestion findings.

---

## Section 7: Handoff Integrity Check

This section reviews predecessor outputs for internal consistency and unresolved contradictions.

### Internal Consistency Checks

**Across T-055, T-056, T-057:**

| Check | Finding | Status |
|---|---|---|
| Do T-055's category counts match T-057's classification totals? | T-055 catalogs ~160 candidates; T-057 classifies 65 of those (focusing on the functionally meaningful subset). GSEA/background/tutorial assets are catalogued but not re-classified, as they are outside T-057's scope. | CONSISTENT — T-057 subset is intentional, not contradictory |
| Do T-056's scenario evidence anchors match T-057's reuse decisions? | All 29 scenarios cite evidence that T-057 has classified: 10 as direct reference, 6 as rewrite needed, several as historical. No scenario cites a "not usable" asset as primary evidence. | CONSISTENT |
| Is the function_index.json gap consistently reported? | T-055 §4 gaps 1 and 5, T-056 SC-023/SC-027, T-057 §3.4, and T-007 GAP-2 all flag this. Build report (M-0252) and builder (M-0373) both confirm the index was built. | CONSISTENT — gap is independently confirmed by all three predecessors |
| Is the LLM instability finding consistent? | T-055 references M-0267 (6/9) and M-0277 (latency). T-056 marks SC-024 INCONSISTENT and SC-025 LATENCY_ISSUE. T-057 classifies M-0267 as direct reference and M-0277 as historical evidence. | CONSISTENT — evidence hierarchy agrees that LLM path is unstable |
| Is the deterministic 7/7 matrix consistently referenced as strongest evidence? | T-055 highlights M-0386/M-0291. T-056's 4 exact/proxy scenarios all cite V-005 and A-006. T-057 classifies M-0291 as direct reference. | CONSISTENT — no predecessor disputes this |
| Do duplicate/timestamped variants cause contradictions? | T-055 flags suite run variants as a gap (GAP-7). T-057 classifies superseded variants as historical evidence only, preferring latest suite_runs versions. | CONSISTENT — T-057 resolves the deduplication issue that T-055 flags |

### Unresolved Contradictions or Ambiguities

**1. Act-1 validation authority (M-0255):**
- **T-055:** Lists M-0255 with note "Mixed authority per latest report index."
- **T-057:** Classifies M-0255 as historical evidence only. M-0239 warns act1 auth-failure path is not valid basis, but the migrated copy contains successful forward EGFR/A549 and reverse apoptosis/MYC/A549 cases.
- **Resolution carried forward:** Follow M-0239 priority. Successful case content can be used as supplementary evidence but not primary validation. T-056 SC-002 and SC-006 reference V-007 (Act-1) as source evidence; this is acceptable with the authority caveat noted.

**2. GSEA script relevance for stress testing:**
- **T-055:** Catalogs 24 GSEA eval scripts as stress-test candidates (GSEA_evaluation category).
- **T-057:** Does not classify individual GSEA scripts; notes they are HPC-specific and historical.
- **Ambiguity:** T-055 includes them as stress-test candidates; T-057's boundary analysis implies low current reuse value due to HPC constraints.
- **Resolution carried forward:** GSEA scripts are methodology reference and provenance only. They should not be ported for local execution in current macOS environment. GSEA result tables may be useful as baselines if symlinks are resolved.

**3. M-0385 suite runner question bank:**
- **T-055:** Lists as "suite runner for 14 predefined forward questions" and the most comprehensive validation script.
- **T-057:** Classifies as rewrite needed. Notes it "uses always_llm and hybrid_fast modes" with a 14-question bank.
- **T-056:** All scenario evidence implicitly references suite questions.
- **No contradiction**, but note: the question bank content (14 specific questions) is not fully enumerated in any single predecessor output. A future porting task should extract the question bank from M-0385 and cross-check against T-056 scenario coverage.

**4. Scope of "stress-test" vs "validation":**
- **T-055:** Catalogs "stress-test candidate assets" broadly, including GSEA eval and tutorial notes.
- **T-056:** Derives 29 stress-test scenarios focused on resolver query behavior.
- **T-057:** Classifies 65 assets focused on resolver logic reusability.
- **Potential tension:** T-055's broader "stress-test" scope (including GSEA pipeline evaluation) is narrower in T-056 (resolver-only scenarios) and T-057 (resolver logic focus). This is not a contradiction — T-056 and T-057 naturally narrow scope to the resolver, which is the immediate stress-test target. GSEA pipeline stress-testing is a distinct future concern.
- **Resolution:** This handoff acknowledges both scopes. The recommended milestone tasks include resolver-focused stress tests (T3-T6) and a separate GSEA baseline task (T7).

### Integrity Verdict

**The predecessor outputs are internally consistent.** All three tasks independently confirm:
1. function_index.json is the critical missing asset.
2. Deterministic forward matrix (7/7) is the strongest evidence.
3. LLM path is unstable and should not be the primary claim.
4. hybrid_fast is the defensible default mode.
5. Old workspace paths are the primary barrier to direct reuse.

The only unresolved ambiguity is the exact question bank content for the 14-question suite (M-0385), which should be extracted during porting. No contradiction prevents coherent synthesis.

---

## Handoff Summary

| Dimension | Key Finding | Risk |
|---|---|---|
| Assets catalogued | ~160 across 10 categories | Gaps: function_index.json, unverified GSEA tables |
| Scenarios derived | 29 across 9 dimensions | 6 FAIL, 5 BORDERLINE, 4 ambiguous |
| Reuse classification | 10 direct reference, 11 rewrite needed, 38 historical, 6 not usable | Highest-value: M-0291, M-0275, M-0267, resolver.py |
| Critical gap | function_index.json missing | Blocks reverse query and function-mapped scenarios |
| Strongest evidence | Deterministic 7/7 forward matrix | Mock hooks, no LLM dependency |
| Weakest area | LLM stability (6/9) and latency (167.3s) | Not manuscript-ready |
| Default mode | hybrid_fast (0.825s/3 queries) | Suitable for demos and deterministic tests |
| Predecessor consistency | Consistent | No contradictions; minor scope tension resolved |

