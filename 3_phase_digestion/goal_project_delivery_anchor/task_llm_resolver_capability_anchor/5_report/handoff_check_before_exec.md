# Check Handoff Before Exec: T-063 llm_resolver_capability_anchor

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories except registered asset symlinks/paths, legacy source root `/Users/dudu/Documents/3_Project/8_functional_query`, `1_project_init/`, `2_project_asset/`, `6_project_deliverable/`
- Required registry: `1_asset/registration.yaml`
- Must stop if: required registered assets become unavailable; defining the anchor would require code implementation, package tests, raw matrix/data analysis, web search, direct legacy-root reads, downstream prompt generation, or a silent downgrade of required LLM/resolver behavior into deterministic lookup or fallback-only behavior.

## Objective Restatement
Create a resolver-specific capability and acceptance anchor for future PxFquery package milestones, especially M3. The output should define the required user-facing natural-language/semi-structured resolver behavior, CyHex-configured AI service use, exact/proxy/not-found routing, fallback semantics, demo cases, and acceptance evidence. This is a design/governance task only; it must not implement or test resolver code.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Trusted source map for migrated development assets and resolver-related source authority. | ok |
| A-002 | `1_asset/t007_development_state_report.md` | Intended product scope plus matrix/index/resolver design interpretation. | ok |
| A-003 | `1_asset/t007_development_gap_and_risk_list.md` | Known resolver, validation, and claim risks. | ok |
| A-004 | `1_asset/t013_mvp_capability_contract.md` | Reviewed MVP capability expectations and boundaries. | ok |
| A-005 | `1_asset/t013_capability_status_matrix.csv` | Evidence for passed, partial, blocked, failed, and missing behaviors. | ok |
| A-006 | `1_asset/t013_failure_missing_capability_list.md` | Missing resolver, natural-language, LLM, and runtime-index behaviors. | ok |
| A-007 | `1_asset/t061_legacy_source_digest.md` | Bounded legacy source digest and resolver-related source hints. | ok |
| A-008 | `1_asset/t061_legacy_reference_boundaries.yaml` | Boundary rules for citing/adapting T-061 findings. | ok |
| A-009 | `1_asset/t062_algorithm_package_delivery_anchor.yaml` | Package-level capability anchor that this task refines. | ok |
| A-010 | `1_asset/t062_algorithm_capability_matrix.csv` | Capability-to-evidence matrix for milestone alignment. | ok |
| A-011 | `1_asset/t062_algorithm_downgrade_rules.md` | Runtime fallback versus unapproved downgrade rules. | ok |
| A-012 | `1_asset/t062_milestone_review_rubric.md` | Evidence hierarchy and review procedure. | ok |
| A-013 | `1_asset/t062_milestone_classification_vocabulary.yaml` | Status vocabulary for delivered/partial/blocked/failed/downgraded/deferred/evidence-insufficient states. | ok |

## Execution Strategy
1. Read only the registered inputs above plus the current task protocol/asset rules; extract resolver-relevant requirements, gaps, source boundaries, downgrade rules, and acceptance vocabulary into working notes under `3_execution/`.
2. Draft the M3 resolver behavior model: supported query modes, required parse fields, ambiguity handling, structured output, confidence/evidence metadata, and user-facing summary expectations.
3. Specify the CyHex-configured AI-service rule: milestones claiming LLM resolver capability must use the current CyHex-registered AI route, currently `deepseek-v4-pro`, unless a later task explicitly changes it.
4. Define exact, proxy, and not-found routing semantics for forward and reverse queries, including what LLM assistance may do and what it must not claim as biological evidence.
5. Define fallback semantics for LLM unavailability, parse failure, proxy failure, missing indexes, unsupported entities, and low-confidence matches; classify fallback as runtime behavior/evidence, not as proof of primary resolver delivery.
6. Build the required demo case catalog and acceptance matrix, covering exact/proxy/not-found, forward/reverse, ambiguous natural language, semi-structured input, LLM-unavailable fallback, and metadata inspection.
7. Produce the reusable YAML anchor, design Markdown, CSV matrix, demo catalog, HTML reports, artifact registry update, and completion report in the specified output directories.

## Conservative Execution Advice
- Start with: a narrow extraction pass over A-009, A-010, A-011, A-012, and A-013 to inherit T-062 vocabulary and downgrade rules before reading the broader T-007/T-013/T-061 context.
- Smoke/demo command or method: create a short `3_execution/` outline or scratch table listing the required output files, resolver capabilities, and status vocabulary before drafting final artifacts.
- Full run only after: confirming the outline contains all required behavior classes: natural-language, semi-structured, forward, reverse, exact, proxy, not-found, fallback, metadata, and downgrade handling.
- Cost/time risk: low compute and no network/API cost; the main risk is over-reading predecessor context or accidentally expanding into implementation/testing.
- Checkpoint advice: before writing final artifacts, compare planned outputs against the deliverables and acceptance criteria in `2_protocol/2_protocol_split/protocol.md`; if a needed claim would require code/runtime proof, label it as future acceptance evidence rather than current proof.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Machine-readable LLM/resolver capability anchor | `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | Defines resolver capabilities, AI-service rule, routing semantics, fallback/downgrade rules, and acceptance evidence in structured form. |
| Human-readable resolver functional design | `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | Concisely explains M3 user-facing resolver behavior without claiming implementation or test success. |
| Resolver acceptance matrix | `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | Maps each capability to required evidence, minimum behavior, disallowed substitutes, failure labels, and review status vocabulary. |
| Resolver demo case catalog | `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | Covers exact/proxy/not-found, forward/reverse, ambiguous NL, semi-structured, LLM-unavailable fallback, and metadata inspection cases. |
| Execution report | `4_artifact/3_document/execution_report_v20260625.html` | Records what was read, how outputs were produced, and confirms no implementation/tests/web/legacy-root reads occurred. |
| Result report | `4_artifact/3_document/result_report_v20260625.html` | Summarizes completed anchor outputs and their acceptance relevance. |
| Artifact registry update | `4_artifact/registry.yaml` | Registers all accepted/reusable outputs with paths, types, provenance, and status. |
| Completion report | `5_report/completion.md` | States completion, constraints honored, outputs produced, and any residual limitations or future-review notes. |

## Failure / Stop Conditions
- Stop if any required registered asset cannot be read and the missing asset prevents defining resolver behavior without guessing.
- Stop if execution would need to inspect the legacy source root, scan arbitrary predecessor folders, use web search, call downstream prompt endpoints, or access unregistered raw project assets.
- Stop if the task starts to require package/API implementation, runtime tests, notebook execution, raw matrix inspection, or biological analysis.
- Stop if predecessor evidence conflicts in a way that prevents a safe resolver anchor; report the conflict rather than inventing a compromise.
- Stop if any output would count deterministic lookup, fallback-only behavior, deferral, or optionalization as delivery of primary LLM/resolver capability without explicit user approval.

## Notes For Delivery QA
- Verify the final outputs are in `4_artifact/` or `5_report/`, not only `3_execution/`.
- Confirm the deliverables do not claim resolver code works, LLM service was tested, or missing indexes were repaired.
- Confirm LLM output is framed as parsing/normalization/summarization assistance, not independent biological evidence.
- Confirm fallback is described as runtime behavior and evidence, not as a substitute for primary LLM/resolver delivery.
- Confirm the current desired model route is stated as CyHex-registered AI address with `deepseek-v4-pro`, unless a later explicit task changes it.
