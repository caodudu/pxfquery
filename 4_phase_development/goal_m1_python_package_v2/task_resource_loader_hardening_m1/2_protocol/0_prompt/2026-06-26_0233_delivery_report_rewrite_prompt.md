# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:33

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-047 resource_loader_hardening_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1`
- Objective:

```text
Harden the loader against real M1 manifest and index resources. Use T-043 for manifest/fixture definitions and T-045 for index health findings; optionally use T-041 legacy source digest if available for implementation clues. Deliver enhanced loader behavior, real-path/index smoke results, and a clear gap list if full hardening is blocked. This is a reusable enhancement asset and must not block the M1 fixture-based path if real resources are incomplete.
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
# T-047 resource_loader_hardening_m1 — Protocol

## Objective

Harden the M1 Python-package resource loader against real full matrix/index resources and the fixture package, using T-043 manifest/fixture definitions and T-045 index health findings. Deliver enhanced loader behavior (real-path loading, schema-aware unwrap, field normalization), smoke results against both full resources and fixtures, and a clear gap/block list for anything that cannot be safely hardened. This is a reusable enhancement asset and must not block the M1 fixture-only path if real resources are incomplete.

## Position In Project

- G-005 `goal_m1_python_package_v2` — development phase, enhancement/reuse asset
- Hard inputs: T-043 data manifest & fixture package, T-045 index health check
- T-041 legacy source digest is not delivered — exclude from configuration; execution may not use it
- T-047 is NOT an M1 blocker — if real resources are incomplete, report gaps and continue with fixture-based path

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-043/D-001 | 4_artifact/2_persist/resource_manifest_m1.yaml | Entry point for full standard resource paths (h5ad, csv, json) and fixture resource paths; defines loader role, required keys/columns, expected shapes, validation rules |
| A-002 | T-043/D-003 | 4_artifact/5_table/expected_shapes_keys_columns_m1.csv | Acceptance evidence for expected shapes, keys, columns, and index semantics |
| A-003 | T-043/D-004 | 4_artifact/5_table/sample_records_m1.csv | Traceable sample rows and keys for smoke verification |
| A-004 | T-045/D-001 | 4_artifact/2_persist/index_health_summary.json | Machine-readable per-index schema status, key completeness, known gaps, patch recommendations |
| A-005 | T-045/D-002 | 4_artifact/2_persist/index_health_report.md | Human-readable index health overview with pass/warn/block per index and M1 readiness verdict |
| A-006 | T-045/D-003 | 4_artifact/3_document/gap_notes.md | Detailed gap severity, demo impact, and resolution paths |
| A-007 | T-043/D-002 | 4_artifact/2_persist/fixture_package_m1/ | Compact real-data fixture bundle for deterministic loader smoke/demo runs |
| A-008 | T-043/D-005 | 4_artifact/2_persist/data_manifest_fixture_m1_readme.md | Downstream usage notes and exclusions |

## Execution Steps

1. **Load and validate the resource manifest.** Read `resource_manifest_m1.yaml` (A-001) and confirm that all listed resource paths are resolvable and non-empty. Record any missing full-resource paths as a gap.
2. **Read index health summary.** Load `index_health_summary.json` (A-004) and extract per-index schema requirements, field mappings, known gaps, and patch recommendations. Cross-reference with `expected_shapes_keys_columns_m1.csv` (A-002).
3. **Implement or enhance the loader against real full resources.** For each resource type (h5ad matrices, csv metadata, json indexes), implement or enhance loader functions that:
   - Open real `.h5ad` matrices (cp_func_ad, sh_func_ad, xpr_func_ad) and validate obs columns, var_names, and shapes against manifest expectations.
   - Load real CSV metadata tables and validate key columns, row counts against manifest.
   - Load real JSON indexes and validate schema/top-level structure against manifest and T-045 health summary.
   - Handle the `function_index.json` non-standard dict structure (`meta/var_names/aliases`) — unwrap per T-045 handoff.
   - Normalize field names where T-045 reports discrepancies (e.g., `gene_index.json` uses `symbol` not `gene_symbol`; `cellline_tree.json` is flat with 3 keys only, not hierarchical).
4. **Run loader smoke tests with the fixture package.** Load all fixture resources from `fixture_package_m1/` (A-007) and verify:
   - Fixture matrices are readable, shapes match manifest, obs columns and var_names are present.
   - Fixture metadata CSV files match expected row counts and key columns.
   - Fixture JSON indexes are parsable and match expected top-level keys.
