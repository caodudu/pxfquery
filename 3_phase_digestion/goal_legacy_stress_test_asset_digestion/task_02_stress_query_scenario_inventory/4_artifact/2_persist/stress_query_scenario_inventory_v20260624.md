# Stress-Query Scenario Inventory

Generated: 2026-06-24
Task: T-056 02_stress_query_scenario_inventory

## Purpose

This document catalogs derived stress-test scenarios for future PxFquery validation. Each scenario is grounded in evidence from T-007 digestion artifacts (A-001 through A-008). No scenarios are hypothetical without documented precedent.

## Scenario Dimensions Covered

1. Complex queries
2. Strict queries
3. Boundary queries
4. No-hit (NOT_FOUND) behavior
5. Overly broad results
6. Proxy/exact matching
7. Difficult perturbation/cell-line/function combinations
8. LLM mode cross-checks
9. Missing/partial index

---

## 1. Complex Queries

### SC-001: Multi-gene forward query

- **Category**: complex_query
- **Query type**: forward
- **Perturbation**: EGFR + KRAS
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_PERT
- **Expected result**: FAIL (risk)
- **Rationale**: Resolver intent parsing must handle multiple perturbation targets. Historical evidence shows single-gene EXACT works (A-006, 7/7 matrix), but multi-gene intent parsing is not validated in any T-007 report. A-002 notes resolver is "implemented with risk" and multi-source genetic behavior exists but is not deeply tested.
- **Source evidence**: A-001 §Implemented Components (resolver with genetic multi-source); A-004 row 7 (resolver "implemented with risk"); A-006 (single-gene only)

### SC-002: Multi-function reverse query

- **Category**: complex_query
- **Query type**: reverse
- **Perturbation**: N/A
- **Context**: A549
- **Function intent**: activate apoptosis + suppress MYC + suppress BCL2
- **Expected hit level**: EXACT
- **Expected result**: PASS (conditional)
- **Rationale**: A-003 §D003 documents reverse apoptosis/MYC/A549 as a recommended smoke test. However, the multi-function vector expands beyond the single-function reverse query validated in Act-1 (V-007). The function_index.json gap (A-001 §Notable gap) may affect resolution if function lookup is required.
- **Source evidence**: A-003 §D003 (reverse apoptosis/MYC/A549); A-001 §Notable gap (function_index.json missing); V-007 (Act-1 reverse example)

### SC-003: Combined drug+gene perturbation forward query

- **Category**: complex_query
- **Query type**: forward
- **Perturbation**: erlotinib + KRAS G12C
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_BOTH
- **Expected result**: FAIL (risk)
- **Rationale**: Combined drug+gene perturbation across different index types (drug_index + gene_index) stresses resolver evidence bundling. No T-007 report validates multi-type perturbation resolution. A-002 §8 notes generic drug behavior is inconsistent (EGFR inhibitor oscillates between PROXY_PERT and NOT_FOUND across runs).
- **Source evidence**: A-002 §8 (inconsistent generic drug behavior); A-004 (drug index ready but risky); A-006 (only single-perturbant cases tested)

---

## 2. Strict Queries

### SC-004: Exact gene forward query (KRAS in A549)

- **Category**: strict_query
- **Query type**: forward
- **Perturbation**: KRAS
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT
- **Expected result**: PASS
- **Rationale**: KRAS is a well-known gene in the index (A-001 §Data, 78,061 full gene entries). A549 is a validated cell line. A-006 CASE_EXACT_GENE passed at EXACT. This is a minimal strict query that must always produce EXACT.
- **Source evidence**: A-001 §Data And Index Readiness (gene index present); A-006 (EXACT gene case passed); V-005 (7/7 deterministic pass)

### SC-005: Exact drug forward query (erlotinib in A549)

- **Category**: strict_query
- **Query type**: forward
- **Perturbation**: erlotinib
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT
- **Expected result**: PASS
- **Rationale**: erlotinib is a named drug in drug_index (5,958 alias entries, V-002). A-006 CASE_EXACT_DRUG passed at EXACT. Must avoid PROXY_PERT fallback and produce direct EXACT match.
- **Source evidence**: A-006 (CASE_EXACT_DRUG passed); V-002 (drug index build success); A-004 (drug index ready)

### SC-006: Strict reverse with proxy disallowed (apoptosis in A549)

