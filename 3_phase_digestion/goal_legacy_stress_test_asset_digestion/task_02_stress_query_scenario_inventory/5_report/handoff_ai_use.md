# AI Handoff: T-056 02_stress_query_scenario_inventory

## Task Goal

Abstract a future stress-test scenario inventory from migrated T-007 materials. Cover 9 dimensions: complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index. Deliver rationale only — no implementation.

## What Was Delivered

- Narrative inventory (29 scenarios) with full evidence traceback to registered T-007 assets
- Tabular CSV (29 rows) with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- Artifact registry updated with D-001, D-002, D-003, D-004
- Delivery QA reports (execution_report, result_report, delivery_qa)

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | Complete narrative of all 29 scenarios with rationale | Read first to understand scenario motivation and evidence basis |
| D-002 | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | Machine-parseable scenario table | Load as CSV in test framework; select rows by category for focused test suites |

## Supporting Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-003 | 4_artifact/3_document/execution_report_v20260624.html | Documents execution process | Human review of what was done |
| D-004 | 4_artifact/3_document/result_report_v20260624.html | Summarizes coverage and acceptance | Human review of output completeness |

## Downstream Use

A future stress-test execution task (e.g., T-057 or later) should:
1. Read D-001 for narrative context and evidence traces
2. Parse D-002 CSV to select scenario rows by category
3. Implement test harness code that exercises pxfquery forward/reverse query API with each scenario's perturbation/context/function parameters
4. Compare actual resolver hit levels against expected_hit_level and expected_result
5. Report deviations as test failures or documentation gaps

## Known Limits / Risks

- 4 scenarios (SC-014, SC-015, SC-016, SC-029) are marked speculative — exact behavior may differ from prediction
- 2 scenarios (SC-011, SC-012) are mode-dependent (LLM mode changes expected result)
- 1 scenario (SC-009, empty perturbation) has no direct T-007 precedent — derived from documented gaps
- Scenarios assume current pxfquery development state as of T-007 (2026-06-17); code changes since then may affect expected results

## Do Not Read / Do Not Reuse

- T-041 outputs — explicitly omitted per protocol constraint
- Old legacy root scripts — not current acceptance criteria
- 3_execution/ contents — empty for this task

## Recommended Next Reads

1. D-001 (narrative inventory) — full scenario rationale
2. D-002 (CSV table) — structured scenario data
3. A-001/A-002 (T-007 source assets) if deeper evidence traceback needed
