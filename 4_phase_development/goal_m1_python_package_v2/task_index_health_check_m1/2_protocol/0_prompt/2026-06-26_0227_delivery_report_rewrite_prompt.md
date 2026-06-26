# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:27

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-045 index_health_check_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1`
- Objective:

```text
Check the health of M1-relevant indexes before any real loader hardening. Use T-021 standard-resource outputs to verify index schema, readability, required keys, missing fields, and known gaps for forward/reverse demos. Deliver an index health report and machine-readable check summary. This task must not rebuild or overwrite authoritative indexes; it may only report minimal patch recommendations.
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
# task_index_health_check_m1 — Protocol

## Objective

Check the health of M1-relevant query indexes from T-021 standard resources before real loader hardening (T-047). Verify index schema, readability, required keys, missing fields, and known gaps for forward/reverse demos. Deliver an index health report and machine-readable check summary. Must not rebuild or overwrite authoritative indexes; may only report minimal patch recommendations.

This is an audit/check asset, not a rebuild task. T-045 supports T-047 (resource_loader_hardening_m1) and must not block the fixture-only M1 path.

## Steps

### Step 1 — Load and inspect required core indexes
- Read `cellline_index.json`, `drug_index.json`, `gene_index.json`, `function_index.json` using Python
- Verify each is valid JSON and parseable
- Record file size, top-level type (array/object), and rough element count
- Output: per-index schema summary in `3_execution/step1_core_schema_summary.json`

### Step 2 — Validate M1-required keys for each core index
- cellline_index: check for valid cell line name list
- drug_index: check for drug alias → BRD-id mapping keys
- gene_index: check for gene symbol lookup keys and type annotation
- function_index: check for 91 function terms (50 Hallmark + 41 3CA MPS) and term-to-id mapping
- Report any structural anomalies (null keys, duplicate keys, malformed values)
- Output: `3_execution/step2_key_validation.json`

### Step 3 — Inspect optional neighbor/tree indexes for forward/reverse query fitness
- Read cellline_neighbors.json, cellline_tree.json, drug_neighbors.json, gene_neighbors.json, gene_neighbors_simple.json, gene_index_simple.json
- Verify neighbor graphs have expected edge cardinality (non-empty for major entities)
- Verify cellline_tree is a valid tree structure
- Report any missing or degenerate graphs that would break proxy-matching in forward/reverse queries
- Output: `3_execution/step3_neighbor_health.json`

### Step 4 — Cross-reference index coverage with M1 demo requirements
- Consult T-042 contract or T-042 demo cases for expected entity types (drug, gene, cell line, function term)
- Check whether the indexes cover the entity types needed for forward query (perturbation + context → function) and reverse query (function + context → perturbation)
- Identify index-to-demo gaps: entities present in demo case but missing from index
- Output: `3_execution/step4_coverage_gap.json`

### Step 5 — Generate machine-readable health summary
- Produce `4_artifact/2_persist/index_health_summary.json` with:
  - per-index schema status (valid/invalid/warning)
  - per-index key completeness score
  - per-index size in bytes and element count
  - known gaps list
  - patch recommendations (if any minimal fixes are safe)
- Output: `4_artifact/2_persist/index_health_summary.json`

### Step 6 — Generate human-readable health report
- Produce `4_artifact/2_persist/index_health_report.md` summarizing:
  - which indexes pass, which have warnings, which block M1 use
  - key findings for T-047 (loader hardening)
  - advice on whether fixture path alone is sufficient or real indexes are M1-ready
- Output: `4_artifact/2_persist/index_health_report.md`

### Step 7 — Write gap notes for human review
- Produce `4_artifact/3_document/gap_notes.md` with:
  - human-readable narrative of each gap
  - affected M1 demo case (forward/reverse)
  - severity (blocker / warning / cosmetic)
  - suggested resolution path (e.g. patch index, adjust demo, accept gap)
- Output: `4_artifact/3_document/gap_notes.md`

## Deliverables

