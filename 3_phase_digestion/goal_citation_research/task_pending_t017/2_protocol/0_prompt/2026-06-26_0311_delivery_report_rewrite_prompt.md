# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:11

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-017 mdpi引用格式
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_citation_research/task_pending_t017`
- Objective:

```text
搜一下mdpi的写作引用格式上哪一种。
可以结合网络搜索，

参考范文的引用区域。

以及wjy的word

但是最后要确定是具体哪一种，因为我需要在zenoto里用

如果是常规模式，我在zenoto里插入

如果不是，帮我搜到下载相关引用格式文件。我忘记一般引用是什么格式文件了
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
# Protocol: MDPI Citation Format Investigation

## Objective
Determine the exact citation/reference format used by MDPI and Genes journal, confirm it is a standard format directly installable in Zotero, and identify the official CSL file and download location. If it is not a standard Zotero-supported style, locate and download the required citation format file.

## Inputs
- A-001: T-015 MDPI submission rules outputs — Prior MDPI submission rules summary; use to cross-reference citation rules mentioned in the official MDPI author guide.
- A-002: WXY manuscript_v8.docx — Published/reviewed Genes submission example; inspect its in-text citation format and reference list to confirm the style used in practice.
- A-003: MDPI Reference List and Citations Style Guide (official) — The authoritative source for MDPI's official citation format. Identifies "Multidisciplinary Digital Publishing Institute" as the Zotero style.
- A-004: MDPI CSL file — The official CSL definition file for the MDPI citation style. Use to verify style details and make the file available for local download if needed.
- A-005: Zotero Style Repository page for MDPI — Confirms the CSL style is in the official Zotero repository and directly installable.
- A-006: Web search results — Supplementary evidence to cross-validate the Zotero style name and CSL download source.

## Steps
1. Read the official MDPI reference/citation guide (A-003) to identify the official citation style requirements: in-text citation format, reference list format, and the recommended Zotero style name.
2. Inspect the WXY manuscript (A-002) reference section and in-text citations to confirm the practical citation format used in a real Genes submission.
3. Search online to confirm the Zotero CSL style name: "Multidisciplinary Digital Publishing Institute".
4. Locate and verify the official CSL file (A-004) from the citation-style-language GitHub repository. Download a local copy to `4_artifact/6_archive/` for offline access.
5. Document the exact steps to install the MDPI citation style in Zotero.
6. Produce a concise findings report in Markdown format.

## Constraints
- Do not modify the original WXY manuscript file.
- Distinguish between official MDPI rules (from mdpi.com/authors/references) and practical observations from the example manuscript.
- The CSL file must be the official version from the citation-style-language/styles repository, not a user-modified fork.
- If the style is a standard Zotero repository style, the answer should be: "MDPI uses the 'Multidisciplinary Digital Publishing Institute' style, which is a numbered (ACS-based) citation style. In Zotero, go to Preferences → Cite → Styles → Get additional styles, search 'Multidisciplinary Digital Publishing Institute', and install. It uses [1], [2] bracket numbering in text."

## Deliverables
- MDPI citation format investigation report: `{taskPath}/4_artifact/2_persist/mdpi_citation_format_findings_v20260623.md`
- Downloaded MDPI CSL file (if needed for offline install): `{taskPath}/4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl`

## Acceptance
- The report clearly states the exact Zotero style name.
- The in-text citation format (numbered brackets [1], [2]) and reference list format are documented.
- The method to install the style in Zotero is explicitly described.
- The WXY manuscript reference format serves as a practical confirmation example.
```

### Artifact Registry
```yaml
artifacts:
- id: ART-001
  identity: T-017/ART-001
  name: MDPI citation format findings report
  type: document
  role: report
  core: false
  lineage_anchor: false
  path: 4_artifact/2_persist/mdpi_citation_format_findings_v20260623.md
  location: local
  source: generated
  produced_by: T-017
  stars: 5
  description: Comprehensive Markdown report on MDPI citation format investigation
    results.
  notes: Final deliverable per protocol §Deliverables.
  pinned: true
  pinned_at: '2026-06-23T04:06:48'
