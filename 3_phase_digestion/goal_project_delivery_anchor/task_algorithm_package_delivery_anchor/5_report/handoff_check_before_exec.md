# Check Handoff Before Exec: T-062 algorithm_package_delivery_anchor

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories, `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/`, `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/`, `/Users/dudu/Documents/3_Project/12_PxFquery/6_project_deliverable/`, and `/Users/dudu/Documents/3_Project/8_functional_query`
- Required registry: `1_asset/registration.yaml` with eight ready registered assets A-001 through A-008
- Must stop if: registered assets are insufficient for a governance anchor, execution would require package code changes, algorithm tests, raw matrix analysis, web lookup, direct legacy-root inspection, or required outputs cannot be written under this task's allowed directories

## Objective Restatement
Create a task-level authoritative delivery anchor for future PxFquery algorithm-package milestones. The execution AI should digest registered predecessor evidence into capability definitions, acceptance vocabulary, downgrade controls, and review rubrics that prevent future milestones from silently reducing PxFquery to deterministic lookup only. This is a governance/digestion task, not a code, test, resource-build, or final-deliverable task.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/project_protocol_revision_report.md` | Protocol-normalization history and source-boundary context. | ok |
| A-002 | `1_asset/pxfquery_development_state_report.md` | Main source for intended package identity, behavior, and completion boundary. | ok |
| A-003 | `1_asset/pxfquery_development_gap_and_risk_list.md` | Risk, missing-capability, and overclaim controls. | ok |
| A-004 | `1_asset/mvp_capability_contract.md` | Prior MVP capability gates to generalize into package-delivery anchors. | ok |
| A-005 | `1_asset/capability_status_matrix.csv` | Current-run evidence for delivered, partial, blocked, failed, and missing capabilities. | ok |
| A-006 | `1_asset/failure_missing_capability_list.md` | Known failure, blocked, partial, and missing capabilities for stop and downgrade rules. | ok |
| A-007 | `1_asset/standard_resource_guide.md` | Verified standard resource basis for package compatibility and acceptance language. | ok |
| A-008 | `1_asset/standard_resources_bundle` | Canonical standard resource bundle reference; inspect names/metadata only if needed. | ok |

## Execution Strategy
1. Read only the registered assets A-001 through A-008 plus the current task protocol and project protocol snapshot; extract capability, acceptance, risk, downgrade, and resource-basis facts into temporary notes under `3_execution/`.
2. Build a project-valid capability set covering forward query, reverse query, biological context handling, exact/proxy/not-found routing, resolver-mediated query entry, LLM-assisted parsing/summarization where milestone scope requires it, deterministic fallback, transparent evidence metadata, and T-021 standard resource compatibility.
3. Write `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` with capability IDs, evidence requirements, allowed fallbacks, acceptance states, downgrade triggers, and user-approval requirements.
4. Write `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` mapping each capability to predecessor evidence, acceptance threshold, failure modes, and blocker/partial/deferral treatment.
5. Write downgrade and review documents under `4_artifact/2_persist/`, explicitly distinguishing runtime fallback from scope downgrade and defining future milestone labels.
6. Write Chinese Markdown and HTML summaries that explain the anchor purpose, required capability set, downgrade rules, and rubric use without overstating implementation readiness.
7. Register reusable outputs in `4_artifact/registry.yaml`, then write `5_report/completion.md` summarizing sources used, outputs produced, and any evidence limits.

## Conservative Execution Advice
- Start with: a short extraction pass over A-004, A-005, and A-006 to verify the T-013 vocabulary and missing-capability evidence before drafting the full anchor.
- Smoke/demo command or method: create a small temporary capability skeleton in `3_execution/` for three representative capabilities: forward query, resolver/LLM entry, and proxy evidence routing; verify each can carry fields for evidence, fallback, downgrade trigger, and approval requirement.
- Full run only after: the skeleton confirms the YAML and CSV schemas can represent deterministic, resolver/LLM, proxy, fallback, not-found, and resource-compatibility capabilities without collapsing them into one lookup category.
- Cost/time risk: low compute and no network/API cost; risk is mainly semantic overreach or accidental scope reduction.
- Checkpoint advice: before writing final `4_artifact/` outputs, compare capability coverage against the protocol's minimum capability list and against A-006 missing-capability categories.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | YAML parses and includes capabilities, evidence requirements, fallbacks, states, downgrade triggers, and approval rules. |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | CSV opens cleanly and maps each required capability to predecessor evidence, threshold, failure modes, and delivery treatment. |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Clearly separates runtime fallback from scope downgrade and requires explicit user approval for required-capability deferral/removal. |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Future reviewers can classify delivered, partial, blocked, failed, downgraded, deferred, out-of-scope, and evidence-insufficient states. |
| Classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | YAML parses and defines all required milestone labels with usage rules. |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` | Human-readable Chinese summary covers purpose, capability set, downgrade rules, and rubric use. |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` | HTML renders as a readable human-review summary. |
| Artifact registry update | `4_artifact/registry.yaml` | All reusable outputs are registered with paths, types, provenance, and status. |
| Completion report | `5_report/completion.md` | Report lists sources used, outputs produced, acceptance checks, and any residual limitations. |

## Failure / Stop Conditions
- Stop if any selected predecessor asset is missing, unreadable, empty, or semantically insufficient to define the anchor without guessing.
- Stop if anchor construction would require implementing or modifying package code.
- Stop if execution would require running algorithm tests, rebuilding indexes/resources, analyzing raw matrices, using web search, or directly reading `/Users/dudu/Documents/3_Project/8_functional_query`.
- Stop if the draft treats resolver, LLM-assisted behavior, proxy routing, not-found routing, or user-facing query transfer as optional when a milestone requires them and no user-approved downgrade is recorded.
- Stop if accepted reusable outputs would remain only in `3_execution/` instead of `4_artifact/`.
- Stop if required outputs or reports cannot be written under allowed task directories.

## Notes For Delivery QA
- Mechanical asset preflight is clean: 8 assets checked, 8 linked, 8 ok, no missing or forbidden-scope assets.
- No Yellow Repair was needed; protocol, registry, and asset rules are mutually consistent.
- The execution AI should not rediscover predecessor context, scan arbitrary predecessor folders, inspect legacy source roots, call web search, or generate downstream prompts.
- QA should check that conservative manuscript claim restraint is not used as a reason to remove development delivery capabilities.
- QA should validate parseability of the YAML and CSV outputs and confirm `4_artifact/registry.yaml` registers all reusable deliverables.