| Path | Type | Description |
|------|------|-------------|
| `4_artifact/2_persist/index_health_summary.json` | deliverable | Machine-readable index health summary with per-index schema, key completeness, size, gaps, and patch recommendations |
| `4_artifact/2_persist/index_health_report.md` | deliverable | Human-readable health report with pass/warn/block per index and T-047 handoff advice |
| `4_artifact/3_document/gap_notes.md` | support | Human-readable gap narrative with severity, affected demo case, and resolution path |
```

### Artifact Registry
```yaml
artifacts:
- id: T-045/D-001/index_health_summary
  name: index_health_summary.json
  type: deliverable
  path: 4_artifact/2_persist/index_health_summary.json
  description: Machine-readable index health summary with per-index schema, key completeness,
    size, gaps, and patch recommendations
  created: '2026-06-24'
  stars: 5
  identity: T-045/T-045/D-001/index_health_summary
  role: support
  core: false
  lineage_anchor: false
- id: T-045/D-002/index_health_report
  name: index_health_report.md
  type: deliverable
  path: 4_artifact/2_persist/index_health_report.md
  description: Human-readable health report with pass/warn/block per index and T-047
    handoff advice
  created: '2026-06-24'
  stars: 4
  identity: T-045/T-045/D-002/index_health_report
  role: report
  core: false
  lineage_anchor: false
- id: T-045/D-003/gap_notes
  name: gap_notes.md
  type: support
  path: 4_artifact/3_document/gap_notes.md
  description: Human-readable gap narrative with severity, affected demo case, and
    resolution path
  created: '2026-06-24'
  stars: 3
  identity: T-045/T-045/D-003/gap_notes
  role: support
  core: false
  lineage_anchor: false
- id: T-045/D-004/execution_report
  name: execution_report_v20260624.html
  type: report
  path: 4_artifact/3_document/execution_report_v20260624.html
  description: Execution report documenting steps performed
  created: '2026-06-24'
  stars: 2
  identity: T-045/T-045/D-004/execution_report
  role: report
  core: false
  lineage_anchor: false
- id: T-045/D-005/result_report
  name: result_report_v20260624.html
  type: report
  path: 4_artifact/3_document/result_report_v20260624.html
  description: Result report with per-index health status and M1 readiness verdict
  created: '2026-06-24'
  stars: 3
  identity: T-045/T-045/D-005/result_report
  role: report
  core: false
  lineage_anchor: false

```

### Completion Report
```md
# Completion — T-045 index_health_check_m1

**Status:** completed  
**Completed:** 2026-06-24  
**Executor:** AGT-002 (CyHex execution agent)

## Completed Steps

1. ✅ **Step 1** — Loaded and inspected 4 core indexes (cellline, drug, gene, function) — all valid JSON
2. ✅ **Step 2** — Validated M1-required keys: cellline (240 names), drug (5,958 entries, 98%+ BRD), gene (78,061 entries, 3 fields), function (91 terms, non-standard structure), data_description (valid YAML)
3. ✅ **Step 3** — Inspected 6 optional neighbor/tree indexes — all valid; neighbor graphs have uniform 50-edge cardinality; cellline_tree is flat (not hierarchical)
4. ✅ **Step 4** — Cross-referenced with T-013 demo evidence (T-042 not yet executed). All expected demo entities (EGFR, A549, HALLMARK_APOPTOSIS, HALLMARK_MYC_TARGETS_V1) present in indexes. 6 structural gaps identified.
5. ✅ **Step 5** — Generated `index_health_summary.json`
6. ✅ **Step 6** — Generated `index_health_report.md`
7. ✅ **Step 7** — Generated `gap_notes.md`

## Deliverables Produced