- id: ART-002
  identity: T-017/ART-002
  name: MDPI CSL style file
  type: archive
  role: data
  core: false
  lineage_anchor: false
  path: 4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl
  location: local
  source: generated
  produced_by: T-017
  stars: 4
  size: 9534
  description: Official MDPI CSL citation style file downloaded from citation-style-language/styles
    GitHub repository.
  notes: For offline Zotero installation. 263 lines, 9,534 bytes.
  pinned: true
  pinned_at: '2026-06-23T04:04:43'
- id: ART-003
  identity: T-017/ART-003
  name: execution_report
  type: report
  role: report
  core: false
  lineage_anchor: false
  path: 4_artifact/3_document/execution_report_v20260623.html
  location: local
  source: generated
  produced_by: T-017
  stars: 5
  description: Step-by-step execution report in HTML format.
  notes: MDPI引用格式调查
- id: ART-004
  identity: T-017/ART-004
  name: result_report
  type: report
  role: report
  core: false
  lineage_anchor: false
  path: 4_artifact/3_document/result_report_v20260623.html
  location: local
  source: generated
  produced_by: T-017
  stars: 5
  description: Chinese HTML result report with findings, examples, and Zotero install
    guide.
  notes: Human-facing result dashboard.  人类使用教程
  pinned: true
  pinned_at: '2026-06-23T04:07:12'

```

### Completion Report
```md
# T-017 Completion Report

**Date:** 2026-06-23  
**Status:** Completed, awaiting human acceptance  
**Task:** MDPI citation format investigation (mdpi引用格式)

## Result

T-017 execution completed. All 6 protocol steps executed successfully.

### Key Finding
MDPI/Genes uses the **"Multidisciplinary Digital Publishing Institute"** Zotero citation style, which is a **numbered (ACS-based) format** with in-text citations as `[1], [2], [3]`. This is a standard Zotero repository style that can be installed directly from within Zotero without manual CSL download.

### Zotero Installation
Preferences → Cite → Get additional styles → Search "Multidisciplinary Digital Publishing Institute" → Install

## Outputs

| File | Type | Size | Status |
|------|------|------|--------|
| `4_artifact/2_persist/mdpi_citation_format_findings_v20260623.md` | Markdown report | ~3.5 KB | ✓ |
| `4_artifact/3_document/execution_report_v20260623.html` | Execution report | ~4 KB | ✓ |
| `4_artifact/3_document/result_report_v20260623.html` | Result report (Chinese) | ~5 KB | ✓ |
| `4_artifact/6_archive/multidisciplinary-digital-publishing-institute.csl` | CSL file | 9,534 B | ✓ |

## Execution Steps

1. **Read MDPI official guide** (A-003) — ✓ Retrieved from https://www.mdpi.com/authors/references
2. **Inspect WXY manuscript** (A-002) — ✓ Extracted 15 reference entries from 44MB .docx via XML parsing
3. **Search confirm Zotero style** (A-005, A-006) — ✓ Confirmed "Multidisciplinary Digital Publishing Institute"
4. **Download CSL file** (A-004) — ✓ 9,534 bytes from raw.githubusercontent.com
5. **Document Zotero install** — ✓ Two methods documented
6. **Produce findings report** — ✓ Markdown + HTML reports generated

## Verification

- Official MDPI guide (A-003) confirms Zotero as recommended tool and numbered citation format
- WXY manuscript (A-002) uses identical `[1]`, `[2]` numbering and author-semicolon format matching MDPI official style
- Zotero repository (A-005) returns status 200 for the style search
- CSL file (A-004) successfully downloaded with 263 lines of valid XML

## Limits

- WXY manuscript is one example; other Genes papers may have slight formatting differences (e.g., DOI inclusion)
- A-003 (mdpi.com) returned 403 to direct HTTP but was successfully fetched via webfetch/browser
- Step 2 required fallback from python-docx to raw XML parsing due to conda module availability

## Residual Issues

No blocking issues.
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
