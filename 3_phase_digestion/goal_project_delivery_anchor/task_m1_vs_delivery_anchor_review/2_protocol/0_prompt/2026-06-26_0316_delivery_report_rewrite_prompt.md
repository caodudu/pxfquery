# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:16

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-065 m1_vs_delivery_anchor_review
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_m1_vs_delivery_anchor_review`
- Objective:

```text
Review the completed M1 package milestone against the project delivery anchors. Classify M1 as full milestone, deterministic kernel/substrate, or partial milestone; list delivered, partial, missing, downgraded, and deferred anchored capabilities; identify unapproved scope shrinkage and recommend the next milestone boundary.
```

## Source Material You May Use

Use only the source material embedded below. Do not read old HTML reports. Do not scan predecessor tasks, raw assets, project asset libraries, CLI logs, prompt files, or unrelated folders.

### Project Overview
```text
# Overview

PxFquery is a macOS-hosted restart of a legacy bioinformatics project for LINCS-based perturbation-to-function analysis.

The project's active purpose is to turn useful legacy code, data, reports, and manuscript strategy into a controlled current workspace for later development and submission work. It is not a continuation of the old Windows-era directory trees.

Scientifically, PxFquery is a Python workflow/tool for querying drug- and gene-induced functional programs from perturbation data. Its core direction is:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- evidence-aware retrieval using exact and proxy matches;
- manuscript positioning around a concrete LINCS functional genomics use case rather than an inflated AI-agent platform claim.

The legacy project contains valuable material, including package code, query indexes, CMAP/LINCS-derived functional matrices, resolver reports, and Genes submission strategy. In the current project, those materials are treated as migrated or registered historical assets. Their useful meaning should be digested into current tasks before reuse.

The current project protocol is the persistent project-level rule layer. It should stay concise, current, and independent of old 4t, Obsidian, checkpoint, or Windows directory protocol shells.

```

### Project Goal
```text
# Goal

## Primary Goal

Build a clean, current PxFquery project that can reuse the valuable legacy assets to support controlled software development, reproducible analysis, and a pragmatic manuscript path.

## Scientific Goal

Position PxFquery as a LINCS-based perturbation-to-function bioinformatics workflow for interpreting drug- and gene-induced functional programs in biological contexts such as cancer cell lines.

## Functional Delivery Goal

PxFquery's project-level functional goal is not limited to static matrix lookup. A project-valid package must preserve the intended user-facing query experience:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- resolver-mediated natural-language or semi-structured query entry;
- exact, proxy, and not-found evidence routing for sparse biological coverage;
- LLM-assisted parsing and summarization through the current configured AI service when a milestone requires the user-facing resolver layer;
- deterministic fallback and transparent evidence metadata when LLM or proxy routing fails.

Milestones may stage these capabilities in layers, but a milestone may not silently redefine PxFquery as only deterministic dictionary or matrix lookup if the user-defined milestone requires resolver, LLM, proxy, or transfer behavior. Any proposed scope reduction, deferral, or optionalization of a functional capability must be explicitly reported to the user before task creation and must receive user approval.

## Manuscript Goal

Prepare for a realistic MDPI Genes-style submission by emphasizing a narrow, reproducible functional genomics workflow and a concrete biological case study, rather than presenting PxFquery as a broad AI-agent platform.

This manuscript path is graduation-oriented and journal-fit-oriented. The target is not to build a genuinely high-novelty tool paper or to compete with venues such as Bioinformatics, Nature-family journals, or other high-bar computational biology outlets. The work should look sufficiently substantial in the style of recent Genes papers while remaining practically lightweight, easy t

...[truncated by CyHex prompt assembler: 1049 chars omitted]
```

### Task Protocol
```text
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
| A-0

