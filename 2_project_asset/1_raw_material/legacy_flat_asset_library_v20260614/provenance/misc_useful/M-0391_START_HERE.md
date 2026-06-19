# START_HERE

## 必读约束（显著）

- 新对话必须先读 L0：`START_HERE.md` -> `AI_READ_PROTOCOL.md` -> `context/INDEX.md`
- 重大结构变更前后必须登记 checkpoint：`workspace/checkpoints/checkpoints.md`
- 当前事实源目录：`workspace/report/03_resolver/06_suite_runs/`

这是 PxFquery 的最小入口文件（低 token 版本）。

## 每次新对话只先读这 3 个文件

1. `workspace/START_HERE.md`
2. `workspace/AI_READ_PROTOCOL.md`
3. `workspace/context/INDEX.md`

## 当前阶段（2026-04-10）

- 索引构建阶段（2~5）已完成并有报告。
- resolver 已进入双模式阶段：`always_llm` / `hybrid_fast`。
- 主证据报告目录：`workspace/report/03_resolver/06_suite_runs/`。

## 本项目的硬约束

- 不改 `workspace/input/`。
- 不碰 `workspace/output/`（除非你明确要求生成新结果）。
- 代码改动前先根据任务按需读取，不全量扫文档。

## 下一步入口

- 看最新有效报告：`workspace/report/00_index/latest_reports_index.md`
- 看风险与行动：`workspace/report/01_status/known_risks.md`、`workspace/report/01_status/next_execution_order.md`
- 看模块职责：`workspace/report/01_status/core_modules_and_tests.md`

## 工作区主文档

- `workspace/context/deep_dive/01_project_design_workspace.md`
- `workspace/context/deep_dive/02_code_design_workspace.md`

