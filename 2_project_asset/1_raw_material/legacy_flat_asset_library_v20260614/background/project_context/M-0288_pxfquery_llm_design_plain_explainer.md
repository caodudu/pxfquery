# PxFquery 当前 LLM 设计说明（通俗版）

更新时间：2026-04-10
目的：不用看源码，也能理解 PxFquery 现在“让 LLM 依次解决什么问题、怎么配合、为什么会出现你现在看到的现象”。

---

## 1. 一句话总览

当前版本里，LLM 主要做的是“语义解析与映射”，不是“直接替代模型做预测”。

也就是说：
- LLM 负责把人话变成结构化查询（你在问什么）；
- 然后系统去真实矩阵里检索证据（exact/proxy）；
- 最后可选让 LLM 把检索结果写成可读 summary。

所以它是“LLM + 证据检索”的混合系统，不是纯 LLM 幻想回答器。

---

## 2. LLM 在正向查询中的完整顺序（核心）

下面是一次 forward query（如“在 A549 里 EGFR knockdown 会怎样”）的实际逻辑顺序。

### Step A: 意图解析（LLM）

目标：先把自然语言拆成统一结构。

LLM 需要产出这些字段：
- query_type：forward 还是 reverse
- bio_context：细胞系名或疾病上下文
- pert_desc：扰动描述（gene/drug）
- pert_class：genetic 或 drug
- 其他字段（top_n 等）

为什么这一层重要：
- 后续每一步都依赖它来决定分流。
- 如果这一步偏了，后面检索方向就偏。

它为什么会慢：
- 有“先快后稳”的两段策略：先尝试轻量解析；若结果不合法，再做一轮更稳的解析。
- 每轮还有网络级重试机制。
- 因此最坏会出现多次 API 尝试。

当前这一步的提示词（核心）：
```text
System:
You are an intent parser for a perturbation-function query toolkit.
Return JSON only.
Schema: {query_type, bio_context, pert_desc, pert_class, function_desc, activate, suppress, top_n}
Rules:
- query_type=forward or reverse
- pert_class=genetic or drug
- unknown fields use null

User:
<原始用户问题>
```

---

### Step B: 生物上下文映射（可能用 LLM）

目标：确定“用哪个 cell line 或 proxy cell 集合去查”。

分两种：
1. 如果输入是精确 cell line（例如 A549）：不需要 LLM，直接 exact + 邻近 cell。
2. 如果输入是疾病/场景描述（例如 NSCLC）：需要在层级树里逐层选节点（lineage -> disease -> subtype -> cells）。

这里 LLM 可能被调用多次：
- 每一层都可能调用一次“从候选列表中选一个”。
- 所以复杂上下文会比精确细胞名慢很多。

当前这一步的提示词（核心）：
```text
System:
You are selecting one option from a controlled list.
Return JSON only with key "selected".
Pick exactly one option from the list.

User:
Biology context: <bio_desc>
Current level: <lineage|disease|subtype|cells>
Options: [opt1, opt2, ...]
Select the single best option.
```

---

### Step C: 扰动映射（按 genetic/drug 分流，可能用 LLM）

目标：把扰动描述映射成“可查询的标准扰动项”。

#### genetic 路径
- 先本地 gene index 查 exact；
- 不行再做快速提取；
- 还不行才调 LLM 做 gene mapping。
- 最后生成 gene neighbors（作为 proxy 候选）。

#### drug 路径
- 先本地 drug index 查；
- 不行先调 LLM 做 drug normalize（同义词/商品名归一）；
- 还不行再调 LLM map drug（从描述猜具体药物）；
- 最后生成 drug neighbors（结构近邻）。

这一步的设计思想是：
“先本地、后 LLM；先精确、后近邻”。

当前这一步的提示词（核心）：
```text
Drug normalize:
- Normalize a drug synonym/brand/translated name into standard generic names.
- Return JSON: {"candidates":[...]}

Drug map:
- Map a drug description to candidate concrete drug names.
- Return JSON: {"candidates":[...]}

Gene map:
- Normalize user gene mention to canonical gene symbols.
- Return JSON: {"candidates":[...]}
```

---

### Step D: 四层证据检索（不靠 LLM）

目标：在真实矩阵中找到可用证据对（B, P）。

四层顺序：
1. EXACT：exact cell + exact perturbation
2. PROXY_PERT：exact cell + pert neighbors
3. PROXY_CELL：proxy cells + exact perturbation
4. PROXY_BOTH：proxy cells + pert neighbors

注意：
这里是“在已有实验矩阵里找可用 pair”，不是生成式预测。

---

### Step E: genetic 双源查询（xpr + sh）

当判定为 genetic 且未强制指定单源时，系统会：
- 用同一套解析结果，分别跑 xpr 和 sh；
- 各自产生自己的命中层级与结果；
- 形成一个双源证据包（bundle）。

这一步确实已经实现了“双查”。

---

### Step F: 对外结果组织（当前版本争议点）

