# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:41

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-053 m1_python_package_milestone
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone`
- Objective:

```text
Deliver the M1 PxFquery Python package milestone. Use T-050 forward validation, T-051 reverse validation, and T-052 package assembly as the three hard evidence gates. Deliver the final package location/version, demo commands, validation evidence index, layered asset map, and known gap report. Do not fix lower-layer implementation here; if evidence is missing, report the precise failed layer and recommend same-layer repair tasks.
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
# T-053 m1_python_package_milestone — Protocol

## Objective

Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable. Produce a layered asset map, evidence index, demo commands, known gap report, and the final package location/version. Do not repair or reimplement any lower-layer code.

## Position In Project

This is the capstone task under `goal_m1_python_package_v2`. T-050, T-051, and T-052 are all completed with PASS verdicts. This task collects their outputs, indexes them, and presents the milestone as a consumable handoff for downstream delivery/review.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-050 | `task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv` | Primary forward validation evidence (11 checks, all PASS) |
| A-002 | T-050 | `task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md` | Full validation narrative for forward query |
| A-003 | T-051 | `task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | Primary reverse validation evidence (42 checks, all PASS) |
| A-004 | T-051 | `task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | Per-check pass/fail table for reverse validation |
| A-005 | T-051 | `task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html` | Human-readable reverse validation HTML report |
| A-006 | T-052 | `task_package_assembly_m1/4_artifact/1_package/` | Assembled M1 pxfquery package source (v0.1.0) |
| A-007 | T-052 | `task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Import smoke test evidence |
| A-008 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json` | Forward demo JSON (EGFR/A549/xpr, found:true) |
| A-009 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json` | Reverse demo JSON (MYC_TARGETS_V1/A549, found:true) |
| A-010 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt` | CLI help text capture |
| A-011 | T-052 | `task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html` | Package assembly execution report |
| A-012 | T-052 | `task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html` | Package assembly result report |

## Execution Steps

1. **Collect & index T-050 forward validation evidence** — Read A-001 and A-002. Record: 11/11 PASS, package v0.1.0, M1FixtureLoader, synthetic_repair manifest.
2. **Collect & index T-051 reverse validation evidence** — Read A-003, A-004, A-005. Record: 42/42 PASS, cosine similarity ranking, top-3 matching reference.
3. **Collect & index T-052 package assembly evidence** — Read A-006 through A-012. Record: pip installable package at source path, version 0.1.0, all 9 acceptance criteria passed, forward/reverse CLI demos working.
4. **Build layered asset map** — Map which predecessor produced which asset, which layer (skeleton → forward implementation → reverse implementation → package assembly → forward validation → reverse validation) each asset belongs to, and which assets are consumed by this milestone.
5. **Write evidence index** — Create a structured index (JSON or Markdown) listing all three evidence streams with verdicts, key metrics, and cross-references.
6. **Record demo commands** — Document working CLI commands for forward query, reverse query, and info subcommand as validated by T-052 and T-050/T-051.
7. **Identify known gaps** — Check for any missing evidence, incomplete coverage, or known limits reported by predecessors. Report precise failed layer if evidence is missing; do not fix.
8. **Write milestone report** — Compile all findings into `5_report/milestone_report_v<timestamp>.md` (or `.html`).
9. **Register deliverables** — Update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not re-run validation or re-assemble the package.
- Do not modify any predecessor task artifact or directory.
- Do not read project-level raw assets under `2_project_asset/`.
- Do not implement, repair, or modify any query logic or package code.
- All information must come from predecessor handoffs and registered artifacts.
- If any required evidence stream is missing, report the failed layer and recommend a same-layer repair task; do not mark gaps as done.

## Forbidden

- Modifying predecessor task files or directories.
- Re-running validation or assembly commands.
- Reading `2_project_asset/` (forbidden for non-digestion task).
- Reading T-024 through T-040 artifacts.
- Creating duplicate or redundant evidence.

## Web Search Allowance

