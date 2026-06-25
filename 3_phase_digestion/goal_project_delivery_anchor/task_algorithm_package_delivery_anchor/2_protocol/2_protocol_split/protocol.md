# T-062 algorithm_package_delivery_anchor — Protocol

## Objective

Create the authoritative PxFquery algorithm-package delivery anchor for future package milestones. The anchor must define the project-valid package capability set, acceptance rubric, downgrade rules, and milestone classification vocabulary so later milestones cannot silently shrink PxFquery into deterministic lookup only.

This is a digestion and governance task only. It must not write package code, rerun algorithm tests, rebuild data resources, or create final project deliverables.

## Position In Project

T-062 sits under the project delivery-anchor goal and converts prior digestion/review evidence into a durable task-level authority for later development planning, milestone review, and capability acceptance. It must separate conservative manuscript claims from development delivery scope: manuscript claim restraint does not make resolver, LLM-assisted parsing/summarization, proxy routing, or user-facing query transfer optional when those capabilities are part of a milestone.

The output should be strong enough for future CyHex tasks to classify package milestones as delivered, partial, blocked, downgraded, deferred, or out of scope, and to identify whether any deferral or scope reduction was user-approved.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-003 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_normalize_project_protocol_from_migrated_context/4_artifact/2_persist/project_protocol_revision_report_v20260616.md` | Preserve protocol-normalization history and source-boundary context. |
| A-002 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Main source for intended package identity, behavior, and completion boundary. |
| A-003 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Risk, missing-capability, and overclaim controls. |
| A-004 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Prior MVP capability contract to generalize into delivery-anchor rules. |
| A-005 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Current-run capability status evidence. |
| A-006 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Known failure, blocked, partial, and missing capabilities. |
| A-007 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Verified standard resource basis and runtime data expectations. |
| A-008 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle reference for acceptance language. |

## Execution Steps

1. Read the registered predecessor artifacts and extract only the capability, acceptance, risk, downgrade, and resource-basis facts needed for a package-delivery anchor.
2. Define the project-valid PxFquery package capability set, including at minimum forward query, reverse query, biological context handling, exact evidence routing, proxy evidence routing, not-found routing, resolver-mediated natural-language or semi-structured entry, LLM-assisted parsing/summarization where required by milestone scope, deterministic fallback, transparent evidence metadata, and standard resource compatibility.
3. Produce a machine-readable anchor YAML that records each capability, required evidence, allowed fallback, acceptance state vocabulary, downgrade triggers, and user-approval requirements.
4. Produce a capability matrix table mapping capabilities to required evidence, current predecessor evidence, acceptance threshold, likely failure modes, and whether absence is a blocker, partial delivery, or approved deferral.
5. Write downgrade rules that clearly distinguish runtime fallback from scope downgrade. A fallback path may be valid behavior, but it cannot count as delivery of the primary resolver/LLM/proxy capability unless the milestone explicitly accepts fallback-only behavior.
6. Write a milestone review rubric and classification vocabulary for future package milestones. Include labels for delivered, partial, blocked, failed, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, and evidence-insufficient.
7. Write a concise Chinese Markdown and HTML summary for human review. The summary should explain the anchor purpose, required capability set, downgrade rules, and how future milestones should use the rubric.
8. Register all reusable outputs in `4_artifact/registry.yaml` and write `5_report/completion.md`.

## Constraints

- Keep this task at digestion/anchor level; do not implement or repair package behavior.
- Use predecessor evidence and the current project protocol as authority. Do not promote old legacy protocol shells into current rules.
- Preserve the full development delivery scope when a milestone calls for resolver, LLM-assisted behavior, proxy routing, transfer behavior, or user-facing query entry.
- Keep manuscript claim restraint separate from software delivery acceptance.
- Use the T-021 standard resources as the canonical data/resource basis for future package compatibility language.
- Store temporary notes, scripts, and intermediate construction files in `3_execution/`; store accepted reusable outputs in `4_artifact/`.

## Forbidden

- Do not write or modify package source code.
- Do not run algorithm tests, rebuild query indexes, regenerate matrices, or perform raw data analysis.
- Do not use web search or external sources.
- Do not read from `/Users/dudu/Documents/3_Project/8_functional_query` directly.
- Do not modify predecessor task directories, project protocol files, project assets, or final project deliverable directories.
- Do not mark the task complete without producing the required anchor YAML, capability matrix, downgrade rules, review rubric, vocabulary, and Chinese summary.

## Web Search Allowance

Allowed: no

Reason: The current task can be safely configured and executed from project protocol plus selected predecessor artifacts. No current external facts are needed to define the project-internal delivery anchor.

Required evidence files, if allowed:
- None.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | yes |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | yes |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | yes |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | yes |
| Milestone classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | yes |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` | yes |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The anchor explicitly preserves PxFquery as a perturbation-to-function package with forward and reverse query behavior, not deterministic lookup only.
- Resolver, LLM-assisted parsing/summarization, proxy routing, not-found routing, deterministic fallback, and transparent evidence metadata are represented as delivery capabilities when a milestone includes them.
- Downgrade rules state that removing, optionalizing, or deferring a required capability requires explicit user approval and must be labeled in future milestone review.
- The rubric distinguishes evidence of working behavior from planned behavior, fallback behavior, blocked behavior, missing behavior, and user-approved deferral.
- The capability matrix ties each capability to predecessor evidence and standard resource assumptions without rerunning code or raw analysis.
- The Chinese summary is understandable to a human reviewer and does not overstate current implementation readiness.
- All reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop if registered predecessor assets are missing or internally insufficient to define the package capability anchor without guessing.
- Stop if execution would require package implementation, test execution, raw matrix analysis, web lookup, or direct legacy-root inspection.
- Stop if the resulting anchor would reduce required resolver/LLM/proxy behavior to optional deterministic lookup without recording a downgrade and user-approval requirement.
- Stop if the required output files cannot be written under this task's `4_artifact/` or reports cannot be written under `5_report/`.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