虽然双源都查了，但当前对外主结果结构仍是“单结果对象”。
所以系统会从 xpr/sh 两路里选一个“主展示源”（selected_source）用于主表展示。

为什么这么做（工程原因）：
- 兼容现有单结果数据结构、下游报告和可视化；
- 避免一次查询返回两套主表导致接口全面改造。

副作用：
- 用户容易误以为只查了一个源；
- 需要看 bundle 才知道双查事实。

你的感受是对的：这在产品表达上确实容易误导。

---

### Step G: summary 生成（可选 LLM）

只有在 summarize=True 且 found=True 时，才会调 LLM 写总结。

如果 found=False，不调用 LLM 生成总结，而是直接返回固定模板：
- "No result found. ..."

这就是你看到那句英文的来源。

当前这一步的提示词（核心）：
```text
Write a concise scientific interpretation (<= max_words).
Input includes:
- perturbation/cell line
- resolver_meta (evidence quality)
- top activated / top suppressed terms
Must explicitly state exact vs proxy evidence quality.
```

---

## 3. 你关心的两个核心误解点

### 3.1 “既然双查了，为什么只显示一个 source？”

结论：
- 双查是“检索层”行为；
- 单 source 是“展示层”行为。

当前实现是“检索双源，展示单源 + 附带双源证据包”。
这不是没查，而是展示口径仍是单主结果。

你说“这会误导”是成立的。

---

### 3.2 “为什么会 No result found？不是有近邻就该永远有结果吗？”

这句 No result found 的真实含义不是“世界上没有近邻概念”，而是：

在当前检索规则和当前矩阵覆盖下，系统没找到可用的 (B,P) 实验对。

常见原因：
1. 解析到的 perturbation 在该源里没有可用键（包括近邻也不在矩阵）；
2. 上下文映射到的 proxy cell 集合里，没有与该 perturbation 形成有效 pair；
3. 近邻阈值/候选策略把可用候选过滤掉；
4. 分流到某一路后（如 cp/xpr/sh），该路覆盖本来就缺；
5. 命中了“证据优先”策略：宁可返回 not found，也不做无证据编造。

所以目前系统哲学是：
“有证据再答；没证据就明说没证据。”

而你想要的是：
“无论如何都给一个参考预测（即使低置信）。”

这两种目标不一样，当前实现更偏第一种。

---

## 4. 现在这套设计是否符合你的原始意图？

如果你的意图是：
- 永远给答案（哪怕弱证据），
- 不要轻易出现 NOT_FOUND，

那当前实现是“部分符合、关键处不符合”。

符合的部分：
- 已做近邻检索、已做 xpr+sh 双源、已做 LLM 语义映射。

不符合的部分：
- 仍可能因为“证据检索不到 pair”而返回 NOT_FOUND；
- 对外默认只给单主源展示，不直观体现双源。

---

## 5. 给你一个不看源码也能理解的定位框架

以后你看到结果不对，先判断是哪个层面的问题：

1. 语义层（LLM）
- 问题被解析错了：把 drug 当 genetic，或上下文理解错。

2. 映射层（LLM + index）
- 词被映射成了一个不在库里的标准项。

3. 检索层（矩阵证据）
- 规则是对的，但库里确实没这个 pair。

4. 展示层（结果包装）
- 实际双查了，但主视图只显示了一个 source，造成误解。

这四层分开看，你会非常快知道是“语义错”还是“数据没覆盖”。

---

## 6. 当前版本最关键的一句话

PxFquery 现在不是“必答型预测器”，而是“证据约束型检索 + LLM解释器”。

如果你要“必答型”，下一步就要明确加入“强制回退预测策略”（即使无直接 pair，也输出最低置信近邻推断），并把“低置信”标注成一级公民。

---

## 7. LLM 对话是连续还是分离？

结论：**当前是分离请求（stateless），不是连续会话（stateful chat）**。

具体含义：
- 每个 LLM 函数调用都单独发一次 HTTP 请求；
- 每次只带“该步所需的 system + user 内容”，不自动继承前一步聊天记忆；
- 没有 conversation_id / thread_id 级别的持久会话状态。

这带来的结果：
1. 可重复性更好（每步独立、可缓存）；
2. 但跨步上下文复用弱，复杂场景下延迟会变高。

补充：
- 当前系统有“函数级缓存”（同进程同参数命中时可复用）；
- 但这不是多轮会话记忆，只是重复输入的结果缓存。

---

## 8. 外部 API 调用机制（你关心的性能点）

当前机制是：
- 通过 OpenAI 兼容客户端调用 provider 的 `chat.completions`；
- 非流式（一次拿完整响应）；
- 每个请求最多重试 3 次（失败时退避等待）。

这意味着：
- 慢的时候，主要慢在“服务端排队+推理时延+可能重试”；
- 不是因为“只用了 request 而没用 LiteLLM”这一个因素。

LiteLLM 可能带来的价值更多是：
- 多 provider 路由和容错策略更方便；
- 统一日志/熔断更好做；
- 但单次模型推理本身不会因为换壳就天然大幅提速。
