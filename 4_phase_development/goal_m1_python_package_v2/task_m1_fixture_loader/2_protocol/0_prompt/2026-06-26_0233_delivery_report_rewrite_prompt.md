# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:33

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-046 m1_fixture_loader
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader`
- Objective:

```text
Implement the low-risk M1 fixture loader. Use T-043 as the hard source for manifest/fixture schema and expected shapes. Deliver reusable loader code and loader smoke evidence showing the M1 fixture can be loaded with stable matrix/index access APIs. This task should be small and reliable; it must not attempt full production resource hardening and must not bypass the T-043 fixture contract.
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
# T-046 m1_fixture_loader — Protocol

## Objective
Implement the low-risk M1 fixture loader using T-043 as the hard source for the manifest, fixture package, expected shapes, keys, columns, and index semantics. Deliver reusable loader code plus smoke evidence showing that the M1 fixture can be loaded through stable matrix/index access APIs.

## Position In Project
This task is the small development bridge between the T-043 data substrate and downstream M1 query/demo tasks. T-048 and T-049 must be able to use the loader API without creating private fixture parsing or bypassing the T-043 fixture contract. This task is not responsible for production resource hardening, biological ranking validation, or full-resource loading.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml` | Hard source for M1 manifest schema and fixture/full-resource path discovery. |
| A-002 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/` | Deterministic fixture package that the loader must load. |
| A-003 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Acceptance reference for expected fixture shapes, keys, columns, validation rules, and index semantics. |

## Execution Steps
1. Inspect the registered T-043 manifest, fixture package, and expected-shapes table only as needed to implement the loader.
2. Locate the current Python package/module layout and add a minimal reusable M1 fixture loader in the existing code style.
3. Expose a stable loader API that reads the T-043 manifest/fixture contract and returns documented matrix/index access objects or mappings suitable for downstream T-048/T-049 use.
4. Keep validation limited to fixture existence, supported file formats, required keys/columns, expected shapes, and stable index/matrix access. Do not add full production resource hardening.
5. Create a small smoke script or test in `3_execution/` that loads the registered fixture through the public loader API and records observed shapes, keys, columns, and example index access.
6. Move accepted reusable outputs and evidence into `4_artifact/`, update `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints
- Use T-043 artifacts as the hard source for manifest and fixture behavior; do not invent alternative schemas.
- Keep the loader deliberately small, deterministic, and reliable.
- The API must be stable enough for T-048 and T-049 to call directly.
- Document the API surface and expected fixture contract in a reusable artifact or report.
- Use the project Python runtime unless the execution stage documents a concrete reason to do otherwise.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.

## Forbidden
- Do not read or use project-level raw assets under `2_project_asset/`.
- Do not scan unrelated tasks or legacy source roots.
- Do not use T024-T040 outputs as authority for the M1 route.
- Do not create private query logic, ranking logic, or biological interpretation.
- Do not claim the fixture validates full-resource coverage or biological ranking quality.
- Do not call downstream CyHex prompt endpoints.

## Web Search Allowance
Allowed: no
Reason: The task is fully scoped by project protocol, current task metadata, and selected T-043 predecessor artifacts. No current external evidence is needed.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Reusable M1 fixture loader code | Existing package/module path chosen by execution after inspecting code layout | Yes |
| Loader API documentation or concise usage note | `4_artifact/2_persist/` or `4_artifact/3_document/` | Yes |
| Loader smoke evidence with observed shapes/keys/index access | `4_artifact/5_table/` and/or `4_artifact/3_document/` | Yes |
| Execution logs or temporary smoke scripts | `3_execution/` | Yes |
| Artifact registry update | `4_artifact/registry.yaml` | Yes |
| Completion report | `5_report/completion.md` | Yes |

## Acceptance Criteria
- The loader reads the T-043 manifest and fixture package rather than hardcoding unrelated paths or schemas.
- The public API can load the fixture and expose stable matrix/index access needed by downstream query tasks.
- Smoke evidence records successful loading plus observed shapes, key names, columns, and at least one stable index/matrix access example.
- Observed fixture structure is checked against T-043 expected shapes/keys/columns.
- Scope remains limited to fixture loading and smoke evidence.
- Reusable outputs are regist

...[truncated by CyHex prompt assembler: 821 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: m1_fixture_loader_code
  type: package_module
  path: 4_artifact/1_package/pxfquery/data/m1_loader.py
  source: pxfquery.data.m1_loader
  notes: Reusable M1FixtureLoader + M1Fixture + M1Manifest classes in the package data subpackage.
  generated_by: T-046 execution
  created: "2026-06-24"
  status: accepted
- id: D-002
  name: m1_loader_api_documentation
  type: document
  path: 4_artifact/2_persist/API_REFERENCE_v20260624.md
  notes: API surface documentation for M1FixtureLoader, M1Fixture, M1Manifest.
  generated_by: T-046 execution
  created: "2026-06-24"
  status: accepted
- id: D-003
  name: smoke_evidence_table
  type: table
  path: 4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
  notes: Observed vs expected shapes/columns for all fixture resources; 8/8 PASS.
  generated_by: T-046 execution
  created: "2026-06-24"
  status: accepted
- id: D-004
  name: smoke_script
  type: script
  path: 3_execution/smoke_m1_loader.py
  notes: Reproducible smoke script that loads fixture through public API and compares against A-003.
  generated_by: T-046 execution
  created: "2026-06-24"
  status: accepted
- id: D-005
  name: smoke_output_log
  type: log
  path: 3_execution/smoke_output.txt
  notes: Full smoke output log; 24 checks passed, 0 failed.
  generated_by: T-046 execution
  created: "2026-06-24"
  status: accepted
```

