# Action Prompt
Generated: 2026-06-23 03:52

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
ID: T-019 | Name: bioinformatics_website_hosting_options
Status: active | Executor: hybrid
Objective: 如果做一个生信查询网站发表论文，一般是放在什么网址上。

一般是不是网站需要收费。

1. 请给我调研一下可否挂在github.io上，这样的网站是否也是合规可以发表。可以的话搜几篇论文上这样挂的。
2. 请调研一下github.io网站可否能支持比如链接一个llm api功能的报告呢。因为我的工具想支持接入大模型api。虽然我自己内部提供了。不知道支持不支持类似于一个微型的在线分析还是必须有一个后台服务器
3. 请给我交付一个关乎生信网站从制作到挂出去允许分析网站的过程报告。
4. 请给我一个如果需要一个有前后端网站的一些便宜简单方法。接受付费一两年。不支持特别贵。所以需要你登记价格，有免费方法更好
这些需要分开哦
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/5_phase_translation/goal_pending_g010/task_pending_t019

## Protocol
---
### protocol.md
# Protocol: 生信查询网站交付可行性调研

## Objective
调研 PxFquery 生信查询工具的网站交付方案：包括托管平台选择（GitHub Pages 等）、LLM API 集成可行性、从制作到部署的全流程，以及低成本前后端方案（含价格对比）。按四个独立子任务交付。

## Inputs
- A-001: T-007 PxFquery development state digest — 了解当前 PxFquery 的技术架构（Python 包、索引查询逻辑、LLM 集成现状），作为网站方案设计的参考背景。
- A-002: PxFquery 项目协议 — 提供项目定位（Genes 投稿导向、轻量实用工具）边界，约束网站方案不偏离项目目标。
- A-003: 外部网络资源 — 通过浏览器搜索获取的在线资料、论文链接、GitHub Pages 案例、云服务定价页面等。此资产为动态获取，不预先存在本地。

## Steps
1. 阅读 T-007 核心报告（A-001）和项目协议（A-002），明确 PxFquery 当前技术形态和项目边界。
2. **子任务 1 — GitHub Pages 调研：** 搜索确认 github.io 是否可作为学术论文配套网站；搜索至少 3 篇已将工具网站托管在 github.io 并正式发表的生物信息学/计算生物学论文，提供论文标题、链接、网站 URL。
3. **子任务 2 — LLM API 集成可行性调研：** 调研 GitHub Pages（纯静态托管）是否能对接大模型 API；分析 PxFquery 的 LLM 功能（自然语言→查询转译）在纯静态站点 vs 需要后台服务器的技术边界；给出可行的集成方案（如客户端直接调 API、Serverless 函数、轻量后端等）。
4. **子任务 3 — 生信网站全流程报告：** 输出一份从网站制作到挂出上线的完整流程，覆盖域名、托管、部署、维护等环节，并说明对分析型网站的特殊要求（如 Python 后端运行环境、数据文件托管）。
5. **子任务 4 — 低成本前后端方案调研与价格登记：** 调研并对比至少 3 种方案（如 GitHub Pages + Vercel/Netlify Functions、Railway、Fly.io、阿里云轻量服务器等），登记每种方案的预估年费（1-2 年）、免费额度、优势与限制。
6. 将四个子任务结果分别写入 `4_artifact/2_persist/` 下的独立 markdown 文件。
7. 整合所有调研结果，在 `4_artifact/3_document/` 下生成两份 HTML 报告：`execution_report_v{YYYYMMDD}.html`（执行情况）和 `result_report_v{YYYYMMDD}.html`（面向人类读者的成果展示）。
8. 编写 `5_report/completion.md`，登记交付物到 `4_artifact/registry.yaml`。

## Constraints
- 这是调研任务，不是实施任务。不搭建实际网站，不购买服务，不注册域名。
- 搜索结果必须给出真实可访问的 URL 和可验证的论文信息，不得编造。
- 涉及外部网络搜索的子步骤必须使用浏览器搜索工具，不得仅凭训练数据记忆。
- 价格信息需注明信息来源（URL）和查询日期。
- 不修改项目代码、迁移资产库或已有任务交付物。

## Deliverables
- `4_artifact/2_persist/github_pages_academic_hosting_research.md` — 子任务 1 成果
- `4_artifact/2_persist/llm_api_static_site_feasibility.md` — 子任务 2 成果
- `4_artifact/2_persist/bioinfo_website_deployment_guide.md` — 子任务 3 成果
- `4_artifact/2_persist/low_cost_fullstack_hosting_comparison.md` — 子任务 4 成果
- `4_artifact/3_document/execution_report_vYYYYMMDD.html`
- `4_artifact/3_document/result_report_vYYYYMMDD.html`

## Acceptance
- 每个子任务都有独立的、内容充实的交付文档。
- 论文案例真实可查，每条均有 URL。
- 价格方案覆盖至少 3 个选项，标注来源和查询日期。
- 全流程报告覆盖从代码到上线的完整环节。
- LLM API 集成分析能区分静态站点能做什么、不能做什么，并给出可行的技术路径。

## Assets (3)
- [deliverable] T-007 core observation report — task_digest_pxfquery_development_state
- [deliverable] PxFquery 项目协议 — project_init
- [external] 外部网络搜索资源 — task_pending_t019

## Asset Rules

### Required
- ../../../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/3_document/pxfquery_t007_core_observation_report_v20260618.html — 了解 PxFquery 当前技术架构、查询机制和 LLM 集成现状，作为网站方案设计的技术背景。
- ../../../../../1_project_init/1_project_protocol/ — 明确项目定位（Genes 投稿、轻量工具）边界，确保网站方案不偏离项目目标。
- None — 浏览器搜索获取论文案例、GitHub Pages 案例、云服务定价等。此资产为动态获取。
### Forbidden
- ../../../../../../6_project_deliverable/ — 调研阶段不触碰最终交付物。
- ../../../../../2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ — 迁移资产库为只读来源；本任务不需要读取其中的代码或数据。
### Output
- 4_artifact/2_persist/
- 4_artifact/3_document/

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_pending_g010/task_pending_t019/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_pending_g010/task_pending_t019/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_pending_g010/task_pending_t019/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
