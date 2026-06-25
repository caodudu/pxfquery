# Check Handoff Before Exec: T-065 m1_vs_delivery_anchor_review

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_m1_vs_delivery_anchor_review`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories except the registered artifact symlinks in `1_asset/`; predecessor `1_asset/`, `2_protocol/`, and `3_execution/`; package source code; `1_project_init/1_project_protocol/`; `6_project_deliverable/`
- Required registry: `1_asset/registration.yaml` and `2_protocol/3_asset_rule/asset_rule.yaml`
- Must stop if: any required registered input cannot be read; M1 behavior is not evidenced in registered M1 artifacts; the review would require runtime testing, code repair, raw data analysis, web search, or modification of predecessor/package/project-protocol/final-deliverable paths

## Objective Restatement
Review the completed M1 package milestone against the T-062 package anchor, T-063 LLM/resolver anchor, and T-064 evidence-routing anchor. The execution AI must classify M1 as `full milestone`, `deterministic kernel/substrate`, or `partial milestone`; assign controlled status labels to anchored capabilities; identify delivered, partial, missing, downgraded, deferred, out-of-scope, and evidence-insufficient items; call out unapproved scope shrinkage; and recommend the next milestone boundary without modifying M1 artifacts or package code.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_milestone_report.md` | Primary M1 milestone summary and claimed delivery basis. | ok |
| A-002 | `1_asset/m1_evidence_index.json` | Structured M1 evidence streams and gate verdicts. | ok |
| A-003 | `1_asset/m1_layered_asset_map.csv` | M1 layer provenance for capability attribution. | ok |
| A-004 | `1_asset/m1_known_gaps.md` | Known M1 gaps to compare with anchor-required capabilities. | ok |
| A-005 | `1_asset/package_delivery_anchor.yaml` | Primary machine-readable package capability anchor. | ok |
| A-006 | `1_asset/package_capability_matrix.csv` | Package capability checklist, evidence requirements, thresholds, and failure modes. | ok |
| A-007 | `1_asset/package_downgrade_rules.md` | Rules distinguishing valid runtime fallback from unapproved scope downgrade. | ok |
| A-008 | `1_asset/package_review_rubric.md` | Review procedure and evidence hierarchy. | ok |
| A-009 | `1_asset/package_classification_vocabulary.yaml` | Controlled classification vocabulary for review outputs. | ok |
| A-010 | `1_asset/llm_resolver_anchor.yaml` | Resolver/LLM capability scope and acceptance baseline. | ok |
| A-011 | `1_asset/llm_resolver_functional_design.md` | Human-readable resolver behavior and disallowed substitutes. | ok |
| A-012 | `1_asset/llm_resolver_demo_cases.md` | Expected resolver demo coverage for exact/proxy/not-found and LLM fallback behavior. | ok |
| A-013 | `1_asset/llm_resolver_acceptance_matrix.csv` | Resolver acceptance matrix and evidence labels. | ok |
| A-014 | `1_asset/evidence_route_taxonomy.md` | Route taxonomy for exact/proxy/no-hit/ambiguous/context-missing/transfer review. | ok |
| A-015 | `1_asset/evidence_metadata_contract.yaml` | Evidence metadata contract for route-aware milestone review. | ok |
| A-016 | `1_asset/evidence_routing_stress_mapping.csv` | Stress-route mapping to identify routing capabilities absent from M1 evidence. | ok |

## Execution Strategy
1. Read A-001 through A-004 first and extract explicit M1 claims, validation scope, entry points, evidence gates, demo scope, provenance layers, and known gaps into a working notes file under `3_execution/`.
2. Read A-005 through A-009 and build the package-anchor checklist using the provided capability matrix, downgrade rules, rubric, and controlled vocabulary.
3. Read A-010 through A-013 and assess resolver/LLM capabilities separately from deterministic lookup, including natural-language or semi-structured entry, LLM-assisted parsing/summarization, fallback behavior, and disallowed substitutes.
4. Read A-014 through A-016 and assess route behavior separately for exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion behavior, and metadata contract support.
5. Compare each anchor capability against M1 evidence, assigning only controlled status labels and citing the registered M1 evidence or registered M1 gap behind each label.
6. Decide one overall M1 classification and explicitly justify why it is `full milestone`, `deterministic kernel/substrate`, or `partial milestone`.
7. Identify unapproved scope shrinkage, especially deterministic lookup substituted for resolver/LLM/proxy/no-hit/metadata behavior, synthetic fixture evidence treated as full capability, or fallback-only behavior counted as primary delivery.
8. Write the required YAML, CSV, Markdown, HTML reports, update `4_artifact/registry.yaml`, and finish with `5_report/completion.md`.

