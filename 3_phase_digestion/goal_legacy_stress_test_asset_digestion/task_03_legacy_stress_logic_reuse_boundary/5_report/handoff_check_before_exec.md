# Check Handoff Before Exec: T-057 03_legacy_stress_logic_reuse_boundary

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `1_project_init/`, `2_project_asset/` (except paths in required asset list), `8_functional_query/`, predecessor task directories
- Required registry: `1_asset/registration.yaml` — all 12 assets preflighted OK
- Must stop if: any required predecessor asset (A-001–A-007, A-012) cannot be resolved; A-009 is empty/inaccessible; reuse category cannot be assigned due to unclear content (use `unknown` with explanation instead)

## Objective Restatement
For each legacy stress-test-related asset in the migrated flat library (scripts, reports, design docs, traces), assign a reuse category (`direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`) with reasoning. Produce a reuse-boundary analysis document and a machine-readable decision matrix CSV.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 1_asset/T-007_development_state_report.md | Code/index/report maturity overview | ok |
| A-002 | 1_asset/T-007_module_asset_status_matrix.csv | Per-component maturity for reuse classification | ok |
| A-003 | 1_asset/T-007_validation_evidence_index.csv | Primary reference for validation-report reuse categories | ok |
| A-004 | 1_asset/T-007_gap_and_risk_list.md | Risk flags for each asset category | ok |
| A-005 | 1_asset/T-001_asset_structure_report.md | Authority rules for operational vs archive | ok |
| A-006 | 1_asset/T-002_library_structure_guide.md | Flat library navigation guide | ok |
| A-007 | 1_asset/T-002_not_migrated_assets_report.md | Prevents evaluating unmigrated assets | ok |
| A-008 | 1_asset/PL_stress_test_scripts | 19 scripts including M-0385–M-0389 test/verify set | ok |
| A-009 | 1_asset/PL_validation_reports_dir | 57 validation reports (the stress-test corpus) | ok |
| A-010 | 1_asset/PL_resolver_source_plus_design.py | Core resolver source | ok |
| A-011 | 1_asset/PL_validation_traces.json | Act-1 validation JSON trace | ok |
| A-012 | 1_asset/T-007_development_source_map.md | Source authority map to avoid superseded reports | ok |

## Execution Strategy
1. **Read authority & context** — A-005, A-006, A-007, A-001, A-012 to establish classification criteria and boundary rules.
2. **Read maturity indexes** — A-002, A-003, A-004 to understand validated status and risk level of components that stress-test assets target.
3. **Read validation reports systematically** — Scan A-009 (57 reports). Cover mandatory set: M-0239 (latest index), M-0291/M-0257 (forward matrix), M-0266/M-0277/M-0275 (question suites), M-0267 (stability), M-0255 (act-1), M-0243 (risks), M-0244 (exec order), M-0245 (obsolete), M-0290 (resolver TODO). Classify each.
4. **Read legacy test scripts** — Read scripts in A-008: M-0385 run_forward_question_suite.py, M-0386 test_forward_matrix.py, M-0387 test_resolver_smoke.py, M-0388 validate_act1.py, M-0389 verify_resolver_cases.py.
5. **Read resolver source & design context** — Read A-010 resolver.py for understanding what the test/verify scripts exercise.
6. **Read validation traces** — Read A-011 (act-1 JSON) to supplement report-based assessment.
7. **Build decision matrix** — tabular rows with asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action.
8. **Write deliverable 1** — `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md`
9. **Write deliverable 2** — `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv`
10. **Register deliverables** — Update `4_artifact/registry.yaml`. Write `5_report/completion.md` and `5_report/delivery_qa.md`.

## Conservative Execution Advice
- Start with: Steps 1–2 (read authority docs + maturity indexes) before touching any validation report.
- Smoke/demo command or method: Read M-0239 (latest reports index) first to understand report landscape before deep-reading individual reports.
- Full run only after: All 10 steps are sequential; the task is read+classify only, no expensive compute.
- Cost/time risk: Low — all assets are local files. No API calls, no script execution, no LLM queries. ~57 reports to read may take moderate reading time but no compute cost.
- Checkpoint advice: After step 6 (all reading done), review whether the mandatory report set is covered before building the matrix.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reuse boundary analysis | `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` | Every evaluated asset has a clear reuse category; classification criteria explained; superseded/duplicate reports noted |
| Reuse decision matrix CSV | `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` | Machine-readable with columns: asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action |
| Completion report | `5_report/completion.md` | Verdict, asset counts, and brief execution summary |
| Delivery QA | `5_report/delivery_qa.md` | Confirms both deliverables present |

## Failure / Stop Conditions
- Required predecessor asset missing/unresolvable → stop and report which asset.
- A-009 (validation_reports/) empty or inaccessible → stop.
- Asset content unclear → classify as `unknown` with explanation; do not guess.
- Superseded/duplicate report identified → note with priority reference; do not treat as primary evidence.

## Notes For Delivery QA
- Use today's date 20260624 in filenames.
- Use exactly the 5 classification categories: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`.
- Do not classify from filename alone — each asset must be read or inspected.
- Do not modify code, repair old scripts, or run production-scale tests.
- Do not claim `direct reference` if asset contains old workspace paths that prevent immediate reuse — flag this.
- T-041 is active; omit it. T-055/T-056 are pending; optional cross-reference only, do not block.
