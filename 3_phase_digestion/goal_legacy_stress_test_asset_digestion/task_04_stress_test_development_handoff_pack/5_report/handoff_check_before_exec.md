# Check Handoff Before Exec: T-058 04_stress_test_development_handoff_pack

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories (except registered paths), `2_project_asset/`, `/Users/dudu/Documents/3_Project/8_functional_query`, `2_protocol/0_prompt/` files
- Required registry: `1_asset/registration.yaml` (verified 9/9 assets ok)
- Must stop if: any A-001–A-009 cannot be read; predecessor outputs internally contradict; meta shows predecessor status != done

## Objective Restatement

Integrate the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a development-phase handoff pack. Produce two deliverables: a narrative handoff pack consolidating all three dimensions, and a set of recommended future stress-test milestone tasks. Cross-reference with T-007 to align with current development state. This is a pure digestion-stage handoff — do not implement or run stress tests, do not invent results to compensate for upstream quality.

## Selected Inputs

| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 1_asset/legacy_stress_test_source_map.md → T-055/D-001 | Primary catalog of ~160 stress-test candidate assets; categorizes by type, relevance, T-007 cross-ref | ok |
| A-002 | 1_asset/stress_test_candidate_asset_index.csv → T-055/D-002 | Machine-readable CSV index for filtering stress-test candidates | ok |
| A-003 | 1_asset/stress_query_scenario_inventory.md → T-056/D-001 | Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale | ok |
| A-004 | 1_asset/stress_query_scenario_table.csv → T-056/D-002 | Tabular CSV of 29 scenarios; parseable for downstream use | ok |
| A-005 | 1_asset/legacy_stress_logic_reuse_boundary.md → T-057/D-001 | Reuse-boundary analysis: 65 classified legacy assets with decisions | ok |
| A-006 | 1_asset/stress_logic_reuse_decision_matrix.csv → T-057/D-002 | Machine-readable decision matrix: reuse_decision, reasoning, risk_gap, recommended_action per asset | ok |
| A-007 | 1_asset/pxfquery_development_state_report.md → T-007/D-002 | Current development-state understanding | ok |
| A-008 | 1_asset/pxfquery_development_gap_and_risk_list.md → T-007/D-005 | High-priority gaps, risks, and claims-to-avoid | ok |
| A-009 | 1_asset/pxfquery_development_phase_handoff.md → T-007/D-006 | Recommended next development tasks and carry-forward guidance | ok |

## Execution Strategy

1. **Re-read all 9 input assets** (A-001 through A-009) to build a complete picture. The checking phase has already confirmed all assets are readable and semantically self-consistent.

2. **Synthesize the three predecessor dimensions into a consolidated findings summary:**
   - T-055: ~160 candidate assets across 10 categories (validation scripts, validation reports, resolver source, query indexes, GSEA eval scripts, GSEA result tables, index builders, demo scripts, digested context, background tutorials). 8 known gaps/missing leads documented.
   - T-056: 29 stress-test scenarios across 9 dimensions (complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index). Each scenario has rationale, expected hit level, expected result, and source evidence anchors.
   - T-057: 65 classified legacy assets (10 direct reference, 11 rewrite needed, 38 historical evidence only, 6 not usable). Clear evidence hierarchy: M-0239 as report authority, deterministic path stronger than LLM, function_index.json as critical rebuild gap.

3. **Cross-reference with T-007 development state** (A-007, A-008, A-009):
   - Align the handoff with the 5-step development interpretation from A-007 (package runnability → index completeness → deterministic smoke → hybrid_fast → case study).
   - Map T-007 gap/risk list to the handoff's risk profile.
   - Use T-007's recommended tasks (D001–D005) as cross-validation for the milestone task recommendations.

4. **Write the handoff pack** (`stress_test_development_handoff_pack_v20260624.md`) with 7 sections:
   - Section 1: Summary of consolidated digestion findings
   - Section 2: Asset-to-scenario cross-walk (map source assets to test scenarios)
   - Section 3: Reuse-ready assets (10 direct-reference items from T-057)
   - Section 4: Rewrite-required assets and risk profile (11 scripts from T-057)
   - Section 5: Known gaps and missing assets (T-055 missing leads + T-057 not usable + T-007 gap list)
   - Section 6: Alignment with current development state (T-007 cross-ref)
   - Section 7: Handoff integrity check (predecessor consistency review)

5. **Write recommended milestone tasks** (`recommended_stress_test_milestone_tasks_v20260624.md`):
   - Logical task sequence for a future stress-test milestone.
   - Each task: name, objective, estimated scope, predecessor dependency, rationale anchored in T-055/056/057/007 evidence.
   - Do not prescribe implementation details.

6. **Register both deliverables** in `4_artifact/registry.yaml`.

7. **Write `5_report/completion.md`**.

## Conservative Execution Advice

- Start with: Reading all 9 input assets to confirm content coherence. The 5-report directory already has a cli_sessions folder and an existing completion.md; work alongside these, do not overwrite unrelated files.
- Smoke/demo method: Before writing full deliverable text, draft a brief outline of each section and verify it maps to the exact assets and predecessor evidence — this prevents scope drift into writing new analysis.
- Full run only after: All asset-to-scenario cross-walk entries are traceable to concrete rows/sections in the 6 input CSVs/MDs; no synthetic scenarios should appear.
- Cost/time risk: This is a text-synthesis task with no compute, network, or storage cost beyond reading existing files. Risk is scope drift (inventing scenarios) or omission (missing a documented gap).
- Checkpoint advice: After step 2 (synthesis), self-review that all key facts carry forward into the handoff pack. After step 4 section 7 (integrity check), verify no predecessor contradiction was suppressed.

## Expected Deliverables

| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Handoff pack | `4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md` | Contains all 7 required sections; all cross-references traceable to predecessor evidence; no invented scenarios |
| Recommended milestone tasks | `4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md` | Each task has name/objective/scope/dependency/rationale anchored in predecessor evidence; task count between 4-8; no implementation prescriptions |
| Updated registry | `4_artifact/registry.yaml` | Both deliverables registered |
| Completion report | `5_report/completion.md` | Written per CyHex conventions |

## Failure / Stop Conditions

- Any predecessor output contains internal contradictions that prevent coherent synthesis → escalate, do not pick a side silently.
- A-001 to A-009 any file becomes unreadable mid-execution → stop.
- The 29 scenarios in T-056 cannot be plausibly cross-walked to the ~160 assets in T-055 → record the mismatch rather than fabricating links.
- Recommended milestone tasks drift into prescribing implementation details → stop and rewrite to task-definition level only.

## Notes For Delivery QA

- The handoff pack is a **digestion-stage handoff**, not a development-phase execution plan. It bridges the stress-test digestion goal to a future stress-test milestone.
- The handoff inherits constraints from all three predecessors: no direct reading of raw legacy assets, no scanning unregistered directories, no rerunning predecessor work.
- The reuse-boundary analysis (T-057) provides an evidence hierarchy with clear direct-reference assets — use these as the primary handoff backbone.
- The scenario inventory (T-056) provides 29 scenarios with expected results (PASS/FAIL/BORDERLINE) — carry these forward as test design guidance without modifying the expectations.
- The source map (T-055) provides the asset landscape — use it for asset-to-scenario mapping and gap identification.
- The T-007 development state (A-007/008/009) anchors the handoff in what the codebase actually supports today — ensure the handoff does not recommend tasks beyond current development readiness.