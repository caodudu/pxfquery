# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:31

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-052 package_assembly_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1`
- Objective:

```text
Assemble the runnable M1 package surface. Use T-044 package skeleton plus T-048 forward and T-049 reverse implementations. Deliver an installable package, import evidence, CLI command wiring, and demo commands for forward and reverse. This task may connect modules and package entry points, but must not reimplement query logic or replace validation evidence from T-050/T-051.
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
# T-052 package_assembly_m1 — Protocol

## Objective

Assemble the runnable M1 package surface from predecessor deliverables T-044 (package skeleton), T-059 (forward query core repair), and T-060 (reverse query core repair). Deliver an installable `pxfquery` package under `src/pxfquery/`, import evidence, CLI command wiring with forward/reverse/info subcommands, and demo command output for forward and reverse queries. Wiring and integration only — do not reimplement query logic or replace validation evidence from T-050/T-051.

## Position In Project

Bottom-layer M1 package assembly. Consumes T-044 skeleton structure and CLI wiring, T-059 forward+reverse query implementations, and T-060 reverse repair fixture. The assembled package becomes the single installable surface consumed by downstream M1 validation and demo tasks.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-044/D-001 | `4_artifact/1_package/pyproject.toml` | Base build config (name=pxfquery, hatchling, src-layout) |
| A-015 | T-059/D-001 | `4_artifact/1_package/pyproject.toml` | pyproject.toml with `[project.scripts]` entry |
| A-002 | T-044/D-002 | `pxfquery/cli/__init__.py` | CLI wiring with forward+reverse+info subcommands |
| A-003 | T-044/D-002 | `pxfquery/cli/__main__.py` | `python -m pxfquery` entry |
| A-004 | T-059/D-001 | `src/pxfquery/query/forward.py` | Forward query implementation |
| A-005 | T-059/D-001 | `src/pxfquery/query/reverse.py` | Reverse query implementation |
| A-010 | T-059/D-001 | `src/pxfquery/core.py` | Reference PxFquery class (func2pert needs rewiring) |
| A-006 | T-059/D-001 | `src/pxfquery/data/` | M1FixtureLoader + base loader |
| A-011 | T-059/D-003 | `forward_repair_fixture_m1_1/` | Forward demo fixture (EGFR/A549/xpr) |
| A-012 | T-059/D-002 | `forward_repair_manifest_m1_1.yaml` | Forward repair manifest |
| A-013 | T-060/D-002 | `reverse_repair_fixture_m1_1/` | Reverse demo fixture (HALLMARK_MYC_TARGETS_V1) |
| A-014 | T-060/D-003 | `reverse_repair_manifest_m1_1.yaml` | Reverse repair manifest |

## Execution Steps

1. **Create task-local package directory** at `4_artifact/1_package/` with `src/pxfquery/` layout.
2. **Establish pyproject.toml** — use T-059 version (A-015) with `[project.scripts]` entry; preserve name, version, build config from T-044 (A-001).
3. **Assemble module tree** — copy from T-059 forward package (A-004, A-005, A-006, A-007, A-008, A-009) into `src/pxfquery/`:
   - `query/forward.py` — forward query logic
   - `query/reverse.py` — reverse query logic
   - `data/` — loader modules
   - `index/` — index modules
   - `llm/` — prompt module
   - `viz/` — viz module
4. **Wire core.py** — create `src/pxfquery/core.py` with `PxFquery` class:
   - `pert2func()` delegates to `query/forward.forward_query()`
   - `func2pert()` delegates to `query/reverse.reverse_query()`
   - `load_data()`, `load_fixture()`, `query()` methods from T-059 pattern
   - This is wiring only — each query function already exists in the imported modules.
5. **Wire `__init__.py`** — export `PxFquery` class and `__version__`.
6. **Wire CLI** — copy T-044 `cli/__init__.py` (A-002) and `cli/__main__.py` (A-003); verify forward, reverse, info subcommands all resolve.
7. **Install package** — `pip install -e .` from the task working directory.
8. **Run import smoke** — verify `import pxfquery`, `from pxfquery.core import PxFquery`, `pxfquery --help`, `pxfquery info` all work.
9. **Run forward demo** — use T-059 repair fixture (A-011, A-012):
   ```
   pxfquery forward --perturbation EGFR --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
   ```
   Capture JSON output as evidence.
10. **Run reverse demo** — use T-060 repair fixture (A-013, A-014):
    ```
    pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
    ```
    Capture JSON output as evidence.
