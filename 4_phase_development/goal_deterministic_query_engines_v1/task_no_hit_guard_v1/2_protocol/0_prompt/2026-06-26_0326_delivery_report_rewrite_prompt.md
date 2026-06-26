# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:26

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-031 no_hit_guard_v1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1`
- Objective:

```text
Create pxfquery-{task_id} no-hit safety guard to prevent fuzzy false-positive perturbation matches. Deliver patch, tests, and NOT_FOUND evidence.
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
# Protocol: no_hit_guard_v1

## Objective
Create a `pxfquery-T-031` no-hit safety guard in `ForwardQuery` so that unsupported perturbations return explicit NOT_FOUND behavior instead of false-positive fuzzy matches. Deliver the guard patch, a negative no-hit test, a positive-control forward query re-run, and NOT_FOUND evidence.

## Inputs
- **A-001**: Current project protocol — pxfquery conda environment and workspace boundary rules.
- **A-002**: T-029 sibling deliverable bundle — `3_execution/forward_engine.py`, result tables, and not-found JSON evidence. Used as the positive-control baseline plus the existing engine script template for the patch.
- **A-003**: T-024 pxfquery workspace package — `ForwardQuery`, `ForwardResult`, `DataLoader` and full package tree. Target of the guard patch; read-only upstream artifact that serves as the source for the local corrected copy.
- **A-004**: T-026 matrix loader package — `load_matrix()`, `load_bundle()`, `load_index()`, `load_metadata()` from `4_artifact/2_persist/loader/`. Required to open the A-005 bundle for guard validation tests.
- **A-005**: T-021 standard_resources bundle (D-004) — `xpr_func_ad.h5ad` float32 functional matrix with `cmap_name`/`pert_id`/`cell_iname` obs columns. Primary data source for positive-control and no-hit tests.
- **A-006**: T-013 MVP capability contract (D-001) — Defines CAP-05 as required MVP behavior: unsupported perturbations must return safely.
- **A-007**: T-013 failure/missing capability list (D-005) — Documents CAP-05 fail: "当前 fuzzy fallback 对无意义扰动名仍会给出相近 token，存在误报风险" and assigns next action to this guard.

## Steps
1. Read A-003 (T-024 workspace `ForwardQuery`) to locate the perturbation resolution path and fuzzy-match fallback logic. Identify where near-token false positives originate.
2. Read A-002 (T-029 forward engine script `3_execution/forward_engine.py`) as the baseline positive-control script template.
3. Read A-006 and A-007 (T-013 capability contract and failure list) to confirm the exact CAP-05 requirement: unsupported perturbations must return `found=False` with a clear not-found message rather than silently matching a near-token gene.
4. Reproduce the false-positive evidence: run a fuzzy fallback test with a nonsense perturbation (e.g. `NONSENSE_ZZZ999`) against the A-005 matrix via A-004 loader and the T-024 ForwardQuery, capturing the current erroneous near-token match.
5. Implement the no-hit guard in a local corrected copy at `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` (or a minimal patch script that wraps ForwardQuery with the guard, or a patched version of the ForwardQuery class). The guard must:
   - Accept a similarity threshold or an explicit allowlist mode for perturbation matching.
   - When no perturbation match meets the required threshold, return `ForwardResult.found=False` with a clear NOT_FOUND message and no activated/suppressed terms.
   - When a perturbation match meets the threshold, proceed with the normal forward query path.
   - Not alter the behavior of the legacy `ForwardQuery` class in-place; the patched version must be locally versioned as `pxfquery-T-031`.
6. Write a negative no-hit test script at `3_execution/test_no_hit_guard.py` that:
   - Imports the T-031 patched forward query guard and the T-026 loader.
   - Runs `NONSENSE_ZZZ999/A549` through the guard and asserts `found=False`.
   - Runs at least two additional nonsense perturbation names through the guard and asserts `found=False` for each.
   - Writes evidence to `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json`.
