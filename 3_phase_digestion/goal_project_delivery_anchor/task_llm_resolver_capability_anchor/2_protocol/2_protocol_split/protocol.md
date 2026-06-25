# T-063 llm_resolver_capability_anchor — Protocol

## Objective

Create the task-level LLM/resolver capability anchor for future PxFquery package milestones, especially M3-level resolver delivery. The task must define the user-facing natural-language and semi-structured query behavior, CyHex-configured AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics, demo cases, and acceptance evidence. It must not implement API code or run package tests.

## Position In Project

This is a digestion/governance task under `goal_project_delivery_anchor`. It refines the T-062 algorithm-package delivery anchor for the specific resolver/LLM layer so later package milestones cannot count deterministic matrix lookup alone as delivery of user-facing resolver behavior when resolver capability is in scope.

The anchor should preserve the project-defined capability shape:

- forward query: biological context plus perturbation to functional response;
- reverse query: desired function plus biological context to candidate perturbations;
- natural-language or semi-structured query entry;
- resolver-mediated exact, proxy, and not-found evidence routing;
- LLM-assisted parsing and summarization through the current CyHex-configured AI service route, currently deepseek-v4-pro unless a later task explicitly changes it;
- deterministic fallback and transparent evidence metadata when LLM, proxy routing, or coverage fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map for migrated PxFquery development assets and resolver-related source authority. |
| A-002 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Intended product scope and matrix/index/resolver design interpretation. |
| A-003 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Known resolver, validation, and claim risks. |
| A-004 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Reviewed MVP capability expectations and boundaries. |
| A-005 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Capability status evidence for passed, partial, blocked, failed, and missing behavior. |
| A-006 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Missing resolver, natural-language, LLM, and runtime-index behaviors that must not be silently downgraded. |
| A-007 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Bounded source digest for legacy package modules and resolver-related source hints. |
| A-008 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Boundary rules for citing or adapting T-061 findings. |
| A-009 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | Package-level capability anchor to refine for resolver delivery. |
| A-010 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | Capability-to-evidence matrix for milestone acceptance alignment. |
| A-011 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Rules distinguishing runtime fallback from unapproved scope downgrade. |
| A-012 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Evidence hierarchy and review procedure for future package milestones. |
| A-013 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | Classification vocabulary for delivered, partial, blocked, failed, downgraded, deferred, and evidence-insufficient states. |

## Execution Steps

1. Read the registered inputs and extract only the resolver-relevant capability requirements, existing gaps, source-boundary rules, downgrade rules, and acceptance vocabulary.
2. Define the expected M3-level user-facing resolver behavior for natural-language and semi-structured query entry, including required input fields, supported ambiguity handling, structured parse output, evidence metadata, and user-facing summary behavior.
3. Specify the CyHex-configured AI service requirement: future resolver milestones that claim LLM capability must route through the current CyHex-registered AI address and currently desired `deepseek-v4-pro` model route unless a later task explicitly changes that route.
4. Define exact, proxy, and not-found resolver routing semantics, including how LLM assistance may parse, normalize, explain, or summarize but must not fabricate matrix evidence.
5. Define fallback semantics for unavailable LLM service, parse failure, proxy failure, missing indexes, unsupported cell lines, unsupported perturbations, unsupported functions, and low-confidence matches. Mark fallback as runtime behavior and evidence, not proof that primary LLM/resolver delivery is complete.
6. Create a demo case catalog with concrete required case types for future M3 acceptance: exact forward query, exact reverse query, proxy forward query, proxy reverse query, not-found query, ambiguous natural-language query, semi-structured query, LLM-service-unavailable fallback, and evidence-metadata inspection.
7. Create an acceptance matrix mapping each resolver capability to required evidence, minimum acceptable behavior, disallowed substitutes, failure labels, and review status vocabulary inherited from T-062.
8. Write a machine-readable resolver capability anchor YAML and a concise human-readable functional design Markdown document.
9. Write required execution and result reports, and register all accepted/reusable outputs in the current task artifact registry.

## Constraints

- This is a design and acceptance-anchor task only.
- Use selected predecessor artifacts and project protocol context; do not perform implementation, runtime tests, raw-data analysis, web search, or manuscript writing.
- Treat T-062 as the package-level anchor and make this task a resolver-specific refinement, not a competing replacement.
- Preserve the difference between conservative manuscript claims and development delivery scope: conservative claims do not make LLM/resolver functions optional when a milestone includes them.
- Require transparent provenance and evidence metadata for exact, proxy, fallback, and not-found outcomes.
- Treat LLM output as parsing/summarization/normalization assistance, not as independent biological evidence.
- Make any proposed deferral, optionalization, or fallback-only acceptance of required resolver behavior visible as a downgrade requiring explicit user approval.

## Forbidden

- Do not implement or modify package/API/source code.
- Do not run package workflows, tests, notebooks, matrix inspection, or biological analysis.
- Do not read or modify legacy source roots.
- Do not browse predecessor task directories beyond registered assets and allowed handoff/report files.
- Do not create final project deliverables under `6_project_deliverable/`.
- Do not call downstream CyHex prompt endpoints.
- Do not use web search.

## Web Search Allowance

Allowed: no

Reason: The current task is a project-internal capability and acceptance anchor. The required information is available from project protocol, current task intent, and selected predecessor handoffs/artifact registries. No current external evidence is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Machine-readable LLM/resolver capability anchor | `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | yes |
| Human-readable resolver functional design | `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | yes |
| Resolver acceptance matrix | `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | yes |
| Resolver demo case catalog | `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260625.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260625.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The anchor explicitly defines M3-level resolver delivery as more than deterministic lookup when resolver is in scope.
- Natural-language and semi-structured entry behavior is specified with required parse fields, ambiguity handling, confidence/evidence metadata, and user-facing output expectations.
- CyHex-configured AI service use is specified, including current desired route `deepseek-v4-pro` and the rule that a later task must explicitly approve any route change.
- Exact, proxy, and not-found handoff behavior is defined for both forward and reverse query modes.
- Fallback semantics are concrete and classify fallback as runtime behavior/evidence, not delivery of the primary LLM/resolver capability.
- Demo cases cover exact, proxy, not-found, ambiguous, semi-structured, and LLM-unavailable scenarios.
- Acceptance evidence requirements include both functional behavior and metadata/provenance evidence.
- Downgrade, deferral, optionalization, and fallback-only acceptance rules are consistent with T-062.
- The task output does not claim that resolver code works, that LLM service was tested, or that missing indexes were repaired.

## Failure / Stop Rules

- Stop if registered predecessor assets are unavailable and the missing asset prevents defining resolver behavior without guessing.
- Stop if the work would require source-code implementation, runtime testing, matrix/raw-data analysis, web search, or direct legacy-root reads.
- Stop if predecessor evidence conflicts in a way that makes the required resolver capability impossible to define safely; report the conflict in `5_report/completion.md`.
- Stop if any output would silently downgrade required LLM/resolver capability into deterministic lookup, fallback-only behavior, or a deferred optional feature.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
