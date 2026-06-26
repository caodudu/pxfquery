# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:27

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-042 contract_and_demo_spec_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1`
- Objective:

```text
Define the minimal M1 contract for the PxFquery Python package. Use T-007 for original tool intent and T-013 for MVP gap/function expectations. Deliver a compact API and CLI contract plus exact forward and reverse demo cases: input fields, output JSON shape, required no-hit/error behavior, and pass/fail criteria. Do not implement code, do not rewrite the full product design, and do not reference failed T024-T040 assets as authorities.
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
# T-042 contract_and_demo_spec_m1 — Protocol

## Objective

Define the single minimal M1 contract for the PxFquery Python package. The execution task must produce a compact API contract, CLI contract, forward demo case, reverse demo case, output JSON schema, no-hit/error behavior, and pass/fail criteria for downstream M1 implementation tasks.

This is a specification task only. It must not implement package code, run package tests, rebuild indexes, analyze raw data, or rewrite the full product design.

## Position In Project

T-042 sits at the start of `goal_m1_python_package_v2`. It translates the authoritative T-007 development-state digestion and T-013 MVP run-through review into a small M1 contract that later implementation and validation tasks can follow without inventing names, argument shapes, output schemas, demo inputs, or acceptance rules.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Anchor source authority, package identity, and safe carry-forward boundaries. |
| A-002 | T-007/D-002 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Keep the M1 contract faithful to the actual PxFquery tool and known component readiness. |
| A-003 | T-007/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Cross-check unsafe claims, scope boundaries, and no-hit/error behavior. |
| A-004 | T-013/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Primary authority for M1 required capabilities, gate capabilities, out-of-scope items, and prohibited claims. |
| A-005 | T-013/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Define negative cases and capabilities M1 must not claim. |
| A-006 | T-013/D-003 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Optional compact cross-check for pass/fail criteria. |
| A-007 | T-013/D-004 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/6_archive/pxfquery_t013_run_evidence_bundle_v20260618/` | Optional evidence-shape reference for prior forward, reverse, and no-hit examples; do not treat as current implementation output. |

## Execution Steps

1. Read A-001, A-002, A-004, and A-005 first; use A-003, A-006, and A-007 only as targeted cross-checks.
2. Extract only M1-relevant facts: package purpose, `(B, P, F)` model, forward query intent, reverse query intent, biological context fields, deterministic evidence boundaries, known missing capabilities, and unsafe claims to avoid.
3. Define a compact Python API contract with exact function names, required parameters, optional parameters, return JSON-like structures, and error/no-hit structures.
4. Define a compact CLI contract with exact command names, required flags, demo commands, output mode, exit behavior, and nonzero/error behavior.
5. Define exactly one forward demo case and exactly one reverse demo case. Each case must include exact input fields, expected output JSON shape, minimum required semantic content, and pass/fail assertions.
6. Define no-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior as deterministic contract-level outputs rather than uncaught crashes.
7. Write only the expected contract deliverables under `4_artifact/`, register them in `4_artifact/registry.yaml`, and summarize completion in `5_report/completion.md`.

## Constraints

- Do not implement code, run package tests, rebuild indexes, analyze raw matrices, or create package release artifacts.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not read the historical source root directly.
- Do not use T024-T040 outputs as authoritative inputs.
- Keep the contract small, deterministic, and directly actionable for T048, T049, and T052.
- M1 acceptance must not depend on LLM resolver success.
- Any uncertain biological or data-specific detail must be

...[truncated by CyHex prompt assembler: 2876 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: D-001
    name: m1_api_contract
    type: yaml
    task_id: T-042
    path: 2_persist/m1_api_contract.yaml
    description: >
      Structured M1 API and CLI contract. Specifies PxFquery class, pert2func/func2pert
      signatures, parameter schemas, return JSON shapes, error/no-hit output objects, CLI
      commands and flags, exit codes, and M1 scope assertions.
    status: accepted
    generated: "2026-06-24"
    authority: T-007 + T-013
    downstream_task: T-048, T-049, T-052

  - id: D-002
    name: m1_demo_cases
    type: yaml
    task_id: T-042
    path: 2_persist/m1_demo_cases.yaml
    description: >
      Exact forward demo case (DEMO-001: EGFR/A549/xpr) and reverse demo case
      (DEMO-002: HALLMARK_APOPTOSIS activation + MYC suppression in A549) with
      input fields, expected output JSON shape, pass/fail assertions, and no-hit variants.
    status: accepted
    generated: "2026-06-24"
    authority: T-007 + T-013
    downstream_task: T-052

  - id: D-003
    name: m1_contract_summary
    type: markdown
    task_id: T-042
    path: 3_document/m1_contract_summary.md
    description: >
      Short human-readable summary of M1 API, CLI, demo cases, scope, and constraints.
    status: accepted
    generated: "2026-06-24"
    authority: T-007 + T-013
    downstream_task: T-048, T-049, T-052

```