7. Write a positive-control re-run at `3_execution/test_positive_control.py` that:
   - Imports the T-031 patched guard and the T-026 loader.
   - Runs `EGFR/A549/xpr` through the guard and asserts `found=True` with at least one activated term.
   - Writes evidence to `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json`.
8. Produce CyHex-mandatory reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese HTML step-by-step execution report.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese HTML result report.
9. Write `4_artifact/registry.yaml` registering all T-031 deliverables.
10. Write `5_report/completion.md` summarizing guard implementation and test outcomes.

### Required Bug-Repair Handling
- If the guard finds that ForwardQuery's fuzzy-match code is structurally blocking any patch approach, repair the blocking code within this task scope by producing a corrected local copy (`pxfquery_T031_<component>_repaired.py`).
- Record what was fixed, the source asset id (A-003), changed files, validation evidence, and which downstream task should consume the repaired version in `5_report/repair_log.md`.
- The guard itself is a scoped local correction; do not modify T-024 workspace files in place.

## Constraints

### Scoped Repair And Versioning
- Every task in this DAG has authority to fix bugs inside its own scope when required to make its 

...[truncated by CyHex prompt assembler: 2914 chars omitted]
```

### Artifact Registry
```yaml
task_id: T-031
task_name: no_hit_guard_v1
guard_version: pxfquery-T-031
artifacts:
- id: T031-D-001
  path: 4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py
  role: no_hit_guard_module
  description: T-031 no-hit guard module. Subclasses ForwardQuery with tunable quality
    thresholds (min_query_length_for_substring=4, min_overlap_for_token_fallback=2)
    to prevent fuzzy-match false positives. Usable as a drop-in wrapper by downstream
    tasks.
  lineage:
    source_asset: A-003 (T-024 pxfquery workspace package)
    version: pxfquery-T-031
    upstream_modified: false
  identity: T-031/T031-D-001
  core: false
  lineage_anchor: false
  stars: 2
- id: T031-D-002
  path: 3_execution/test_no_hit_guard.py
  role: no_hit_test_script
  description: Runs 11 nonsense perturbations through the guard, asserts found=False
    for each, writes evidence JSON.
  identity: T-031/T031-D-002
  core: false
  lineage_anchor: false
  stars: 2
- id: T031-D-003
  path: 3_execution/test_positive_control.py
  role: positive_control_test_script
  description: Runs EGFR/A549 and TP53/MCF7 through the guard, asserts found=True
    with activated and suppressed terms, writes evidence JSON.
  identity: T-031/T031-D-003
  core: false
  lineage_anchor: false
  stars: 2
- id: T031-D-004
  path: 4_artifact/5_table/pxfquery_T031_false_positive_reproduced.json
  role: cap05_false_positive_reproduction
  description: Reproduced 7/9 false positives using unguarded T-024 ForwardQuery to
    confirm CAP-05 failure before guard intervention.
  identity: T-031/T031-D-004
  core: false
  lineage_anchor: false
  stars: 1
- id: T031-D-005
  path: 4_artifact/5_table/pxfquery_T031_no_hit_evidence.json
  role: no_hit_evidence
  description: '11/11 no-hit test evidence: all nonsense names return found=False
    through the guard.'
  identity: T-031/T031-D-005
  core: false
  lineage_anchor: false
  stars: 1
- id: T031-D-006
  path: 4_artifact/5_table/pxfquery_T031_positive_control_evidence.json
  role: positive_control_evidence
  description: '2/2 positive-control evidence: EGFR/A549 and TP53/MCF7 return found=True
    with functional terms through the guard.'
  identity: T-031/T031-D-006
  core: false
  lineage_anchor: false
  stars: 1
- id: T031-D-007
  path: 4_artifact/3_document/execution_report_v20260623.html
  role: execution_report
  description: CyHex-mandatory Chinese HTML execution report (step-by-step).
  identity: T-031/T031-D-007
  core: false
  lineage_anchor: false
  stars: 5
