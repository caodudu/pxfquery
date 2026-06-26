# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:27

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-044 package_skeleton_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1`
- Objective:

```text
Create the clean M1 Python package skeleton for PxFquery. Use T-007 to anchor package name, module boundaries, and original tool intent. Deliver pyproject.toml, src/pxfquery layout, minimal package metadata, import smoke evidence, and a clear placeholder structure for loader/query/CLI modules. Do not migrate old implementation code here and do not implement query behavior beyond import-safe stubs.
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
# T-044 package_skeleton_m1 — Protocol

## Objective

Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence. Anchor the package name and module boundaries in T-007 development state report. Do not migrate legacy implementation code and do not implement query behavior beyond import-safe stubs.

## Position In Project

This is the first development-phase task for `goal_m1_python_package_v2`. It delivers the bottom-layer Python package skeleton that later tasks will populate with actual loader, query, CLI, and resolver logic. The skeleton must remain reusable even if later implementation fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | .../4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Anchors intended package name (pxfquery), module structure (core/data/query/index/llm/viz), and component boundaries from legacy development state |
| A-002 | T-007/D-003 | .../4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Confirms per-module status: which modules are implemented/incomplete/historical, guiding what to stub and what to leave for later tasks |
| A-003 | T-007/D-006 | .../4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Provides recommended D001 package setup scope, acceptance criteria, and explicit do-not-do rules (do not copy main.py, do not edit flat assets) |

## Execution Steps

1. Read T-007 development state report and module status matrix to confirm the canonical package name (`pxfquery`) and intended subpackage boundaries: `core`, `data`, `query`, `index`, `llm`, `viz`.
2. Create `pyproject.toml` at the task's working directory with:
   - `[build-system]` using `setuptools` or `hatchling`
   - `[project]` with `name = "pxfquery"`, minimal metadata (version `0.1.0`, Python `>=3.10`), and no external dependencies beyond stubs
   - `[tool.setuptools.packages.find]` or equivalent pointing to `src`
3. Create the `src/pxfquery/` directory structure:
   - `src/pxfquery/__init__.py` — empty package marker
   - `src/pxfquery/core.py` — import-safe stub class `PxFquery` with `__init__` taking optional config dict, no functional methods
   - `src/pxfquery/data/__init__.py` — empty subpackage; stub `loader.py` with a `DataLoader` class placeholder
   - `src/pxfquery/query/__init__.py` — empty subpackage; stub `forward.py` and `reverse.py` with class placeholders
   - `src/pxfquery/index/__init__.py` — empty subpackage; stub `cellline_index.py`, `drug_index.py`, `gene_index.py`, `function_index.py` with class placeholders
   - `src/pxfquery/llm/__init__.py` — empty subpackage; stub `prompts.py` with function placeholders
   - `src/pxfquery/viz/__init__.py` — empty subpackage; stub `plots.py` with function placeholders
   - `src/pxfquery/cli/__init__.py` — empty subpackage for future CLI entry points
4. Run import smoke test: `python -c "import pxfquery; print(pxfquery.__version__)"` from the package root.
5. Record import smoke evidence as a file in `4_artifact/`.

## Constraints

- Use package name `pxfquery` as anchored by T-007 legacy codebase (`core.py` defines `PxFquery`, old package lives under `code/pxfquery_package/`).
- Use `src/pxfquery` layout (src-layout).
- All module stubs must be import-safe: no external imports that would fail, no filesystem operations, no network calls.
- Do not migrate, copy, or read legacy implementation code from `2_project_asset/` or the legacy source root.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep the skeleton dependency-free except for `setuptools`/`hatchling` build requirements.
- The `main.py` file identified by T-007 as historical/incomplete must not appear in this skeleton.

## Forbidden

- Do not copy legacy `code/pxfquery_package/` implementation or any migrated flat asset.
- Do not implement functional query, loader, resolver, index, LLM, or viz behavior.
- Do not install or require runtime dependencies (numpy, pandas, anndata, openai, etc.).
- Do not modify `2_project_asset/`, the migrated flat asset library, or the legacy source root.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| pyproject.toml | task working directory/ | yes |
| Package skeleton with stubs | src/pxfquery/ | yes |
| Import smoke evidence | 4_artifact/2_import_smoke/ | yes |
| Execution script/log | 3_execution/ | yes |
| Completion report | 5_report/completion.md | yes |

## Acceptance Criteria

- `pyproject.toml` exists with name `pxfquery`, minimum Python spec, and build-system declaration.
- `src/pxfquery/` layout exists with all subpackage `__init__.py` files and import-safe stub modules for `core`, `data/loader`, `query/forward`, `query/reverse`, `index/*`, `llm/prompts`, `viz/plots`, and `cli`.
- `python -c "fro

...[truncated by CyHex prompt assembler: 821 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: D-001
    name: package_skeleton_pyproject
    type: config
    path: 4_artifact/1_package/pyproject.toml
    status: accepted
    notes: pyproject.toml with name=pxfquery, version=0.1.0, hatchling build, src-layout, Python>=3.10

  - id: D-002
    name: package_skeleton_src
    type: code
    path: 4_artifact/1_package/pxfquery/
    status: accepted
    notes: src/pxfquery/ package skeleton with core, data, query, index, llm, viz, cli subpackages and import-safe stubs

  - id: D-003
    name: import_smoke_evidence
    type: document
    path: 4_artifact/2_import_smoke/smoke_test_v20260624.txt
    status: accepted
    notes: Import smoke test results — all imports pass, version 0.1.0, no runtime deps

  - id: D-004
    name: execution_log
    type: script
    path: 3_execution/create_skeleton.sh
    status: accepted
    notes: Shell script recording all steps to create the package skeleton

  - id: D-005
    name: execution_report
    type: document
    path: 4_artifact/3_document/execution_report_v20260624.html
    status: accepted
    notes: HTML execution report

  - id: D-006
    name: result_report
    type: document
    path: 4_artifact/3_document/result_report_v20260624.html
    status: accepted
    notes: HTML result report

```

