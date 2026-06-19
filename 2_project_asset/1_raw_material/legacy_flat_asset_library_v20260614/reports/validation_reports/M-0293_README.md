# Report Hub

本目录采用“分层目录 + 历史保留”的方式管理日志与报告。

## 阅读顺序

1. `workspace/report/00_index/latest_reports_index.md`
2. `workspace/report/00_index/log_files_index.md`
3. `workspace/report/01_status/core_modules_and_tests.md`
4. `workspace/report/01_status/known_risks.md`
5. `workspace/report/01_status/next_execution_order.md`

## 目录结构

- `00_index/`：总索引与阅读入口
- `01_status/`：模块职责、风险、过时清单、执行顺序、4t质量评估
- `02_steps/`：2~5 步索引构建阶段报告
- `03_resolver/`：resolver 阶段（验证、demo、稳定性、套件）
- `04_management/`：持续开发记录（development / todo）
- `6_llm_resovler_suite_runs/`：旧路径兼容入口（已迁移到 `03_resolver/06_suite_runs/`）

## 说明

- 原始日志保留，不做删减。
- 新增报告优先进入对应子目录，不再堆在根目录。
- logger 重构后的运行日志默认建议放在：`report/04_management/logs/`（按日期命名）。