| Deliverable | Path | Status |
|---|---|---|
| index_health_summary.json | `4_artifact/2_persist/index_health_summary.json` | ✓ |
| index_health_report.md | `4_artifact/2_persist/index_health_report.md` | ✓ |
| gap_notes.md | `4_artifact/3_document/gap_notes.md` | ✓ |
| execution_report_v20260624.html | `4_artifact/3_document/execution_report_v20260624.html` | ✓ |
| result_report_v20260624.html | `4_artifact/3_document/result_report_v20260624.html` | ✓ |

## Registry

Artifact registry updated: `4_artifact/registry.yaml`

## Execution Report

`4_artifact/3_document/execution_report_v20260624.html`

## Result Report

`4_artifact/3_document/result_report_v20260624.html`

## Validation Performed

- All 10 indexes validated: JSON parse, schema shape, element counts
- Key completeness scores computed per index
- Neighbor graphs checked for empty/missing edges
- Entity coverage checked against T-013 historical demo entities
- `index_health_summary.json` validated as parseable JSON

## Caveats

- T-042 (contract_and_demo_spec_m1) has not been executed — coverage gap analysis uses T-013 historical evidence as proxy. Re-check when actual T-042 demo cases exist.
- function_index.json has non-standard structure (dict with meta/var_names/aliases) — loaders must unwrap before use.
- cellline_tree.json is flat, not hierarchical — proxy expansion via ontology not available without rebuild.

## T-047 Handoff

**Verdict: M1-ready.** All indexes valid. 4 warnings (non-blocking). No fixture-only path needed — real indexes are ready for loader hardening.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-045 index_health_check_m1

## Task Goal
Audit 10 M1-relevant query indexes from T-021 standard resources (D-004). Verify JSON schema, required keys, neighbor graph completeness, and coverage gaps against M1 demo cases. Report only — do not modify indexes.

## What Was Delivered
- Machine-readable health summary (JSON, per-index schema status, key completeness, size, gaps, patch recommendations)
- Human-readable health report (MD, pass/warn/block per index, T-047 handoff advice)
- Gap notes (MD, severity/demo-impact/resolution per gap)
- Execution report (HTML) and result report (HTML)

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T-045/D-001 | 4_artifact/2_persist/index_health_summary.json | Programmatic health check: per-index schema, key completeness, known gaps, patch recommendations | Load into T-047 hardening script to configure loader expectations |
| T-045/D-002 | 4_artifact/2_persist/index_health_report.md | Human-readable overview: which indexes pass/warn/block, M1 readiness verdict | Quick reference for T-047 developer; guides loader hardening priorities |

## Supporting Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T-045/D-003 | 4_artifact/3_document/gap_notes.md | Detailed severity, demo impact, and resolution per structural gap | Reference when deciding which gaps to fix vs accept |
| T-045/D-004 | 4_artifact/3_document/execution_report_v20260624.html | Full step-by-step execution record | Audit trail for what was checked |
| T-045/D-005 | 4_artifact/3_document/result_report_v20260624.html | Per-index health table and M1 readiness verdict | Human-facing summary for review |

## Downstream Use
- **T-047 (resource_loader_hardening_m1):** Primary consumer. Use `index_health_summary.json` to configure loader field mappings, unwrap logic, and validation rules.
- **T-042 (contract_and_demo_spec_m1):** Cross-reference once executed — this task used T-013 as proxy for entity coverage.

## Known Limits / Risks
1. T-042 not yet executed — coverage gap analysis uses T-013 historical evidence as proxy. Re-check when actual T-042 demo cases exist.
2. function_index.json has non-standard dict structure (meta/var_names/aliases) — loaders must unwrap.
3. cellline_tree.json is flat (3 keys), not hierarchical — no ontology-based proxy expansion.
4. gene_index.json field names: `symbol` not `gene_symbol`, no `ensembl_id`.

## Do Not Read / Do Not Reuse
- Execution intermediate outputs under `3_execution/` (step1-3 checkpoints) — summary already consolidated in D-001.

## Recommended Next Reads
1. `4_artifact/2_persist/index_health_summary.json` — programmatic input for T-047
2. `4_artifact/3_document/gap_notes.md` — gap decisions before T-047 hardening

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
