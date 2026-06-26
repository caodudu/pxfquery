# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:10

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-055 01_legacy_stress_test_source_map
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map`
- Objective:

```text
Create a source map for migrated legacy materials that may relate to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports.

Deliverables: 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md and 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv.

Reference T-001 because it defines legacy background, old structure interpretation, and source authority rules. Reference T-002 because it defines the migrated flat asset library and prevents direct legacy-root wandering. Reference T-007 because it summarizes current development asset/code/index/report maturity.

Important constraints: do not scan the unregistered legacy root; do not claim any old script is runnable; create candidate source mapping only; record missing or ambiguous leads honestly.
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
# T-055 01_legacy_stress_test_source_map — Protocol

## Objective

Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. The source map must be a structured guide that later tasks can use to locate, assess, and reuse these materials without directly scanning the unregistered legacy root.

## Position In Project

This is a digestion-phase task under G-005 (legacy stress test asset digestion). It follows T-001 (legacy semantic digestion), T-002 (flat asset migration), and T-007 (development state digestion). This task does not execute, run, or validate any old script. It produces a candidate map only, enabling later assessment tasks to proceed without legacy-root access.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|----------|-------------|------|------------|
| A-001 | T-002 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for all migrated legacy materials that may contain stress-test/validation content |
| A-002 | T-002/D-002 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json | Full migration manifest to trace which stress-test files were migrated, their source paths, and any not-migrated items |
| A-003 | T-001/D-003 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md | Understanding legacy source structure and identification of operational vs archive layers |
| A-004 | T-001/D-004 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md | Project background context for understanding why certain stress-test assets were created |
| A-005 | T-007/D-002 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development state summary to understand which validation gaps are already documented |
| A-006 | T-007/D-004 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence index to avoid redundant cataloging and identify gaps |
| A-007 | T-007/D-005 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps and risks to cross-reference against discovered stress-test materials |
| A-008 | T-002/D-005 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Chinese structure explanation for the flat library navigation |
| A-009 | T-002/D-007 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Record of intentionally not-migrated assets; may contain stress-test content that was explicitly excluded |

## Execution Steps

1. Read A-001 (flat asset library) structure to understand available directories.
2. Read A-005, A-006, A-007 (T-007 handoff) to understand already-documented validation landscape.
3. Read A-002 (migration manifest) and A-009 (not-migrated report) to identify stress-test-related entries.
4. Browse the following high-priority directories within A-001 for stress-test/validation content:
   - `reports/validation_reports/` — resolver validation, suite runs, stability checks, known risks
   - `code/index_builders/` — test scripts (test_resolver_smoke, test_forward_matrix, verify_resolver_cases, run_forward_question_suite, validate_act1, check_llm_stability)
   - `code/pxfquery_package/query/` — resolver pipeline source with forward search policy (L1-L4 logic)
   - `data/query_indexes/` — index files used by the resolver for query resolution
   - `reports/digested_context/` — any context reports mentioning validation outcomes
   - `code/analysis_scripts/` — GSEA evaluation scripts (cp_gsea_eval, sh_gsea_eval, xpr_gsea_eval) and analysis notebooks
   - `results/gsea_tables/` — GSEA result tables used as validation baselines
5. For each candidate asset found, record:
   - Migrated path within flat library (or explicit not-migrated status)
   - Original legacy source path (from manifest or A-003/A-008 context)
   - Asset type: script, report, data, index, result, design_doc
   - Stress-test relevance category: complex_query, resolver_edge_case, validation_script, validation_report, stability_check, GSEA_evaluation, performance, edge_case_input, known_risk
   - Brief assessment of what it tests or validates
   - Caveat if the asset is not directly runnable or has ambiguous provenance
6. Produce `4_art

...[truncated by CyHex prompt assembler: 3436 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: legacy_stress_test_source_map
  type: document
  path: 4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md
  status: accepted
  description: Categorized inventory of migrated legacy stress-test assets covering
    7 target directories in the flat asset library. Includes cross-reference to T-007
    validation evidence index, missing/ambiguous leads documentation, and guidance
    for later tasks.
  generated: '2026-06-24'
  identity: T-055/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-002
  name: stress_test_candidate_asset_index
  type: table
  path: 4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv
  status: accepted
  description: 'Machine-readable CSV index of stress-test candidate assets. Columns:
    category, migrated_path, original_path, asset_type, relevance, runnable_claim,
    T-007_cross_ref, notes.'
  generated: '2026-06-24'
  identity: T-055/D-002
  role: data
  core: false
  lineage_anchor: false
  stars: 2

```

