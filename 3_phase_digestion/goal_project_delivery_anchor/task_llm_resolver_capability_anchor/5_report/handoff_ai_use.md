# AI Handoff: T-063 llm_resolver_capability_anchor

## Task Goal

Create a reusable LLM/resolver capability and acceptance anchor for future PxFquery package milestones, especially M3 resolver delivery. The task is governance/design only; it does not implement or validate runtime resolver code.

## What Was Delivered

T-063 delivered a machine-readable resolver capability anchor, a human-readable functional design, a required demo case catalog, an acceptance matrix, and Chinese execution/result reports. The outputs define natural-language and semi-structured query entry, CyHex-registered AI service use with current desired route `deepseek-v4-pro`, exact/proxy/not-found routing, fallback semantics, downgrade controls, and future acceptance evidence.

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T063-A-001 | `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | Primary machine-readable anchor for resolver/LLM capability scope and acceptance. | Use as the baseline when configuring or checking any milestone that claims M3 resolver capability. |
| T063-A-002 | `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | Human-readable interpretation of required user-facing resolver behavior. | Read before implementation planning to avoid reducing resolver delivery to deterministic lookup. |
| T063-A-004 | `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | Maps each resolver capability to evidence, minimum behavior, disallowed substitutes, and review labels. | Use during milestone QA to classify delivered, partial, blocked, failed, downgraded, deferred, or evidence-insufficient states. |

## Supporting Artifacts

| ID | Path | Role |
|---|---|---|
| T063-A-003 | `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | Required future M3 demo case set covering exact/proxy/not-found, forward/reverse, ambiguous NL, semi-structured input, LLM fallback, and metadata inspection. |
| T063-A-005 | `4_artifact/3_document/execution_report_v20260625.html` | Chinese execution audit report. |
| T063-A-006 | `4_artifact/3_document/result_report_v20260625.html` | Chinese result summary for human review. |
| process | `3_execution/resolver_requirement_extraction_v20260625.md` | Task-local extraction notes only; useful for audit, not the primary downstream source. |

## Downstream Use

Future config/check/execute agents should treat this task as the resolver-specific refinement of T-062, not as a competing package anchor. If a future milestone includes user-facing resolver, LLM parsing/summarization, proxy routing, or not-found behavior, use T063-A-001 and T063-A-004 as mandatory acceptance references. Fallback-only behavior, endpoint connectivity alone, or direct matrix lookup alone must not be counted as full resolver delivery.

## Known Limits / Risks

These artifacts are design and acceptance anchors only. They do not prove that resolver code works, that the LLM service has been exercised through a resolver, that missing indexes have been repaired, or that package runtime tests pass. LLM output is defined as parsing, normalization, ambiguity explanation, and summarization assistance; it is not independent biological evidence.

## Do Not Read / Do Not Reuse

Do not reuse prompt files in `2_protocol/0_prompt/` as scientific or capability authority. Do not read predecessor task directories or legacy source roots for this handoff unless a later task explicitly registers and justifies those reads. Do not treat `3_execution/` notes as the authoritative deliverable over the registered artifacts.

## Recommended Next Reads

1. `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml`
2. `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv`
3. `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md`
4. `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md`
