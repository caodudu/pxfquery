# PxFquery Evidence Routing Route Taxonomy

Generated: 2026-06-25
Task: T-064 evidence_routing_anchor
Phase: Digestion
Status: Accepted deliverable
Dependencies: T-007 (A-001, A-005), T-013 (A-002), T-021 (A-003), T-058 (A-004)

---

## 1. Foundation: Current Evidence Landscape

This route taxonomy is grounded in completed predecessor outputs:

- **A-001 (T-007 D-002):** PxFquery has a credible technical base for a lightweight Genes-style workflow. Deterministic matrix retrieval plus evidence-aware proxy resolver logic is the strongest reusable core. The migrated package implements forward/reverse query classes, a resolver pipeline (L1-L4 search policy), index wrappers, and LLM prompt functions. A deterministic forward matrix test passed 7/7 across EXACT, PROXY_PERT, PROXY_CELL, and PROXY_BOTH hit levels. However, the real LLM path is unstable (6/9 stability), always_llm mode costs 167.3s for 4 queries, and generic drug queries oscillate between PROXY_PERT and NOT_FOUND.
- **A-002 (T-013 D-005):** CAP-05 (no-hit safe return) fails because the current fuzzy fallback matches meaningless perturbation names to real gene names without similarity thresholding. CAP-07 (NL resolver/proxy retrieval) is blocked by index naming mismatches and the missing function_index.json.
- **A-003 (T-021 D-001):** The canonical standard resource set includes 3 functional matrices (cp/sh/xpr, float32, 91 functions), 10 query indexes (including a rebuilt function_index.json with schema-compatible aliases), and 5 metadata tables. All 19 files are Python-verified.
- **A-004 (T-058 D-001):** 29 stress-test scenarios derived across 9 query dimensions, with 12 PASS, 6 FAIL, 5 BORDERLINE, 4 ambiguous, 1 INCONSISTENT, and 1 LATENCY_ISSUE. The deterministic forward matrix test (M-0386, 7/7) is the strongest validation evidence. hybrid_fast mode (0.825s/3 queries) is the defensible default.
- **A-005 (T-007 D-005):** Known risks: LLM stability 6/9, always_llm latency 167.3s, NOT_FOUND for generic drugs. Safer claims center on deterministic core with exact/proxy retrieval, not AI-agent platform claims.

### Canonical Resource Set (T-021)

All route definitions reference the following T-021 standard resources as the canonical index/matrix input set:

| Resource | Type | Role in routing |
|---|---|---|
| `cp_func_ad.h5ad` | Functional matrix | Compound perturbation scores (201,014 obs × 91 func) |
| `sh_func_ad.h5ad` | Functional matrix | shRNA perturbation scores (189,365 obs × 91 func) |
| `xpr_func_ad.h5ad` | Functional matrix | ORF perturbation scores (132,464 obs × 91 func) |
| `cellline_index.json` | Query index | Valid cell line name resolution |
| `cellline_neighbors.json` | Query index | Lineage/disease/subtype proxy paths |
| `cellline_tree.json` | Query index | Cell line ontology for proxy resolution |
| `drug_index.json` | Query index | Drug alias → BRD-id (5,958 entries) |
| `drug_neighbors.json` | Query index | Drug similarity neighbors (5,312 drugs) |
| `gene_index.json` / `gene_index_simple.json` | Query index | Gene symbol lookup (78,061 full / 25,036 simple) |
| `gene_neighbors.json` / `gene_neighbors_simple.json` | Query index | Gene semantic neighbors (33,791 full / 30,319 simple) |
| `function_index.json` | Query index | 91-function term catalog with aliases (rebuilt by T-021) |

---

## 2. Route Taxonomy

### 2.1 exact-hit

**Definition:** Perturbation and biological context both resolve to exact entries in their respective query indexes; deterministic numeric retrieval from the appropriate functional matrix produces a valid function_response.

**Resolution path:**
1. Perturbation is matched exactly in drug_index, gene_index, or gene_index_simple.
2. Biological context (cell_line) is matched exactly in cellline_index.
3. The appropriate functional matrix (cp/sh/xpr) is selected by perturbation type.
4. Perturbation observation is located in the matrix's obs by pert_id/sig_id and cell_iname.
5. The full 91-function score vector is extracted from the matrix's X layer.

**Deterministic nature:** This route uses no LLM, no proxy, and no fuzzy matching. It is the strongest evidence pathway—the deterministic 7/7 matrix test (M-0386, M-0291) fully validates this route.

**Confidence:** `high` — both dimensions resolved by exact index lookup into a verified float32 functional matrix with perfect rank preservation (T-021 rank correlation = 1.000000).

