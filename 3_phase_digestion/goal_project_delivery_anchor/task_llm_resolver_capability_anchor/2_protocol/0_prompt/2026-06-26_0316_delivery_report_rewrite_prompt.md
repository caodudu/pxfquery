# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:16

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-063 llm_resolver_capability_anchor
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor`
- Objective:

```text
Create the LLM/resolver capability anchor for future PxFquery package milestones. Specify user-facing natural-language/semi-structured query behavior, CyHex-configured AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics, demo cases, and acceptance evidence for M3-level resolver delivery.
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
| A-012 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_r

...[truncated by CyHex prompt assembler: 7127 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: T063-A-001
  name: pxfquery_llm_resolver_capability_anchor
  type: yaml
  path: 4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 5
  description: Machine-readable LLM/resolver capability anchor for future M3-level
    PxFquery resolver milestones.
  source_assets:
  - A-001
  - A-002
  - A-003
  - A-004
  - A-005
  - A-006
  - A-007
  - A-008
  - A-009
  - A-010
  - A-011
  - A-012
  - A-013
  notes: Design and acceptance anchor only; not runtime implementation evidence.
  identity: T-063/T063-A-001
  role: support
  core: false
  lineage_anchor: false
- id: T063-A-002
  name: pxfquery_llm_resolver_functional_design
  type: document
  path: 4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 5
  description: Human-readable functional design for natural-language/semi-structured
    resolver behavior, AI routing, evidence routing, fallback, and disallowed substitutes.
  source_assets:
  - A-001
  - A-002
  - A-003
  - A-004
  - A-005
  - A-006
  - A-007
  - A-009
  - A-011
  - A-012
  - A-013
  identity: T-063/T063-A-002
  role: support
  core: false
  lineage_anchor: false
- id: T063-A-003
  name: pxfquery_llm_resolver_demo_case_catalog
  type: document
  path: 4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 4
  description: Required future M3 resolver demo case catalog covering exact, proxy,
    not-found, ambiguous, semi-structured, LLM fallback, and metadata inspection cases.
  source_assets:
  - A-005
  - A-006
  - A-009
  - A-010
  - A-011
  - A-012
  identity: T-063/T063-A-003
  role: support
  core: false
  lineage_anchor: false
- id: T063-A-004
  name: pxfquery_llm_resolver_acceptance_matrix
  type: table
  path: 4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 5
  description: Capability-to-evidence matrix for resolver acceptance, minimum behavior,
    disallowed substitutes, and review labels.
  source_assets:
  - A-005
  - A-006
  - A-009
  - A-010
  - A-011
  - A-012
  - A-013
  identity: T-063/T063-A-004
  role: data
  core: false
  lineage_anchor: false
- id: T063-A-005
  name: execution_report
  type: html_report
  path: 4_artifact/3_document/execution_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 3
  description: Chinese execution report recording inputs read, methods, boundaries,
    and verification.
  identity: T-063/T063-A-005
  role: report
  core: false
  lineage_anchor: false
- id: T063-A-006
  name: result_report
  type: html_report
  path: 4_artifact/3_document/result_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  reusable: true
  stars: 3
  description: Chinese result report summarizing produced anchor outputs and future
    use.
  identity: T-063/T063-A-006
  role: report
  core: false
  lineage_anchor: false

```

### Completion Report
```md
# Completion

Task: T-063 `llm_resolver_capability_anchor`  
Date: 2026-06-25  
State: completed

## Completed Steps

1. Confirmed task workspace and all 13 registered required assets were available.
2. Confirmed local CyHex API version endpoint once: app version `1.2.20`.
3. Read only registered inputs A-001 through A-013 and extracted resolver-relevant requirements, gaps, downgrade rules, source boundaries, and vocabulary.
4. Wrote execution extraction notes under `3_execution/`.
5. Produced the machine-readable LLM/resolver capability anchor.
6. Produced the human-readable functional design document.
7. Produced the resolver demo case catalog.
8. Produced the resolver acceptance matrix.
9. Produced the required HTML execution and result reports.
10. Updated `4_artifact/registry.yaml` with all accepted/reusable outputs.

## Deliverables Produced

- `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml`
- `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md`
- `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md`
- `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv`
- `4_artifact/3_document/execution_report_v20260625.html`
- `4_artifact/3_document/result_report_v20260625.html`
- `4_artifact/registry.yaml`

## Verification Performed

- Required input existence check passed before drafting.
- Deliverable existence and non-empty checks passed.
- YAML and CSV parse checks passed.
- Content coverage check confirmed key required terms: `deepseek-v4-pro`, `CyHex-registered AI address`, exact/proxy/not-found routing, fallback semantics, downgrade control, natural-language entry, semi-structured entry, and evidence metadata.

## Boundaries Observed

- No package/API/source implementation or modification.
- No package workflow, runtime test, notebook, matrix inspection, or biological analysis.
- No direct legacy source-root read.
- No web search.
- No downstream prompt endpoint call.
- No final project deliverable directory modification.

## Caveats

The outputs are design and acceptance anchors only. They do not prove that the current resolver code works, that the LLM service was tested through the resolver, that missing indexes were repaired, or that package runtime tests pass.

```

### Existing AI Handoff, If Any
```md
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

Do not reuse prompt files in `2_protocol/0_prompt/` as scientific or capability authority. Do not read predecessor task directories or legacy source roots for this handoff u

...[truncated by CyHex prompt assembler: 510 chars omitted]
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