## Conservative Execution Advice
- Start with: a small evidence inventory from A-001 through A-004 before reading all anchor files, so the execution AI knows what M1 actually claims before applying the anchors.
- Smoke/demo command or method: parse/read the YAML, JSON, and CSV inputs with a short script or manual structured read and confirm required top-level fields/columns are usable before drafting conclusions.
- Full run only after: all 16 registered inputs are readable and the controlled vocabulary/status labels from A-009 are available.
- Cost/time risk: low compute and no network/API cost; main risk is overreading predecessor context or inventing capability evidence that is not in the registered inputs.
- Checkpoint advice: keep an intermediate checklist in `3_execution/` mapping `anchor capability -> M1 evidence/gap -> proposed status`; only promote accepted reusable outputs into `4_artifact/`.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Machine-readable M1 anchor gap review YAML | `4_artifact/2_persist/m1_vs_delivery_anchor_gap_review_v20260625.yaml` | Valid YAML with overall classification, capability statuses, evidence notes, and downgrade/shrinkage flags. |
| Capability status matrix | `4_artifact/5_table/m1_vs_delivery_anchor_capability_matrix_v20260625.csv` | CSV covers in-scope package, resolver/LLM, and evidence-route capabilities with controlled labels. |
| Chinese narrative review report | `4_artifact/2_persist/m1_vs_delivery_anchor_review_report_v20260625.md` | Chinese report states classification, evidence basis, gaps, downgrade findings, and caveats. |
| Next milestone boundary recommendations | `4_artifact/2_persist/m1_next_milestone_boundary_recommendations_v20260625.md` | Chinese/clear recommendations define the next milestone boundary without silently downgrading required anchors. |
| Chinese execution report | `4_artifact/3_document/execution_report_v20260625.html` | HTML execution summary exists and reflects methods, inputs, and stop-condition handling. |
| Chinese result report | `4_artifact/3_document/result_report_v20260625.html` | HTML result report exists and summarizes classification and gap findings. |
| Artifact registry update | `4_artifact/registry.yaml` | All accepted reusable outputs are registered with paths and brief descriptions. |
| Completion report | `5_report/completion.md` | States what was produced, where, and whether any required item is incomplete or evidence-insufficient. |

## Failure / Stop Conditions
- Any required registered input asset is unreadable or structurally unusable.
- The controlled vocabulary or anchor rules cannot be interpreted well enough to assign statuses.
- A needed conclusion would require scanning unregistered predecessor folders, package source modification, runtime package validation, raw data analysis, or web search.
- M1 behavior is not present in registered evidence; mark the relevant capability `evidence-insufficient` or missing instead of inferring it.
- The task would need to alter T-053, T-062, T-063, T-064, project protocol, package code, or `6_project_deliverable/`.

## Notes For Delivery QA
- Check that the final outputs do not call M1 a complete algorithm package unless resolver/LLM behavior, evidence routing, fallback behavior, and metadata support are actually evidenced or explicitly approved as out-of-scope.
- Check that deterministic forward/reverse lookup is not counted as a substitute for user-facing resolver, LLM-assisted parsing/summarization, proxy/no-hit routing, or transfer/suggestion behavior.
- Check that the review separates delivered, partial, missing, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, and evidence-insufficient statuses.
- Check that all reusable outputs are in `4_artifact/`, not only `3_execution/`, and that `4_artifact/registry.yaml` includes them.
- Check that no downstream prompt generation endpoint was called during checking or execution.