**Supported by evidence:**
- T-007: deterministic resolver forward matrix test passed 7/7 for EXACT hit levels
- T-021: all 3 functional matrices Python-verified, all 10 indexes loadable
- T-058: 4 exact/proxy scenarios marked PASS (SC-004, SC-005, SC-017, SC-019)

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-001 | exact-hit | Forward: perturbation="gefitinib", cell_line="A549", direction="forward" | drug_index → BRD-K68045993; cellline_index → A549; cp_func_ad.h5ad → X row for matching sig_id + cell_iname | route_type=exact-hit, query_context=A549/compound, perturbation_resolution=exact_match, function_response=91-score vector, confidence=high, proxy_chain=null, diagnostics={}, suggestions=[] | 91-score vector returned; all scores within [-10,10]; perturbation and cell line confirmed exact in respective indexes | SC-005 (exact drug) |
| AC-002 | exact-hit | Forward: perturbation="EGFR", cell_line="A375", direction="forward" | gene_index → EGFR; cellline_index → A375; xpr_func_ad.h5ad → X row (ORF overexpression) or sh_func_ad.h5ad (knockdown) depending on pert_type | route_type=exact-hit, query_context=A375/gene, perturbation_resolution=exact_match, function_response=91-score vector, confidence=high, proxy_chain=null, diagnostics={}, suggestions=[] | 91-score vector returned for EGFR overexpression or knockdown; perturbation_type is recorded | SC-004 (exact gene) |
| AC-003 | exact-hit | Reverse: function_target="HALLMARK_APOPTOSIS", direction="activate", cell_line="A549" | function_index → HALLMARK_APOPTOSIS; cellline_index → A549; cp_func_ad.h5ad → ranked pert_ids by apoptosis score descending (top-k where cell_iname matches) | route_type=exact-hit, query_context=A549/reverse, perturbation_resolution=all_exact, function_response=ranked_candidates, confidence=high, proxy_chain=null, diagnostics={}, suggestions=[] | Ranked list of compound candidates returned; top candidates show positive apoptosis scores; ranking consistent with score ordering | SC-006 (strict reverse no-proxy) |

### 2.2 proxy-hit

**Definition:** One or both query dimensions (perturbation, biological context) cannot be resolved exactly but can be resolved via a neighbor/proxy index. The proxy source, proxy chain, and confidence downgrade must be documented in evidence metadata.

**Proxy tiers (from resolver.py L1-L4 architecture, A-001):**
- **PROXY_PERT:** Cell line exact; perturbation resolved via nearest neighbor in drug_neighbors or gene_neighbors.
- **PROXY_CELL:** Perturbation exact; cell line resolved via lineage/subtype hierarchy in cellline_neighbors.
- **PROXY_BOTH:** Neither dimension exact; both resolved via respective neighbor indexes.

**Resolution path:**
1. For each unresolved dimension, query the appropriate neighbor index:
   - Cell line: cellline_neighbors.json → lineage/disease/subtype group → nearest cell line present in matrix obs.
   - Perturbation: drug_neighbors.json (Tanimoto) or gene_neighbors.json (cosine) → nearest neighbor above threshold.
2. Select functional matrix by perturbation type.
3. Retrieve functional scores for the proxy-matched observation.
4. Record the full proxy chain (e.g., "imatinib → dasatinib via Tanimoto 0.78" or "A549 → NCI-H226 via lung/NSCLC/adenocarcinoma").

**Confidence:** 
- `medium` for single-proxy (PROXY_PERT or PROXY_CELL): validated by 7/7 matrix test
- `low` for double-proxy (PROXY_BOTH): multiple approximations compound error

**Similarity threshold requirement (mandated by protocol):**
- Drug proxy: Tanimoto similarity ≥ 0.40 (T_DRUG_PROXY_THRESHOLD)
- Gene proxy: cosine similarity ≥ 0.50 (per gene_neighbors integer coding: ≥ 50)
- Cell-line proxy: must belong to same lineage/disease/subtype group
- If no neighbor exceeds threshold, route falls through to no-hit