- **Category**: strict_query
- **Query type**: reverse
- **Perturbation**: N/A
- **Context**: A549
- **Function intent**: activate apoptosis
- **Expected hit level**: EXACT
- **Expected result**: PASS
- **Rationale**: Act-1 reverse example (V-007) found candidates for apoptosis/MYC/A549. With proxy explicitly disallowed, the resolver must produce EXACT-only results from functional matrix. This tests whether the resolver honors a strict-mode constraint.
- **Source evidence**: V-007 (Act-1 reverse apoptosis/MYC/A549); A-003 §D003 (reverse smoke test recommendation); A-001 §Resolver proxy logic

---

## 3. Boundary Queries

### SC-007: Unknown cell line (EGFR in FAKE_CELL)

- **Category**: boundary_query
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: FAKE_CELL (unknown/absent from cellline_index)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_CELL
- **Expected result**: PASS
- **Rationale**: A-006 CASE_UNKNOWN_CELL_INPUT tested exactly this pattern and passed at PROXY_CELL. The cell line neighbor tree (A-001 §Data) supports proxy cell resolution via lineage/disease hierarchy. However, if the resolver is in strict mode, it should produce NOT_FOUND — this mode sensitivity is the boundary to test.
- **Source evidence**: A-006 (CASE_UNKNOWN_CELL_INPUT → PROXY_CELL); A-001 (cellline_neighbors.json for proxy); A-007 (mode inconsistency risk — always_llm vs hybrid_fast may behave differently)

### SC-008: Unknown drug forward query (FAKE_DRUG_XYZ in A549)

- **Category**: boundary_query
- **Query type**: forward
- **Perturbation**: FAKE_DRUG_XYZ
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND
- **Expected result**: PASS (if NOT_FOUND correctly returned)
- **Rationale**: Drug with no alias or neighbor match must produce NOT_FOUND. A-007 §4 warns that NOT_FOUND and PROXY_* coexisting require strict evidence-quality differentiation. The resolver must not hallucinate proxy matches for absent drugs.
- **Source evidence**: A-007 §4 (NOT_FOUND + PROXY distinction); A-002 §8 (generic drug fallback inconsistent); A-004 (drug index has 5,958 aliases — FAKE_DRUG_XYZ should not match any)

### SC-009: Empty/partial perturbation string ("" in A549)

- **Category**: boundary_query
- **Query type**: forward
- **Perturbation**: "" (empty string)
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND
- **Expected result**: PASS (if error handled gracefully)
- **Rationale**: Empty perturbation string is a malformed input boundary. The resolver must return a clear error or NOT_FOUND, not crash or produce random proxy results. No T-007 report tests this case — it is a gap-derived boundary scenario.
- **Source evidence**: A-002 §1-4 (gaps include unverified runnable state); A-001 §Validation State (no empty-input test recorded)

### SC-010: Typo/partial cell line ("A54" instead of A549)

- **Category**: boundary_query
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: "A54" (typo variant)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND or PROXY_CELL
- **Expected result**: FAIL (risk)
- **Rationale**: No T-007 report validates fuzzy cell-line matching. The resolver may treat "A54" as unknown and use PROXY_CELL or return NOT_FOUND. Mode-dependent behavior is likely. This tests the resolver's tolerance for near-miss cell line identifiers.
- **Source evidence**: A-007 §3 (mode consistency risk); A-001 (cellline_index with valid_cells list — "A54" not present); A-006 (only exact cell names tested)

---

## 4. No-Hit (NOT_FOUND) Behavior

### SC-011: Generic drug description ("EGFR inhibitor" in A549)

- **Category**: no_hit
- **Query type**: forward
- **Perturbation**: "EGFR inhibitor" (generic, not a drug alias)
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND
- **Expected result**: PASS (if NOT_FOUND) / FAIL (if inconsistent)
- **Rationale**: This is the most documented failure case. A-002 §8 reports EGFR inhibitor oscillates between PROXY_PERT and NOT_FOUND in different runs. V-009 (LLM stability 6/9) includes EGFR inhibitor as a failure case. V-010 (always-LLM stats) reports several NOT_FOUND cases. The stress test must verify consistent NOT_FOUND across all modes, or at minimum document which modes produce which behavior.
- **Source evidence**: A-002 §8 (EGFR inhibitor inconsistent); V-009 (6/9 stability, EGFR inhibitor failure); V-010 (always-LLM NOT_FOUND cases); A-007 §1 (LLM stability risk)

### SC-012: Free-text biological context (EGFR in "non-small cell lung carcinoma")

- **Category**: no_hit
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: "non-small cell lung carcinoma" (NSCLC, free text)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND
- **Expected result**: PASS (if NOT_FOUND) / FAIL (if hallucinated)
- **Rationale**: V-009 explicitly records NSCLC as a failure case in always-LLM mode. The resolver must not hallucinate PROXY_CELL or PROXY_BOTH when the context string does not match any cell line in the index. A-001 §Risk notes NSCLC returned NOT_FOUND in always-LLM.
- **Source evidence**: V-009 (NSCLC failure in LLM stability); A-001 §Risk (NSCLC NOT_FOUND in always-LLM); A-007 §1 (LLM stability 6/9)

