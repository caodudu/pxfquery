# M1 与交付锚点差距复核报告

生成日期：2026-06-25  
任务：T-065 `m1_vs_delivery_anchor_review`

## 总体结论

M1 应分类为：**deterministic kernel/substrate（确定性内核/底座）**。

理由是：M1 已经证明 `pxfquery` 0.1.0 能以 editable install 方式安装，提供 `forward`、`reverse`、`info` CLI，并在合成 fixture 上跑通一个正向 exact 示例、一个反向 exact 示例和若干确定性错误处理。但注册证据没有证明 resolver 入口、LLM 解析/总结、proxy 路由、transfer/suggestion、T-064 八字段证据元数据契约，也没有证明 T-021 标准矩阵和索引资源在当前包中可加载。因此，M1 不能被称为完整算法包里程碑，只能作为后续包能力的确定性内核。

## 状态统计

partial: 10
downgraded: 4
deferred-not-approved: 4
evidence-insufficient: 4


## M1 已交付的有效内容

- 包装层：`pxfquery` 0.1.0、`pip install -e .`、CLI 入口和 help/info 可用。
- 正向内核：`EGFR` / `A549` / `xpr` 合成 fixture 查询返回 `found:true`，CLI 输出 JSON。
- 反向内核：`HALLMARK_APOPTOSIS` activate + `HALLMARK_MYC_TARGETS_V1` suppress / `A549` 返回候选扰动排序。
- 基础错误处理：未知基因 token 可返回 `PerturbationNotFound`；反向验证列出若干结构化错误类。

## 主要未交付或未充分证明的锚点能力

- 标准资源兼容性：M1 明确使用 `M1FixtureLoader` 和 synthetic fixture，未证明 T-021 的 cp/sh/xpr h5ad 矩阵、查询索引和 `function_index.json` 在当前包中可加载。
- resolver 入口：无自然语言或半结构化 resolver parse、normalize、dispatch 证据；直接 CLI 参数不能替代 resolver。
- LLM 能力：只有包树中存在 prompt template 的间接信息，没有 CyHex AI route、`deepseek-v4-pro` 或替代模型、解析/总结调用、延迟、失败或 fallback 元数据。
- proxy 路由：没有 proxy perturbation、proxy cell、proxy both、function alias proxy 的现行证据。
- route-aware metadata：没有证明每次响应都包含 T-064 要求的 `route_type`、`query_context`、`perturbation_resolution`、`function_response`、`confidence`、`proxy_chain`、`diagnostics`、`suggestions`。
- transfer/suggestion：没有对 no-hit、ambiguous 或 context-missing 情况给出可执行改写、替代上下文或相关扰动建议。

## 未批准的范围收缩

如果 M1 只被称为“确定性内核/底座”，上述缺口可以作为阶段性边界记录；但如果把 M1 称为完整算法包，则存在未批准范围收缩：

1. 用 direct CLI / deterministic function call 替代 resolver-mediated user entry。
2. 用 exact-only synthetic fixture demo 替代 proxy/no-hit/ambiguous/context/transfer 路由覆盖。
3. 用 prompt template 或包内 `llm/` 目录的存在替代真实 LLM parse/summary 证据。
4. 把 synthetic fixture 与 minimal index gap 标为低严重度，从而弱化标准资源兼容性要求。

## 能力矩阵