**Supported by evidence:**
- T-007: resolver proxy logic validated in 7/7 matrix (PROXY_PERT, PROXY_CELL, PROXY_BOTH all passed)
- T-058: SC-017, SC-018, SC-019, SC-020 all marked PASS
- T-021: drug_neighbors (5,312 drugs), gene_neighbors (33,791 entries), cellline_neighbors available
- T-013: CAP-05 — proxy without threshold risks false positive; threshold enforcement is mandatory per protocol constraint

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-004 | proxy-hit (PROXY_CELL) | Forward: perturbation="gefitinib" (exact), cell_line="NCI-H226" (proxy) | drug_index → BRD-K68045993 (exact); cellline_index → NCI-H226 not valid matrix cell → cellline_neighbors → lung/NSCLC/adenocarcinoma → A549 as proxy; cp_func_ad.h5ad → A549 row for gefitinib | route_type=proxy-hit, query_context=A549(via NCI-H226)/compound, perturbation_resolution=exact_match, function_response=91-score vector, confidence=medium, proxy_chain="cell: NCI-H226 → A549 via lung/NSCLC/adenocarcinoma", diagnostics={warn: "cell_line_proxy_used"}, suggestions=[] | 91-score vector returned; proxy_chain documents exact path; confidence=medium not high | SC-018 (proxy cell) |
| AC-005 | proxy-hit (PROXY_PERT) | Forward: perturbation="imatinib" (not in matrix, but neighbor available), cell_line="A375" (exact) | drug_index → imatinib not in matrix obs → drug_neighbors → nearest neighbor dasatinib (Tanimoto ≥ 0.40) → cp_func_ad.h5ad → A375 row for dasatinib | route_type=proxy-hit, query_context=A375/compound, perturbation_resolution=proxy_neighbor, function_response=91-score vector, confidence=medium, proxy_chain="pert: imatinib → dasatinib via Tanimoto 0.78", diagnostics={warn: "perturbation_proxy_used"}, suggestions=[] | 91-score vector returned using neighbor drug; proxy_chain cites exact neighbor and similarity score | SC-020 (proxy pert) |
| AC-006 | proxy-hit (PROXY_BOTH) | Forward: perturbation="imatinib" (proxy), cell_line="NCI-H226" (proxy) | drug_neighbors → dasatinib; cellline_neighbors → A549; cp_func_ad.h5ad → A549 row for dasatinib | route_type=proxy-hit, query_context=A549(via NCI-H226)/compound, perturbation_resolution=proxy_neighbor, function_response=91-score vector, confidence=low, proxy_chain=["cell: NCI-H226 → A549 via lung/NSCLC/adenocarcinoma", "pert: imatinib → dasatinib via Tanimoto 0.78"], diagnostics={warn: "double_proxy_used"}, suggestions=["Consider using A549 as cell_line directly for higher confidence"] | 91-score vector returned; confidence=low; both proxy chains documented; suggestions include reformulated query | SC-019 (proxy both) |
| AC-007 | proxy-hit (threshold guard) | Forward: perturbation="ZZZ-FAKE-DRUG-12345", cell_line="A549" (exact) | drug_index → no match; drug_neighbors → no neighbor above Tanimoto 0.40 threshold | route_type=no-hit (see §2.3) | This case demonstrates proxy threshold guard: despite fuzzy matching finding some token overlap, the similarity threshold blocks escalation to proxy-hit. Routes to no-hit instead. | — |

### 2.3 no-hit

**Definition:** No resolvable perturbation exists in the index, no neighbor exceeds the similarity threshold, or the context/perturbation combination has no observation in any functional matrix. Returns a structured NO_HIT result with diagnostic metadata and transfer suggestions.

**Mandatory similarity thresholding (protocol constraint):**
- **Explicit threshold required.** The current fuzzy fallback behavior (CAP-05, T-013) that matches meaningless perturbation names to real gene names without similarity thresholding is explicitly disallowed.
- Perturbation matching must pass through:
  1. Exact match in index (→ exact-hit or proxy-hit for context dimension).
  2. If no exact match: neighbor lookup with threshold (→ proxy-hit if neighbor passes threshold).
  3. If no neighbor above threshold: → no-hit.
- **Fuzzy / token-similarity fallback without similarity thresholding is disallowed.** The CAP-05 evidence from T-013 shows this produces false positives.

**Resolution path:**
1. Perturbation not found in drug_index, gene_index, or gene_index_simple.
2. OR: perturbation found but no neighbor above the threshold in drug_neighbors or gene_neighbors.
3. OR: perturbation resolved but no observation in any functional matrix for the given cell context.
4. Result: `function_response = NO_HIT` with full diagnostic metadata.

**Confidence:** `high` (negative determination is precise when thresholded and index-verified).

**Diagnostic metadata must include:**
- Which index was searched (drug/gene/cellline)
- Whether any partial/token match was found (without threshold claims)
- Whether any neighbor was found below threshold
- Which standard resources were consulted