### Completion Report
```md
# Completion Report — T-046 m1_fixture_loader

## Summary

Implemented a minimal, reusable M1 fixture loader (`M1FixtureLoader`) in the `pxfquery.data.m1_loader` module within the existing M1 Python package skeleton. The loader reads the T-043 manifest and fixture package, validates structure against A-003 expected shapes, and exposes stable matrix/index access APIs suitable for downstream T-048/T-049 use.

## Implementation

### Loader Code
- **Module:** `task_package_skeleton_m1/src/pxfquery/data/m1_loader.py`
- **Public classes:** `M1FixtureLoader`, `M1Fixture`, `M1Manifest`
- **Re-exports in:** `pxfquery.data.__init__` (updated to export new symbols)

The API reads a T-043 `resource_manifest_m1.yaml` manifest and a `fixture_package_m1/` directory, returning documented dataclass objects with AnnData matrices, pandas DataFrames, and dict-based JSON indices. Convenience methods (`matrix_shape`, `get_matrix_row`, etc.) provide stable access for downstream tasks.

The package was installed in dev mode (`pip install -e`) in the project conda environment.

### Smoke Evidence

A smoke script (`3_execution/smoke_m1_loader.py`) loads the registered fixture and validates:

| Check type | Count | Result |
|---|---|---|
| Matrix shapes | 3 | All PASS (4x7) |
| Metadata table shapes | 5 | All PASS |
| JSON index key counts | 10 | All PASS |
| Stable index access examples | 6 | All PASS |
| **Total** | **24** | **24/24 PASS** |

All observed shapes, columns, and key counts match the A-003 expected-shapes reference exactly.

### Environment Changes

- `pxfquery` package re-installed as editable from `task_package_skeleton_m1/` (was pointing to old `goal_package_foundation_v1` path).
- Stale editable-install pth files from T-024 and T-032 cleaned from site-packages.
- No new packages installed.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Loader code | `task_package_skeleton_m1/src/pxfquery/data/m1_loader.py` | Accepted |
| API documentation | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Accepted |
| Smoke evidence table | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Accepted |
| Smoke script | `3_execution/smoke_m1_loader.py` | Accepted |
| Smoke output log | `3_execution/smoke_output.txt` | Accepted |
| Artifact registry | `4_artifact/registry.yaml` | Updated (5 artifacts) |
| Completion report | `5_report/completion.md` | This file |

## Acceptance Criteria Met

1. **Manifest-driven loading:** Loader reads the registered T-043 manifest and fixture package; no hardcoded paths.
2. **Stable API:** `M1FixtureLoader` exposes `manifest` and `fixture` properties with documented matrix/index access methods.
3. **Smoke evidence:** Records all observed shapes, key names, columns, and stable sig_id row access.
4. **Contract check:** All 24 checks match A-003 expected values.
5. **Scope discipline:** No private query/ranking logic, no raw project-asset reads, no schema invention.

## Scope Limitations

- Fixture loading only; no full-resource hardening.
- No biological ranking or interpretation.
- No query/index resolver integration (reserved for T-048/T-049).

## Stop Rules Compliance

- A-001, A-002, A-003: present and consistent (no stop required).
- No `2_project_asset/` reads performed.
- Package layout identified within project boundary.
- T-043 fixture contract followed without schema invention.
- No expensive/networked/downstream operations attempted.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-046 m1_fixture_loader

## Task Goal
Provide a small, deterministic M1 fixture loader that downstream query tasks can call without re-parsing the T-043 fixture package privately.

## What Was Delivered
T-046 produced a loader module, API reference, smoke script, smoke output, evidence table, HTML reports, registry, and completion report. The successful execute session reported 24/24 smoke checks passing against the T-043 expected-shapes reference.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_package/pxfquery/data/m1_loader.py` | Task-local copy of the M1 fixture loader implementation. | T048/T049 can copy or merge this into their task-local package version. |
| D-002 | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Documents `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. | Read before using the loader API. |
| D-003 | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Records observed vs expected fixture structures. | Use as evidence that fixture loading works for M1 smoke data. |

## Supporting Artifacts
- `3_execution/smoke_m1_loader.py`
- `3_execution/smoke_output.txt`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Downstream Use
T048 and T049 should use this loader to access the T-043 fixture matrices and indexes. They should not implement separate ad hoc fixture parsing unless they record a deliberate compatibility reason.

## Known Limits / Risks
The loader is fixture-focused. It does not prove full-resource performance, biological ranking quality, or production-grade resource hardening. The successful execute session also modified the T044 skeleton package during editable install work; this handoff includes a task-local copy to keep the T046 deliverable self-contained.

## Do Not Read / Do Not Reuse
Do not use this task to justify resolver/LLM behavior, biological interpretation, or full-resource claims. Do not treat T024-T040 artifacts as authority.

## Recommended Next Reads
1. `4_artifact/2_persist/API_REFERENCE_v20260624.md`
2. `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv`
3. `3_execution/smoke_output.txt`
4. `5_report/completion.md`

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