### Completion Report
```md
# Completion Report — T-055 01_legacy_stress_test_source_map

Generated: 2026-06-24

## Status
Completed.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Legacy stress test source map | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Accepted |
| Stress test candidate asset index | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Accepted |

## Coverage Summary

All 7 target directories were browsed and cataloged:
- `reports/validation_reports/` — 57 items (15 overlapped with T-007, ~42 newly cataloged)
- `code/index_builders/` — 19 items (6 validation scripts, 6 index builders, 6 demos, 1 install doc)
- `code/pxfquery_package/query/` — 5 items (resolver.py 1072 lines, forward.py, reverse.py, init, pycache)
- `data/query_indexes/` — 9 index files (function_index.json confirmed missing)
- `reports/digested_context/` — 9 items (minimal validation relevance)
- `code/analysis_scripts/` — 55 items (GSEA eval scripts, notebooks, duplicates)
- `results/gsea_tables/` — 6 large symlink items (244-372MB each)

Total candidate assets cataloged: ~160 entries in the CSV index.

## Key Findings

1. **Strongest validation baseline**: M-0386 (test_forward_matrix.py) with deterministic 7/7 pass rate.
2. **Critical gap**: `function_index.json` missing from migrated query indexes. Must be rebuilt via M-0373.
3. **LLM stability risk**: 6/9 success rate documented; conservative claims advised.
4. **Performance data**: always_LLM is ~200x slower than hybrid_fast (167.3s vs 0.825s for comparable queries).
5. **Script path assumptions**: All scripts use legacy workspace paths; none are directly runnable in current environment.
6. **Duplicate scripts**: M-013x and M-034x/035x series appear to be duplicates from different legacy versions.
7. **Systematic migration gap**: No GSEA table symlinks >10% of referenced files were unresolvable, but the function_index.json gap is significant.

## Notes

- `runnable_claim: false` set for all entries per protocol constraint.
- T-007 cross-reference documented in source map section 3.
- Missing/ambiguous leads documented in source map section 4.
- Guidance for later tasks provided in source map section 5.
- No legacy-root paths appear in deliverables.
- No modifications made to flat asset library or predecessor artifacts.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-055 01_legacy_stress_test_source_map

## Task Goal
Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. This is a candidate catalog only -- no execution, no validation.

## What Was Delivered
- `legacy_stress_test_source_map_v20260624.md`: Categorized inventory of ~160 candidate stress-test assets across 7 target directories in the flat asset library. Includes cross-reference to T-007 validation evidence index, missing/ambiguous leads, and guidance for later tasks.
- `stress_test_candidate_asset_index_v20260624.csv`: Machine-readable index with one row per candidate asset (8 columns).

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Primary catalog of all stress-test candidates with relevance categories and T-007 cross-ref | Read first to identify which assets to use for validation suite design |
| D-002 | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Queryable machine-readable index for filtering by category, type, or cross-ref | Load as DataFrame for filtering/analysis |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html` — execution process summary
- `4_artifact/3_document/result_report_v20260624.html` — result summary for human review

## Downstream Use
1. **Validation suite design**: Use section 2.1 (validation scripts) and section 5 guidance to build a current-environment validation suite.
2. **Gap remediation**: Rebuild `function_index.json` via M-0373_build_function_index.py.
3. **Baseline comparison**: Use M-0386 (test_forward_matrix.py) as primary regression test.
4. **Performance characterization**: Reference M-0277 (timing) and M-0275 (hybrid_fast v3) for expectations.
5. **LLM risk assessment**: Reference M-0377 and M-0267 (6/9 success rate) for conservative claims.

## Known Limits / Risks
- All scripts marked `runnable_claim: false` — none are directly runnable in current environment.
- `function_index.json` is missing from migrated query indexes (must be rebuilt).
- GSEA eval scripts have HPC-specific dependencies (SLURM, scanpy, gseapy).
- GSEA tables in results/gsea_tables/ are symlink placeholders (244-372MB each).
- Duplicate script pairs exist (M-013x vs M-034x/035x series).
- Suite run variants require deduplication.

## Do Not Read / Do Not Reuse
- Legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`) — not registered for task access.
- Predecessor task folders (T-001, T-002, T-007) — outputs are already consumed via asset registry.
- `1_project_init/` — not needed for stress-test source map consumption.
- Flat asset library (`2_project_asset/`) — read-only; do not modify.

## Recommended Next Reads
1. `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` — full catalog
2. `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` — machine index
3. `5_report/completion.md` — execution summary

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