Allowed: no
Reason: All evidence is local from predecessor tasks. No external information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Milestone report | `4_artifact/3

...[truncated by CyHex prompt assembler: 1661 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: milestone_report
  type: document
  path: 4_artifact/3_document/milestone_report_v20260624_061117.md
  role: primary
  description: M1 milestone report summarizing all three evidence streams, package
    location/version, layered asset map, known gaps, and demo commands
  generated: 2026-06-24
  status: accepted
  stars: 5
  task_id: T-053
  identity: T-053/D-001
  core: false
  lineage_anchor: false
- id: D-002
  name: evidence_index
  type: data
  path: 4_artifact/2_persist/evidence_index_v20260624_061117.json
  role: primary
  description: Structured JSON index of all three evidence streams with verdicts,
    key metrics, and cross-references
  generated: 2026-06-24
  status: accepted
  stars: 5
  task_id: T-053
  identity: T-053/D-002
  core: false
  lineage_anchor: false
- id: D-003
  name: layered_asset_map
  type: table
  path: 4_artifact/5_table/layered_asset_map_v20260624_061117.csv
  role: primary
  description: CSV mapping each asset to its predecessor task, layer (skeleton → forward
    impl → reverse impl → package assembly → forward validation → reverse validation),
    and milestone role
  generated: 2026-06-24
  status: accepted
  stars: 4
  task_id: T-053
  identity: T-053/D-003
  core: false
  lineage_anchor: false
- id: D-004
  name: known_gap_report
  type: document
  path: 4_artifact/5_table/known_gaps_v20260624_061117.md
  role: primary
  description: List of 7 low-severity known gaps identified from predecessor reports
  generated: 2026-06-24
  status: accepted
  stars: 4
  task_id: T-053
  identity: T-053/D-004
  core: false
  lineage_anchor: false
- id: D-005
  name: demo_commands_reference
  type: document
  path: 4_artifact/2_persist/demo_commands_v20260624_061117.md
  role: primary
  description: Working CLI commands for forward query, reverse query, and info subcommand
    with Python API examples
  generated: 2026-06-24
  status: accepted
  stars: 4
  task_id: T-053
  identity: T-053/D-005
  core: false
  lineage_anchor: false
- id: D-006
  name: completion_report
  type: document
  path: 5_report/completion.md
  role: process
  description: Completion report indicating all deliverables produced and accepted
  generated: 2026-06-24
  status: accepted
  stars: 2
  task_id: T-053
  identity: T-053/D-006
  core: false
  lineage_anchor: false

```

### Completion Report
```md
# Completion — T-053 m1_python_package_milestone

**Status:** Completed  
**Generated:** 2026-06-24  

## Summary

All 6 deliverables produced and registered. All three evidence streams (T-050 forward validation, T-051 reverse validation, T-052 package assembly) collected with PASS verdicts. No predecessor artifacts modified.

## Deliverables Produced

| ID | Name | Path | Status |
|----|------|------|--------|
| D-001 | milestone_report | `4_artifact/3_document/milestone_report_v20260624_061117.md` | accepted |
| D-002 | evidence_index | `4_artifact/2_persist/evidence_index_v20260624_061117.json` | accepted |
| D-003 | layered_asset_map | `4_artifact/5_table/layered_asset_map_v20260624_061117.csv` | accepted |
| D-004 | known_gap_report | `4_artifact/5_table/known_gaps_v20260624_061117.md` | accepted |
| D-005 | demo_commands_reference | `4_artifact/2_persist/demo_commands_v20260624_061117.md` | accepted |
| D-006 | completion_report | `5_report/completion.md` | accepted |

## Key Results

- **Package:** `pxfquery` v0.1.0 at `1_asset/assembled_package_source/`
- **Forward validation:** 11/11 PASS (T-050)
- **Reverse validation:** 42/42 PASS (T-051)
- **Package assembly:** 9/9 acceptance criteria PASS (T-052)
- **Known gaps:** 7 low-severity gaps documented
- **Status:** No blocked conditions. All gates green.

## Constraints Compliance

- No predecessor task artifacts modified ✓
- No validation or assembly commands re-run ✓
- No project-level raw assets read ✓
- All information from predecessor handoffs only ✓

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-053 m1_python_package_milestone

## Task Goal
Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable. Produce final package path/version, demo commands, evidence index, layered asset map, and known gap report.

## What Was Delivered
All 6 protocol-required deliverables produced and registered. Three evidence gates confirmed PASS: forward validation (11/11), reverse validation (42/42), package assembly (9/9 acceptance criteria). 7 low-severity known gaps documented.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/3_document/milestone_report_v20260624_061117.md` | Single entry point summarizing all M1 evidence | Read first for M1 overview |
| D-002 | `4_artifact/2_persist/evidence_index_v20260624_061117.json` | Machine-readable index of all evidence streams | Parse programmatically to verify gate status |
| D-003 | `4_artifact/5_table/layered_asset_map_v20260624_061117.csv` | Provenance trace for every asset across 6 layers | Use to understand which task produced what |
| D-004 | `4_artifact/5_table/known_gaps_v20260624_061117.md` | 7 low-severity gaps from predecessor reports | Read before planning M2; decide which to fix |
| D-005 | `4_artifact/2_persist/demo_commands_v20260624_061117.md` | Working CLI and Python API examples | Use for quick-start or smoke tests |