### SC-013: Impossible gene+context combination (MYC in erythroid progenitor)

- **Category**: no_hit
- **Query type**: forward
- **Perturbation**: MYC
- **Context**: erythroid progenitor (cell line with no MYC relevance)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND (or very weak proxy)
- **Expected result**: PASS
- **Rationale**: Tests whether the resolver correctly identifies biologically implausible combinations and returns NOT_FOUND rather than fabricating proxy evidence. No direct T-007 precedent, but derived from A-002 §Claims To Avoid (not a stable broad AI-agent system) and A-001 §Intended Product (evidence-aware retrieval).
- **Source evidence**: A-002 §Claims To Avoid (do not claim broad stability); A-001 §Intended Product (evidence-aware retrieval); A-004 (cell line neighbor tree may find distant proxy)

---

## 5. Overly Broad Results

### SC-014: Vehicle control (DMSO in A549)

- **Category**: overly_broad
- **Query type**: forward
- **Perturbation**: DMSO
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_PERT (too many matches) or EXACT
- **Expected result**: BORDERLINE (too many hits to be useful)
- **Rationale**: DMSO is a common vehicle control that may appear in the drug index as a named compound. Its broad biological effects mean functional matrix hits may be numerous and non-specific. The stress test must verify that the resolver either returns a manageable result set or clearly labels the result as overly broad.
- **Source evidence**: A-004 (drug index has 5,958 aliases — DMSO likely present); A-001 §Intended Product (evidence-aware retrieval); A-006 (no broad-drug case tested)

### SC-015: Pan-cancer reverse query (activate apoptosis in "cancer")

- **Category**: overly_broad
- **Query type**: reverse
- **Perturbation**: N/A
- **Context**: "cancer" (overly broad)
- **Function intent**: activate apoptosis
- **Expected hit level**: PROXY_CELL (many cell lines match)
- **Expected result**: BORDERLINE (excessively broad proxy)
- **Rationale**: The term "cancer" is not a specific cell line. The resolver would need proxy matching across many cell lines, producing an unmanageable result set. No T-007 report tests broad context terms for reverse query. This tests whether the resolver provides a useful result or degrades gracefully.
- **Source evidence**: A-001 (reverse query mechanism); A-003 §D005 (prefer narrow demonstrations); A-002 §Claims To Avoid (not stable across all biological domains)

### SC-016: Common drug with many neighbors (aspirin in A549)

- **Category**: overly_broad
- **Query type**: forward
- **Perturbation**: aspirin
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_PERT (many neighbor matches)
- **Expected result**: BORDERLINE
- **Rationale**: Aspirin is a common drug that may appear in the drug index. If present, its broad mechanism of action may produce many proxy neighbor hits. If absent, the resolver must handle the NOT_FOUND case cleanly. This tests both outcomes.
- **Source evidence**: A-004 (drug index with 5,958 aliases and 5,312 neighbor entries); A-002 §8 (generic drug behavior inconsistent)

---

## 6. Proxy/Exact Matching

### SC-017: EXACT gene with known cell line (EGFR in A549)

- **Category**: proxy_exact
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT
- **Expected result**: PASS
- **Rationale**: Baseline exact match case. A-006 CASE_EXACT_GENE passed. Both EGFR and A549 are in their respective indexes. This is the simplest proxy/exact differentiation test.
- **Source evidence**: A-006 (CASE_EXACT_GENE → EXACT); V-005 (7/7 deterministic); A-001 §Data (gene 78k, cell line present)

### SC-018: PROXY_CELL for unknown cell (EGFR in unknown_cell)

- **Category**: proxy_exact
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: UNKNOWN_CELL (not in cellline_index)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_CELL
- **Expected result**: PASS
- **Rationale**: A-006 CASE_UNKNOWN_CELL_INPUT passed at PROXY_CELL. The cell line neighbor tree proxies via lineage. This is the canonical PROXY_CELL test.
- **Source evidence**: A-006 (CASE_UNKNOWN_CELL_INPUT → PROXY_CELL); A-001 (cellline_neighbors.json for proxy)

### SC-019: PROXY_BOTH for unknown cell + proxy pert (EGFR_inhibitor_gene proxy in unknown_cell)

