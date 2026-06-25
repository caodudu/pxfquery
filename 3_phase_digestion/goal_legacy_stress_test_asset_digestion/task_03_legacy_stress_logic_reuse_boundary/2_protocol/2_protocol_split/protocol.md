# T-057 03_legacy_stress_logic_reuse_boundary — Protocol

## Objective

Judge the reuse boundary for each legacy stress-test-related logic, script, report, and query-validation idea found in the migrated flat asset library. For each candidate, assign one of: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, or `unknown`. Produce a reusable decision document and a decision matrix CSV.

## Position In Project

This is task 3 of 4 in goal G-026 (legacy_stress_test_asset_digestion). It follows T-055 (source map — pending) and T-056 (scenario inventory — pending). Since predecessors are not yet delivered, this task works directly from T-001/T-002/T-007 digested outputs and the project-level flat asset library. Its output feeds T-058 (development handoff pack).

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Code/index/report maturity overview |
| A-002 | T-007 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Per-component maturity for reuse classification |
| A-003 | T-007 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Validation evidence status — primary reference for validation-report reuse |
| A-004 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Risk flags for each asset category |
| A-005 | T-001 | 4_artifact/2_persist/old_asset_structure_report.md | Authority rules for distinguishing operational vs archive material |
| A-006 | T-002 | 4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Flat library navigation guide |
| A-007 | T-002 | 4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Prevents evaluating unmigrated assets |
| A-008 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders/ | Legacy test/verify scripts for reuse classification |
| A-009 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/ | 57 validation reports forming the stress-test evidence corpus |
| A-010 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py | Core resolver logic that stress tests exercise |
| A-011 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json | JSON validation traces for reproducibility assessment |
| A-012 | T-007 | 4_artifact/2_persist/pxfquery_development_source_map_v20260617.md | Source authority map to avoid superseded/duplicate reports |

## Execution Steps

1. **Read authority and context.** Read A-005 (T-001 authority), A-006 (T-002 structure guide), A-007 (not-migrated report), A-001 (T-007 state report), A-012 (source map) to establish classification criteria and boundary rules.

2. **Read T-007 maturity indexes.** Read A-002 (module asset status matrix), A-003 (validation evidence index), A-004 (gap/risk list) to understand the validated status and risk level of each component that stress-test assets target.

3. **Read legacy validation reports systematically.** Scan A-009 (validation_reports/ directory). For each report, read its content and classify it. At minimum cover:
   - Latest reports index (M-0239)
   - Forward matrix tests (M-0291, M-0257)
   - Forward question suites (M-0266, M-0277, M-0275)
   - LLM stability check (M-0267)
   - Act-1 validation (M-0255)
   - Known risks (M-0243), execution order (M-0244), obsolete list (M-0245)
   - Resolver TODO (M-0290)

4. **Read legacy test scripts.** Read the scripts in A-008 (index_builders/ directory). At minimum:
   - M-0385 test_resolver_smoke.py (if exists)
   - M-0386 test_forward_matrix.py (deterministic mock)
   - M-0389 verify_resolver_cases.py (real LLM)

5. **Read resolver source and design context.** Read A-010 (resolver.py) and relevant design docs from A-008's design_docs/ to understand what the test/verify scripts exercise.

6. **Read validation traces.** Read A-011 (act1 validation JSON) to supplement report-based assessment.

7. **Build decision matrix.** For each evaluated candidate, record:
   - Asset name/path
   - Asset type (script / report / design doc / other)
   - Reuse decision: direct reference / rewrite needed / historical evidence only / not usable / unknown
   - Reasoning summary
   - Key risk or gap
   - Recommended next action

8. **Write deliverable 1: Persist document.** Write `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md` with full reuse-boundary analysis organized by asset category.

9. **Write deliverable 2: Decision matrix.** Write `4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv` with the tabular decision matrix.

10. **Register deliverables.** Update `4_artifact/registry.yaml` with both outputs.

## Constraints

- Do not modify code, repair old scripts, or run production-scale tests.
- Do not scan the unregistered legacy root (8_functional_query).
- If a script or report references workspace paths that do not exist in the current project, note this but do not fix them.
- If T-041 is done, it may be consulted as an optional supplementary source; if T-041 is still active (its current status), omit it.
- If T-055 (source map) or T-056 (scenario inventory) become available during execution, they may be used as cross-reference but must not block this task.
- Use the classification categories exactly: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`.
- Use today's date YYYYMMDD = 20260624.
- Do not treat older/superseded validation reports as primary evidence; use the T-007 validation evidence index (A-003) and the latest reports index (M-0239) for priority.

## Forbidden

- Modifying any file inside `2_project_asset/`, `1_project_init/`, or predecessor task directories.
- Running old scripts, rebuilding indexes, or executing LLM queries.
- Producing final deliverables before the full matrix is populated.
- Claiming an asset is `direct reference` if it contains old workspace paths that prevent immediate reuse.

## Web Search Allowance

Allowed: no
Reason: This is a digestion task operating on migrated legacy assets only. No external or current information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reuse boundary analysis document | 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md | yes |
| Reuse decision matrix CSV | 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv | yes |

## Acceptance Criteria

- Every evaluated asset has a clear reuse category assignment with reasoning.
- At minimum, all scripts in the `code/index_builders/` test/verify set and all validation reports in the `reports/validation_reports/` set are evaluated.
- The decision document explains the reuse classification criteria and any cross-cutting patterns.
- Superseded/duplicate reports are noted with a clear priority reference.
- No asset is classified purely from its filename; each must be read or inspected.
- The decision matrix CSV is machine-readable with columns: asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action.

## Failure / Stop Rules

- If required predecessor assets (A-001 through A-007, A-012) cannot be resolved, stop and report which asset is missing.
- If the validation_reports/ directory (A-009) is empty or inaccessible, stop and report.
- If reuse categories cannot be assigned because an asset's content is unclear, classify as `unknown` with explanation rather than guessing.

## Delivery Requirements

- Register both deliverables in `4_artifact/registry.yaml` with type `persist` and `table`.
- Keep temp state in `3_execution/`.
- Write `5_report/completion.md` with verdict and asset counts.
- Write `5_report/delivery_qa.md` confirming both deliverables are present.