## Supporting Artifacts
- `4_artifact/registry.yaml` — Registry with star ratings for all deliverables
- `5_report/completion.md` — Process completion record

## Downstream Use
- M2 or later milestone tasks: read D-001 for M1 completion summary, D-002 for structured evidence, D-004 for gaps to address.
- Any task needing package provenance: read D-003 for layer-to-task mapping.
- Any task needing to run queries: read D-005 for CLI commands.

## Known Limits / Risks
- All validation uses synthetic fixtures, not real LINCS data.
- No wheel/distribution build tested; editable install only.
- Demo scope minimal (1-2 test cases per direction).
- See D-004 for all 7 gaps.

## Do Not Read / Do Not Reuse
- `3_execution/` (empty)
- Predecessor task directories (T-050, T-051, T-052) — already consumed via assets

## Recommended Next Reads
1. `4_artifact/3_document/milestone_report_v20260624_061117.md` — full M1 summary
2. `4_artifact/5_table/known_gaps_v20260624_061117.md` — gaps to consider for M2
3. `4_artifact/2_persist/demo_commands_v20260624_061117.md` — quick-start guide

```

## Required Writes

Overwrite or create both files:

1. `4_artifact/3_document/execution_report_v20260626.html`
2. `4_artifact/3_document/result_report_v20260626.html`

Then update `5_report/delivery_qa.md` briefly with `Verdict: yellow_repair`, saying the repair was human-readable report rewriting only. Do not modify core deliverables, registry paths, code, data, or analysis results.

## Writing Standard

Write in Chinese. Use natural-language paragraphs, not an audit checklist. Tables are allowed only for a short artifact guide; they must not be the main report.

Each HTML report must have at least 900 Chinese characters of visible explanation. Each major section should contain a paragraph of 3-6 sentences. Every paragraph should include task-specific nouns, artifact names, findings, counts, decisions, or boundaries from this task.

Do not copy old HTML with only date/path changes. Do not write generic phrases like "completed successfully" unless you explain exactly what was completed.

## execution_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 任务意图
2. 输入资产与依据
3. 实际执行过程
4. 关键判断与证据
5. 交付物清单
6. 边界与未完成事项

The execution report should explain the work process: why the task was needed, what evidence was used, what the original execution did, what concrete findings or counts were produced, where the artifacts are, and what was intentionally not done.

## result_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 一句话结论
2. 项目背景
3. 核心结果
4. 项目价值
5. 交付物导读
6. 后续使用方式
7. 边界与风险

The result report should read like a concise project briefing. It should help a human quickly understand the value of this task without reading registry.yaml, completion.md, or source assets.

## Final Response

Return a short Chinese summary:

```md
### 交付报告重写完成
- 写入:
- 修复重点:
- 仍需注意:
```