**Supported by evidence:**
- T-013 CAP-05: the current no-hit path is unsafe; fuzzy fallback produces false positives
- T-007: generic drug queries (e.g., "EGFR inhibitor") return NOT_FOUND in some modes
- T-058: SC-011 (generic drug), SC-012 (free-text), SC-013 (impossible combo) all test no-hit behavior
- A-005: NOT_FOUND for generic drugs is a known risk pattern

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-008 | no-hit (unknown perturbation) | Forward: perturbation="ZZZ-FAKE-GENE-XYZ", cell_line="A549" | gene_index → no match; gene_index_simple → no match; gene_neighbors → no neighbor above cosine 0.50 | route_type=no-hit, query_context=A549/gene, perturbation_resolution=unmatched, function_response=NO_HIT, confidence=high, proxy_chain=null, diagnostics={perturbation_not_found: true, indexes_searched: ["gene_index", "gene_index_simple", "gene_neighbors"], neighbor_search: "no_candidate_above_threshold"}, suggestions=["Check perturbation name spelling", "Try HUGO gene symbol or common alias"] | NO_HIT result; diagnostics confirm exhaustive index search; no false proxy; suggestions provide actionable guidance | SC-008 (fake drug, adapted) |
| AC-009 | no-hit (generic drug, threshold blocked) | Forward: perturbation="EGFR inhibitor", cell_line="A549" | drug_index → no exact match for free-text "EGFR inhibitor"; drug_neighbors → no structured neighbor for free-text query → threshold cannot be applied → no-hit | route_type=no-hit, query_context=A549/compound, perturbation_resolution=unmatched, function_response=NO_HIT, confidence=high, proxy_chain=null, diagnostics={perturbation_not_found: true, free_text_query: true, note: "free-text drug descriptions cannot be resolved deterministically. LLM-assisted resolution is a separate path."}, suggestions=["Try a specific drug name: gefitinib, erlotinib, osimertinib", "Try BRD-ID if available"] | NO_HIT result; diagnostics note that free-text drug descriptions are not deterministically resolvable; suggestions list specific exact-match alternatives from the same drug class | SC-011 (generic drug description) |
| AC-010 | no-hit (no observation in matrix) | Forward: perturbation="aspirin" (in drug_index but not in any matrix obs), cell_line="A549" | drug_index → BRD match found; cp_func_ad.h5ad → no obs row with pert_id=aspirin AND cell_iname=A549; sh_func_ad/xpr_func_ad → no matching obs | route_type=no-hit, query_context=A549/compound, perturbation_resolution=identified_but_no_observation, function_response=NO_HIT, confidence=high, proxy_chain=null, diagnostics={perturbation_identified: true, perturbation_id: "BRD-KXXXXXX", matrices_searched: ["cp", "sh", "xpr"], cell_line: "A549", result: "no_observation_for_this_context"}, suggestions=["Try a related perturbation with LINCS data", "Use proxy search with drug neighbors"] | NO_HIT with identified perturbation noted; diagnostics show all three matrices searched; suggestions offer alternative routes | SC-013 (impossible combo, adapted) |
| AC-011 | no-hit (threshold-enforced guard) | Forward: perturbation="ZZZ-RANDOM-TOKEN", cell_line="A549" | gene_index → no match; token-similarity fuzzy match would hit "ZZZ3" gene but similarity < threshold → blocked | route_type=no-hit, query_context=A549/gene, perturbation_resolution=unmatched, function_response=NO_HIT, confidence=high, proxy_chain=null, diagnostics={perturbation_not_found: true, fuzzy_candidate_blocked: "ZZZ3 (similarity below threshold)", threshold_applied: "cosine >=0.50"}, suggestions=["Check perturbation name", "ZZZ3 is a real gene — did you mean ZZZ3?"] | NO_HIT result; diagnostics explicitly show fuzzy match was considered and blocked by threshold; suggestion offers nearest plausible redirect | CAP-05 evidence from T-013 |

### 2.4 ambiguous-hit

**Definition:** Query resolves to multiple plausible perturbations or biological contexts where a single top result cannot be confidently selected. Returns ranked candidates with confidence scores and disambiguation guidance.

**Common triggers:**
- Perturbation name matches multiple gene symbols or aliases.
- Drug name matches multiple BRD-IDs or salt forms.
- Cell line name is ambiguous (e.g., common abbreviation matching multiple cell lines).
- Reverse query returns many candidates with near-identical functional scores.

**Resolution path:**
1. Multiple index entries match the perturbation query.
2. Each candidate is resolved against the biological context.
3. Candidates are ranked by:
   - If forward: presence in functional matrix with the requested cell context.
   - If reverse: functional score for the target function.
4. If top-1 and top-2 scores are within epsilon (ε = 0.01), or if multiple candidates map to different perturbation types, the result is ambiguous.

**Confidence:** `low` — multiple valid interpretations exist.

