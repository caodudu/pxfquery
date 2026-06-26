# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:15

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-062 algorithm_package_delivery_anchor
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor`
- Objective:

```text
Create the authoritative PxFquery algorithm-package delivery anchor. Define the project-valid package capability set, acceptance rubric, downgrade rules, and milestone classification vocabulary so future package milestones cannot silently shrink into deterministic lookup only.
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
5. Write downgrade rules that clearly distinguish runtime fallback from scope downgrade. A fallback path may be valid behavior, but it cannot count as delivery of the primary resolver/LLM/proxy capability unless the milestone explicitly accepts fallback-only behavio

...[truncated by CyHex prompt assembler: 5174 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: T062-A-001
  name: pxfquery_algorithm_package_delivery_anchor
  type: yaml
  path: 2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-001
    - A-002
    - A-003
    - A-004
    - A-005
    - A-006
    - A-007
    - A-008
  notes: Machine-readable delivery anchor with capabilities, evidence requirements,
    fallback rules, and downgrade triggers.
  stars: 5
  identity: T-062/T062-A-001
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-002
  name: pxfquery_algorithm_capability_matrix
  type: table
  path: 5_table/pxfquery_algorithm_capability_matrix_v20260625.csv
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-002
    - A-003
    - A-004
    - A-005
    - A-006
    - A-007
  notes: Capability-to-evidence matrix for future package milestone reviews.
  stars: 5
  identity: T-062/T062-A-002
  role: data
  core: false
  lineage_anchor: false
- id: T062-A-003
  name: pxfquery_algorithm_downgrade_rules
  type: document
  path: 2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-001
    - A-002
    - A-003
    - A-004
    - A-006
  notes: Rules distinguishing runtime fallback from scope downgrade and requiring
    approval for capability reduction.
  stars: 5
  identity: T-062/T062-A-003
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-004
  name: pxfquery_milestone_review_rubric
  type: document
  path: 2_persist/pxfquery_milestone_review_rubric_v20260625.md
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-002
    - A-003
    - A-005
    - A-006
    - A-007
  notes: Review rubric and evidence hierarchy for algorithm-package milestone acceptance.
  stars: 5
  identity: T-062/T062-A-004
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-005
  name: pxfquery_milestone_classification_vocabulary
  type: yaml
  path: 2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-003
    - A-004
    - A-005
    - A-006
  notes: Machine-readable vocabulary for delivered, partial, blocked, failed, downgraded,
    deferred, out-of-scope, and evidence-insufficient states.
  stars: 5
  identity: T-062/T062-A-005
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-006
  name: pxfquery_algorithm_package_delivery_anchor_summary_md
  type: document
  path: 2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-001
    - A-002
    - A-003
    - A-004
    - A-005
    - A-006
    - A-007
  notes: Chinese human-readable summary of anchor purpose, capability set, downgrade
    rules, and review use.
  stars: 4
  identity: T-062/T062-A-006
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-007
  name: pxfquery_algorithm_package_delivery_anchor_summary_html
  type: document
  path: 3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - T062-A-006
  notes: Chinese HTML summary for human review.
  stars: 4
  identity: T-062/T062-A-007
  role: support
  core: false
  lineage_anchor: false
- id: T062-A-008
  name: execution_report
  type: document
  path: 3_document/execution_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - A-001
    - A-002
    - A-003
    - A-004
    - A-005
    - A-006
    - A-007
    - A-008
  notes: Required Chinese execution report for T-062.
  stars: 3
  identity: T-062/T062-A-008
  role: report
  core: false
  lineage_anchor: false
- id: T062-A-009
  name: result_report
  type: document
  path: 3_document/result_report_v20260625.html
  created: '2026-06-25'
  status: accepted
  provenance:
    task_id: T-062
    sources:
    - T062-A-001
    - T062-A-002
    - T062-A-003
    - T062-A-004
    - T062-A-005
    - T062-A-006
  notes: Required Chinese result report summarizing produced anchor artifacts.
  stars: 3
  identity: T-062/T062-A-009
  role: report
  core: false
  lineage_anchor: false

```

### Completion Report
```md
# Completion

Task: T-062 algorithm_package_delivery_anchor  
Completed: 2026-06-25  
Status: Completed

## Completed Steps

1. Confirmed task-local structure and selected registered assets A-001 through A-008 were available through the task `1_asset/` registry links.
2. Read only the registered predecessor artifacts needed for capability, acceptance, risk, downgrade, and resource-basis extraction.
3. Wrote step discipline and extraction notes under `3_execution/step_list_and_extraction_notes_v20260625.md`.
4. Produced all required reusable deliverables under `4_artifact/`.
5. Validated the two YAML files parse as dictionaries and the capability matrix parses as CSV with 11 capability rows.
6. Registered accepted artifacts in `4_artifact/registry.yaml`.
7. Wrote required Chinese HTML execution and result reports.

## Deliverables Produced

| Deliverable | Path |
|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` |
| Milestone classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` |
| Required execution report | `4_artifact/3_document/execution_report_v20260625.html` |
| Required result report | `4_artifact/3_document/result_report_v20260625.html` |
| Artifact registry | `4_artifact/registry.yaml` |

## Validation Evidence

Command run:

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "from pathlib import Path; import yaml,csv; base=Path('3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor'); files=['4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml','4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml']; [print(f, type(yaml.safe_load((base/f).read_text())).__name__) for f in files]; rows=list(csv.DictReader((base/'4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv').open(newline=''))); print('matrix_rows', len(rows)); print('matrix_fields', ','.join(rows[0].keys()))"
```

Observed output:

```text
4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml dict
4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml dict
matrix_rows 11
matrix_fields capability_id,capability,required_when,required_evidence,current_predecessor_evidence,acceptance_threshold,likely_failure_modes,absence_treatment,user_approval_required_for_deferral
```

## Evidence Limits

- This was a digestion/governance task only.
- No package source code was modified.
- No algorithm tests were run.
- No query indexes, matrices, or raw resources were rebuilt.
- No web search or external sources were used.
- No direct read from `/Users/dudu/Documents/3_Project/8_functional_query` was performed.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-062 algorithm_package_delivery_anchor

## Task Goal

Create a task-level authoritative delivery anchor for future PxFquery algorithm-package milestones. The anchor prevents future milestones from silently shrinking PxFquery into deterministic lookup only when resolver, LLM-assisted behavior, proxy routing, fallback behavior, or user-facing query transfer are in scope.

## What Was Delivered

T-062 delivered a machine-readable package delivery anchor, capability matrix, downgrade rules, milestone review rubric, classification vocabulary, Chinese Markdown/HTML summary, and Chinese execution/result reports. The outputs are governance and review artifacts only; no package code, algorithm tests, resources, matrices, or final project deliverables were modified.

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T062-A-001 | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | Primary machine-readable capability anchor. | Start here when configuring or reviewing any future algorithm-package milestone. |
| T062-A-002 | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | Maps required capabilities to evidence, thresholds, failure modes, and deferral treatment. | Use as the checklist for milestone acceptance and gap review. |
| T062-A-003 | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Defines what counts as runtime fallback versus scope downgrade. | Read before proposing deferral, optionalization, or fallback-only acceptance. |
| T062-A-004 | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Provides evidence hierarchy and review procedure. | Use during check/review stages for package milestones. |
| T062-A-005 | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | Machine-readable status vocabulary for capability review. | Reuse labels in future reports and task registries. |

## Supporting Artifacts

| ID | Path | Use |
|---|---|---|
| T062-A-006 | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` | Human-readable Chinese summary for quick review. |
| T062-A-007 | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` | HTML version of the Chinese summary. |
| T062-A-008 | `4_artifact/3_document/execution_report_v20260625.html` | Chinese execution report for audit. |
| T062-A-009 | `4_artifact/3_document/result_report_v20260625.html` | Chinese result report summarizing outputs and downstream use. |

## Downstream Use

Future package milestone tasks should read the anchor YAML first, then the capability matrix and downgrade rules. Any milestone review should classify each in-scope capability as delivered, partial, blocked, failed, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, or evidence-insufficient. Required resolver, LLM, proxy, not-found, metadata, or user-entry behavior must not be counted as delivered solely because a deterministic fallback exists.

## Known Limits / Risks

This task is a digestion/governance anchor. It does not prove that package behavior works, does not run algorithm tests, and does not validate resources beyond using registered predecessor evidence. Future execution tasks still need working-code evidence for any capability they claim as delivered.

## Do Not Read / Do Not Reuse

Do not treat `3_execution/step_list_and_extraction_notes_v202606

...[truncated by CyHex prompt assembler: 623 chars omitted]
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
