# 下一步执行顺序（建议 5 步）

1. 每次看结果先读 `workspace/report/00_index/latest_reports_index.md`。
2. 新跑 resolver 套件统一写入 `workspace/report/03_resolver/06_suite_runs/`。
3. 同一批问题同时跑 `always_llm` 与 `hybrid_fast`，并并列记录。
4. 对 `NOT_FOUND`、`PROXY_*` 场景使用固定解释模板。
5. 文档稳定后再进入源码级算法迭代。
