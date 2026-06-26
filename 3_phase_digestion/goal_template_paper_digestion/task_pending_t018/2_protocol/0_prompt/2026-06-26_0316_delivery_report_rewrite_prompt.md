# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:16

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-018 生信论文模板拆解
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_pending_t018`
- Objective:

```text
为t012 的交付物d013里记录的每篇论文建立单独的拆解md讲解。
每一篇单独一个md。要有总的html最后汇总。

不需要先考虑对我项目本身启迪。

而是讲解每一篇的介绍写作逻辑。结果写作逻辑。图的摆放逻辑

注意这是mdpi杂志不是什么好杂志。我们说学习不是说他们多好多科学。而是对齐genes喜欢的风格以及工作量设置。不要用nature或者大sci标准理解它们。

这里其实是开始归纳我们写作的参考模板了

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
# Protocol: 生信论文模板拆解

## Objective
对 T-012 交付物 D-013 记录的 5 篇 Genes 生信论文（GENES-02459 OHDLF、GENES-02981 CrossMP、GENES-02693 DTVF、GENES-04451 StrainIQ、GENES-02925 GENet），逐篇拆解其介绍写作逻辑、结果写作逻辑和图摆放逻辑，为 PxFquery 写作提供 Genes 风格的参考模板。目标是对齐 Genes 喜欢的风格和工作量设置，不做 Nature/大 SCI 标准的评判。

## Inputs
- A-001: T012 D-013 重点阅读论文记录 HTML — 获取 5 篇论文的基本信息、DOI、结构指标和后续重点方向
- A-002: T012 D-006 逐篇记录 — OHDLF 的 T012 catalog 记录，含交付物归类、验证证据和表达模式
- A-003: T012 D-006 逐篇记录 — CrossMP 的 T012 catalog 记录
- A-004: T012 D-006 逐篇记录 — DTVF 的 T012 catalog 记录
- A-005: T012 D-006 逐篇记录 — StrainIQ 的 T012 catalog 记录
- A-006: T012 D-006 逐篇记录 — GENet 的 T012 catalog 记录
- A-007: T012 D-001 范围说明 — 了解 T012 的 artifact-deliverable 筛选标准和范围边界
- A-008: T012 D-009 综合分析报告 — 了解 Genes 论文交付物描述模式和写作风格基线
- A-009: T012 D-008 短语库 — 可复用的交付物描述表达模式
- A-010: 原始论文网页 — 从 MDPI 官网逐篇阅读原文，提取介绍/结果/图摆放逻辑

## Steps
1. 读取 T012 D-013 确定 5 篇论文的列表、DOI、各篇结构指标和后续重点。
2. 读取 T012 D-006 中对应 5 篇的逐篇记录（含交付物归类、验证证据、限制和表达模式）。
3. 读取 T012 D-001 和 D-009 确认 Genes 论文交付物描述的总体风格基线。
4. 对每一篇论文，通过 MDPI 官网打开原文，提取：
   - 介绍写作逻辑：如何引出问题、如何构建 gap、如何引导到自己的交付物。
   - 结果写作逻辑：段落结构、每段讲什么、如何安排子结果顺序、如何用图表支撑每个结论。
   - 图摆放逻辑：图与结果段落的对应关系、图类型（流程图/性能表/案例展示/截图等）、每张图回答什么。
5. 每篇写一个独立的中文 MD 拆解文件，按统一模板记录介绍逻辑、结果逻辑和图逻辑。
6. 编写总 HTML 汇总页面，包含 5 篇的交叉对比表、写作模式归纳和 Genes 风格要点总结。
7. 将每篇拆解 MD 放入 4_artifact/2_persist/paper_deconstruction/。
8. 将总 HTML 汇总页面放入 4_artifact/2_persist/。

## Constraints
- 每篇拆解 MD 包含三个核心章节：介绍写作逻辑、结果写作逻辑、图摆放逻辑。
- 拆解目标是"学习 Genes 喜欢的叙述方式"，不是评判论文科学质量或对 PxFquery 的直接启示。
- 不要用 Nature/Bioinformatics 的标准去批评 MDPI 论文。接受 Genes 的叙述惯性，提炼可模仿的模式。
- 只处理 D-013 明确的 5 篇论文，不扩展到 T012 的 103 篇全集。
- 图摆放逻辑需要说明每张图回答什么、放在哪个段落之后、图类型和叙述配合方式。
- 每篇拆解末尾附"可模仿要点"小节，提炼该篇最值得 PxFquery 对标的部分。

## Deliverables
- 5 篇论文各自的拆解 MD：`4_artifact/2_persist/paper_deconstruction/{GENES-ID}_{deliverable_name}_template_deconstruction.md`
- 总 HTML 汇总：`4_artifact/2_persist/paper_deconstruction_summary_v20260623.html`
- 完成报告：`5_report/completion.md`

## Acceptance
- 5 篇拆解 MD 完整，每篇都包含介绍、结果、图三个逻辑分析。
- 总 HTML 汇总包含交叉对比表和 Genes 风格要点归纳。
- 分析语气是"学习模板"而非"评判科学水平"。
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: GENES-02459_OHDLF_template_deconstruction.md
  path: 4_artifact/2_persist/paper_deconstruction/GENES-02459_OHDLF_template_deconstruction.md
  type: persist
  origin_step: 05_write_deconstruction_md
  purpose: OHDLF论文的介绍/结果/图摆放逻辑拆解
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 4
  identity: T-018/D-001
  role: support
  core: true
  lineage_anchor: true
