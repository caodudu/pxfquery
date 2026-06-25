# T-065 m1_vs_delivery_anchor_review — Protocol

## Objective

Review the completed M1 Python package milestone against the project delivery anchors. Classify M1 as one of: full milestone, deterministic kernel/substrate, or partial milestone. List anchored capabilities as delivered, partial, missing, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, or evidence-insufficient. Identify any unapproved scope shrinkage and recommend the next milestone boundary.

## Position In Project

This is a digestion-stage review/gap task under `goal_project_delivery_anchor`. It does not modify M1 artifacts, package code, predecessor reports, or project protocol. Its job is to make the post-M1 status explicit so later development milestones do not treat a deterministic kernel as a complete algorithm package unless the delivery anchors are satisfied.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-053 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/3_document/milestone_report_v20260624_061117.md` | Primary M1 milestone summary and claimed delivery basis. |
| A-002 | T-053 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/2_persist/evidence_index_v20260624_061117.json` | Structured M1 evidence streams and gate verdicts. |
| A-003 | T-053 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/5_table/layered_asset_map_v20260624_061117.csv` | M1 layer provenance for capability attribution. |
| A-004 | T-053 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/5_table/known_gaps_v20260624_061117.md` | Known M1 gaps to compare with anchor-required capabilities. |
| A-005 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | Primary package capability anchor. |
| A-006 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | Capability checklist, evidence requirements, and failure modes. |
| A-007 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Rules for fallback versus unapproved scope downgrade. |
| A-008 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Review procedure and evidence hierarchy. |
| A-009 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | Controlled classification vocabulary for the review output. |
| A-010 | T-063 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | Resolver/LLM capability anchor. |
| A-011 | T-063 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | Human-readable resolver behavior and disallowed substitutes. |
| A-012 | T-063 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | Resolver demo coverage expectations for later milestones. |
| A-013 | T-063 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | Resolver acceptance matrix and evidence labels. |
| A-014 | T-064 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md` | Evidence route taxonomy for exact/proxy/no-hit/transfer review. |
| A-015 | T-064 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml` | Required route evidence metadata contract. |
| A-016 | T-064 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv` | Route stress mapping to identify untested or missing M1 behavior. |

## Execution Steps

1. Read the registered M1 artifacts first and extract each capability that M1 explicitly claims, including validation scope, package entry points, evidence gates, demo scope, known gaps, and provenance layers.
2. Read the T-062 package anchor artifacts and build a review checklist using the anchor capability matrix, downgrade rules, review rubric, and classification vocabulary.
3. Read the T-063 resolver anchor artifacts and separately assess natural-language/semi-structured query entry, LLM-assisted parsing/summarization, resolver evidence, fallback behavior, and disallowed substitutes.
4. Read the T-064 routing anchor artifacts and separately assess exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion behavior, metadata contract support, and stress-route coverage.
5. Compare M1 evidence against the combined anchor checklist. For each capability, assign a controlled status label and cite the specific M1 evidence or gap that supports the label.
6. Decide the overall M1 classification: full milestone, deterministic kernel/substrate, or partial milestone. State why the selected classification follows from the anchor evidence.
7. Identify any unapproved scope shrinkage, including cases where deterministic lookup, synthetic fixtures, missing resolver behavior, missing LLM evidence, missing proxy/no-hit routing, or fallback-only behavior was treated as complete capability.
8. Recommend the next milestone boundary, including which capabilities should be required before calling the next package milestone complete and which items can remain documented gaps.
9. Produce the required machine-readable gap YAML, Chinese narrative Markdown report, and Chinese HTML result/execution reports. Register all accepted outputs in `4_artifact/registry.yaml`.

## Constraints

- This is a review/gap task only.
- Treat T-053 as M1 evidence, not as an authority that can override project delivery anchors.
- Use T-062, T-063, and T-064 as anchor inputs for capability expectations and downgrade rules.
- Use the T-062 classification vocabulary where applicable.
- Be explicit if M1 is only a deterministic kernel/substrate.
- Do not call M1 a complete algorithm package unless anchor-required resolver, LLM, evidence-routing, fallback, and metadata behaviors are supported by evidence or explicitly marked out-of-scope with approval.
- Distinguish runtime fallback behavior from a scope downgrade.
- Write review outputs in Chinese where human narrative is required; machine-readable YAML keys may remain English.

## Forbidden

- Do not modify T-053, T-062, T-063, T-064, or their artifacts.
- Do not modify package code, package resources, project protocol, or final project deliverables.
- Do not run M1 package validation, repair code, analyze raw data, or create new benchmark results.
- Do not read predecessor `2_protocol/`, `1_asset/`, or `3_execution/` directories unless a later approved prompt explicitly allows it.
- Do not perform web search.
- Do not use future-stage prompt files from `2_protocol/0_prompt/`.

## Web Search Allowance

Allowed: no

Reason: The task is an internal milestone-vs-anchor review and can be configured and executed from registered project/predecessor artifacts. No current external evidence is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Machine-readable M1 anchor gap review YAML | `4_artifact/2_persist/m1_vs_delivery_anchor_gap_review_v20260625.yaml` | yes |
| Capability status matrix | `4_artifact/5_table/m1_vs_delivery_anchor_capability_matrix_v20260625.csv` | yes |
| Chinese narrative review report | `4_artifact/2_persist/m1_vs_delivery_anchor_review_report_v20260625.md` | yes |
| Next milestone boundary recommendations | `4_artifact/2_persist/m1_next_milestone_boundary_recommendations_v20260625.md` | yes |
| Chinese execution report | `4_artifact/3_document/execution_report_v20260625.html` | yes |
| Chinese result report | `4_artifact/3_document/result_report_v20260625.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The review gives one explicit overall classification for M1: full milestone, deterministic kernel/substrate, or partial milestone.
- Every anchor capability considered in scope is assigned a controlled status label and has a short evidence note.
- The output separates delivered, partial, missing, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, and evidence-insufficient items.
- Resolver/LLM behavior is reviewed separately from deterministic forward/reverse lookup.
- Evidence routing behavior is reviewed separately for exact, proxy, no-hit, ambiguous, context-missing, and transfer/suggestion routes.
- Any unapproved scope shrinkage is explicitly named, or the report states that none was found.
- Next milestone recommendations define a practical boundary and do not silently downgrade required project anchors.
- All accepted outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop and report evidence-insufficient if any required registered input asset cannot be read.
- Stop and report evidence-insufficient rather than inventing M1 behavior not present in the registered M1 artifacts.
- Stop before modifying predecessor artifacts, package code, project protocol, or final deliverable folders.
- Stop if the review would require new runtime testing or raw data analysis; recommend a separate execution/validation task instead.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