- **Category**: proxy_exact
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: unknown_cell
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_BOTH
- **Expected result**: PASS
- **Rationale**: A-006 CASE_PROXY_BOTH_GENE passed at PROXY_BOTH. Tests the most complex proxy level where both perturbation and context require proxy resolution.
- **Source evidence**: A-006 (CASE_PROXY_BOTH_GENE → PROXY_BOTH); V-005 (7/7 pass coverage includes PROXY_BOTH)

### SC-020: PROXY_PERT drug with exact cell (erlotinib in A549, forcing proxy path)

- **Category**: proxy_exact
- **Query type**: forward
- **Perturbation**: erlotinib (forced to proxy via test config)
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_PERT
- **Expected result**: PASS
- **Rationale**: When the exact match path is blocked, the resolver must fall back to PROXY_PERT via drug neighbors. A-006 CASE_PROXY_PERT_DRUG passed. This tests that proxy fallback works correctly with drug indexes.
- **Source evidence**: A-006 (CASE_PROXY_PERT_DRUG → PROXY_PERT); V-002 (drug index build with 5,314 neighbors)

---

## 7. Difficult Combos

### SC-021: Drug alias conflict across cancer types (erlotinib in H1975 vs A549)

- **Category**: difficult_combo
- **Query type**: forward
- **Perturbation**: erlotinib
- **Context**: H1975 (T790M mutation, erlotinib-resistant)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT (drug match) but potential function conflict
- **Expected result**: BORDERLINE
- **Rationale**: erlotinib is effective in EGFR-mutant A549 but ineffective in T790M-positive H1975. The functional matrix may show different perturbation signatures. The stress test must verify that the resolver correctly retrieves context-specific functional scores and does not conflate results across EGFR-mutant vs resistant contexts.
- **Source evidence**: A-001 §Intended Product (context-aware retrieval); V-007 (Act-1 EGFR/A549 forward); A-002 §7 (reverse less validated than forward — asymmetry may affect interpretation)

### SC-022: Multi-drug multi-cancer comparison (cisplatin + erlotinib in A549 + H1975)

- **Category**: difficult_combo
- **Query type**: forward
- **Perturbation**: cisplatin + erlotinib
- **Context**: A549 + H1975 (multi-context)
- **Function intent**: activated/suppressed programs
- **Expected hit level**: PROXY_BOTH (or ambiguous)
- **Expected result**: FAIL (risk)
- **Rationale**: Multiple perturbations across multiple contexts with conflicting resistance profiles. No T-007 report validates multi-drug multi-context resolution. This is a high-complexity stress test for intent parsing and evidence bundling.
- **Source evidence**: A-001 §Resolver (multi-source behavior exists but untested); A-003 §Do-Not-Do (avoid broad analyses during setup); A-007 §4 (NOT_FOUND + PROXY coexistence needs strict differentiation)

### SC-023: Function not in 91-function index (activate "autophagy")

- **Category**: difficult_combo
- **Query type**: reverse
- **Perturbation**: N/A
- **Context**: A549
- **Function intent**: activate autophagy
- **Expected hit level**: NOT_FOUND
- **Expected result**: PASS (if NOT_FOUND correctly returned)
- **Rationale**: V-004 reports 91 functions in the function index. "Autophagy" may not be one of them. The resolver must correctly report NOT_FOUND rather than returning a false proxy match. This is directly linked to the function_index.json gap (A-001 §Notable gap).
- **Source evidence**: V-004 (91-function index, 11 lookup tests pass — but only tested 11 of 91); A-001 §Notable gap (function_index.json missing); A-004 row 11 (function index implemented but runtime asset missing)

---

## 8. LLM Mode Cross-Checks

### SC-024: Generic query divergence (always_llm vs hybrid_fast for "EGFR inhibitor" in A549)

- **Category**: llm_mode_crosscheck
- **Query type**: forward
- **Perturbation**: "EGFR inhibitor" (generic)
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: NOT_FOUND (hybrid_fast) vs variable (always_llm)
- **Expected result**: INCONSISTENT (known risk)
- **Rationale**: A-007 §3 explicitly warns that always_llm and hybrid_fast may produce different results for boundary cases. V-009 (6/9) and A-002 §8 document EGFR inhibitor failures. This cross-check captures the known mode inconsistency.
- **Source evidence**: A-007 §3 (mode consistency risk); V-009 (EGFR inhibitor failure in some runs); A-002 §8 (EGFR inhibitor oscillates PROXY_PERT/NOT_FOUND)

### SC-025: always_llm latency stress (4+ generic queries)

