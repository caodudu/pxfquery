# T-058 04_stress_test_development_handoff_pack — Protocol

## Objective

Integrate the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a single development-phase handoff pack. The pack serves as a structured bridge from the stress-test digestion goal to a future stress-test milestone in the development phase.

Produce two deliverables:
1. A narrative handoff pack consolidating what is known, reusable, risky, and missing across all three predecessor outputs.
2. A set of recommended future development tasks (not execution steps) that a stress-test milestone should include.

Reference T-007 to keep the handoff aligned with current development asset understanding (code maturity, index status, known gaps).

## Position In Project

This is the final integration task of `goal_legacy_stress_test_asset_digestion`. It is a pure digestion-stage handoff task:
- Does not implement or run stress tests.
- Does not compensate for missing upstream quality by inventing results.
- Recommends future development tasks only.

The output is a digestion-stage handoff pack, not a development-phase execution plan.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-055 | 4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md | Primary catalog of ~160 stress-test candidate assets; used to understand what legacy material exists and where |
| A-002 | T-055 | 4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv | Machine-readable index for filtering candidates by category, type, or relevance |
| A-003 | T-056 | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale |
| A-004 | T-056 | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | Tabular scenario table; parseable for downstream test framework use |
| A-005 | T-057 | 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md | Reuse-boundary analysis covering 65 classified legacy assets with decisions |
| A-006 | T-057 | 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv | Machine-readable decision matrix with reuse_decision, reasoning, risk_gap, recommended_action per asset |
| A-007 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development-state understanding: code, data, index, and report maturity |
| A-008 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | High-priority gaps, risks, and claims-to-avoid for development phase |
| A-009 | T-007 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Recommended next development tasks and carry-forward guidance from T-007 |

## Execution Steps

1. **Read all registered inputs** (A-001 through A-009) to build a complete picture of the stress-test digestion landscape.
2. **Synthesize the three dimensions:**
   - From T-055: what legacy stress-test assets exist, their categories, and known gaps.
   - From T-056: what stress-test scenarios should be exercised, grouped by query dimension.
   - From T-057: which legacy assets are directly referable, which need rewrite, which are historical-only, and which are not usable.
3. **Cross-reference with T-007** to align the handoff with the current development state — ensuring recommendations are grounded in what the codebase actually supports today.
4. **Write the handoff pack** (`stress_test_development_handoff_pack_v20260624.md`):
   - Section 1: Summary of consolidated digestion findings (what the three predecessors collectively established).
   - Section 2: Asset-to-scenario cross-walk (which source assets map to which test scenarios).
   - Section 3: Reuse-ready assets (from T-057 decisions marked "direct reference").
   - Section 4: Rewrite-required assets and their risk profile.
   - Section 5: Known gaps and missing assets (from T-055 missing leads + T-057 "not usable" + T-007 gap list).
   - Section 6: Alignment with current development state (via T-007 cross-ref).
   - Section 7: Handoff integrity check (are predecessor outputs internally consistent? Any unresolved contradictions?).
5. **Write recommended milestone tasks** (`recommended_stress_test_milestone_tasks_v20260624.md`):
   - Define a logical task sequence for a future stress-test milestone.
   - Each recommended task should have: name, objective, estimated scope, predecessor dependency, and rationale anchored in T-055/056/057/007 evidence.
   - Do not prescribe implementation details — recommend what should be done, not how.
6. **Register both deliverables** in `4_artifact/registry.yaml`.
7. **Write `5_report/completion.md`**.

## Constraints

- Do not implement or run stress tests.
- Do not compensate for missing upstream quality by inventing results.
- Recommend future development tasks only; keep the result as digestion-stage asset handoff.
- Do not modify predecessor task outputs.
- Do not read raw legacy assets or scan unregistered directories.
- If predecessor outputs conflict or are ambiguous, record the conflict honestly rather than picking a side silently.

## Forbidden

- Running pxfquery code, queries, or tests.
- Modifying legacy scripts or source files.
- Creating new stress-test scenarios beyond what predecessors already describe.
- Reading unregistered predecessor task directories or `3_execution/`.
- Reading `2_protocol/0_prompt/` files.

## Web Search Allowance

Allowed: no
Reason: All information needed for this integration/handoff task is sourced from completed predecessor digestion outputs and T-007 development state. No external or current web information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Handoff pack | 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md | yes |
| Recommended milestone tasks | 4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md | yes |

## Acceptance Criteria

- The handoff pack integrates findings from all three predecessors (T-055, T-056, T-057) in a coherent, non-redundant narrative.
- The recommended milestone tasks are grounded in predecessor evidence, not invented.
- Cross-reference with T-007 is explicit and traceable.
- Gaps, risks, and ambiguous findings from predecessors are honestly carried forward, not patched.
- Both deliverables are registered in `4_artifact/registry.yaml`.
- `5_report/completion.md` is written.

## Failure / Stop Rules

- If any predecessor meta shows `status != done`, stop and report the incomplete dependency.
- If any required input asset (A-001 through A-009) cannot be read at its registered path, stop and report the missing asset.
- If predecessor outputs are internally contradictory in a way that prevents coherent synthesis, stop and escalate rather than guessing.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.