5. **Execute real full-resource loading where feasible.** Attempt to load full standard resources from paths defined in the manifest. For each resource:
   - If load succeeds: record shape, key presence, and any field normalizations applied.
   - If load fails or a resource is missing: document the specific gap (path, reason), assess whether fixture covers the gap, and classify as block/warn/note.
6. **Produce gap list.** Aggregate all gaps from steps 1–5 into a structured gap list with: resource ID, path, issue, severity (block/warn/info), whether fixture covers it, recommended action.
7. **Produce smoke results report.** Generate a machine-readable result summary (JSON) and a human-readable report (MD) with: per-resource load status, shape/key validation results, any field normalizations applied, gap list.
8. **Deliver artifacts.** Register all accepted outputs in `4_artifact/registry.yaml`. Write `5_report/completion.md`.

## Constraints

- This is an enhancement/reuse asset — do NOT blo

...[truncated by CyHex prompt assembler: 2835 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: loader_hardening_m1_code
  type: code
  source: T-047
  origin: 3_execution/loader_hardening_m1.py
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/1_code/loader_hardening_m1.py
  notes: Enhanced loader module with h5ad/CSV/JSON handlers, function_index unwrap,
    field normalization
  identity: T-047/D-001
  role: script
  core: false
  lineage_anchor: false
  stars: 2
- id: D-002
  name: loader_smoke_results_json
  type: data
  source: T-047
  origin: T-047/D-001
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/2_persist/loader_smoke_results_m1.json
  notes: Machine-readable per-resource load status, shape validation, normalizations,
    gap list
  identity: T-047/D-002
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: D-003
  name: loader_smoke_report
  type: document
  source: T-047
  origin: T-047/D-001
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/3_document/loader_smoke_report_m1.md
  notes: Human-readable smoke report with summary, per-resource results, normalizations,
    gaps, verdict
  identity: T-047/D-003
  role: report
  core: false
  lineage_anchor: false
  stars: 4
- id: D-004
  name: loader_gap_list
  type: document
  source: T-047
  origin: T-047/D-001
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/3_document/loader_gap_list_m1.md
  notes: Structured gap list with resource ID, path, issue, severity, fixture coverage,
    recommended action
  identity: T-047/D-004
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-005
  name: execution_report_html
  type: document
  source: T-047
  origin: T-047/D-001
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/3_document/execution_report_v2.html
  notes: Traceable execution log with commands, outputs, timestamps (v2)
  identity: T-047/D-005
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: D-006
  name: result_report_html
  type: document
  source: T-047
  origin: T-047/D-001
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/3_document/result_report_v2.html
  notes: Formatted result summary with tables, gap classification, recommendations
    (v2)
  identity: T-047/D-006
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: D-007
  name: fixture_package_copy
  type: package
  source: T-047
  origin: A-007 (fixture_package_m1)
  registered: '2026-06-24'
  status: accepted
  path: 4_artifact/2_persist/fixture_package_m1
  notes: Copy of fixture package at expected loader path (18 files)
  identity: T-047/D-007
  role: delivery
  core: false
  lineage_anchor: false
  stars: 1

```

### Completion Report
```md
# Completion — T-047 resource_loader_hardening_m1

**Status:** Complete
**Completed:** 2026-06-24T04:58

## Summary

T-047 successfully implemented and executed a hardened resource loader for M1 Python-package resources. Both the fixture package (18 files) and full standard resources (18 files) were loaded and validated. The loader was re-run after fixing gap severity mapping and obs column filtering — all 36 resources pass.

## Results

| Metric | Count |
|---|---|
| Total resources | 36 |
| Loaded successfully | 36 |
| Missing | 0 |
| Errors | 0 |
| Field normalizations applied | 4 |
| Gaps (T-045 known, non-blocking) | 6 (4 warn, 2 cosmetic) |

## Loader Capabilities

- **h5ad matrices**: anndata read, shape validation, obs column presence check, var_names matching (fixture) / var count (full)
- **CSV metadata**: pandas read, row count validation, required column presence check
- **JSON indexes**: parse validation, top-level schema checks
  - `function_index.json` unwrap (meta/var_names/aliases extraction)
  - Category derivation (Hallmark / 3CA MPS from `source` field)
  - `gene_index.json` field normalization (`symbol` → `gene_symbol`)
  - `cellline_index.json` unwrap (`valid_cells` extraction)
  - `cellline_tree.json` flat structure documented
  - Generic JSON key count validation for neighbor indexes

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Enhanced loader code (v2) | `4_artifact/1_code/loader_hardening_m1.py` | accepted |
| Smoke results JSON | `4_artifact/2_persist/loader_smoke_results_m1.json` | accepted |
| Smoke report MD | `4_artifact/3_document/loader_smoke_report_m1.md` | accepted |
| Gap list MD | `4_artifact/3_document/loader_gap_list_m1.md` | accepted |
| Execution report HTML (v2) | `4_artifact/3_document/execution_report_v2.html` | accepted |
| Result report HTML (v2) | `4_artifact/3_document/result_report_v2.html` | accepted |
| Artifact registry | `4_artifact/registry.yaml` | accepted |
| Fixture package copy | `4_artifact/2_persist/fixture_package_m1/` | accepted |

## Notes

- Full standard resources: 18/18 loaded. All 3 h5ad matrices (cp: 201014×91, sh: 189365×91, xpr: 132464×91), 6 CSV tables (cellline_meta 240×8, cellline_info 240×20, compound_meta 6647×9, compound_info 39321×7, gene_info 12328×7), and 9 JSON indexes parsed and validated.
- Fixture resources: 18/18 loaded. All fixture shapes and columns match manifest specifications.
- No authoritative indexes or bundle resources were mutated.
- All 6 remaining gaps are known T-045 health findings (4 warning, 2 cosmetic) — all addressed by loader normalizations or documented. No new gaps discovered.
- Bugs fixed during execution: gap severity summary normalized warning/cosmetic to warn/info; required obs column filtering cleaned up to avoid matching var_names as obs columns.
```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-047 resource_loader_hardening_m1

## Task Goal
Harden the M1 Python-package resource loader against real full matrix/index resources and the fixture package using T-043 manifest/fixture definitions and T-045 index health findings. Deliver enhanced loader code, smoke results for both paths, and a structured gap list.

## What Was Delivered
- Enhanced loader module handling h5ad/CSV/JSON with function_index unwrap and field normalization
- Smoke results (JSON + MD report): 36/36 resources pass (18 fixture + 18 full standard)
- Gap list: 6 known T-045 findings (4 warn, 2 cosmetic), no new gaps
- Execution/result HTML reports (v2)
- Fixture package copy at expected loader path

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_code/loader_hardening_m1.py` | Main hardened loader code; handles all M1 resource types | Import or call via `python loader_hardening_m1.py --root <path>` |
| D-002 | `4_artifact/2_persist/loader_smoke_results_m1.json` | Machine-readable per-resource pass/fail, shapes, normalizations, gaps | Load as JSON for downstream dashboards or CI checks |
| D-003 | `4_artifact/3_document/loader_smoke_report_m1.md` | Human-readable summary, per-resource tables, gap assessment, M1 readiness verdict | Read for quick task outcome overview |
| D-004 | `4_artifact/3_document/loader_gap_list_m1.md` | Structured gap list with severity, fixture coverage, recommended actions | Reference for M1 go/no-go decisions and follow-up tasks |

## Supporting Artifacts
| ID | Path | Why it matters |
|---|---|---|
| D-005 | `4_artifact/3_document/execution_report_v2.html` | Traceable execution log with commands, outputs, timestamps |
| D-006 | `4_artifact/3_document/result_report_v2.html` | Formatted result tables, gap classification, recommendations |
| D-007 | `4_artifact/2_persist/fixture_package_m1/` | 18-fixture bundle copied to loader-expected path for deterministic reuse |

## Downstream Use
- **M1 Python package v2**: The loader is ready for integration. Use it as the standard resource-loading entry point.
- **Follow-up hardening tasks**: Gap list (D-004) identifies 6 items to address in future tasks.
- **Demo/CI**: Fixture path (D-007) provides a deterministic 18-file bundle for quick smoke tests.

## Known Limits / Risks
- 6 remaining gaps are T-045 known issues (4 warn, 2 cosmetic) — all handled by loader normalizations; no new issues discovered.
- Full resource loading depends on `t021_standard_resources_bundle/` being present at the configured root. Fixture path works independently.
- `function_index.json` unwrap and `gene_index.json` field normalization are explicit and logged, but downstream code must consume the normalized output.

## Do Not Read / Do Not Reuse
- `3_execution/gen_reports.py`: Internal HTML generation helper, not a reusable deliverable.
- `3_execution/loader_hardening_m1.py` (original): Superseded by `4_artifact/1_code/loader_hardening_m1.py`.
- v1 HTML reports: Superseded by v2.

## Recommended Next Reads
1. `4_artifact/3_document/loader_smoke_report_m1.md` — overall outcome summary
2. `4_artifact/3_document/loader_gap_list_m1.md` — what remains to fix
3. `4_artifact/1_code/loader_hardening_m1.py` — the loader code itself

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