**Supported by evidence:**
- T-007: gene_index contains 78,061 entries; gene_index_simple has 25,036; name collisions are structurally possible
- T-058: no specific ambiguous-hit scenario in the 29-scenario catalog (this is a gap—complex queries SC-001 through SC-003 could trigger ambiguity with multi-gene inputs, but the scenarios are designed as multi-gene coordination tests, not name-collision tests)
- T-013: no explicit ambiguous-hit evidence

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-012 | ambiguous-hit (gene collision) | Forward: perturbation="ACT", cell_line="A549" | gene_index → multiple matches (e.g., ACTA1, ACTA2, ACTB, ACTC1, ACTG1, ACTG2, ACTN1-4, ACTR, etc.); all valid gene symbols; ambiguous without disambiguation | route_type=ambiguous-hit, query_context=A549/gene, perturbation_resolution=ambiguous, function_response=NO_RANKING (cannot select single perturbation), confidence=low, proxy_chain=null, diagnostics={ambiguous_perturbation: true, candidates: ["ACTA1", "ACTB", ...], candidate_count: N}, suggestions=["Select a specific gene from the candidate list", "Use full gene symbol (e.g., ACTB) for exact match"] | Ambiguous-hit returned with ranked/filtered candidate list; candidates present in A549 matrix observations shown first; user prompted for disambiguation | — (no direct T-058 scenario; gap noted) |
| AC-013 | ambiguous-hit (reverse near-tie) | Reverse: function_target="HALLMARK_APOPTOSIS", direction="activate", cell_line="A549" | function_index → HALLMARK_APOPTOSIS; cp_func_ad.h5ad → ranked pert_ids by apoptosis score; top-2 candidates have scores within ε=0.01 of each other | route_type=ambiguous-hit, query_context=A549/reverse, perturbation_resolution=ambiguous_ranking, function_response={candidates: [{pert_id, score, rank}, ...], tie_epsilon: 0.01}, confidence=low, proxy_chain=null, diagnostics={near_tie: true, score_difference: 0.003, top_candidates: [pert_1, pert_2]}, suggestions=["Top candidates have near-identical scores", "Consider additional filtering by drug class or mechanism"] | Both top candidates returned with near-identical scores; user informed of near-tie; ranking with score difference documented | SC-006 (adapted to near-tie condition) |
| AC-014 | ambiguous-hit (drug multi-BRD) | Forward: perturbation="dexamethasone", cell_line="A549" | drug_index → multiple BRD-IDs (multiple salt forms/formulations); cp_func_ad.h5ad → observations exist for multiple BRD-IDs with A549 | route_type=ambiguous-hit, query_context=A549/compound, perturbation_resolution=ambiguous, function_response={candidates: [{brd_id, cmap_name, sig_id}, ...]}, confidence=low, proxy_chain=null, diagnostics={multiple_brd_ids: true, candidate_count: K}, suggestions=["Multiple BRD-IDs found for dexamethasone", "Select a specific BRD-ID for exact retrieval"] | Multiple BRD-IDs returned with metadata; user can select one or route all to function_response aggregation | — (no direct T-058 scenario; gap noted) |

### 2.5 context-missing

**Definition:** Query lacks the biological context required for functional matrix retrieval. Returns a prompt for required context fields with validation rules, without proceeding to matrix lookup.

**Required context fields:**
| Field | Required | Validation rule |
|---|---|---|
| cell_line | yes (for forward/reverse with context) | Must be in cellline_index.json or have a valid proxy path |
| direction | yes (for forward) | Must be "forward" or "reverse" |
| function_target | yes (for reverse) | Must be in function_index.json (91 HALLMARK or 3CA MPS terms) |

**Resolution path:**
1. Parse query for cell_line.
2. If missing: return context-missing with prompt for cell_line.
3. If present but invalid: return context-missing with validation error and suggestions from cellline_index.
4. For reverse: additionally require function_target.

**Confidence:** Not applicable — no functional retrieval attempted.

**Supported by evidence:**
- T-058: SC-009 (empty input), SC-010 (typo cell) test boundary conditions
- T-007: cellline_index.json exists with valid cells list; current resolver requires cell context

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-015 | context-missing | Forward: perturbation="gefitinib", direction="forward", cell_line=missing | No cell_line in query → cannot select matrix or row | route_type=context-missing, query_context=null, perturbation_resolution=exact_match (drug identified but not resolved), function_response=NO_RETRIEVAL, confidence=n/a, proxy_chain=null, diagnostics={missing_fields: ["cell_line"], required: ["cell_line"], found: {perturbation: "gefitinib", perturbation_type: "compound"}}, suggestions=["Provide a cell line name (e.g., A549, MCF7, PC3)", "Cell lines available in the index: A549, A375, MCF7, ..."] | Context-missing returned; identified fields listed; missing fields enumerated; suggestions include example cell lines from the index | SC-009 (empty input, adapted) |
| AC-016 | context-missing (reverse) | Reverse: function_target="HALLMARK_APOPTOSIS", direction="reverse", cell_line=missing | function_index → HALLMARK_APOPTOSIS found; cell_line missing → cannot filter observations | route_type=context-missing, query_context=null, perturbation_resolution=n/a, function_response=NO_RETRIEVAL, confidence=n/a, proxy_chain=null, diagnostics={missing_fields: ["cell_line"], required: ["cell_line"], found: {function_target: "HALLMARK_APOPTOSIS", direction: "reverse"}}, suggestions=["Provide a cell line for candidate filtering", "Available: A549, MCF7, PC3, ..."] | Context-missing returned; identified function_target noted; cell_line prompt issued | SC-009 variant |
| AC-017 | context-missing (invalid cell_line) | Forward: perturbation="gefitinib", cell_line="ZZZ-INVALID-CELL" | cellline_index → no match; cellline_neighbors → no valid proxy path; cell_line invalid | route_type=context-missing, query_context=null, perturbation_resolution=exact_match (drug identified), function_response=NO_RETRIEVAL, confidence=n/a, proxy_chain=null, diagnostics={invalid_fields: ["cell_line: ZZZ-INVALID-CELL not found in cellline_index"], missing_fields: [], required: ["valid cell_line"]}, suggestions=["Cell line 'ZZZ-INVALID-CELL' not found", "Did you mean one of: A549, A375, ...?"] | Context-missing with validation error; invalid field flagged; nearest cell-line suggestions from index | SC-010 (typo cell) |

