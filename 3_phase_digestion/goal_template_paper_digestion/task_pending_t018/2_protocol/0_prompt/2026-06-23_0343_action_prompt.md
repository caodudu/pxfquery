# Action Prompt
Generated: 2026-06-23 03:43

## 第一步：必读文件（按顺序）
1. ~/.cyhex/app/cyhex_protocol.md          ← CyHex 系统规范（版本验证 + 执行规则）
2. ~/.cyhex/profile.yaml                   ← 全局工具配置（账号/代理/API Key/SSH）

## Project Context
Project: PxFquery (P-012)
Phase: development | Status: active

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

# Goal

## Primary Goal

Build a clean, current PxFquery project that can reuse the valuable legacy assets to support controlled software development, reproducible analysis, and a pragmatic manuscript path.

## Scientific Goal

Position PxFquery as a LINCS-based perturbation-to-function bioinformatics workflow for interpreting drug- and gene-induced functional programs in biological contexts such as cancer cell lines.

## Manuscript Goal

Prepare for a realistic MDPI Genes-style submission by emphasizing a narrow, reproducible functional genomics workflow and a concrete biological case study, rather than presenting PxFquery as a broad AI-agent platform.

This manuscript path is graduation-oriented and journal-fit-oriented. The target is not to build a genuinely high-novelty tool paper or to compete with venues such as Bioinformatics, Nature-family journals, or other high-bar computational biology outlets. The work should look sufficiently substantial in the style of recent Genes papers while remaining practically lightweight, easy to understand, and close to article patterns that Genes has already accepted.

## Migration Goal

Use the T-001 semantic digestion outputs and the T-002 flat migrated asset library as the current bridge from legacy materials into new tasks. Future work should read migrated or registered assets first, then create new project outputs inside this repository.

## Near-Term Goals

1. Finish digestion-phase tasks until legacy assets, source authority, and project rules are clear enough for controlled development.
2. Define the minimal development and analysis work needed to produce manuscript-grade evidence.
3. Use the Genes literature survey to identify accepted paper patterns, workload presentation styles, and understandable result structures that PxFquery can realistically imitate.
4. Keep code, reports, figures, tables, and manuscript materials in the current project structure unless a task explicitly registers an external source.
5. Preserve provenance from legacy assets without reviving legacy directory structures as active protocol.

# Rule

## Source Boundary

- `/Users/dudu/Documents/3_Project/8_functional_query` is a read-only historical source root.
- Do not continue active development, manuscript drafting, analysis reruns, or protocol writing inside legacy Windows-era folders.
- Prefer the migrated flat asset library and task-registered assets before consulting the old source root.
- If a future task must read the old source root directly, it must state why the migrated assets were insufficient and record that reason in its task output.

## Current Workspace Boundary

- New project work belongs under `/Users/dudu/Documents/3_Project/12_PxFquery`.
- Project-level hard rules belong only in `1_project_init/1_project_protocol/`.
- Task-specific decisions, uncertainty, interpretation, strategy, and commentary belong in the relevant task's `4_artifact/` or `5_report/`, not in the project protocol.
- Final deliverable directories should not be touched by digestion tasks unless the task protocol explicitly allows it.

## Legacy Asset Use

- Treat T-001 semantic digestion outputs as the first source for project background, old structure interpretation, and authority rules.
- Treat the T-002 flat asset library as the preferred location for migrated legacy materials.
- Treat old protocol shells, navigation files, checkpoint templates, MOC files, and AI handoff prompts as historical evidence only; do not preserve their structure as current project rules.
- Secret-bearing legacy files must remain redacted or excluded unless a future task explicitly defines a secure handling rule.

## Authority

- For operational truth about old code, indexes, reports, and resolver behavior, use T-001/T-002 records that point to legacy workspace canonical design documents and latest report indexes.
- For manuscript framing, use the migrated Genes strategy and timing analysis materials.
- For later project navigation or staged planning, use later overlay materials only after checking whether T-001/T-002 already digested the same content.
- When current user requirements conflict with old protocol fragments, the current user requirement and current CyHex-managed project structure take priority.

## Development Posture