### Completion Report
```md
# Completion — T-044 package_skeleton_m1

Status: **COMPLETED**

## What Was Done

Created the M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, import-safe stubs, and import smoke evidence.

## Deliverables Produced

| Deliverable | Path | Status |
|---|---|---|
| pyproject.toml | task working directory/ | Delivered |
| Package skeleton | src/pxfquery/ | Delivered |
| Import smoke evidence | 4_artifact/2_import_smoke/smoke_test_v20260624.txt | Delivered |
| Execution script | 3_execution/create_skeleton.sh | Delivered |
| Registry | 4_artifact/registry.yaml | Delivered (6 entries) |
| Execution report | 4_artifact/3_document/execution_report_v20260624.html | Delivered |
| Result report | 4_artifact/3_document/result_report_v20260624.html | Delivered |

## Acceptance Criteria Check

- pyproject.toml with name=pxfquery, hatchling build, Python >=3.10: PASS
- src/pxfquery layout with all subpackages and stubs: PASS
- `python -c "from pxfquery import PxFquery"` succeeds: PASS
- No legacy code present in skeleton: PASS
- All outputs registered in registry.yaml: PASS

## Package Structure Created

```
src/pxfquery/
├── __init__.py          # __version__ = "0.1.0", exports PxFquery
├── core.py              # class PxFquery(config=None)
├── data/
│   ├── __init__.py
│   └── loader.py        # class DataLoader
├── query/
│   ├── __init__.py
│   ├── forward.py       # class ForwardQuery, ForwardResult
│   └── reverse.py       # class ReverseQuery, ReverseResult
├── index/
│   ├── __init__.py
│   ├── cellline_index.py  # class CellLineIndex
│   ├── drug_index.py      # class DrugIndex
│   ├── gene_index.py      # class GeneIndex
│   └── function_index.py  # class FunctionIndex
├── llm/
│   ├── __init__.py
│   └── prompts.py       # 6 prompt builder stub functions
├── viz/
│   ├── __init__.py
│   └── plots.py         # 3 plot function stubs
└── cli/
    └── __init__.py      # placeholder
```

## Constraints Honored

- Package name `pxfquery` confirmed from T-007 assets
- `src/pxfquery` src-layout used
- All stubs are import-safe (no external imports, no IO, no network)
- No legacy code migrated, copied, or read from legacy sources
- No runtime dependencies required
- `main.py` not present
- Did not read `2_project_asset/` or modify predecessor task directories

## Deviations

None. All protocol steps executed as specified.
```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-044 package_skeleton_m1

## Task Goal
Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence.

## What Was Delivered
- `pyproject.toml` with name=pxfquery, version=0.1.0, hatchling build, Python>=3.10, src-layout
- `src/pxfquery/` package skeleton with 8 subpackages (core, data, query, index, llm, viz, cli) and import-safe stubs
- Import smoke test results — all imports pass
- Execution script, HTML execution report, HTML result report

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_package/pyproject.toml` | Build configuration anchoring package name & version | Copy to task root or reference as canonical package metadata |
| D-002 | `4_artifact/1_package/pxfquery/` | Package skeleton with all stub modules | Copy into new task's working directory; populate stubs with implementation |
| D-003 | `4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Evidence that the skeleton is import-safe | Run same tests after modifying skeleton to verify no regressions |

## Supporting Artifacts
| ID | Path | Type | Stars |
|---|---|---|---|
| D-004 | `3_execution/create_skeleton.sh` | script | 2 |
| D-005 | `4_artifact/3_document/execution_report_v20260624.html` | report | 3 |
| D-006 | `4_artifact/3_document/result_report_v20260624.html` | report | 3 |

## Downstream Use
The skeleton is the bottom-layer asset for all later M1 development tasks. Downstream tasks should:
- Copy `4_artifact/1_package/pyproject.toml` and `4_artifact/1_package/pxfquery/` into their working directory
- Extend stubs with actual loader, query, index, LLM, viz, and CLI logic
- Do NOT modify the skeleton's package name (`pxfquery`) or src-layout

## Known Limits / Risks
- No runtime dependencies are declared yet (numpy, pandas, anndata, etc. will be needed by later tasks)
- Stubs have empty method bodies — they are not functional
- `pyproject.toml` references `README_TASK.md` which does not exist at the project root (only relevant for `pip install -e .` outside the task directory)

## Do Not Read / Do Not Reuse
- Legacy implementation code under `2_project_asset/` or legacy source root — intentionally excluded from skeleton scope
- `main.py` — identified as historical/incomplete by T-007

## Recommended Next Reads
1. `4_artifact/1_package/pyproject.toml` — canonical package metadata
2. `4_artifact/1_package/pxfquery/__init__.py` — version and top-level exports
3. `4_artifact/2_import_smoke/smoke_test_v20260624.txt` — import test patterns to replicate
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