11. **Collect evidence** — save import smoke evidence, forward demo JSON, reverse demo JSON, and CLI help text under `4_artifact/`.
12. **Register artifacts** — update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not reimplement forward or reverse query logic. All query functions already exist in predecessor modules; only wire them in `core.py`.
- Do not replace, re-validate, or modify validation evidence from T-050/T-051.
- Do not use T024-T040 blocked assets.
- Do not use T-048/T-049 failed predecessor outputs. Use T-059/T-060 replacement outputs only.
- Do not read project-level raw assets under `2_project_asset/`.
- T-060/D-001 (package code) is a symlink to T-044 and is not accepted as standalone reverse implementation. Use T-059 `query/reverse.py` (A-005) as the authoritative reverse query source.
- Preserve `synthetic_repair` provenance labels when using T-059/T-060 fixtures.
- Do not modify predecessor task artifacts.

## Forbidden

- Reimplementing `forward_query()`, `rever

...[truncated by CyHex prompt assembler: 2687 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: assembled_package_source
  type: code
  path: 4_artifact/1_package/
  description: Assembled M1 pxfquery package source (src/pxfquery/ layout, pyproject.toml,
    CLI wiring)
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-001
  role: script
  core: false
  lineage_anchor: false
  stars: 2
- id: D-002
  name: import_smoke_evidence
  type: document
  path: 4_artifact/2_import_smoke/smoke_test_v20260624.txt
  description: Import smoke test evidence — import pxfquery, version, PxFquery class,
    CLI --help, info command
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-002
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-003
  name: forward_demo_json
  type: data
  path: 4_artifact/2_persist/forward_demo_v20260624.json
  description: Forward demo output — EGFR/A549/xpr with found:true, top_activated,
    top_suppressed
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-003
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: D-004
  name: reverse_demo_json
  type: data
  path: 4_artifact/2_persist/reverse_demo_v20260624.json
  description: Reverse demo output — HALLMARK_APOPTOSIS activate / HALLMARK_MYC_TARGETS_V1
    suppress / A549 with found:true, top_candidates
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-004
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: D-005
  name: cli_help_text
  type: document
  path: 4_artifact/2_persist/cli_help_v20260624.txt
  description: CLI help text for pxfquery, forward, reverse, and info subcommands
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-005
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-006
  name: execution_report
  type: document
  path: 4_artifact/3_document/execution_report_v20260624.html
  description: Execution report documenting the package assembly process
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-006
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: D-007
  name: result_report
  type: document
  path: 4_artifact/3_document/result_report_v20260624.html
  description: Result report documenting demo outputs and acceptance criteria
  generated: '2026-06-24'
  task_id: T-052
  status: accepted
  identity: T-052/D-007
  role: report
  core: false
  lineage_anchor: false
  stars: 5

```

### Completion Report
```md
# Completion

Task T-052 package_assembly_m1 completed successfully on 2026-06-24.

## Summary

Assembled the runnable M1 pxfquery package from T-044 package skeleton + T-059 forward repair + T-060 reverse repair.

## Deliverables Produced

| # | Deliverable | Path | Status |
|---|---|---|---|
| D-001 | Assembled package source | 4_artifact/1_package/ | accepted |
| D-002 | Import smoke evidence | 4_artifact/2_import_smoke/smoke_test_v20260624.txt | accepted |
| D-003 | Forward demo JSON | 4_artifact/2_persist/forward_demo_v20260624.json | accepted |
| D-004 | Reverse demo JSON | 4_artifact/2_persist/reverse_demo_v20260624.json | accepted |
| D-005 | CLI help text | 4_artifact/2_persist/cli_help_v20260624.txt | accepted |
| D-006 | Execution report | 4_artifact/3_document/execution_report_v20260624.html | accepted |
| D-007 | Result report | 4_artifact/3_document/result_report_v20260624.html | accepted |

## Acceptance Criteria

All 9 acceptance criteria passed:
1. pip install -e . succeeds
2. import pxfquery; print(__version__) returns 0.1.0
3. pxfquery info returns valid JSON with package name and version
4. pxfquery forward --help shows subcommand options
5. pxfquery reverse --help shows subcommand options
6. Forward demo returns found: true for EGFR/A549/xpr
7. Reverse demo returns found: true for HALLMARK_MYC_TARGETS_V1 + A549
8. All output JSON is well-formed per T-042 contract shape
9. No query logic was reimplemented — all query functions come from predecessor modules via import

## Key Wiring Change

The single most important assembly change was rewiring `func2pert()` in `core.py` from `NotImplemented` to delegate to `query/reverse.reverse_query()`. This connects the T-059 reverse query implementation to the PxFquery class API, enabling the `pxfquery reverse` CLI command.

## Constraints Compliance

- No query logic reimplemented
- No T-050/T-051 validation evidence modified
- No T024-T040 blocked assets used
- No T-048/T-049 artifacts referenced
- No project-level raw assets read
- synthetic_repair provenance preserved
- No predecessor task artifacts modified

## Issues Resolved

- pyproject.toml referenced README_TASK.md which didn't exist; fixed to README.md and created stub README.md in the package directory.
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