### 2.6 transfer/suggestion

**Definition:** When a query produces no-hit or ambiguous-hit, the system provides user-facing suggestions for reformulated queries, alternative biological contexts, or related perturbations that may yield results. This route does not produce functional scores directly—it produces actionable next steps.

**This is a required capability per the project goal (1_goal.md):** "resolver-mediated natural-language or semi-structured query entry" and "transfer/suggestion semantics." It cannot be reduced to returning empty results.

**Transfer/suggestion must include:**
1. **Reformulated query suggestions:** Specific, executable alternatives (e.g., "Try gefitinib instead of EGFR inhibitor").
2. **Alternative context suggestions:** Related cell lines or tissue contexts where the perturbation may have data.
3. **Related perturbation suggestions:** Structurally or functionally similar perturbations with data coverage.
4. **LLM-assisted explanation (when LLM mode is enabled):** A human-readable explanation of why the original query failed and what the nearest reachable alternatives are. This is distinct from deterministic proxy behavior—it generates user-facing text, not a proxy substitution.

**Distinction from other routes:**
- **Not proxy-hit:** Transfer/suggestion presents alternatives to the user without automatically substituting them. Proxy-hit selects and uses the proxy automatically.
- **Not no-hit:** No-hit returns diagnostic metadata; transfer/suggestion builds on no-hit to generate user-facing next steps.
- **LLM-assisted explanation is separate from deterministic transfer:** The deterministic path generates specific index-based suggestions (alternative cell lines, drug names, gene symbols). The LLM path generates natural-language explanations of why the query could not be resolved.

**Resolution path (triggered by no-hit or ambiguous-hit):**
1. From no-hit diagnostics, extract: searched indexes, perturbation name, cell context.
2. Generate deterministic suggestions:
   - Alternative cell lines: from same lineage/disease/subtype via cellline_neighbors.
   - Alternative perturbations: from the same drug/gene class or with similar Tanimoto/cosine values (even if below proxy threshold).
   - Known perturbations with data in the requested cell context.
3. If LLM mode is enabled: augment with natural-language explanation.
4. Return as the `suggestions` array in evidence metadata.

**Supported by evidence:**
- Project goal §Functional Delivery Goal: "resolver-mediated natural-language or semi-structured query entry" and "transfer/suggestion" are required capabilities
- T-013 CAP-07: resolver blocked by index issues; transfer/suggestion must be defined even if full resolver is not yet operational
- T-058: no direct transfer/suggestion scenarios; this is part of the anchor specification that T-064 defines for future stress testing
- T-007: development interpretation says "LLMs assist parsing/summarization, not scientific core" — transfer/suggestion aligns with this: deterministic suggestions are core, LLM explanation is supplementary

**Acceptance cases:**