- Keep scope pragmatic: prioritize working code, traceable evidence, manuscript-grade results, and clear provenance over broad platform claims.
- Do not overstate LLM or agent capabilities; deterministic indexes and evidence retrieval are the safer manuscript foundation.
- Treat Genes as a pragmatic graduation target with a relatively low acceptance bar compared with high-impact bioinformatics venues; do not design tasks as if the project must satisfy Bioinformatics, Nature-family, or top-tier computational biology expectations.
- Favor work that appears substantial in figures, tables, workflow steps, coverage summaries, and case-study evidence while staying lightweight enough to finish quickly.
- Prefer simple, readable, Genes-like manuscript logic over technically ambitious novelty claims.
- When choosing between a clever but hard-to-explain method and a familiar Genes-style analysis pattern, prefer the familiar and explainable pattern unless the task explicitly requires innovation.
- Separate hard constraints from soft working preferences so future tasks can follow rules without inheriting unnecessary commentary.

## Task
ID: T-018 | Name: 生信论文模板拆解
Status: active | Executor: hybrid
Objective: 为t012 的交付物d013里记录的每篇论文建立单独的拆解md讲解。
每一篇单独一个md。要有总的html最后汇总。

不需要先考虑对我项目本身启迪。

而是讲解每一篇的介绍写作逻辑。结果写作逻辑。图的摆放逻辑

注意这是mdpi杂志不是什么好杂志。我们说学习不是说他们多好多科学。而是对齐genes喜欢的风格以及工作量设置。不要用nature或者大sci标准理解它们。

这里其实是开始归纳我们写作的参考模板了

Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_template_paper_digestion/task_pending_t018

## Protocol
---
### protocol.md
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

## Assets (9)
- [deliverable] T012 D-013 priority reading papers HTML — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-006 per-paper record — OHDLF — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-006 per-paper record — CrossMP — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-006 per-paper record — DTVF — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-006 per-paper record — StrainIQ — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-006 per-paper record — GENet — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-001 scope note — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-009 synthesis report — task_genes_bioinformatics_deliverable_catalog
- [deliverable] T012 D-008 phrase library — task_genes_bioinformatics_deliverable_catalog

## Asset Rules

### Required
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_priority_reading_papers_v20260619.html — T012 D-013 priority reading paper list — identifies the 5 papers and their key metrics
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_records_v20260618/GENES-02459_OHDLF_A_Method_for_Selecting_Orthologous_Genes_for_Phylogenetic_Construction_and_Its_App.md — T012 per-paper catalog record for OHDLF
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_records_v20260618/GENES-02981_CrossMP_Enabling_Cross-Modality_Translation_between_Single-Cell_RNA-Seq_and_Single-Cell.md — T012 per-paper catalog record for CrossMP
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_records_v20260618/GENES-02693_DTVF_A_User-Friendly_Tool_for_Virulence_Factor_Prediction_Based_on_ProtT5_and_Deep_Trans.md — T012 per-paper catalog record for DTVF
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_records_v20260618/GENES-04451_StrainIQ_A_Novel_n-Gram-Based_Method_for_Taxonomic_Profiling_of_Human_Microbiota_at_the.md — T012 per-paper catalog record for StrainIQ
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_records_v20260618/GENES-02925_GENet_A_Graph-Based_Model_Leveraging_Histone_Marks_and_Transcription_Factors_for_Enhance.md — T012 per-paper catalog record for GENet
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_deliverable_catalog_scope_note_v20260618.md — T012 scope note — defines artifact-deliverable boundaries and context
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_artifact_deliverable_synthesis_report_v20260618.md — T012 synthesis report — Genes deliverable description patterns and writing style baseline
- ../task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/genes_bioinformatics_deliverable_phrase_library_v20260618.md — T012 phrase library — reusable deliverable description patterns
### Forbidden
- ../../../../8_functional_query/ — Legacy project source root is unrelated to this paper template deconstruction task
- ../../../6_project_deliverable/ — T-018 is digestion-phase paper analysis, not final deliverable production
### Output
- 4_artifact/2_persist/paper_deconstruction/
- 4_artifact/2_persist/
- 5_report/

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_template_paper_digestion/task_pending_t018/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_template_paper_digestion/task_pending_t018/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_template_paper_digestion/task_pending_t018/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