...[truncated by CyHex prompt assembler: 6176 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: T065-A-001
  name: m1_vs_delivery_anchor_gap_review_v20260625
  type: machine_readable_review
  path: 4_artifact/2_persist/m1_vs_delivery_anchor_gap_review_v20260625.yaml
  created: '2026-06-25'
  status: accepted
  role: core_gap_review
  produced_by: T-065
  description: Machine-readable M1-versus-delivery-anchor gap review with overall classification, capability statuses, evidence notes, downgrade/shrinkage flags, and next-boundary signals.
  usable_by: future config/check/execute agents deciding whether M1 can be treated as a full package milestone or only as a deterministic kernel/substrate.
  core: true
  lineage_anchor: T-053 M1 evidence compared against T-062, T-063, and T-064 anchors.
  stars: 5
  notes: Produced by T-065 milestone-vs-delivery-anchor review.
- id: T065-A-002
  name: m1_vs_delivery_anchor_capability_matrix_v20260625
  type: table
  path: 4_artifact/5_table/m1_vs_delivery_anchor_capability_matrix_v20260625.csv
  created: '2026-06-25'
  status: accepted
  role: capability_status_matrix
  produced_by: T-065
  description: Tabular capability-by-capability status matrix covering package, resolver/LLM, and evidence-route anchors with controlled labels.
  usable_by: downstream milestone planners, check agents, and repair-task authors needing a compact capability checklist.
  core: true
  lineage_anchor: T-053 M1 evidence compared against T-062, T-063, and T-064 anchors.
  stars: 5
  notes: Produced by T-065 milestone-vs-delivery-anchor review.
- id: T065-A-003
  name: m1_vs_delivery_anchor_review_report_v20260625
  type: document
  path: 4_artifact/2_persist/m1_vs_delivery_anchor_review_report_v20260625.md
  created: '2026-06-25'
  status: accepted
  role: narrative_review
  produced_by: T-065
  description: Chinese narrative review explaining why M1 is classified as deterministic kernel/substrate and not a complete anchored algorithm package.
  usable_by: humans and future AI agents needing the reasoning behind the machine-readable gap review.
  core: true
  lineage_anchor: T-053 M1 evidence compared against T-062, T-063, and T-064 anchors.
  stars: 5
  notes: Produced by T-065 milestone-vs-delivery-anchor review.
- id: T065-A-004
  name: m1_next_milestone_boundary_recommendations_v20260625
  type: document
  path: 4_artifact/2_persist/m1_next_milestone_boundary_recommendations_v20260625.md
  created: '2026-06-25'
  status: accepted
  role: next_milestone_boundary
  produced_by: T-065
  description: Chinese recommendations for the next milestone boundary, separating M2 current-resource evidence routing from M3 resolver/LLM user-facing work.
  usable_by: future task configuration and milestone planning.
  core: true
  lineage_anchor: Recommendations derived from the T-065 gap review.
  stars: 5
  notes: Produced by T-065 milestone-vs-delivery-anchor review.
- id: T065-A-005
  name: execution_report_v20260625
  type: html_report
  path: 4_artifact/3_document/execution_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  role: human_execution_report
  produced_by: T-065
  description: Chinese HTML execution report summarizing scope, steps, classification, and capability statuses.
  usable_by: human review and audit.
  core: false
  lineage_anchor: Rendered human-facing report for T-065 outputs.
  stars: 3
  notes: Produced by T-065 milestone-vs-delivery-anchor review.
- id: T065-A-006
  name: result_report_v20260625
  type: html_report
  path: 4_artifact/3_document/result_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  role: human_result_report
  produced_by: T-065
  description: Chinese HTML result report summarizing the M1 classification, major gaps, and recommended milestone sequence.
  usable_by: human review and audit.
  core: false
  lineage_anchor: Rendered human-facing report for T-065 outputs.
  stars: 3
  notes: Produced by T-065 milestone-vs-delivery-anchor review.

```

### Completion Report
```md
# Completion

Task: T-065 `m1_vs_delivery_anchor_review`  
Completed: 2026-06-25  
Status: complete

## Completed Steps

1. Verified registered input assets A-001 through A-016 were available under `1_asset/`.
2. Extracted M1 claims from the milestone report, evidence index, layered asset map, and known-gap report.
3. Compared M1 evidence against T-062 package delivery anchors, T-063 resolver/LLM anchors, and T-064 evidence-routing anchors.
4. Classified M1 as `deterministic kernel/substrate`.
5. Produced the required YAML, CSV, Markdown, HTML reports and updated the artifact registry.

## Deliverables

- `4_artifact/2_persist/m1_vs_delivery_anchor_gap_review_v20260625.yaml`
- `4_artifact/5_table/m1_vs_delivery_anchor_capability_matrix_v20260625.csv`
- `4_artifact/2_persist/m1_vs_delivery_anchor_review_report_v20260625.md`
- `4_artifact/2_persist/m1_next_milestone_boundary_recommendations_v20260625.md`
- `4_artifact/3_document/execution_report_v20260625.html`
- `4_artifact/3_document/result_report_v20260625.html`
- `4_artifact/registry.yaml`

## Validation Performed

- Parsed JSON/YAML/CSV/Markdown inputs needed for the review.
- Wrote outputs with controlled status labels from the T-062/T-063 vocabulary.
- Confirmed final artifact paths exist and are non-empty after generation.

## Caveats

This task did not run package validation, repair code, analyze raw data, or inspect unregistered predecessor folders. The review is evidence-based only on the 16 registered input assets.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-065 m1_vs_delivery_anchor_review

## Task Goal
Review the completed M1 package milestone against the project delivery anchors, classify M1, identify anchored capability gaps and unapproved scope shrinkage, and recommend the next milestone boundary.

## What Was Delivered
T-065 delivered a post-M1 anchor review. The key conclusion is that M1 should be treated as `deterministic kernel/substrate`, not as a full anchored algorithm package. M1 has deterministic forward/reverse substrate evidence, but lacks sufficient standard-resource, resolver/LLM, proxy routing, transfer/suggestion, and route-aware metadata evidence for full milestone credit.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T065-A-001 | `4_artifact/2_persist/m1_vs_delivery_anchor_gap_review_v20260625.yaml` | Machine-readable source of the overall classification, status labels, downgrade flags, and next-boundary signals. | Read first when configuring any follow-up task that depends on whether M1 is complete. |
| T065-A-002 | `4_artifact/5_table/m1_vs_delivery_anchor_capability_matrix_v20260625.csv` | Compact capability checklist across package, resolver/LLM, and evidence-routing anchors. | Use as the starting checklist for M2/M3 scope, acceptance gates, and repair tickets. |
| T065-A-003 | `4_artifact/2_persist/m1_vs_delivery_anchor_review_report_v20260625.md` | Chinese narrative explanation of the classification and evidence basis. | Read after the YAML when human-readable reasoning or caveats are needed. |
| T065-A-004 | `4_artifact/2_persist/m1_next_milestone_boundary_recommendations_v20260625.md` | Defines recommended next milestone boundaries without silently downgrading project anchors. | Use when drafting the next milestone protocol or task DAG. |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260625.html`: Chinese HTML execution summary for human audit.
- `4_artifact/3_document/result_report_v20260625.html`: Chinese HTML result summary for human review.
- `3_execution/working_notes_v20260625.md`: execution-side working notes; use only if audit detail is needed.
- `3_execution/generate_t065_outputs.py`: generation script; use only for reproducibility inspection, not as a downstream source of truth.

## Downstream Use
Future tasks should not cite M1 as a complete algorithm package. They should cite T-065 when stating that M1 is a deterministic kernel/substrate and should use the capability matrix to decide which gaps belong in M2 versus M3.

Recommended boundary from T-065: M2 should focus on current-resource evidence routing and metadata; M3 should focus on resolver/LLM user-facing entry, parsing, summarization, and required demo coverage.

## Known Limits / Risks
The review is evidence-based only on the 16 registered task inputs. It did not rerun package validation, inspect predecessor task internals, modify package code, analyze raw data, or use web search. Absence of evidence in T-065 should be interpreted as absence from registered M1/anchor evidence, not as a fresh runtime failure.

## Do Not Read / Do Not Reuse
Do not read predecessor task directories to reinterpret this review unless a future protocol explicitly permits it. Do not use `3_execution/` files as accepted deliverables when the same information exists in `4_artifact/`. Do not treat deterministic CLI/fixture behavior as a substitute for resolver/LLM, proxy, transfer/suggestion, or route-metadata capabilities.

## Recommended N

...[truncated by CyHex prompt assembler: 319 chars omitted]
```

## Required Writes

Overwrite or create both files:

1. `4_artifact/3_document/execution_report_v20260626.html`
2. `4_artifact/3_document/result_report_v20260626.html`

Then update `5_report/delivery_qa.md` briefly with `Verdict: yellow_repair`, saying the repair was human-readable report rewriting only. Do not modify core deliverables, registry paths, code, data, or analysis results.

## Writing Standard

Write in Chinese. Use natural-language paragraphs, not an audit checklist. Tables are allowed only for a short artifact guide; they must not be the main report. The report should read like a concise project briefing for a busy human decision-maker, not like a compliance form.

Each HTML report must have at least 900 Chinese characters of visible explanation. Each major section should contain a paragraph of 3-6 sentences. Every paragraph should include task-specific nouns, artifact names, findings, counts, decisions, or boundaries from this task.

Do not copy old HTML with only date/path changes. Do not write generic phrases like "completed successfully" unless you explain exactly what was completed.

Do not expose internal repair mechanics in the visible HTML body. Forbidden visible phrases include "报告重写", "重写版本", "为了通过 validator", "health warning", "低信息量报告修复", and similar wording. It is acceptable to record repair mechanics in `5_report/delivery_qa.md`, but the HTML reports must look like first-class task reports, not patched validator output.

The first screen of each report should immediately orient a reader who knows nothing: name the project problem, explain this task's role in the task chain, and state the concrete outcome. Include a specific project-value paragraph that explains how the task changes future work, risk, capability, or decision-making.

## execution_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 任务意图
2. 输入资产与依据
3. 实际执行过程
4. 关键判断与证据
5. 交付物清单
6. 边界与未完成事项

The execution report should explain the work process: why the task was needed, what evidence was used, what the original execution did, what concrete findings or counts were produced, where the artifacts are, and what was intentionally not done. It should help the project owner reconstruct the task without reading execution logs.

## result_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 一句话结论
2. 项目背景
3. 核心结果
4. 项目价值
5. 交付物导读
6. 后续使用方式
7. 边界与风险

The result report should read like a concise project briefing. It should help a human quickly understand the value of this task without reading registry.yaml, completion.md, or source assets. Avoid sounding like a template; if a paragraph could apply to any task, rewrite it with this task's concrete names, decisions, numbers, and consequences.

## Final Response

Return a short Chinese summary:

```md
### 交付报告重写完成
- 写入:
- 修复重点:
- 仍需注意:
```
