# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:32

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-058 04_stress_test_development_handoff_pack
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack`
- Objective:

```text
Integrate the completed digestion outputs from tasks 01-03 into a development-phase handoff pack for a future PxFquery stress-test milestone.

Deliverables: 4_artifact/2_persist/stress_test_development_handoff_pack_vYYYYMMDD.md and 4_artifact/2_persist/recommended_stress_test_milestone_tasks_vYYYYMMDD.md.

Must use tasks 01, 02, and 03 because this task is an integration/handoff layer and should not redo source mapping, scenario inventory, or reuse-boundary judgment. Reference T-007 to keep the handoff aligned with current development asset understanding.

Important constraints: do not implement or run stress tests; do not compensate for missing upstream quality by inventing results; recommend future development tasks only, and keep the result as digestion-stage asset handoff.
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
# T-058 04_stress_test_development_handoff_pack — Protocol

## Objective

Integrate the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a single development-phase handoff pack. The pack serves as a structured bridge from the stress-test digestion goal to a future stress-test milestone in the development phase.

Produce two deliverables:
1. A narrative handoff pack consolidating what is known, reusable, risky, and missing across all three predecessor outputs.
2. A set of recommended future development tasks (not execution steps) that a stress-test milestone should include.

Reference T-007 to keep the handoff aligned with current development asset understanding (code maturity, index status, known gaps).

## Position In Project

This is the final integration task of `goal_legacy_stress_test_asset_digestion`. It is a pure digestion-stage handoff task:
- Does not implement or run stress tests.
- Does not compensate for missing upstream quality by inventing results.
- Recommends future development tasks only.

The output is a digestion-stage handoff pack, not a development-phase execution plan.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-055 | 4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md | Primary catalog of ~160 stress-test candidate assets; used to understand what legacy material exists and where |
| A-002 | T-055 | 4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv | Machine-readable index for filtering candidates by category, type, or relevance |
| A-003 | T-056 | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale |
| A-004 | T-056 | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | Tabular scenario table; parseable for downstream test framework use |
| A-005 | T-057 | 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md | Reuse-boundary analysis covering 65 classified legacy assets with decisions |
| A-006 | T-057 | 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv | Machine-readable decision matrix with reuse_decision, reasoning, risk_gap, recommended_action per asset |
| A-007 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development-state understanding: code, data, index, and report maturity |
| A-008 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | High-priority gaps, risks, and claims-to-avoid for development phase |
| A-009 | T-007 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Recommended next development tasks and carry-forward guidance from T-007 |

## Execution Steps

1. **Read all registered inputs** (A-001 through A-009) to build a complete picture of the stress-test digestion landscape.
2. **Synthesize the three dimensions:**
   - From T-055: what legacy stress-test assets exist, their categories, and known gaps.
   - From T-056: what stress-test scenarios should be exercised, grouped by query dimension.
   - From T-057: which legacy assets are directly referable, which need rewrite, which are historical-only, and which are not usable.
3. **Cross-reference with T-007** to align the handoff with the current development state — ensuring recommendations are grounded in what the codebase actually supports today.
4. **Write the handoff pack** (`stress_test_development_handoff_pack_v20260624.md`):
   - Section 1: Summary of consolidated digestion findings (what the three predecessors collectively established).
   - Section 2: Asset-to-scenario cross-walk (which source assets map to which test scenarios).
   - Section 3: Reuse-ready assets (from T-057 decisions marked "direct reference").
   - Section 4: Rewrite-required assets and their risk profile.
   - Section 5: Known gaps and missing assets (from T-055 missing leads + T-057 "not usable" + T-007 gap list).
   - Section 6: Alignment with current development state (via T-007 cross-ref).
   - Section 7: Handoff integrity check (are predecessor outputs internally consistent? Any unresolved contradictions?).
5. **Write recommended milestone tasks** (`recommended_stress_test_milestone_tasks_v20260624.md`):
   - Define a logical task sequence for a future stress-test milestone.
   - Each recommended task should have: name, objective, estimated scope, predecessor dependency, and rationale anchored in T-055/056/057/007 evidence.
   - Do not prescribe implementation details — recommend what should be done, not how.