- **Category**: llm_mode_crosscheck
- **Query type**: forward
- **Perturbation**: Multiple generic queries ("EGFR inhibitor", "MEK inhibitor", "PI3K inhibitor", "CDK4/6 inhibitor")
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: mixed (NOT_FOUND / PROXY_PERT)
- **Expected result**: LATENCY_ISSUE (performance concern)
- **Rationale**: V-010 documents 4 queries in always_LLM took 167.3s with llm_parse_intent consuming 117.142s. Scaling to more queries would produce unacceptable latency. This stress test measures whether the resolver degrades gracefully or times out.
- **Source evidence**: V-010 (always-LLM 167.3s/4 queries); A-007 §2 (always_llm latency risk); A-002 §3 (LLM path unstable and slow)

### SC-026: Deterministic vs hybrid_fast result consistency (EGFR in A549)

- **Category**: llm_mode_crosscheck
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT
- **Expected result**: PASS (both modes identical)
- **Rationale**: For well-behaved exact queries, deterministic mode and hybrid_fast mode must produce identical hit levels and comparable evidence bundles. Any divergence indicates a mode consistency bug.
- **Source evidence**: A-003 §D004 (hybrid_fast validation recommendation); V-011 (hybrid-fast 3 queries in 0.825s, exact/proxy-cell cases found); A-007 §3 (mode inconsistency risk)

---

## 9. Missing/Partial Index

### SC-027: Reverse query with missing function_index.json (activate apoptosis in A549)

- **Category**: missing_partial_index
- **Query type**: reverse
- **Perturbation**: N/A
- **Context**: A549
- **Function intent**: activate apoptosis
- **Expected hit level**: EXACT or FAIL
- **Expected result**: FAIL (if function_index.json required)
- **Rationale**: A-001 §Notable gap: function_index.json is missing from migrated query indexes. The FunctionIndex class exists but cannot load. Reverse query may depend on function index for mapping "apoptosis" to functional matrix columns. This stress test verifies whether the resolver has a fallback or crashes.
- **Source evidence**: A-001 §Notable gap (function_index.json missing); A-004 row 11 (function index implemented but runtime asset missing); V-004 (function index build report says 91 functions built but JSON not found)

### SC-028: Drug neighbor failure edge (drug with 0 neighbors)

- **Category**: missing_partial_index
- **Query type**: forward
- **Perturbation**: drug with zero neighbor entries
- **Context**: A549
- **Function intent**: activated/suppressed programs
- **Expected hit level**: EXACT (if in index) or NOT_FOUND
- **Expected result**: PASS (graceful handling required)
- **Rationale**: V-002 reports 5,312 drug-neighbor entries for 5,314 fingerprints, meaning some drugs have 0 neighbors. The resolver must handle zero-neighbor lookups without crashing. No T-007 report tests this edge case explicitly.
- **Source evidence**: V-002 (5,314 fingerprints, 5,312 neighbor entries — 2 drugs with 0 neighbors); A-004 (drug index ready, but neighbor completeness not 100%)

### SC-029: Cell line with no lineage neighbors

- **Category**: missing_partial_index
- **Query type**: forward
- **Perturbation**: EGFR
- **Context**: cell line with valid_cells entry but no neighbors in neighbor tree
- **Expected hit level**: PROXY_CELL or NOT_FOUND
- **Expected result**: BORDERLINE
- **Rationale**: A-001 §Data reports cellline_neighbors.json has lineage/disease/subtype tree. If a cell line is valid but has no neighbors, PROXY_CELL cannot produce meaningful proxy context. The resolver must either fall back to NOT_FOUND or clearly label the weak proxy.
- **Source evidence**: A-001 (cellline_index and cellline_neighbors present, but neighbor coverage unknown); A-007 §4 (NOT_FOUND + PROXY_* coexistence needs clear labeling)

---

## Summary

| Dimension | Scenarios | Earliest source evidence |
|-----------|-----------|-------------------------|
| Complex queries | SC-001, SC-002, SC-003 | A-001, A-004 |
| Strict queries | SC-004, SC-005, SC-006 | A-006, V-007 |
| Boundary queries | SC-007, SC-008, SC-009, SC-010 | A-006, A-007 |
| No-hit behavior | SC-011, SC-012, SC-013 | V-009, A-002 |
| Overly broad results | SC-014, SC-015, SC-016 | A-004, A-001 |
| Proxy/exact matching | SC-017, SC-018, SC-019, SC-020 | A-006, V-005 |
| Difficult combos | SC-021, SC-022, SC-023 | V-004, A-001 |
| LLM mode cross-checks | SC-024, SC-025, SC-026 | A-007, V-010 |
| Missing/partial index | SC-027, SC-028, SC-029 | A-001, V-004 |
