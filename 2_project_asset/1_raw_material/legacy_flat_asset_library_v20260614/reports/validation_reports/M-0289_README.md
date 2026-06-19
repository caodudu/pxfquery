# Management Notes

- `development.md`：持续开发记录（时间线）
- `todolist.md`：待办与收尾清单
- `logs/`：统一 logger 输出目录（按日期文件命名，如 `pxfquery_2026-04-10.log`）

## Logger 重构状态（2026-04-10）

- 已统一 `pxfquery.core` / `pxfquery.resolver` / `pxfquery.llm` 日志格式。
- 支持 `verbosity=quiet|normal|debug`。
- 支持 `log_enabled`、`log_to_file`、`log_dir`、`log_llm_io` 开关。
- resolver 每次查询会生成 `query_id`，并写入日志与 `resolver_meta.query_id`。