6. **Register both deliverables** in `4_artifact/registry.yaml`.
7. **Write `5_report/completion.md`**.

## Constraints

- Do not implement or run stress tests.
- Do not compensate for missing upstream quality by inventing results.
- Recommend future development tasks only; keep the result as digestion-stage asset handoff.
- Do not modify predecessor task o

...[truncated by CyHex prompt assembler: 2138 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: stress_test_development_handoff_pack
  type: document
  path: 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md
  version: v20260624
  created: '2026-06-24'
  status: delivered
  notes: 7-section narrative handoff pack consolidating T-055, T-056, T-057, and T-007
    findings into a single bridge from stress-test digestion to a future stress-test
    milestone.
  identity: T-058/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-002
  name: recommended_stress_test_milestone_tasks
  type: document
  path: 4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md
  version: v20260624
  created: '2026-06-24'
  status: delivered
  notes: 7 recommended future development tasks (ST-M01 through ST-M07) forming a
    logical stress-test milestone sequence. Each task has name, objective, estimated
    scope, predecessor dependency, and rationale anchored in T-055/056/057/007 evidence.
  identity: T-058/D-002
  role: support
  core: false
  lineage_anchor: false
  stars: 4

```

### Completion Report
```md
# Completion

Task: T-058 04_stress_test_development_handoff_pack
Completed: 2026-06-24

## Deliverables Produced

| ID | Deliverable | Path | Status |
|---|---|---|---|
| D-001 | Stress Test Development Handoff Pack | `4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md` | delivered |
| D-002 | Recommended Stress Test Milestone Tasks | `4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md` | delivered |

## Execution Summary

All 9 registered input assets (A-001 through A-009) were read and synthesized. The three predecessor dimensions (T-055 source map, T-056 scenario inventory, T-057 reuse boundary) were cross-referenced with T-007 development state to produce a coherent handoff pack with 7 sections:

1. **Summary of consolidated digestion findings**: Synthesized ~160 cataloged assets, 29 stress-test scenarios, and 65 classified legacy assets into a unified evidence hierarchy.
2. **Asset-to-scenario cross-walk**: Mapped all 29 scenarios to their primary source assets with T-057 reuse decisions and T-007 cross-references.
3. **Reuse-ready assets**: Listed 10 direct-reference assets (8 reports + resolver.py + design docs) ready for immediate handoff.
4. **Rewrite-required assets and risk profile**: Cataloged 11 scripts needing rewrite with risk assessment, and ranked M-0373 (function index builder) as highest rewrite priority.
5. **Known gaps and missing assets**: Consolidated 19 gaps from T-055 (8), T-057 (1 not-usable group), and T-007 (11), ranked by priority.
6. **Alignment with current development state**: Mapped the handoff to T-007's 5-step development interpretation and safer claims.
7. **Handoff integrity check**: Verified cross-consistency of predecessor outputs; documented 4 honest ambiguities (Act-1 authority conflict, suite variant proliferation, GSEA symlinks, mode coexistence).

The recommended milestone tasks define 7 sequential tasks (ST-M01 through ST-M07) with objectives, scope estimates, dependencies, and rationale anchored in predecessor evidence.

## Integrity Check Pass

- All 29 T-056 scenarios are traceable to T-055 cataloged assets
- All T-057 reuse decisions are consistent with T-055 content descriptions
- T-007 cross-references are explicit in both Section 2 cross-walk and Section 6 alignment
- No new scenarios, assets, or test cases were invented
- Gaps and ambiguities from predecessors are carried forward honestly
- The deterministic 7/7 matrix test (M-0291) is independently identified as the strongest evidence by all three predecessors
- The `function_index.json` gap is independently confirmed by all three predecessors
- Both deliverables are registered in `4_artifact/registry.yaml`

## Constraint Compliance

- [x] Did not implement or run stress tests
- [x] Did not compensate for missing upstream quality by inventing results
- [x] Recommended future development tasks only; handoff is digestion-stage
- [x] Did not modify predecessor task outputs
- [x] Did not read raw legacy assets or scan unregistered directories
- [x] Did not read `2_protocol/0_prompt/` files
- [x] No web search performed (disallowed by protocol)
- [x] Both deliverables registered in `4_artifact/registry.yaml`
- [x] `5_report/completion.md` written
```

### Existing AI Handoff, If Any
```md
# Handoff for Future AI Tasks

Task: T-058 04_stress_test_development_handoff_pack
Generated: 2026-06-24

## What This Task Produced

This is the final integration task of `goal_legacy_stress_test_asset_digestion`. It synthesizes predecessor outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a development-phase handoff pack. The outputs are digestion-stage handoff artifacts — no stress tests were implemented or run.

### Deliverables

| ID | Name | Path | How to use |
|---|---|---|---|
| D-001 | Stress Test Development Handoff Pack | `4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md` | Entry point for understanding what legacy stress-test assets exist, what scenarios to test, what is reusable, and what needs rewrite |
| D-002 | Recommended Stress Test Milestone Tasks | `4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md` | 7-task sequence (ST-M01 through ST-M07) for a future stress-test milestone in the development phase |

### Handoff Pack Section Guide

| Section | Content | When to read |
|---|---|---|
| §1 Summary | Consolidated findings from all 3 predecessors | Always — provides the big picture |
| §2 Cross-Walk | Maps each asset to specific test scenarios | When selecting which script/report to use for a specific scenario |
| §3 Reuse-Ready | 10 direct-reference assets (no modification needed) | When you need validation evidence, report routing, or resolver reference |
| §4 Rewrite-Needed | 11 scripts requiring path updates; risk profile per asset | When planning porting work |
| §5 Known Gaps | 19 consolidated gaps ranked by priority | When scoping next tasks; function_index.json is #1 |
| §6 Development Alignment | Cross-reference with T-007 state | When aligning stress-test work with overall project state |
| §7 Integrity Check | Predecessor consistency review | When you need to understand known ambiguities |

## Key Facts for Downstream Tasks

1. **function_index.json is missing** — the single highest-priority gap. Must be rebuilt via M-0373 before reverse query validation.
2. **Deterministic 7/7 matrix (M-0291/M-0386) is the strongest evidence** — use it as the primary regression baseline.
3. **hybrid_fast (0.825s) is the defensible default mode** — not always_llm (167.3s, 6/9 stability).
4. **29 scenarios defined, 12 PASS, 6 expected FAIL** — the scenario inventory provides a ready-to-execute test plan.
5. **10 assets are direct-reference** — no modification needed; usable as-is for evidence reading.
6. **11 scripts need rewrite but have sound core logic** — old workspace paths are the only barrier.
7. **All predecessor outputs are internally consistent** — no contradiction blocks coherent synthesis.
8. **T-007 D001 (establish package workspace) is the entry prerequisite** for all ST-Mxx tasks.

## How to Read the Predecessor Asset Links

All 9 input assets (A-001 through A-009) are symlinked in `1_asset/`. The handoff pack's cross-walk (Section 2) maps each asset to specific T-056 scenarios. When a future task needs to trace evidence back to a predecessor, follow the symlink to the source task's artifact.

## What NOT to Do

- Do not treat this task's outputs as execution plans — they are digestion-stage recommendations only.
- Do not redo source mapping (use T-055), scenario inventory (use T-056), or reuse-boundary analysis (use T-057).
- Do not invent new stress-test scenarios beyond the 29 T-056 defines.
- Do not run stress tests from

...[truncated by CyHex prompt assembler: 83 chars omitted]
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

Mandatory final self-check before your final response: inspect the visible text of both HTML files you wrote. If either file contains "报告重写", "重写版本", "为了通过 validator", "validator", "health warning", or "低信息量报告修复", rewrite the visible title/body immediately and check again. Do not finish while any forbidden internal repair phrase remains visible in the HTML reports.

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