### Completion Report
```md
# T-042 contract_and_demo_spec_m1 — Completion Report

## Summary

T-042 delivered the M1 API/CLI contract for the PxFquery Python package. All required deliverables are produced and registered.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Structured API + CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | accepted |
| Forward + reverse demo cases with assertions | `4_artifact/2_persist/m1_demo_cases.yaml` | accepted |
| Human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | accepted |
| Artifact registry | `4_artifact/registry.yaml` | accepted |
| Completion note | `5_report/completion.md` | (this file) |

## Evidence Traceability

- **A-001 (T-007 source map)**: Used for package identity, asset boundary, and source priority rules.
- **A-002 (T-007 state report)**: Extracted `(B,P,F)` model, `pert2func`/`func2pert` intent, component readiness, index inventory, and validated examples.
- **A-004 (T-013 capability contract)**: Used for M1 scope (deterministic forward/reverse only), gated capabilities (resolver/LLM), and unsafe-claim boundaries.
- **A-005 (T-013 failure list)**: Provided negative cases (CAP-03 index naming gap, CAP-05 no-hit false-positive risk, CAP-06 numerical warnings) — all incorporated as contract-level error structures.
- **A-003 / A-006 / A-007**: Used as targeted cross-checks for risk validation and output JSON shape reference.

## Key Decisions And Assumptions

1. **function_index.json gap**: The contract defines `pert2func` and `func2pert` as operating directly on functional score matrices (h5ad). The missing `function_index.json` is noted as an implementation gap that T-048/T-049 must resolve; it does not block the contract.

2. **No-hit behavior**: Defined as structured JSON error objects, not exceptions. The `PerturbationNotFound` / `ContextNotFound` / `ProgramNotFound` / `NoMatrixLoaded` error types are deterministic and carry all identifying fields.

3. **Low-confidence detection**: Not hardcoded in the contract. A validation requirement is stated in `m1_demo_cases.yaml`: the implementation task should define a threshold (e.g. `max(|similarity|) < 0.05`).

4. **Reverse query numerical warnings**: The contract accepts warnings in the `warnings` field of `reverse_result`. Implementation must guarantee all top_candidate similarity values are finite.

5. **M1 scope**: Deterministic forward and reverse only. LLM, resolver, proxy retrieval, fuzzy matching, multi-matrix merge, plotting, and Zenodo download are explicitly out of scope.

## Assets Used

All 7 registered assets (A-001 through A-007) were read. Primary extraction used A-001, A-002, A-004, A-005. Cross-checks used A-003, A-006, A-007.

## Forbidden Paths Compliance

- Did not read `2_project_asset/`.
- Did not read `/Users/dudu/Documents/3_Project/8_functional_query`.
- Did not read or cite T024-T040 outputs.
- Did not implement code, analyze matrices, run tests, or produce package artifacts.

## Handoff For Downstream Tasks

- **T-048 / T-049 (M1 implementation)**: Follow `m1_api_contract.yaml` for exact class, method, parameter, return, and error structures. Rebuild or mock `function_index.json` as needed. Do not add resolver/LLM modes.
- **T-052 (M1 validation)**: Use `m1_demo_cases.yaml` DEMO-001 and DEMO-002 pass/fail criteria. Verify no-hit variants and error structures.
- Counter-indications: Do not rely on the old `main.py` entry point. Do not use migrated index JSON files as-is without name-prefix stripping.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-042 contract_and_demo_spec_m1

## Task Goal
Define the M1 API, CLI, demo-case, and error/no-hit contract for the PxFquery Python package using trusted T-007 and T-013 inputs.

## What Was Delivered
T-042 delivered a structured API/CLI contract, concrete forward/reverse demo cases, and a concise human-readable contract summary. It did not implement code, inspect raw project assets, or use T024-T040 outputs as authority.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/m1_api_contract.yaml` | Defines the M1 public API, CLI commands, return shapes, and error/no-hit objects. | T048/T049/T052 should treat this as the contract authority. |
| D-002 | `4_artifact/2_persist/m1_demo_cases.yaml` | Defines exact forward and reverse demo cases plus pass/fail assertions. | T048/T049 should implement against these shapes; T050/T051 should validate them. |
| D-003 | `4_artifact/3_document/m1_contract_summary.md` | Human-readable summary of scope and constraints. | Use as a quick orientation document before reading the YAML files. |

## Supporting Artifacts
- `4_artifact/registry.yaml`
- `5_report/completion.md`
- `5_report/handoff_check_before_exec.md`

## Downstream Use
T048 and T049 should implement deterministic forward/reverse behavior only. T052 should wire package/API/CLI behavior against the YAML contract. LLM resolver, fuzzy matching, plotting, Zenodo download, and full-resource biological claims remain out of M1 scope.

## Known Limits / Risks
This is a contract task, not an implementation task. If a later implementation needs to change a field or threshold, it should create an explicit compatibility note rather than silently diverging from this contract.

## Do Not Read / Do Not Reuse
Do not treat T024-T040 outputs, migrated raw code, or raw `2_project_asset/` files as authority for this contract. Do not use this task as evidence that implementation already runs.

## Recommended Next Reads
1. `4_artifact/2_persist/m1_api_contract.yaml`
2. `4_artifact/2_persist/m1_demo_cases.yaml`
3. `4_artifact/3_document/m1_contract_summary.md`
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
