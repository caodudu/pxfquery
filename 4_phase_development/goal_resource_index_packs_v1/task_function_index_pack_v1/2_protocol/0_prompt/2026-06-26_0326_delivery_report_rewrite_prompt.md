# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:26

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-028 function_index_pack_v1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1`
- Objective:

```text
Create pxfquery-{task_id} function_index.json pack with 91 functions and aliases. Deliver index JSON, validation table, and reports.
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
# Protocol: function_index_pack_v1

## Objective

Produce a `pxfquery-T-028` runtime function-index pack that:

- contains **exactly the 91 function terms** that appear as `var` columns in the upstream H5AD matrices (`cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad`), as observed by the T-026 loader using `anndata.read_h5ad` on the T-021 standard resources bundle; and
- carries, for each function term, a list of **aliases** that downstream query/resolver tasks can use for proxy/match-style retrieval.

The deliverable must be a JSON pack (`function_index.json`) accompanied by a machine-readable validation table that proves every entry in the pack maps to a real loader-observed matrix var term, plus a short downstream-usage note.

If the upstream `function_index.json` (resolved through the T-027 runtime query index pack) is missing or insufficient, T-028 must produce a **corrected** `pxfquery-T-028` local version inside its own `4_artifact/2_persist/` directory and record lineage, source asset id, repairs performed, validation evidence, and downstream consumer guidance. T-028 must not overwrite the upstream T-021/D-004 file.

## Inputs

- A-001 T-026 loader package (D-001) — used to call `load_matrix('cp_func_ad' / 'sh_func_ad' / 'xpr_func_ad')` and read `var_names` at runtime.
- A-002 T-026 loader validation record (D-003) — JSON evidence confirming the upstream matrix var dimensions (n_var = 91). Source of the 91-row function-term list before re-reading from H5AD.
- A-003 T-026 loader validation summary (D-004) — Markdown cross-reference for matrix schemas.
- A-004 T-027 runtime query index pack (D-001) — symlink directory; T-028 reads `function_index.json` from here (or its canonical T-021 target) as the alias seed.
- A-005 T-027 schema report (D-002) — describes the upstream `function_index.json` top-level key shape (`{var_names, meta, aliases}`) for cross-reference.
- A-006 T-021 standard resources bundle (D-004) — canonical read-only source. The `function_index.json` actually consumed is here; it is also symlinked by T-027.
- A-007 T-013 MVP capability contract (D-001) — explicit gap evidence: legacy `function_index.json` is missing or incomplete.
- A-008 T-013 failure / missing capability list (D-005) — official predecessor gap record.
- A-009 T-013 MVP run-through review report (D-006) — Chinese HTML context for the function-index gap.

## Steps

### Step 1 — Verify the 91-term matrix var source

Use the T-026 loader (A-001) to read `cp_func_ad.h5ad`, `sh_func_ad.h5ad`, `xpr_func_ad.h5ad` from the T-021 bundle (A-006) and cross-check `var_names`. Confirm:

- `len(var_names) == 91` for all three matrices.
- The three `var_names` lists are identical (same 91 terms, same order) so a single function index can serve all matrices.

Do **not** hard-code the 91 terms in source code. They must be read from the H5AD files via `anndata.read_h5ad` and the T-026 loader. Write the observed `var_names` to `3_execution/01_var_names.json` as evidence.

### Step 2 — Read upstream function_index.json (when present)

Resolve `function_index.json` through the T-027 runtime index pack (A-004) and read it with `json.load`:

- If present and well-formed (top-level keys include `var_names`, `meta`, `aliases`), capture its `aliases` mapping as the seed.
- If absent or malformed, record the gap with explicit evidence (file existence, `json.load` success/failure, key shape mismatch) and proceed using alias seeds from other legitimate sources (T-021 metadata CSV columns, T-013 evidence notes, conservative default empty list).

Write the upstream-read record to `3_execution/02_upstream_function_index.json`.

### Step 3 — Build pxfquery-T-028 function index pack

Construct `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` with structure:

```json
{
  "version": "pxfquery-T-028",
  "matrix_source": "T-021 standard_resources bundle (D-004)",
  "loader_source": "pxfquery-T-026 matrix loader",
  "n_functions": 91,
  "var_names": [...91 strings...],
  "aliases": {"function_term": ["alias1", "alias2", ...], ...},
  "meta": {
    "built_on": "YYYY-MM-DD",
    "upstream_function_index_status": "present|missing|partial",
    "alias_seed_sources": [...],
    "notes": "..."
  }
}
```