| # | Route type | Input query description | Expected resolution path | Expected evidence metadata | Pass condition | T-058 scenario |
|---|---|---|---|---|---|---|
| AC-018 | transfer/suggestion (from no-hit) | Forward: perturbation="EGFR inhibitor", cell_line="A549" → routes to no-hit (see AC-009) → transfer/suggestion generated | no-hit diagnostics → deterministic suggestions: [gefitinib, erlotinib, osimertinib, afatinib] from drug_index/drug_neighbors in EGFR TKI class | route_type=transfer/suggestion, query_context=A549/compound, perturbation_resolution=unmatched, function_response=NO_HIT, confidence=high, proxy_chain=null, diagnostics={inherited from no-hit}, suggestions=[{type: "reformulated_query", text: "Try 'gefitinib' (BRD-K68045993) in A549", action: "forward_query(perturbation='gefitinib', cell_line='A549')"}, {type: "related_perturbation", text: "Related EGFR-targeting compounds: erlotinib, osimertinib, afatinib"}, {type: "alternative_context", text: "EGFR perturbation data also available in A375, MCF7"}] | Suggestions array populated with specific executable alternatives; each suggestion has type, text, and action; transfer/suggestion built on no-hit diagnostics | SC-011 (generic drug description, transfer layer) |
| AC-019 | transfer/suggestion (from ambiguous-hit) | Forward: perturbation="ACT", cell_line="A549" → routes to ambiguous-hit (see AC-012) → transfer/suggestion generated | ambiguous-hit diagnostics → candidate list → suggestions: [select specific gene, show candidates with data in A549 first] | route_type=transfer/suggestion, query_context=A549/gene, perturbation_resolution=ambiguous, function_response=NO_RANKING, confidence=low, proxy_chain=null, diagnostics={inherited from ambiguous-hit}, suggestions=[{type: "disambiguation", text: "Select a specific gene from: ACTA1, ACTB, ACTG1 (have data in A549)", options: ["ACTA1", "ACTB", "ACTG1"]}, {type: "reformulated_query", text: "Try 'ACTB' for exact match", action: "forward_query(perturbation='ACTB', cell_line='A549')"}] | Suggestions include disambiguation options prioritized by data availability; user can select from list or enter reformulated query | — (gap for future stress test) |
| AC-020 | transfer/suggestion (LLM-assisted, when enabled) | Forward: perturbation="EGFR inhibitor in lung cancer", cell_line=missing → routes to context-missing → transfer/suggestion with LLM | Deterministic context-missing diagnostics → LLM generates: "Your query 'EGFR inhibitor in lung cancer' is missing a specific cell line and uses a general drug class name. Here are specific suggestions: 1) Try 'gefitinib' in 'A549' (non-small cell lung cancer), 2) Try 'erlotinib' in 'NCI-H226' (lung squamous cell carcinoma). EGFR-targeting compounds with LINCS data in lung cancer lines include gefitinib, erlotinib, afatinib, and osimertinib." | route_type=transfer/suggestion, query_context=null, perturbation_resolution=unmatched, function_response=NO_RETRIEVAL, confidence=n/a, proxy_chain=null, diagnostics={inherited from context-missing}, suggestions=[{type: "llm_explanation", text: "...", llm_mode: "enabled"}, {type: "reformulated_query", text: "Try gefitinib in A549", action: "..."}] | LLM-assisted suggestions are generated only when LLM mode is enabled; deterministic fallback suggestions provided even without LLM; LLM explanation clearly labeled as LLM-generated | SC-012 (free-text context, with LLM augmentation) |
| AC-021 | transfer/suggestion (deterministic fallback, LLM disabled) | Same as AC-020 but LLM mode disabled | Deterministic context-missing diagnostics → suggestions: [provide cell_line, try specific drug names] without natural-language narrative | route_type=transfer/suggestion, query_context=null, perturbation_resolution=unmatched, function_response=NO_RETRIEVAL, confidence=n/a, proxy_chain=null, diagnostics={inherited from context-missing}, suggestions=[{type: "missing_field", text: "Provide a cell line (e.g., A549)", required_field: "cell_line"}, {type: "reformulated_query", text: "Try a specific drug name instead of drug class", examples: ["gefitinib", "erlotinib"]}] | Deterministic suggestions are functional and actionable; no LLM-dependent text; format is structured, not narrative | SC-011/SC-012 deterministic path |

---

## 3. Route Decision Flow

```
Query enters
  │
  ├── cell_line missing? ──YES──► context-missing ──► transfer/suggestion
  │
  ├── function_target (reverse) invalid/missing? ──YES──► context-missing ──► transfer/suggestion
  │
  ├── perturbation in index? ──NO──► perturbation in neighbor index above threshold? ──NO──► no-hit ──► transfer/suggestion
  │                                    │
  │                                    └── YES ──► proxy-hit (PROXY_PERT)
  │
  ├── cell_line in matrix obs? ──NO──► cell_line in neighbors? ──NO──► no-hit ──► transfer/suggestion
  │                                      │
  │                                      └── YES ──► proxy-hit (PROXY_CELL)
  │
  ├── perturbation resolves to multiple candidates? ──YES──► ambiguous-hit ──► transfer/suggestion
  │
  └── both exact AND obs exists ──► exact-hit
```

**Priority order within proxy-hit:**
- PROXY_CELL (preferred): exact perturbation is more informative than exact context
- PROXY_PERT: exact context with proxy perturbation
- PROXY_BOTH: last resort, confidence=low

---

## 4. Distinction Between Deterministic, Proxy, and LLM-Assisted Routing

