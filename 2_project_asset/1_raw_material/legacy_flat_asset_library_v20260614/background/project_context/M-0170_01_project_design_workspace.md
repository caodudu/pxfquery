# Project Design (Workspace Canonical)

来源：
- `markdown/PxFquery_project.md`
- `workspace/WORKSPACE_CONVENTION.md`
- `workspace/report/00_index/latest_reports_index.md`

本文件是工作区内“项目叙事与阶段”的主文档，面向人类快速理解与后续扩展。

## 1. 项目目标

PxFquery 是基于 LINCS L1000 预计算功能矩阵的扰动查询系统，服务于科研分析与论文产出。

核心查询：
- 正向（pert2func）：给定 `(B, P)` 推断 `F`
- 反向（func2pert）：给定 `(B, F)` 推荐 `P`

## 2. 当前阶段（2026-04-10）

- 2~5 步索引构建已完成并有报告。
- resolver 已进入双模式：
  - `always_llm`（叙事完整）
  - `hybrid_fast`（容灾/低延迟）
- resolver 主证据目录：`workspace/report/03_resolver/06_suite_runs/`

## 3. 方法叙事（对外）

对外叙事采用“证据邻域整合 + LLM综合解释”：
1. 在 `(B,P)` 周围收集 exact 与 proxy 证据。
2. 遗传扰动在需要时融合 `xpr + sh` 双源证据。
3. 形成一段证据质量明确的科学解释。

备注：`EXACT/PROXY_*` 属于内部检索诊断标签。

## 4. 数据与资产概览

- 输入：`workspace/input/`（只读）
- 产出：`workspace/output/`（table/store/picture）
- 索引：`workspace/output/store/query_index/`
- 报告：`workspace/report/`

## 5. 当前关键风险

- LLM 稳定性波动（见 `workspace/report/03_resolver/04_stability/`）
- always_llm 模式时延偏高
- 双模式边界问题一致性需持续回归

## 6. 推荐阅读顺序

1. `workspace/START_HERE.md`
2. `workspace/context/module_cards/50_risks_and_actions.md`
3. `workspace/report/00_index/latest_reports_index.md`
4. `workspace/report/03_resolver/06_suite_runs/<latest>.md`
