# 下一里程碑边界建议

生成日期：2026-06-25  
任务：T-065 `m1_vs_delivery_anchor_review`

## 推荐边界

建议把 M1 明确命名为 **deterministic kernel/substrate**，并把下一阶段拆为两个边界：

1. **M2：current-resource evidence-routing package milestone**  
   目标是证明当前包能在标准资源或批准继承资源上完成 evidence-aware routing，而不是继续扩大 resolver/LLM 范围。

2. **M3：resolver/LLM user-facing milestone**  
   目标是在 M2 的路由和元数据契约稳定后，再交付自然语言/半结构化 resolver、LLM parse/summary 和完整 demo catalog。

## M2 必须完成后才能称为完整包里程碑

- 加载或批准继承 T-021 标准资源：cp/sh/xpr h5ad 矩阵、查询索引、metadata 表和 `function_index.json`。
- 跑通 exact forward、exact reverse、no-hit、context-missing、至少一个 proxy route。
- 每个结果输出 T-064 八字段元数据：`route_type`、`query_context`、`perturbation_resolution`、`function_response`、`confidence`、`proxy_chain`、`diagnostics`、`suggestions`。
- 对 no-hit 证明不会把低置信 fuzzy token 报成 found。
- 对 reverse 查询记录 function mapping、排序数值 sanity、warning 和 low-confidence 行为。

## M3 必须完成后才能称为 resolver/LLM 里程碑

- 自然语言输入和半结构化输入都能生成结构化 parse。
- Parse 记录包含 T-063 要求字段，包括 missing fields、ambiguity flags、parse confidence、parse method、AI route 和 fallback 状态。
- 使用 CyHex 注册 AI route 和 `deepseek-v4-pro` 或明确批准的替代模型，产生 parse 或 summary 调用证据。
- 覆盖 T-063 demo catalog：exact forward、exact reverse、proxy forward、proxy reverse、not-found、ambiguous NL、semi-structured、LLM unavailable fallback、metadata inspection。
- LLM 只能辅助解析、归一化和总结；不能制造生物学证据或把低置信实体改成 found。

## 可以作为文档化缺口保留的事项

- wheel/distribution build 可在内部开发期后移，只要 editable install 已满足当前工程运行。
- 大规模多场景 stress test 可在 M2 路由契约稳定后扩展。
- 复杂多 perturbation、多 context 聚合可以作为后续分析功能，不应阻塞 M2 的单查询路由契约。

## 不建议的边界

- 不建议把 M2 定义为“更多 synthetic fixture demo”。这会继续回避标准资源和 route metadata。
- 不建议把 M3 的 LLM 能力降级为 endpoint connectivity 或 prompt template 存在。
- 不建议把 proxy route 标为 optional，除非有明确用户批准和后续里程碑记录。
