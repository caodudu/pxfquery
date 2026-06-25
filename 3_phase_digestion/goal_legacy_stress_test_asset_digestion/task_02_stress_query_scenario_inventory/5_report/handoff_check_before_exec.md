# Check Handoff Before Exec: T-056 02_stress_query_scenario_inventory

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories, `2_project_asset/` (read-only via symlinks), non-modifiable per asset_rule.yaml
- Required registry: `4_artifact/registry.yaml` — currently empty, must be updated after deliverables
- Must stop if: any step attempts to run test code, execute queries, modify predecessor assets, or read T-041 outputs

## Objective Restatement
Derive a categorized stress-test scenario inventory (narrative + CSV) from 8 registered T-007 assets. Cover 9 scenario dimensions: complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index. Deliver rationale only — no implementation, no test execution, no legacy root reads.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/pxfquery_development_state_report.md` | Forward/reverse query mechanism, resolver modes, index gaps — foundational for scenario categories | ok |
| A-002 | `1_asset/pxfquery_gap_and_risk_list.md` | Known gaps/risks directly inform stress-test pattern categories | ok |
| A-003 | `1_asset/pxfquery_development_handoff.md` | Concrete query examples (EGFR/A549, apoptosis/MYC/A549) and do-not-do boundaries | ok |
| A-004 | `1_asset/pxfquery_module_asset_status_matrix.csv` | Module coverage verification for scenario completeness | ok |
| A-005 | `1_asset/pxfquery_validation_evidence_index.csv` | Historical pass/fail patterns as scenario data points | ok |
| A-006 | `1_asset/forward_matrix_test_report.md` | 7/7 deterministic EXACT/PROXY test cases as scenario templates | ok |
| A-007 | `1_asset/known_risks_list.md` | LLM stability risks, mode inconsistency, NOT_FOUND+PROXY boundaries | ok |
| A-008 | `1_asset/latest_reports_index.md` | Authority rules for validation conflict resolution | ok |

## Execution Strategy
1. Read all 8 registered input assets (A-001 through A-008) — extract query semantics, resolver modes, known edge cases, historical validation evidence.
2. Derive and categorize stress-test scenarios across all 9 dimensions listed in protocol step 2.
3. For each scenario, record: unique ID, category, query parameters (forward/reverse, perturbation, context, function intent), expected resolver hit level, expected pass/fail, rationale citing specific source evidence, source reference.
4. Compile narrative inventory document (`4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md`) — explain each scenario's motivation with evidence traceback.
5. Compile tabular CSV (`4_artifact/5_table/stress_query_scenario_table_v20260624.csv`) — one row per scenario with all columns.
6. Update `4_artifact/registry.yaml` with both output artifacts.
7. (Optional) Write execution summary to `5_report/completion.md`.

## Conservative Execution Advice
- Start with: Read A-001 (development state report) to understand query model, then read A-007 (known risks) for concrete edge cases — these two provide the widest coverage.
- Smoke/demo method: After reading 2-3 assets, draft 5 representative scenarios covering 5 different categories to confirm the derivation pattern works before scaling to full set.
- Full run only after: the 5-scenario smoke draft is coherent and correctly cites sources.
- Cost/time risk: Low — all processing is local file reading and document writing. No API calls, no test execution. Estimated 1-2 hours for thorough coverage.
- Checkpoint advice: After step 2 (scenario derivation), commit a draft scenario list to `3_execution/scenario_draft.yaml` before writing final documents.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Scenario inventory (narrative) | `4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md` | Covers all 9 dimensions; each scenario has ID, category, params, expected hit level, expected result, rationale, source evidence |
| Scenario table (CSV) | `4_artifact/5_table/stress_query_scenario_table_v20260624.csv` | One row per scenario with 10+ columns; parseable by standard CSV tools |
| Artifact registry update | `4_artifact/registry.yaml` | Both outputs registered with correct source_task=T-056, type, path, status=active |

## Failure / Stop Conditions
- Any registered asset is found empty, truncated, or corrupt during read → stop, document in `5_report/blocked.md`
- Scenario derivation requires information not in the 8 registered assets → stop, do not invent hypotheticals without documented precedent per protocol constraint
- Any step begins to write test code, execute queries, or build infrastructure → stop immediately — this is explicitly forbidden
- T-041 outputs are referenced or read → stop — T-041 is active and omitted by constraint
- LLM stability issues cause repeated contradictory scenario classifications → checkpoint and flag for human review

## Notes For Delivery QA
- Verify CSV columns match: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- Verify narrative document includes at least one scenario per dimension (9 total minimum)
- Verify no test code, no query execution results, no legacy root paths appear in deliverables
- Verify artifact registry entries point to the correct absolute paths within this task's `4_artifact/`
- Date in filenames should match execution date (YYYYMMDD format)