| 能力 | 状态 | 证据/缺口 |
|---|---|---|
| `CAP-FWD-001` Forward perturbation-to-function query | `partial` | A-001/A-002: EGFR/A549/xpr forward demo found:true; CLI exit 0; JSON valid. 缺口：Only one exact positive and one no-hit case on synthetic_repair fixture; no real LINCS/T-021 standard-resource evidence. |
| `CAP-REV-001` Reverse function-to-perturbation query | `partial` | A-001/A-002: apoptosis activation plus MYC suppression in A549 returns ranked top candidates; 42/42 validation checks pass. 缺口：Synthetic fixture only; minimal one-profile coverage; one zero-norm candidate skipped with warning; no full matrix numeric robustness evidence. |
| `CAP-CTX-001` Biological context handling | `partial` | A-001/A-002: A549 is accepted in forward and reverse demos; ContextNotFound is listed among structured reverse errors. 缺口：No multi-cell-line, lineage, disease, subtype, or context-proxy evidence; context route metadata is not shown against T-064 contract. |
| `CAP-EVD-EXACT-001` Exact evidence routing | `partial` | A-001/A-002: exact EGFR/A549 and exact reverse function examples succeed. 缺口：Outputs are reported as found:true and valid JSON, but route_type=exact-hit, source index/matrix references, and full metadata contract are not evidenced. |
| `CAP-EVD-PROXY-001` Proxy evidence routing | `downgraded` | No proxy forward, proxy reverse, proxy-cell, proxy-perturbation, or proxy-both case appears in A-001 to A-004. 缺口：M1 validates exact fixture paths only; no exact-miss trigger, neighbor source, similarity/hierarchy basis, proxy confidence, or limitation metadata. |
| `CAP-EVD-NOTFOUND-001` Not-found and no-hit routing | `partial` | A-001/A-002: UNKNOWN_GENE_XYZ999/A549 returns structured PerturbationNotFound without traceback. 缺口：Only one negative control; no attempted-route metadata, threshold guard evidence, context/function no-hit, or no-false-positive confirmation under T-064 contract. |
| `CAP-ENTRY-RESOLVER-001` Resolver-mediated query entry | `downgraded` | A-001 lists direct CLI subcommands forward/reverse/info; no resolver startup, parse object, or dispatch log is evidenced. 缺口：Direct deterministic CLI parameters substitute for resolver-mediated natural-language or semi-structured entry. |
| `CAP-LLM-001` LLM-assisted parsing and summarization | `deferred-not-approved` | A-001 package tree includes llm/prompt templates, but A-001 to A-004 contain no LLM call, parse, summary, route, latency, failure, or fallback evidence. 缺口：Prompt/code presence is not delivery evidence; endpoint connectivity or templates would also be insufficient under T-063. |
| `CAP-FALLBACK-001` Deterministic fallback and runtime resilience | `partial` | A-001/A-002: structured errors are shown for perturbation not found and reverse error classes such as NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, EmptyTarget. 缺口：No primary resolver/LLM/proxy failure trigger is exercised; fallback metadata distinguishing primary versus fallback paths is absent. |
| `CAP-META-001` Transparent evidence metadata | `partial` | A-001/A-002: outputs are JSON and include found/not-found status; forward reference comparison excludes a harness _evidence field. 缺口：No evidence that all 8 T-064 fields are present: route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, suggestions. |
| `CAP-RES-001` Standard resource compatibility | `evidence-insufficient` | A-004 GAP-001/GAP-002/GAP-004 state synthetic fixture validation and minimal/synthetic indexes; A-001 package uses M1FixtureLoader. 缺口：No T-021 functional matrix/index loading or function_index runtime compatibility evidence appears in M1 artifacts. |
| `RES-ENTRY-NL-001` Natural-language resolver entry | `deferred-not-approved` | No natural-language input case in A-001 to A-004. 缺口：No raw NL input, parse, ambiguity fields, dispatch log, or route metadata. |
| `RES-ENTRY-STRUCT-001` Semi-structured resolver entry | `downgraded` | CLI flags provide structured parameters, but no resolver parse/normalization record is shown. 缺口：Manual CLI parameters bypass resolver parse metadata and supported-field normalization. |
| `RES-AI-001` CyHex-configured LLM route | `evidence-insufficient` | No CyHex AI route, deepseek-v4-pro or successor, parse/summary call, latency, failure, or fallback metadata in M1 artifacts. 缺口：LLM prompt templates in the package tree do not demonstrate configured LLM behavior. |
| `RES-DEMO-001` Required M3 demo coverage | `deferred-not-approved` | M1 has exact forward, exact reverse, and one no-hit fixture case; no proxy, ambiguous NL, semi-structured resolver, LLM-unavailable fallback, or metadata-inspection demo. 缺口：M3 demo catalog coverage is mostly absent. |
| `ROUTE-EXACT-HIT` T-064 exact-hit route | `partial` | Exact fixture examples succeed. 缺口：Missing route_type exact-hit and full source/index/matrix metadata. |
| `ROUTE-PROXY-HIT` T-064 proxy-hit route | `downgraded` | No proxy case. 缺口：No proxy chain, threshold, similarity, hierarchy, or limitation metadata. |
| `ROUTE-NO-HIT` T-064 no-hit route | `partial` | One unknown gene token returns PerturbationNotFound. 缺口：No threshold-guard, indexes-searched, proxy-below-threshold, or suggestions metadata. |
| `ROUTE-AMBIGUOUS-HIT` T-064 ambiguous-hit route | `evidence-insufficient` | No ambiguous perturbation, multi-BRD, or near-tie reverse case in M1 artifacts. 缺口：No candidate list, ambiguity flags, or clarification/suggestion behavior. |
| `ROUTE-CONTEXT-MISSING` T-064 context-missing route | `partial` | Reverse validation lists ContextNotFound among structured errors. 缺口：No explicit missing/invalid context demo with required fields, validation errors, or suggestions. |
| `ROUTE-TRANSFER-SUGGESTION` T-064 transfer/suggestion route | `deferred-not-approved` | No actionable reformulation, alternative context, related perturbation, or LLM-assisted explanation appears in M1 artifacts. 缺口：M1 returns deterministic results/errors but no user-facing transfer/suggestion semantics. |
| `ROUTE-METADATA-CONTRACT` T-064 eight-field metadata contract | `evidence-insufficient` | A-001/A-002 state JSON is valid and found/not-found exists. 缺口：No evidence that route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, and suggestions are all present in every response. |

## 复核限制

本任务没有运行包、没有修复代码、没有分析原始数据，也没有读取未注册的前序目录。结论只基于 A-001 至 A-016 注册资产。
