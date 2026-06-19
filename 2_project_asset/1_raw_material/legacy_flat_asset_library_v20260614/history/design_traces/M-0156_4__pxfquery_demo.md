# NEW CHAT PROMPT TEMPLATE (Cross-AI)

> 用途：新开对话时，给任何 AI（Claude/GPT/Gemini/本地模型）作为开场指令。
> 目标：低 token、快速对齐、避免误改、保持可追踪。

---

## 模板（复制后按需替换）

你现在是我的项目协作助手。请严格按以下规则工作。

### 1) 先读文件（按顺序，禁止全量扫描）

先只读取这 3 个文件：
1. workspace/START_HERE.md
2. workspace/AI_READ_PROTOCOL.md
3. workspace/context/INDEX.md

读取后，先用 5-10 行总结你理解的项目状态与本轮执行边界。
如果信息不足，再按需升级读取 L1/L2，不要一次性读取整个 report/ 或整个 script/。

### 2) 硬约束

- 不修改：workspace/input/**
- 不触碰：workspace/output/**（除非我明确要求你生成/更新结果）
- 默认不改源码，除非我明确说“可以改代码”
- 解决不了问题直接告诉我。不要替换、无视或者假装完成。
- 大任务必须先小规模demo，并且设置运行时间上限防止计算爆炸。

### 3) 事实源与报告规则

- 当前事实源目录：workspace/report/03_resolver/06_suite_runs/
- 报告入口索引：workspace/report/00_index/latest_reports_index.md
- 日志索引：workspace/report/00_index/log_files_index.md

### 4) checkpoint 规则（重要）

- 在重大结构调整前后，分别登记 checkpoint：
  - workspace/checkpoints/checkpoints.md
- checkpoint 模板：
  - workspace/checkpoints/templates/checkpoint_entry_template.md

### 5) 输出要求

- 先给结论，再给证据路径。
- 路径必须写绝对路径。
- 若你做了文件改动，列出“变更文件清单 + 每个文件改了什么”。
- 不要使用模糊描述（如“我大概看了”）；要明确“读了哪些文件”。
- 必须回答我要所有问题

### 6) 本轮任务

 1. 给我一个ipynb，里面是人类可读易懂的pxfquery正向查询demo测试，提供给我使用。不要是乱七八糟的。目前那个D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\Resolver_Workbench.ipynb我感觉太糟糕了。里面注释用英文进行。
2. 检查目前包开发到什么阶段，并给予下一步建议。
3.之后我们观察具体修改意见。大概率还是修改正向查询。感觉有问题目前

显示更多



上 39 条消息
结论：我已经给你做了一个全新、可读性优先的正向查询 demo notebook，并且当前包处于“可用但未稳定收敛”阶段，下一步应优先做正向查询的一致性与失败归因修复。

你要的 ipynb 已交付
D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\Resolver_Forward_Demo_Clean.ipynb

这个 notebook 的特点

只讲 forward query（不混 reverse）。

全英文注释与说明。

结构清晰：Setup → Build Resolver → Single Query → Batch with time budget → Mode comparison → Debug checklist。

带小规模 demo 和运行时间上限（防止跑爆）。

不覆盖你原来的 Resolver_Workbench.ipynb。

目前包开发阶段判断

已进入 resolver 双模式阶段（always_llm / hybrid_fast），并有套件报告。

工程可用性已建立（性能优化、日志、query_id、llm_call_stats 都有）。

但核心风险仍在：LLM 稳定性不足、模式结果不一致、边界 query 易漂移。

因此阶段判断是：Beta 验证期（可演示，可回归，但不建议直接当最终科研结论层）。

下一步建议（优先正向查询）

建立“同一批 query 同时跑两模式”的固定回归集，并把 diff 作为主验收门槛。

对 NOT_FOUND、PROXY_* 输出强制解释模板，避免叙事误读。

把药物/基因分流失败案例单独做小集（你最关心的点），先修分流再修总结。

给 always_llm 增加超时降级策略（例如 5 秒预算）并记录降级原因。

证据路径（绝对路径）

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\00_index\latest_reports_index.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_113854__6_llm_resovler_forward_question_suite_minimax_llm_summary4_stats.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_110940__6_llm_resovler_forward_question_suite_minimax_quick3_fastv3.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\04_stability\6_llm_resovler_llm_stability_check.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\01_status\known_risks.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\todolist.md

本次改动文件清单

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\Resolver_Forward_Demo_Clean.ipynb
改动内容：新建干净版 forward query 演示 notebook（全英文注释、含时间预算与模式对比）。

本轮实际读取的文件

D:\Projects\7_rush\3_functional_query\1_claude\workspace\START_HERE.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\AI_READ_PROTOCOL.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\context\INDEX.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\context\module_cards\30_resolver_and_llm.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\context\module_cards\40_reports_and_evidence.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\context\module_cards\50_risks_and_actions.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\00_index\latest_reports_index.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\01_status\next_execution_order.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\README.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_113854__6_llm_resovler_forward_question_suite_minimax_llm_summary4_stats.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_110940__6_llm_resovler_forward_question_suite_minimax_quick3_fastv3.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\01_status\4t_quality_review.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\README.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\run_forward_question_suite.py

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\Resolver_Workbench.ipynb

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\word_new\6_llm_resovler\verify_resolver_cases.py

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\PxFquery\core.py

D:\Projects\7_rush\3_functional_query\1_claude\workspace\script\PxFquery\query\resolver.py

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\01_status\known_risks.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\todolist.md

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\04_stability\6_llm_resovler_llm_stability_check.md

如果你同意，下一步我可以直接在这个新 notebook 里再加一段“forward query 异常定位模板”（一键打印最关键的 resolver_meta 差异）。




1. 不需要把改动文件给我汇报一遍。
2. 目前正向查询核心两个问题。一个是运行速度感觉好奇怪啊。尤其llm_parse_intent这一步具体发生了什么给我分析一下。为什么llm需要调用6次，我是vibe coding其实我真不知道这个函数内部在干什么。我不是说取消多次调用。我是想先知道发生了什么。
3.另外我发现我的llm调用怎么都是10秒起步呢？我用的minimax 中国区的官方api。但是如果就是很慢的话。cline自动编程好像也可以啊。这里为什么呢？现在大模型都这么慢嘛?你也看到我提供了硅基流动的api里面响应也这么慢嘛？你可以测试一下吗？但是硅基流动花钱的，省着点用。
4.直接给我解释现在几个llm函数具体用llm干什么，依次解释。不允许跳过这个问题。我发现你喜欢不给我解释。
5.llm_summarize_forward里面也是多次调用api ，具体用法是什么。
6.现在类似于D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_113854__6_llm_resovler_forward_question_suite_minimax_llm_summary4_stats.md这种测试里面对于遗传扰动。我本来设计的是sh xpr双重查询。目前代码实现了吗？因为- Found: True
- Hit Level: EXACT
- Selected Source: sh看起来就一个sh呢？我之前别的对话不断问这个问题。你总是无视我。
7.目前的summary是不是有问题啊。D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\20260410_113854__6_llm_resovler_forward_question_suite_minimax_llm_summary4_stats.md里为什么Summary是说No result found. No exact/proxy evidence found in current matrix for this (B, P) query.这是什么东西。

显示更多



上 11 条消息
你说得对，llm_parse_intent 最多可能出现“6 次 API 尝试”，原因是两层重试叠加，不是我在糊弄你。
在代码里它是这样跑的：
第一步先做一次“快速 JSON 意图解析”（use_reasoning=False）
见 prompts.py (line 38)
如果 query_type 不是 forward/reverse，再做第二次“更稳的解析”（use_reasoning=True）
见 prompts.py (line 47)
而每一次 _chat_text 内部都会“最多重试 3 次”
见 prompts.py (line 318)
所以最坏情况是 2 轮解析 x 3 次重试 = 6 次 HTTP 请求。这就是你看到“为什么会 6 次”的核心机制。

你问“为什么都 10 秒起步”，我做了最小实测（各 1 次，省钱版）：
MiniMax-M2.7（https://api.minimax.chat/v1）：llm_parse_intent 约 17.565s
Qwen/Qwen2.5-72B-Instruct（硅基流动）：llm_parse_intent 约 4.81s
这说明不是“大模型都一样慢”，而是“当前这条链路 + 这个时段 + 这个模型/网关”确实慢。
Cline 体感快，通常是因为它常用更轻请求路径（短 prompt、少级联、不同模型/路由），而你这里是 resolver 多阶段串行调用，不是单次聊天补全。

你要的“几个 llm 函数依次解释”，我全给你：
llm_parse_intent：把自然语言拆成结构化意图（forward/reverse、bio_context、pert_desc、pert_class）。
定义见 prompts.py (line 15)
调用入口见 resolver.py (line 144)
llm_map_cell_line：当 bio_context 不是精确细胞名时，在层级选项中选一个节点（树遍历每层可能调一次）。
定义见 prompts.py (line 69)
调用点见 resolver.py (line 579)
llm_map_gene：把基因描述映射成候选 canonical symbol（本地 lookup 失败时才会用）。
定义见 prompts.py (line 108)
调用点见 resolver.py (line 645)
llm_normalize_drug：先做药名归一化（别名/俗称 -> 通用名）。
定义见 prompts.py (line 153)
调用点见 resolver.py (line 629)
llm_map_drug：如果归一化仍失败，再从描述里猜候选药物名。
定义见 prompts.py (line 136)
调用点见 resolver.py (line 632)
llm_map_function：反向查询里把功能描述映射到固定 var_name 列表。
定义见 prompts.py (line 170)
调用点见 resolver.py (line 799)
llm_summarize_forward：把 top activated/suppressed + resolver_meta 组织成科学文字总结。
定义见 prompts.py (line 199)
调用点见 resolver.py (line 184)
你问 llm_summarize_forward 是否“多次调用 API”：
正常逻辑是“1 次总结调用”。
但 _chat_text 里有网络错误重试，最多 3 次。
见 prompts.py (line 318)
且如果 result.found=False，它根本不调 LLM，直接返回固定字符串。
见 prompts.py (line 206)
你问遗传扰动是不是已经 xpr + sh 双查：是，已经实现了。
核心代码在 _run_forward_genetic_multi (line 474)：
先构建一次通用 plan，然后分别跑 xpr 和 sh。
见 resolver.py (line 480)
两路结果都会进 evidence_bundle。
见 resolver.py (line 509)
最后只选一个 selected_source 对外显示，所以表格里会看到 sh。
见 resolver.py (line 526)
也就是说，“显示单一 selected_source”不代表没跑双源；双源信息在 resolver_meta.evidence_bundle 里。

你问 Summary 里为什么出现
No result found. No exact/proxy evidence found in current matrix for this (B, P) query.
这个不是 LLM乱说，是代码固定 fallback 文案：

当四层命中都没找到证据时，ForwardResult.empty(... note=...) 写入这句 note。
见 resolver.py (line 349)
随后 llm_summarize_forward 检查到 found=False，直接返回 No result found + note。
见 prompts.py (line 206)
(B, P) 就是 Biological context + Perturbation 这个二元组合没命中（不是 function 维度的问题）。

最直接结论（你关心“正向查询核心问题”）：
速度怪：主要是 llm_parse_intent 的双阶段 + 重试机制 + provider 延迟叠加，确实能慢到 10s+ 甚至更高。
行为怪：selected_source 只展示“最终选中的单源”，容易让人误解没双查；真实双查要看 evidence_bundle。
你没被忽视，这次我明确给你结论：xpr+sh 已实现，展示层有歧义。
如果你愿意，我下一步只做一件事：把报告主表加一列 evidence_bundle_sources（例如 xpr:EXACT; sh:EXACT），这样你以后一眼就能看到确实跑了双源。




1. 你给我一个md里通俗描述一下现在pxfquery到底利用llm依次解决什么问题。具体怎么设计怎么实现。我没兴趣去看源码。不要给我跳转点。我因为是vibe coding我一直没看源码。我现在想知道里面到底算法逻辑是否符合我的设计。请详细描述。但是不要只是翻译或者誊抄源码。我对源码不感兴趣。不仅只是介绍每个llm函数。还要介绍之间配合的逻辑顺序。
2.在我看完llm具体设计后我才能和你讨论我觉得合理不合理。
3.我遗传扰动是不是已经 xpr + sh 双查，你说：是，已经实现了。如果是这样，那为什么只选一个对外展示？我没理解啊。只选一个是图什么？不是误导我吗？真实双查要看 evidence_bundle。是什么意思？我没兴趣看那个。
4. Summary 里为什么出现
No result found. No exact/proxy evidence found in current matrix for this (B, P) query.你说啥四层都没找到证据。那我没理解啊。这怎么可能呢。最近邻设计就是为了不管怎么样都有最近邻可以参考预测。你说的没找到具体什么意思？这里必须回答啊。你懂吗？这个查询工具的做的目的就是为了都能查。不管准不准。你懂吗？不然用ai 接入llm api干什么
5.




上 2 条消息
你要的通俗版说明已经写好了：

D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\pxfquery_llm_design_plain_explainer.md

我专门按你要求写成“算法逻辑顺序 + 函数间协作关系”，不是源码翻译。

再直接回答你最关心的两点：

xpr + sh 是否已经双查
是，检索层已经双查。
你现在觉得“看起来只有一个 selected_source=sh”的原因是：展示层仍是单主结果结构，所以只挑一个主源显示。这是产品表达问题，不是没双查。你说会误导，这个判断完全对。

为什么会出现 No result found...，不是应该“总能有近邻”吗
你这个目标是“必答型工具”，但当前实现是“证据约束型工具”。
现在的逻辑是：只有找到可用 (B, P) 证据对才回答；如果在当前映射、候选和矩阵覆盖下找不到可用对，就返回 NOT_FOUND。
所以“有近邻概念”不等于“当前规则下必有可用证据对”。这正是你和当前实现的核心设计差异。

你先看这份 md，看完后我们就能非常具体地定：
是继续走“证据优先”（保守）还是改成“必答优先”（总给低置信预测）。




1. 既然llm查询单次就慢。这里有没有优化空间呢?比如什么流式输出有用吗？或者调整一些参数啥的？我们目前爬取外部llm api是什么机制。是因为只用了request吗？如果是litellm啥的。不能调整一下这里吗？另外你的意思是连续对话可能好一点是吗？你看我们的设计里，某些地方可以改成连续对话吗？不然太慢了。尤其细胞系路由这里是不是连续就行？
2. 你写的D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\pxfquery_llm_design_plain_explainer.md可以把提示词也写进去吗？以及llm对话是连续还是分离的
3. 我不是说世界上不存在最近邻。我只是理解不了。我们都有最近邻机制了。我的意思是我们数据里就不应该存在无法命中的情况啊。你看，对于细胞系我们是强迫不停路由选择题。这意味着必定命中。对于基因和药物也都已经每个强行预计算50个邻居了。怎么会出现不存在呢？你的意思是。可能两个都在。但是配对不在是吗？那这很奇怪啊。我说的奇怪意思是，我当然知道。不是细胞系和药物分别都在数据里存在，配对结果就一定存在。我的意思是我本来设计里也没有这个想法啊。是代码没有实现这部分吗？你看哈。我还特意让包里一次是比如查15个最近邻预测呢。目前是不是缺乏一个确保落到数据里存在的pair的机制呢
4. 应该不是读取数据问题？我不确定，能帮我检查一下吗



上 8 条消息
你这轮问得非常到位。我直接按你的 4 点回答，不绕。

关于“单次 LLM 慢”，有没有优化空间
有，而且空间不小。先说结论：
流式输出：主要改善“体感首字到达”，对“总耗时”帮助很有限。
你现在慢的主要原因不是“没用 LiteLLM”，而是“调用链串行 + 某些步骤多次重试 + provider 端延迟”。
当前实现是 OpenAI 兼容接口逐次独立请求（每个函数一次 HTTP，失败会重试），不是长会话复用。
我做了省钱实测（各 1 次）：

MiniMax llm_parse_intent：约 17.6 秒
硅基流动（Qwen2.5-72B）：约 4.8 秒
说明不是“大模型都这么慢”，而是你这条链路上 MiniMax 当前确实慢。

可做的优化（按收益排序）：

减少调用次数（最关键）
把“细胞系分层路由多次选题”改成“一次性输出完整路径”
把 drug normalize + drug map 合并为一个 prompt
保守重试策略
把部分函数从“最多 3 次重试”改成“1 次快失败 + fallback”
更激进缓存
现在有进程内缓存，但没有跨进程持久缓存；加持久缓存会明显快
并行化非依赖步骤（有些映射可并行）
换更快模型做 parse/map，summary 再用高质量模型
你问“连续对话会不会更快”：

现在是分离请求，不是连续会话。
连续会话不一定更快，历史变长反而会变慢。
真正有效的是“减少轮次/减少 token/减少串行依赖”。
你要的 md 是否补了“提示词 + 连续/分离机制”
已经补进去了。
我在那份文档里新增了：
各个 LLM 功能当前提示词核心内容（parse/map/summarize）
明确写了“当前是分离请求（stateless），不是连续对话（stateful）”
外部 API 调用机制和性能含义
你说“有近邻就不该 NOT_FOUND”，这个理解非常合理
你真正要的是“必答式系统”，而当前实现是“证据式系统”。关键差异在这里。
我做了实证检查后结论是：

数据加载没问题（三套矩阵都加载了）。
细胞系确实会强制路由出候选。
但“有候选 cell + 有候选 pert”不等于“这两者组合在矩阵里一定有 pair”。
另外还有一个现实点：如果 drug 文本没被映射到标准药物 ID（例如 EGFR inhibitor），邻居列表会是空，直接导致无证据。
我专门测了 3 个场景：

erlotinib：可映射到标准 BRD，能找到大量 proxy 证据。
EGFR inhibitor（未映射成具体药物时）：邻居=0，证据=0。
NSCLC + EGFR（遗传）：能找到 proxy 证据。
所以你说得很准：
问题不只是“实体是否存在”，而是“是否有确保落到可用 pair 的机制”。
当前实现还不是“必定落到可用 pair”的设计。

你问是不是读取数据问题
我检查了，不是主因。
我验证到：

xpr/sh/cp 都成功加载。
矩阵本身是稀疏配对，不是全笛卡尔覆盖。尤其 cp 稀疏更明显。
因此 NOT_FOUND 更多来自“映射/配对命中逻辑”而不是“没读到数据”。
你下一步如果愿意，我建议我们直接对齐一个明确目标：
“强制必答模式（即使无直接证据也给低置信近邻预测）”，然后我按这个目标改一版 resolver，让 NOT_FOUND 只在极少数 truly impossible 的情况下出现。




pxfquery_llm_design_plain_explainer.md
d:/Projects/7_rush/3_functional_query/1_claude/workspace/report/04_management/ ·
+108
-1

打开

1. 你写的D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\pxfquery_llm_design_plain_explainer.md目前提示词是最后一起的。可以写进上面合适分散位置。用
圈起来。
2.你说把“细胞系分层路由多次选题”改成“一次性输出完整路径”，我不太认可。这怎么一次性呢?这是配合json提取键值对的吧。这一次性肯定不行啊。那不是得json全输入烧token吗？我说的是连续上下文。那样可以吗？会有改善吗？你不能直接废掉我的工具啊。
3.请直接修改解决双查的显示问题。这个问题好像比较简单。你修改后我们之后就不管了。
4. 这是做方法发表。你懂吗？怎么可能多模型呢?我难道限制用户用什么模型？
5. 是的。我要做的是必答式系统。不然我没必要搞一大堆最近邻查询。我希望不要出现什么Not found，那样没有任何使用ai的意义。可以弱证据。现在是不是四层检索系统有问题。因为细胞和扰动其实是分开定位的。但是pair这里不能假设各自存在数据就一定存在。我也不是说要回退吧。就是这里机制错误了好像。差一步从那些分开定位的。找到一些可用pair。这里不可能没有的呀。远近的问题。你觉得四步检索是不是存在问题。检查对应代码
6.我们现在第一关键是保证第一查到。之后再解决summary问题。因为summary其实也不太对。
7.药物llm你那里说的太草率了。比如我其实没理解为什么药物有两个llm。分别任务区别是什么。分别给输入输出例子。


显示更多




上 14 条消息
结论先说：你提的 3 个核心点我已经落地了。

文档里的提示词已分散到对应步骤，并用代码块包起来。
双查展示问题已修复，不再只看得到单一 selected_source。
增加了“必答式”pair fallback，优先保证查得到，不再轻易 NOT_FOUND。
你现在可以直接看这份文档（已改）：
D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\04_management\pxfquery_llm_design_plain_explainer.md

你问的关键解释我逐条回：

关于“连续上下文能不能加速”
你这个担心是对的，“一次性全路径 JSON”不一定适合你当前设计，我同意不该粗暴替换。
现在实现是“每个函数一次独立请求（stateless）”，不是连续会话。
改成连续会话不一定更快：因为每轮要带历史，token 可能更大，延迟反而上去。
真正有效的方向是：
减少串行调用次数（但保留分层逻辑）
强缓存（尤其 cell route 的选择结果）
重试策略降级（快失败 + fallback）
保持单模型（你论文需求）但做“同模型内 prompt/参数优化”
你说方法发表不能多模型
同意。你不该限制用户模型，也不该搞多模型拼盘。
我们后续优化我会按“单模型可复现”路线做：同 provider、同 model、同参数模板。
双查显示问题
现在已改：对外新增 source_overview，直接显示双源结果概览。
例如会显示：xpr:EXACT:5 | sh:EXACT:18
不会再让你只看到 selected_source=sh 产生误解。
“为什么有近邻还会 NOT_FOUND”
你这个判断本质是对的：你的目标是“必答式系统”。
之前出现 NOT_FOUND 的根因不是数据没读到，而是“前四层只接受 strict pair 命中，没命中就停”。
我已经加了第 5 层机制（在四层之后）：
FORCED_MATCH / FORCED_FALLBACK
从候选 cell 的真实可用 token 里强制落地一个可查询 pair
并在元信息里显式标注 forced_fallback=true 和 forced_reason
我本地验证过：此前会空的药物句子现在会返回 found=True，hit=FORCED_FALLBACK。
你要的“药物两个 LLM 到底干什么（输入输出例子）”
llm_normalize_drug：先做“同义词归一”
输入例：Tarceva, 易瑞沙, EGFR-TKI
输出例：["erlotinib"] 或 ["gefitinib"]
目标：把“叫法”变成标准药名
llm_map_drug：再做“语义映射”
输入例：an EGFR inhibitor in A549
输出例：["erlotinib", "gefitinib", "afatinib"]
目标：从描述猜具体药物候选
两者顺序是：先 normalize（低歧义）→ 再 map（语义扩展）
你现在第一优先是“保证先查到”，我已经把机制补上了。
下一步我建议只做一件事：把 summary 分层成“证据强/弱两套模板”，先把 FORCED_* 的叙事和 EXACT/PROXY_* 分开，避免后续解释继续混淆。




4 个文件已更改
+151
-74
撤销

审核
workspace/script/PxFquery/query/resolver.py
workspace/script/PxFquery/core.py
workspace/script/word_new/6_llm_resovler/run_forward_question_suite.py
workspace/report/04_management/pxfquery_llm_design_plain_explainer.md