| Layer | Mechanism | When used | Dependencies | Confidence |
|---|---|---|---|---|
| Deterministic (exact-hit, no-hit) | Index lookup + matrix retrieval | Primary path; always attempted first | drug_index, gene_index, cellline_index, functional matrices | high |
| Proxy (proxy-hit) | Neighbor-index lookup with similarity thresholds | When deterministic exact match fails; applied transparently | drug_neighbors, gene_neighbors, cellline_neighbors | medium (single), low (double) |
| No-hit routing (no-hit + threshold guard) | Negative determination after exhaustive index search | When perturbation not found AND no neighbor above threshold | All indexes + threshold enforcement | high (for the negative determination) |
| Transfer/suggestion | Suggestions derived from no-hit/ambiguous diagnostics | After no-hit or ambiguous-hit; presented to user not applied | Index metadata + (optionally) LLM explanation | n/a (provides guidance not results) |
| LLM-assisted explanation | Natural-language text generation for user-facing suggestions | Only when LLM mode enabled; never used for retrieval decisions | LLM provider (MiniMax or configured endpoint) | low (6/9 stability per A-005) |

**Key separation rule:** LLM is never used for the retrieval decision (which route, which perturbation, which matrix row). LLM is only used for user-facing explanation and query parsing. Retrieval decisions are always deterministic (index + threshold) or proxy (index + threshold + neighbor). This separation is mandated by T-007's development interpretation and A-005's risk evidence (LLM stability 6/9).

---

## 5. Gaps and Caveats

### 5.1 Gap: ambiguous-hit not covered by T-058 scenarios

The 29 T-058 stress-test scenarios do not include a dedicated ambiguous-hit scenario. Complex multi-gene queries (SC-001–SC-003) test coordination of multiple perturbations, not name-collision ambiguity. A future stress-test milestone should add scenarios for:
- Gene symbol collision (e.g., short names matching multiple full symbols)
- Drug multi-BRD-ID resolution
- Reverse query near-tie ranking

### 5.2 Caveat: transfer/suggestion requires user-facing semantics

Per protocol constraint, the transfer/suggestion route must describe "user-facing semantics: what a user sees, not just an empty result or error code." Acceptance cases AC-018 through AC-021 define these semantics. Future implementation must render suggestions as actionable UI elements (clickable queries, selectable options, formatted text), not as log-level diagnostics.

### 5.3 Caveat: LLM-assisted transfer is supplementary

Per A-005 and T-007, the LLM path has 6/9 stability and 167.3s latency in always_llm mode. LLM-assisted transfer/suggestion explanations should be treated as supplementary convenience, not as the only user-facing output. Deterministic transfer suggestions (based on index metadata and neighbor proximity) must always be produced regardless of LLM availability.

### 5.4 Gap: function_index.json runtime availability

While T-021 rebuilt the function_index.json as a standard resource, the runtime path expected by the pxfquery package (the current resolver) may not align. Transfer/suggestion and reverse routing that reference function terms depend on this index being loadable at runtime, not just available on disk.

---

## 6. References to T-021 Standard Resources

| Route type | Standard resources referenced | How used |
|---|---|---|
| exact-hit | drug_index, gene_index, cellline_index, function_index, cp/sh/xpr_func_ad | Exact lookup → matrix retrieval |
| proxy-hit | drug_neighbors, gene_neighbors, cellline_neighbors, drug_index, gene_index, cellline_index, cp/sh/xpr_func_ad | Neighbor lookup with threshold → matrix retrieval |
| no-hit | drug_index, gene_index, gene_index_simple, cellline_index, drug_neighbors, gene_neighbors | Exhaustive search → negative determination |
| ambiguous-hit | drug_index, gene_index, cellline_index, cp/sh/xpr_func_ad | Multi-match detection → candidate ranking |
| context-missing | cellline_index, function_index | Validation of required fields |
| transfer/suggestion | cellline_neighbors, drug_neighbors, gene_neighbors, function_index, cellline_meta, compound_meta | Suggestion generation from index metadata |

---

## 7. Acceptance Criteria Cross-Reference

| Protocol acceptance criterion | Covered by | Status |
|---|---|---|
| All six route types defined with concrete acceptance cases | §2.1–2.6, AC-001 through AC-021 | ✓ |
| Each acceptance case includes route type, input query, expected resolution path, evidence metadata fields, pass condition | All AC tables | ✓ |
| No-hit route requires explicit similarity thresholding; fuzzy fallback disallowed unless thresholded | §2.3, AC-007, AC-011 | ✓ |
| Transfer/suggestion route describes user-facing suggestion semantics | §2.6, AC-018–AC-021 | ✓ |
| Route definitions reference T-021 standard resources where applicable | §1 (Canonical Resource Set), §6 | ✓ |
| Distinguish deterministic fallback, proxy evidence, and LLM-assisted explanation | §4 (Distinction Table) | ✓ |
| Stress-test mapping covers all 29 T-058 scenarios | See stress_test_mapping deliverable | ✓ |