- id: T031-D-008
  path: 4_artifact/3_document/result_report_v20260623.html
  role: result_report
  description: CyHex-mandatory Chinese HTML result report with guard results, evidence
    tables, and CAP-05 resolution summary.
  identity: T-031/T031-D-008
  core: false
  lineage_anchor: false
  stars: 5
- id: T031-D-009
  path: 4_artifact/registry.yaml
  role: artifact_registry
  description: This file.
  identity: T-031/T031-D-009
  core: false
  lineage_anchor: false
  stars: 1
- id: T031-D-010
  path: 5_report/completion.md
  role: completion_report
  description: Completion summary for T-031.
  identity: T-031/T031-D-010
  core: false
  lineage_anchor: false
  stars: 4
- id: T031-D-011
  path: 5_report/handoff_check_before_exec.md
  role: handoff_check_before_exec
  description: CyHex 1.2.19 check-to-execute handoff summary reconstructed from completed guard evidence.
  identity: T-031/T031-D-011
  core: false
  lineage_anchor: false
  stars: 4
- id: T031-D-012
  path: 5_report/cyhex_1_2_19_supplement.md
  role: cyhex_1_2_19_supplement
  description: Supplemental reliability and reuse note for future tasks that may consume the no-hit guard asset.
  identity: T-031/T031-D-012
  core: false
  lineage_anchor: false
  stars: 4

```

### Completion Report
```md
# T-031 Completion: no_hit_guard_v1

Generated: 2026-06-23

## Result Summary

T-031 produced `pxfquery-T-031`, a no-hit safety guard that prevents fuzzy false-positive perturbation matches in `ForwardQuery`.

### Guard Implementation
- File: `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py`
- Class: `NoHitGuardForwardQuery(ForwardQuery)` with two tunable thresholds:
  - `min_query_length_for_substring=4` — blocks short random tokens like `egr` (3 chars)
  - `min_overlap_for_token_fallback=2` — blocks single-token overlaps like `egfr_random`
- Does **not** modify T-024 workspace or any upstream artifact.
- Drop-in compatible: replaces `ForwardQuery(adata)` with `NoHitGuardForwardQuery(adata)`.

### CAP-05 Resolution
- Reproduced: 7/9 false positives with unguarded ForwardQuery (evidence: `pxfquery_T031_false_positive_reproduced.json`)
- Resolved: 11/11 nonsense names correctly blocked by guard (`pxfquery_T031_no_hit_evidence.json`)
- Positive-control preserved: EGFR/A549 (found=True, 20 act + 20 sup) and TP53/MCF7 (found=True, 20 act + 20 sup) (`pxfquery_T031_positive_control_evidence.json`)

### Output List
- `4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` — Guard module
- `3_execution/test_no_hit_guard.py` — Negative test (11/11)
- `3_execution/test_positive_control.py` — Positive-control test (2/2)
- `4_artifact/5_table/pxfquery_T031_false_positive_reproduced.json` — CAP-05 reproduction evidence
- `4_artifact/5_table/pxfquery_T031_no_hit_evidence.json` — No-hit evidence
- `4_artifact/5_table/pxfquery_T031_positive_control_evidence.json` — Positive-control evidence
- `4_artifact/3_document/execution_report_v20260623.html` — Execution report
- `4_artifact/3_document/result_report_v20260623.html` — Result report
- `4_artifact/registry.yaml` — Deliverable registry
- `5_report/completion.md` — This file

### Upstream Asset Integrity
No upstream artifact was modified. T-024 workspace, T-026 loader, T-021 bundle, T-029 engine, and T-013 reports remain unchanged.
No local repair was needed.

### Downstream Consumption
- Replacement: `from pxfquery_T031_forward_no_hit_guard import NoHitGuardForwardQuery`
- Tuning: `NoHitGuardForwardQuery(adata, min_overlap_for_token_fallback=3)` for stricter matching
- The guard targets only CAP-05 (perturbation fuzz false-positives); it does not address resolver, NL, or function_index issues.
```

### Existing AI Handoff, If Any
```md
(missing)
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