Rules:

- `var_names` MUST be exactly the loader-observed 91 matrix var terms in their original order.
- For every term, `aliases[term]` must be a non-null list. Each term MUST include itself as its primary entry. Additional aliases are accepted from the upstream file when present, or are explicitly empty when absent — never silently dropped.
- Do not invent or guess aliases beyond what the upstream file or accepted metadata sources provide; missing aliases are recorded as empty lists and reported in the validation table.
- Persist the file at `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json`. The directory is the task-versioned pack; the JSON inside is the core artifact.

### Step 4 — Build machine-readable val

...[truncated by CyHex prompt assembler: 6906 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: pxfquery_T028_function_index_pack
  path: 4_artifact/2_persist/pxfquery_T028_function_index/function_index.json
  type: data
  origin_step: 03_build_pack
  purpose: Core T-028 deliverable — validated 91-function index JSON with var_names
    from T-021 H5AD matrices and enriched aliases (self, lowercase, human-readable
    label). Versioned as pxfquery-T-028.
  usable_by: downstream query/resolver tasks in goal_resource_index_packs_v1 DAG
  created: '2026-06-23'
  identity: T-028/D-001
  role: deliverable
  core: true
  lineage_anchor: true
  stars: 5
  notes: '7/7 validation checks pass. 91 function terms, 273 total alias entries.

    Each term carries [uppercase, lowercase, label]. Upstream T-021

    function_index.json is present and served as alias seed.

    '
- id: D-002
  name: step1_var_names_evidence
  path: 3_execution/01_verify/01_var_names.json
  type: support
  origin_step: 01_verify_matrix_var_source
  purpose: Runtime observed var_names from all three T-021 H5AD matrices via anndata.read_h5ad.
    Confirms 91 terms, identical across cp/sh/xpr.
  usable_by: validation and reproducibility audits
  created: '2026-06-23'
  identity: T-028/D-002
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-003
  name: step2_upstream_function_index_record
  path: 3_execution/02_inspect/02_upstream_function_index.json
  type: support
  origin_step: 02_inspect_upstream_function_index
  purpose: Record of the upstream T-021 function_index.json resolved path, top-level
    keys, n_var_names, status, and match with observed matrix var_names.
  usable_by: lineage tracking
  created: '2026-06-23'
  identity: T-028/D-003
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-004
  name: validate_function_index_script
  path: 3_execution/validate_function_index.py
  type: script
  origin_step: 05_validate
  purpose: Python validation driver. Opens all three H5AD matrices, upstream JSON,
    and T-028 pack; runs 7 structured checks. Executable inside pxfquery conda env.
  usable_by: re-validation, reproducibility
  created: '2026-06-23'
  identity: T-028/D-004
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-005
  name: validation_record
  path: 3_execution/05_validate/03_validation.json
  type: support
  origin_step: 05_validate
  purpose: Machine-readable structured validation record with per-check pass/fail,
    evidence, and upstream inspection results.
  usable_by: check AI, human review
  created: '2026-06-23'
  identity: T-028/D-005
  role: support
  stars: 4
  core: false
  lineage_anchor: false
- id: D-006
  name: validation_summary
  path: 3_execution/05_validate/03_validation_summary.md
  type: support
  origin_step: 05_validate
  purpose: Human-readable Markdown validation summary.
  usable_by: human review
  created: '2026-06-23'
  identity: T-028/D-006
  role: support
  stars: 4
  core: false
  lineage_anchor: false
- id: D-007
  name: function_index_validation_table
  path: 4_artifact/5_table/pxfquery_t028_function_index_validation.csv
  type: table
  origin_step: 04_build_validation_table
  purpose: Per-term validation table — 91 rows covering all function terms with alias
    counts, JSON, and status.
  usable_by: human review, manuscript preparation
  created: '2026-06-23'
  identity: T-028/D-007
  role: data
  stars: 4
  core: false
  lineage_anchor: false
- id: D-008
  name: downstream_usage_notes_en
  path: 4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md
  type: document
  origin_step: 06_write_downstream_usage_notes
  purpose: English downstream usage notes for query/resolver tasks.
  usable_by: developers, downstream task config
  created: '2026-06-23'
  identity: T-028/D-008
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-009
  name: downstream_usage_notes_zh
  path: 4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md
  type: document
  origin_step: 06_write_downstream_usage_notes
  purpose: Chinese downstream usage notes for query/resolver tasks.
  usable_by: developers, downstream task config
  created: '2026-06-23'
  identity: T-028/D-009
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-010
  name: execution_report_v20260623
  path: 4_artifact/3_document/execution_report_v20260623.html
  type: document
  origin_step: 07_completion
  purpose: CyHex-required Chinese execution report for the T-028 function-index pack.
  usable_by: delivery QA and human acceptance review
  created: '2026-06-23'
  identity: T-028/D-010
  role: report
  stars: 5
  core: false
  lineage_anchor: false
- id: D-011
  name: result_report_v20260623
  path: 4_artifact/3_document/result_report_v20260623.html
  type: document
  origin_step: 07_completion
  purpose: CyHex-required Chinese result report summarizing the 91-term function index,
    alias coverage, and validation outcome.
  usable_by: delivery QA, human review, and downstream task configuration
  created: '2026-06-23'
  identity: T-028/D-011
  role: report
  stars: 5
  core: false
  lineage_anchor: false
- id: D-012
  name: completion_md
  path: 5_report/completion.md
  type: report
  origin_step: 07_completion
  purpose: Completion report replacing the previous pending stub and summarizing
    validation, deliverables, and downstream use.
  usable_by: delivery QA and downstream task configuration
  created: '2026-06-24'
  identity: T-028/D-012
  role: support
  stars: 4
  core: false
  lineage_anchor: false
- id: D-013
  name: handoff_check_before_exec
  path: 5_report/handoff_check_before_exec.md
  type: report
  origin_step: cyhex_1_2_19_repair
  purpose: Check-to-execute handoff reconstructed from existing task evidence for
    newer CyHex prompt assembly.
  usable_by: future CyHex prompts and delivery QA
  created: '2026-06-24'
  identity: T-028/D-013
  role: support
  stars: 3
  core: false
  lineage_anchor: false
- id: D-014
  name: cyhex_1_2_19_supplement
  path: 5_r

...[truncated by CyHex prompt assembler: 411 chars omitted]
```

### Completion Report
```md
# T-028 Completion: function_index_pack_v1

Generated: 2026-06-23  
CyHex 1.2.19 compatibility supplement added: 2026-06-24

## Result Summary

T-028 produced `pxfquery-T-028`, a validated function-index pack containing exactly the 91 function terms observed in the upstream H5AD matrices.

Core artifact:

- `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json`

## Validation Summary

Latest validation command:

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/validate_function_index.py
```

Result: 7/7 checks pass.

Validation checks:

- `JSON_loads_ok`: T-028 `function_index.json` loads as valid JSON.
- `top_level_keys_present`: 7/7 required keys found.
- `n_functions_equals_91`: `n_functions=91`.
- `var_names_match_matrix`: T-028 `var_names` match matrix-observed `var_names`.
- `var_set_match_all_matrices`: cp/sh/xpr all match.
- `aliases_covers_all_terms`: aliases cover 91/91 terms.
- `alias_nonnull_self_first`: 91/91 terms have a non-null alias list with self first.

## Deliverables

- `4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` — core function index pack.
- `4_artifact/5_table/pxfquery_t028_function_index_validation.csv` — 91-row validation table.
- `3_execution/01_verify/01_var_names.json` — matrix var-name evidence.
- `3_execution/02_inspect/02_upstream_function_index.json` — upstream function-index inspection record.
- `3_execution/05_validate/03_validation.json` — machine-readable validation record.
- `3_execution/05_validate/03_validation_summary.md` — readable validation summary.
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes.md` — English usage notes.
- `4_artifact/2_persist/pxfquery_T028_downstream_usage_notes_zh.md` — Chinese usage notes.
- `4_artifact/3_document/execution_report_v20260623.html` — Chinese execution report.
- `4_artifact/3_document/result_report_v20260623.html` — Chinese result report.
- `4_artifact/registry.yaml` — artifact registry.
- `5_report/process_record.yaml` — CyHex process record refreshed by API.
- `5_report/handoff_check_before_exec.md` — execution handoff for newer CyHex prompts.

## Scope And Integrity

No upstream T-021, T-026, T-027, or T-013 artifact was modified. T-028 is a derived, task-versioned index pack. It is safe to use as a downstream reference asset for function terms and aliases, but it is not a resolver, query engine, or package milestone.

## Downstream Use

Downstream tasks should read:

- `var_names` for the canonical ordered 91-term function list.
- `aliases` for term matching/proxy matching.
- `4_artifact/5_table/pxfquery_t028_function_index_validation.csv` when human-readable per-term audit is needed.

Avoid treating this task as evidence that resolver or LLM functionality is complete.

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
