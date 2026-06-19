# 已知风险清单（截至 2026-04-10）

1. LLM 稳定性风险
- `workspace/report/03_resolver/04_stability/6_llm_resovler_llm_stability_check.md` 显示成功率 6/9。

2. always_llm 延迟风险
- `llm_parse_intent` 仍是主要耗时项。

3. 模式一致性风险
- `always_llm` 与 `hybrid_fast` 在边界问题上可能命中不同。

4. 证据解释风险
- `NOT_FOUND` 与 `PROXY_*` 并存时，外部叙事需严格区分证据质量。

5. 资产组织风险
- 历史 legacy 报告与 suite_runs 并存，若不先看索引容易误判“最新结论”。

6. 路径漂移风险
- 历史文档中仍可能出现旧路径，需以本轮结构为准。
