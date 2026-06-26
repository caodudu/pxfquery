# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:19

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-056 02_stress_query_scenario_inventory
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory`
- Objective:

```text
Abstract a future stress-test scenario inventory from migrated materials and existing digestion results, focusing on complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, and difficult perturbation/cell-line/function combinations.

Deliverables: 4_artifact/2_persist/stress_query_scenario_inventory_vYYYYMMDD.md and 4_artifact/5_table/stress_query_scenario_table_vYYYYMMDD.csv.

Reference T-007 because it explains forward/reverse query intent, resolver/index status, and current development-state boundaries. Use T-041 only as a may input if it is done; if T-041 is still active or unavailable, omit it completely and proceed from T-007.

Important constraints: deliver stress-test scenarios and rationale only, not implementation; do not run large tests; do not treat old scripts as current acceptance criteria.
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
# T-056 02_stress_query_scenario_inventory — Protocol

## Objective

Abstract a future stress-test scenario inventory from migrated materials and T-007 digestion results. The inventory must cover: complex queries, strict queries, boundary queries, no-hit (NOT_FOUND) behavior, overly broad results, proxy/exact matching edge cases, and difficult perturbation/cell-line/function combinations. Deliver scenarios and rationale only — not implementation or test execution.

## Position In Project

This is a digestion-phase task under goal_legacy_stress_test_asset_digestion. It precedes any actual stress-test execution tasks. It consumes T-007's development-state understanding to derive what a future stress-test framework must cover, without running tests or building infrastructure.

T-041 (legacy_source_digest_for_m1) is still active; omitted per constraint.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Forward/reverse query mechanism, resolver modes, index gaps — foundational for scenario categories |
| A-002 | T-007/D-005 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps/risks directly inform stress-test pattern categories |
| A-003 | T-007/D-006 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Concrete query examples and do-not-do boundaries |
| A-004 | T-007/D-003 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Module coverage verification for scenario completeness |
| A-005 | T-007/D-004 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Historical pass/fail patterns as scenario data points |
| A-006 | T-007/M-0257 | reports/validation_reports/M-0257_6_llm_resovler_forward_matrix.md | 7/7 deterministic EXACT/PROXY test cases as scenario templates |
| A-007 | T-007/M-0243 | reports/validation_reports/M-0243_known_risks.md | LLM stability risks, mode inconsistency, NOT_FOUND+PROXY boundaries |
| A-008 | T-007/M-0239 | reports/validation_reports/M-0239_latest_reports_index.md | Authority rules for validation conflict resolution |

## Execution Steps

1. Read all registered input assets (A-001 through A-008) to extract query semantics, resolver behavior, known edge cases, and validation evidence.
2. Derive and categorize stress-test scenarios covering these dimensions:
   - **Complex queries**: multi-gene, multi-drug, combined perturbation+context queries that stress resolver intent parsing and evidence bundling
   - **Strict queries**: exact-match-only cases that should produce EXACT hits; cases where proxy fallback should be explicitly disallowed
   - **Boundary queries**: cell-line not in index, drug not in index, function alias edge cases, empty/partial perturbation strings
   - **No-hit behavior**: queries expected to produce NOT_FOUND — generic drug descriptions (EGFR inhibitor), unknown cell lines, impossible gene+context combinations
   - **Overly broad results**: queries likely to produce many proxy hits or ambiguous evidence bundles (common drugs like DMSO, pan-cancer queries)
   - **Proxy/exact matching**: cases where EXACT vs PROXY_PERT vs PROXY_CELL vs PROXY_BOTH must be explicitly distinguished and the boundary tested
   - **Difficult combos**: perturbation+cell-line+function triples that are biologically questionable, conflict across indexes, or fail in historical reports
   - **LLM mode cross-checks**: scenarios where always_llm vs hybrid_fast vs deterministic produce different results
   - **Missing/partial index**: function_index.json gap scenarios, partial neighbor failures
3. For each scenario, record: unique ID, category, query parameters (forward/reverse, perturbation, context, function intent), expected resolver hit level, expected pass/fail, rationale citing specific source evidence, and notes on historical validation status.
4. Compile the narrative inventory document from step 3 results.
5. Compile the tabular CSV from the same scenario records.
6. Register outputs in 4_artifact/registry.yaml.

## Constraints

- Deliver stress-test scenarios and rationale only. Do not implement test code, run queries, or build test infrastructure.
- Do not reference T-041; it is still active and not available.
- Do not read old legacy root scripts or run them.
- Base all scenario derivation on the 8 registered input assets only.
- Keep scenarios grounded in T-007 evidence (validation reports, gaps, known risks). Do not invent hypothetical scenarios without documented precedent.
- Use the latest-reports-index (A-008) authority rules when historical validation reports conflict.

## Forbidden

- No test execution or query runs.
- No modification of predecessor artifacts or project assets.
- No creation of package code or test scripts.
- No reading of T-041 outputs.
- No web search for external information.

## Web Search Allowance

Allowed: no
Reason: All required information is a