- id: D-002
  name: GENES-02981_CrossMP_template_deconstruction.md
  path: 4_artifact/2_persist/paper_deconstruction/GENES-02981_CrossMP_template_deconstruction.md
  type: persist
  origin_step: 05_write_deconstruction_md
  purpose: CrossMP论文的介绍/结果/图摆放逻辑拆解
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 4
  identity: T-018/D-002
  role: support
  core: true
  lineage_anchor: true
- id: D-003
  name: GENES-02693_DTVF_template_deconstruction.md
  path: 4_artifact/2_persist/paper_deconstruction/GENES-02693_DTVF_template_deconstruction.md
  type: persist
  origin_step: 05_write_deconstruction_md
  purpose: DTVF论文的介绍/结果/图摆放逻辑拆解
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 4
  identity: T-018/D-003
  role: support
  core: true
  lineage_anchor: true
- id: D-004
  name: GENES-04451_StrainIQ_template_deconstruction.md
  path: 4_artifact/2_persist/paper_deconstruction/GENES-04451_StrainIQ_template_deconstruction.md
  type: persist
  origin_step: 05_write_deconstruction_md
  purpose: StrainIQ论文的介绍/结果/图摆放逻辑拆解
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 4
  identity: T-018/D-004
  role: support
  core: true
  lineage_anchor: true
- id: D-005
  name: GENES-02925_GENet_template_deconstruction.md
  path: 4_artifact/2_persist/paper_deconstruction/GENES-02925_GENet_template_deconstruction.md
  type: persist
  origin_step: 05_write_deconstruction_md
  purpose: GENet论文的介绍/结果/图摆放逻辑拆解
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 4
  identity: T-018/D-005
  role: support
  core: true
  lineage_anchor: true
- id: D-006
  name: paper_deconstruction_summary_v20260623.html
  path: 4_artifact/2_persist/paper_deconstruction_summary_v20260623.html
  type: persist
  origin_step: 06_write_summary_html
  purpose: 5篇论文拆解的总HTML汇总，含交叉对比表和Genes风格要点
  usable_by: task_genes_manuscript_preparation
  created: '2026-06-23'
  stars: 5
  identity: T-018/D-006
  role: report
  core: true
  lineage_anchor: true
  notes: 五篇Genes论文拆
  pinned: true
  pinned_at: '2026-06-23T04:10:35'
- id: D-007
  name: execution_report_v20260623.html
  path: 4_artifact/3_document/execution_report_v20260623.html
  type: document
  origin_step: 09_generate_execution_report
  purpose: 执行情况报告
  created: '2026-06-23'
  stars: 5
  identity: T-018/D-007
  role: report
  core: false
  lineage_anchor: false
  pinned: true
  pinned_at: '2026-06-23T04:09:43'
  notes: 生信论文模板拆解执行情况说明
- id: D-008
  name: result_report_v20260623.html
  path: 4_artifact/3_document/result_report_v20260623.html
  type: document
  origin_step: 09_generate_result_report
  purpose: 成果展示报告（面向人类阅读者）
  created: '2026-06-23'
  stars: 5
  identity: T-018/D-008
  role: report
  core: false
  lineage_anchor: false
core_artifact_id: D-006

```

### Completion Report
```md
# T-018 completion report

Completed: 2026-06-23

## Result

T-018 对 T-012 D-013 中 5 篇 Genes 生信论文逐篇拆解了介绍写作逻辑、结果写作逻辑和图摆放逻辑，输出 5 篇独立 MD 拆解文件和 1 个总 HTML 汇总。

## Per-Paper Deconstructions

| 论文 | 交付类型 | 关键发现 |
|------|---------|---------|
| OHDLF (GENES-02459) | workflow/pipeline | 最短 Intro(731字)，案例应用驱动双线叙事 |
| CrossMP (GENES-02981) | web portal | 以可及性缺口为 Gap；missing_full_text，基于模式分析 |
| DTVF (GENES-02693) | web server | 经典六段式 Results；超参数优化加分，但无代码仓库 |
| StrainIQ (GENES-04451) | software tool | 78段 Results + 三级验证体系，感知工作量最大 |
| GENet (GENES-02925) | software tool | 最长 Intro(2003字)，graph model 需更多背景铺垫 |

## Genes Pattern Summary

1. 题名固定格式："工具名: 功能 + 应用场景"
2. Intro 700-2000字，从具体生物学痛点切入
3. Results 短段落密集推进，每段配图表引用
4. 图4-6张：架构图(图1) + 性能图 + 对比表 + 案例/UI
5. 固定交付描述框架：用户输入→处理→输出→验证→获取
6. Discussion 中主动承认弱点

## Known Limitation

MDPI 官网使用 Akamai 反爬保护，无法自动化获取全文 HTML。Step 4 基于 T012 全文结构统计 + catalog 证据完成拆解。CrossMP 无本地 PDF，拆解基于 portal 型论文通用模式，深度不如其余 4 篇。

## Outputs

- 5 篇拆解 MD: `4_artifact/2_persist/paper_deconstruction/`
- 总 HTML 汇总: `4_artifact/2_persist/paper_deconstruction_summary_v20260623.html`
- 执行报告: `4_artifact/3_document/execution_report_v20260623.html`
- 成果报告: `4_artifact/3_document/result_report_v20260623.html`
- 登记: `4_artifact/registry.yaml`
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
