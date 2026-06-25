# T-056 02_stress_query_scenario_inventory — Protocol

## Objective

Abstract a future stress-test scenario inventory from migrated materials and T-007 digestion results. The inventory must cover: complex queries, strict queries, boundary queries, no-hit (NOT_FOUND) behavior, overly broad results, proxy/exact matching edge cases, and difficult perturbation/cell-line/function combinations. Deliver scenarios and rationale only — not implementation or test execution.

## Position In Project

This is a digestion-phase task under goal_legacy_stress_test_asset_digestion. It precedes any actual stress-test execution tasks. It consumes T-007's development-state understanding to derive what a future stress-test framework must cover, without running tests or building infrastructure.

T-041 (legacy_source_digest_for_m1) is still active; omitted per constraint.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Forward/reverse query mechanism, resolver modes, index gaps — foundational for scenario categories |
| A-002 | T-007/D-005 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps/risks directly inform stress-test pattern categories |
| A-003 | T-007/D-006 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Concrete query examples and do-not-do boundaries |
| A-004 | T-007/D-003 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Module coverage verification for scenario completeness |
| A-005 | T-007/D-004 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Historical pass/fail patterns as scenario data points |
| A-006 | T-007/M-0257 | reports/validation_reports/M-0257_6_llm_resovler_forward_matrix.md | 7/7 deterministic EXACT/PROXY test cases as scenario templates |
| A-007 | T-007/M-0243 | reports/validation_reports/M-0243_known_risks.md | LLM stability risks, mode inconsistency, NOT_FOUND+PROXY boundaries |
| A-008 | T-007/M-0239 | reports/validation_reports/M-0239_latest_reports_index.md | Authority rules for validation conflict resolution |

## Execution Steps

1. Read all registered input assets (A-001 through A-008) to extract query semantics, resolver behavior, known edge cases, and validation evidence.
2. Derive and categorize stress-test scenarios covering these dimensions:
   - **Complex queries**: multi-gene, multi-drug, combined perturbation+context queries that stress resolver intent parsing and evidence bundling
   - **Strict queries**: exact-match-only cases that should produce EXACT hits; cases where proxy fallback should be explicitly disallowed
   - **Boundary queries**: cell-line not in index, drug not in index, function alias edge cases, empty/partial perturbation strings
   - **No-hit behavior**: queries expected to produce NOT_FOUND — generic drug descriptions (EGFR inhibitor), unknown cell lines, impossible gene+context combinations
   - **Overly broad results**: queries likely to produce many proxy hits or ambiguous evidence bundles (common drugs like DMSO, pan-cancer queries)
   - **Proxy/exact matching**: cases where EXACT vs PROXY_PERT vs PROXY_CELL vs PROXY_BOTH must be explicitly distinguished and the boundary tested
   - **Difficult combos**: perturbation+cell-line+function triples that are biologically questionable, conflict across indexes, or fail in historical reports
   - **LLM mode cross-checks**: scenarios where always_llm vs hybrid_fast vs deterministic produce different results
   - **Missing/partial index**: function_index.json gap scenarios, partial neighbor failures
3. For each scenario, record: unique ID, category, query parameters (forward/reverse, perturbation, context, function intent), expected resolver hit level, expected pass/fail, rationale citing specific source evidence, and notes on historical validation status.
4. Compile the narrative inventory document from step 3 results.
5. Compile the tabular CSV from the same scenario records.
6. Register outputs in 4_artifact/registry.yaml.

## Constraints

- Deliver stress-test scenarios and rationale only. Do not implement test code, run queries, or build test infrastructure.
- Do not reference T-041; it is still active and not available.
- Do not read old legacy root scripts or run them.
- Base all scenario derivation on the 8 registered input assets only.
- Keep scenarios grounded in T-007 evidence (validation reports, gaps, known risks). Do not invent hypothetical scenarios without documented precedent.
- Use the latest-reports-index (A-008) authority rules when historical validation reports conflict.

## Forbidden

- No test execution or query runs.
- No modification of predecessor artifacts or project assets.
- No creation of package code or test scripts.
- No reading of T-041 outputs.
- No web search for external information.

## Web Search Allowance

Allowed: no
Reason: All required information is available in registered T-007 artifacts and project assets.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Stress-test scenario inventory (narrative) | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | yes |
| Stress-test scenario table (CSV) | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | yes |
| Artifact registry update | 4_artifact/registry.yaml | yes |

## Acceptance Criteria

- Inventory covers all 9 scenario dimensions listed in Execution Steps step 2.
- Each scenario has a unique ID, category, query parameters, expected resolver hit level, expected pass/fail, rationale citing specific source evidence.
- CSV table has one row per scenario with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence.
- Narrative document explains each scenario's motivation and traces back to registered asset evidence.
- No implementation code or test scripts are delivered.
- Outputs are registered in 4_artifact/registry.yaml.

## Failure / Stop Rules

- If any required input asset (A-001 through A-008) is unreadable or corrupted, report and stop.
- If scenario derivation cannot be grounded in registered asset evidence, mark those scenarios as speculative with explicit notes.

## Delivery Requirements

- Register all accepted outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
