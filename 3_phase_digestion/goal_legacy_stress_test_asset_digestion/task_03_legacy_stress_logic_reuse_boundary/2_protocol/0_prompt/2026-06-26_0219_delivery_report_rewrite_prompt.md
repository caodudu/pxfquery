# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:19

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-057 03_legacy_stress_logic_reuse_boundary
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary`
- Objective:

```text
Judge the reuse boundary for legacy stress-test-related logic, scripts, reports, and query-validation ideas: which are suitable as references, which require rewrite, which are historical-only, and which are insufficiently supported.

Deliverables: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md and 4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv.

Reference T-001 for authority rules over messy legacy evidence. Reference T-002 for migrated asset entry points and migration status. Reference T-007 for code/index/report maturity. Use T-041 only as a may input if done; otherwise omit it.

Important constraints: do not modify code, do not repair old scripts, do not run production-scale tests; produce reuse decisions with reasons: direct reference, rewrite needed, historical evidence only, not usable, or unknown.
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
# T-057 03_legacy_stress_logic_reuse_boundary — Protocol

## Objective

Judge the reuse boundary for each legacy stress-test-related logic, script, report, and query-validation idea found in the migrated flat asset library. For each candidate, assign one of: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, or `unknown`. Produce a reusable decision document and a decision matrix CSV.

## Position In Project

This is task 3 of 4 in goal G-026 (legacy_stress_test_asset_digestion). It follows T-055 (source map — pending) and T-056 (scenario inventory — pending). Since predecessors are not yet delivered, this task works directly from T-001/T-002/T-007 digested outputs and the project-level flat asset library. Its output feeds T-058 (development handoff pack).

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Code/index/report maturity overview |
| A-002 | T-007 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Per-component maturity for reuse classification |
| A-003 | T-007 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Validation evidence status — primary reference for validation-report reuse |
| A-004 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Risk flags for each asset category |
| A-005 | T-001 | 4_artifact/2_persist/old_asset_structure_report.md | Authority rules for distinguishing operational vs archive material |
| A-006 | T-002 | 4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Flat library navigation guide |
| A-007 | T-002 | 4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Prevents evaluating unmigrated assets |
| A-008 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders/ | Legacy test/verify scripts for reuse classification |
| A-009 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/ | 57 validation reports forming the stress-test evidence corpus |
| A-010 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py | Core resolver logic that stress tests exercise |
| A-011 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json | JSON validation traces for reproducibility assessment |
| A-012 | T-007 | 4_artifact/2_persist/pxfquery_development_source_map_v20260617.md | Source authority map to avoid superseded/duplicate reports |

## Execution Steps

1. **Read authority and context.** Read A-005 (T-001 authority), A-006 (T-002 structure guide), A-007 (not-migrated report), A-001 (T-007 state report), A-012 (source map) to establish classification criteria and boundary rules.

2. **Read T-007 maturity indexes.** Read A-002 (module asset status matrix), A-003 (validation evidence index), A-004 (gap/risk list) to understand the validated status and risk level of each component that stress-test assets target.

3. **Read legacy validation reports systematically.** Scan A-009 (validation_reports/ directory). For each report, read its content and classify it. At minimum cover:
   - Latest reports index (M-0239)
   - Forward matrix tests (M-0291, M-0257)
   - Forward question suites (M-0266, M-0277, M-0275)
   - LLM stability check (M-0267)
   - Act-1 validation (M-0255)
   - Known risks (M-0243), execution order (M-0244), obsolete list (M-0245)
   - Resolver TODO (M-0290)

4. **Read legacy test scripts.** Read the scripts in A-008 (index_builders/ directory). At minimum:
   - M-0385 test_resolver_smoke.py (if exists)
   - M-0386 test_forward_matrix.py (deterministic mock)
   - M-0389 verify_resolver_cases.py (real LLM)

5. **Read resolver source and design context.** Read A-010 (resolver.py) and relevant design docs from A-008's design_docs/ to understand what the test/verify scripts exercise.

6. **Read validation traces.** Read A-011 (act1 validation JSON) to supplement report-based assessment.

7. **Build decision matrix.** For each evaluated candidate, record:
   - Asset name/path
   - Asset type (script / report / design doc / other)
   - Reuse decision: direct reference / rewrite needed / historical evidence only / not usable / unknown
   - Reasoning summary
   - Key risk or gap
   - Recommended next action

8. **Write deliverable 1: Persist document.** Write `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md` with full reuse-boundary analysis organized by asset category.

9. **Write deliverable 2: Decision matrix.** Write `4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv` with the tabular decision matrix.

10. **Register deliverables.** Update `4_artifact/registry.yaml` with both outputs.

## Constraints

- Do not modify code, repair o

...[truncated by CyHex prompt assembler: 3025 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: legacy_stress_logic_reuse_boundary_v20260624
  type: persist
  path: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md
  created: '2026-06-24'
  status: delivered
  notes: Full reuse-boundary analysis organized by asset category. Covers 65 classified assets.
- id: D-002
  name: stress_logic_reuse_decision_matrix_v20260624
  type: table
  path: 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv
  created: '2026-06-24'
  status: delivered
  notes: Machine-readable CSV with columns asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action. 65 rows covering all evaluated assets.
```

### Completion Report
```md
# Completion

Task: T-057 03_legacy_stress_logic_reuse_boundary
Completed: 2026-06-24
Verdict: **completed** — all protocol deliverables produced.

## Execution Summary

Read all 12 required predecessor assets (A-001 through A-012), systematically read the mandatory validation report set (M-0239, M-0291, M-0257, M-0266, M-0277, M-0275, M-0267, M-0255, M-0243, M-0244, M-0245, M-0290), read all 5 mandatory test scripts (M-0385 through M-0389), read resolver source code (A-010), and read validation traces (A-011). 

All 57 validation reports in the A-009 directory were inspected. All 19 files in the A-008 scripts directory were inspected. The remaining README, log, and GSEA err/out files were classified. No assets were classified from filename alone.

## Asset Counts

| Category | Count |
|---|---|
| **Total assets classified** | **65** |
| Direct reference | 10 |
| Rewrite needed | 11 |
| Historical evidence only | 38 |
| Not usable | 6 |
| Unknown | 0 |

### By asset type

| Type | Count |
|---|---|
| Validation reports | 47 |
| Test/verify scripts | 15 |
| Source code | 1 |
| Design docs | 1 |
| Validation traces (JSON) | 1 |

## Key Findings

1. **Deterministic resolver core is the strongest reuse candidate**: 7/7 mock tests pass, hybrid_fast achieves 0.825s for 3 queries.
2. **LLM parsing is unstable**: 6/9 stability rate, 167.3s latency in always_llm mode. Cannot be primary manuscript claim.
3. **All scripts need rewrite** due to old workspace paths — none are runnable as-is.
4. **function_index.json is the critical missing runtime asset** — builder exists but runtime JSON was not migrated.
5. **Validation evidence hierarchy is clear** — M-0239 + T-007 source map resolve all report priority conflicts.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Reuse boundary analysis | `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` | Delivered |
| Decision matrix CSV | `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` | Delivered |
| Artifact registry | `4_artifact/registry.yaml` | Registered D-001, D-002 |

## Stop Conditions Checked

- All required predecessor assets (A-001–A-007, A-012) were resolved: **PASS**
- A-009 (validation_reports/) was accessible and contained 57 files: **PASS**
- No asset was classified with `unknown` due to unclear content: **PASS**
- Superseded/duplicate reports are noted with priority references: **PASS**
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