...[truncated by CyHex prompt assembler: 1631 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: D-001
    name: stress_query_scenario_inventory
    type: document
    description: "Narrative inventory of 29 stress-test scenarios across 9 dimensions, grounded in T-007 digestion evidence"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md"
    status: active
    created: "2026-06-24"
    stars: 5
    notes: "Core deliverable. Covers all 9 scenario dimensions with evidence traceback to registered T-007 assets"

  - id: D-002
    name: stress_query_scenario_table
    type: table
    description: "Tabular CSV of 29 stress-test scenarios with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/5_table/stress_query_scenario_table_v20260624.csv"
    status: active
    created: "2026-06-24"
    stars: 5
    notes: "One row per scenario; parseable by standard CSV tools. Machine-readable version of D-001"

  - id: D-003
    name: execution_report
    type: document
    description: "HTML execution report documenting process, input assets, and constraints observed"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/3_document/execution_report_v20260624.html"
    status: active
    created: "2026-06-24"
    stars: 2
    notes: "Human-readable execution trace for delivery review"

  - id: D-004
    name: result_report
    type: document
    description: "HTML result report summarizing scenario coverage, acceptance criteria, and notable items"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/3_document/result_report_v20260624.html"
    status: active
    created: "2026-06-24"
    stars: 3
    notes: "Human-readable result summary for downstream task planning"

```

### Completion Report
```md
# Completion

Task: T-056 02_stress_query_scenario_inventory
Generated: 2026-06-24
Agent: opencode (AGT-002)

## Summary

Executed the task protocol successfully. Delivered 29 stress-test scenarios derived from 8 registered T-007 input assets (A-001 through A-008).

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Narrative inventory | `4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md` | delivered |
| Tabular CSV | `4_artifact/5_table/stress_query_scenario_table_v20260624.csv` | delivered |
| Artifact registry | `4_artifact/registry.yaml` | updated |

## Coverage

All 9 scenario dimensions covered with at least 2 scenarios each (29 total):

| Dimension | Scenario IDs | Count |
|---|---|---|
| Complex queries | SC-001, SC-002, SC-003 | 3 |
| Strict queries | SC-004, SC-005, SC-006 | 3 |
| Boundary queries | SC-007, SC-008, SC-009, SC-010 | 4 |
| No-hit behavior | SC-011, SC-012, SC-013 | 3 |
| Overly broad results | SC-014, SC-015, SC-016 | 3 |
| Proxy/exact matching | SC-017, SC-018, SC-019, SC-020 | 4 |
| Difficult combos | SC-021, SC-022, SC-023 | 3 |
| LLM mode cross-checks | SC-024, SC-025, SC-026 | 3 |
| Missing/partial index | SC-027, SC-028, SC-029 | 3 |

## Acceptance Criteria Verification

- [x] Covers all 9 scenario dimensions
- [x] Each scenario has unique ID, category, query parameters, expected hit level, expected result, rationale citing source evidence
- [x] CSV columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- [x] Narrative explains each scenario's motivation with evidence traceback
- [x] No implementation code, test scripts, or query execution results delivered
- [x] Outputs registered in `4_artifact/registry.yaml`

## Constraints Observed

- No test execution or query runs performed
- No modification of predecessor artifacts or project assets
- No package code or test scripts created
- No T-041 outputs read or referenced
- All scenario derivation grounded in registered T-007 evidence (A-001 through A-008)
- Used latest-reports-index authority rules (A-008) when applicable

## Notes

- 4 scenarios marked as speculative or borderline (SC-014, SC-015, SC-016, SC-029) where the evidence supports the category but exact behavior cannot be predicted from T-007 reports alone
- 2 scenarios (SC-011, SC-012) flagged as mode-dependent with expected_result=PASS or FAIL to document known inconsistency
- 1 scenario (SC-009, empty perturbation) has no direct T-007 precedent but is derived from documented gaps (A-002 §1-4, unverified runnable state)

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-056 02_stress_query_scenario_inventory

## Task Goal

Abstract a future stress-test scenario inventory from migrated T-007 materials. Cover 9 dimensions: complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index. Deliver rationale only — no implementation.

## What Was Delivered

- Narrative inventory (29 scenarios) with full evidence traceback to registered T-007 assets
- Tabular CSV (29 rows) with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- Artifact registry updated with D-001, D-002, D-003, D-004
- Delivery QA reports (execution_report, result_report, delivery_qa)

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | Complete narrative of all 29 scenarios with rationale | Read first to understand scenario motivation and evidence basis |
| D-002 | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | Machine-parseable scenario table | Load as CSV in test framework; select rows by category for focused test suites |

## Supporting Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-003 | 4_artifact/3_document/execution_report_v20260624.html | Documents execution process | Human review of what was done |
| D-004 | 4_artifact/3_document/result_report_v20260624.html | Summarizes coverage and acceptance | Human review of output completeness |

## Downstream Use

A future stress-test execution task (e.g., T-057 or later) should:
1. Read D-001 for narrative context and evidence traces
2. Parse D-002 CSV to select scenario rows by category
3. Implement test harness code that exercises pxfquery forward/reverse query API with each scenario's perturbation/context/function parameters
4. Compare actual resolver hit levels against expected_hit_level and expected_result
5. Report deviations as test failures or documentation gaps

## Known Limits / Risks

- 4 scenarios (SC-014, SC-015, SC-016, SC-029) are marked speculative — exact behavior may differ from prediction
- 2 scenarios (SC-011, SC-012) are mode-dependent (LLM mode changes expected result)
- 1 scenario (SC-009, empty perturbation) has no direct T-007 precedent — derived from documented gaps
- Scenarios assume current pxfquery development state as of T-007 (2026-06-17); code changes since then may affect expected results

## Do Not Read / Do Not Reuse

- T-041 outputs — explicitly omitted per protocol constraint
- Old legacy root scripts — not current acceptance criteria
- 3_execution/ contents — empty for this task

## Recommended Next Reads

1. D-001 (narrative inventory) — full scenario rationale
2. D-002 (CSV table) — structured scenario data
3. A-001/A-002 (T-007 source assets) if deeper evidence traceback needed

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
