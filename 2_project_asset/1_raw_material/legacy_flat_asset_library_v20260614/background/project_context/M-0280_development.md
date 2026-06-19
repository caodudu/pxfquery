# PxFquery 开发日志

记录对包本身的修改、重要决策、待办事项。
时间轴倒序（最新在前）。

---

## TODO（待实现，下次对话接续）

- [ ] `index/cellline_index.py` — CellLineIndex 类
      - `is_valid(name)` — 查 valid_cells，L1 精确验证
      - `traverse(bio_context, llm_fn)` — LLM 引导树遍历；单子节点自动跳过不调 LLM
      - 运行时 Cellosaurus 查询：`cellosaurus_lookup(name)` → site/disease，供 resolver 调用
- [ ] `llm/prompts.py` — 完整实现
      - `llm_parse_intent` / `llm_map_cell_line` / `llm_map_gene` / `llm_map_drug` / `llm_summarize_*`
      - `llm_normalize_drug(name) → list[str]`：用户药物名查不到时，LLM 返回 INN 候选列表
      - `llm_map_function(user_desc, function_list_str) → list[str]`：F 维度描述 → var_name 列表
- [ ] `index/drug_index.py` — lookup() 返回 None 后接入 llm_normalize_drug fallback
- [ ] `query/resolver.py` — 三元组解析器核心流程

---

## 2026-04-09

### Act-1：Resolver + LLM MVP 骨架落地（进行中）

**新增文件**：

| 文件 | 内容 |
|------|------|
| `script/PxFquery/index/cellline_index.py` | CellLineIndex：`is_valid/canonical/traverse` |
| `script/PxFquery/llm/prompts.py` | Resolver 使用的英文 prompt 函数集合 |
| `script/PxFquery/query/resolver.py` | QueryResolver + ResolverConfig（intent→resolve→query） |
| `script/word_new/6_llm_resovler/README.md` | 本步骤计划、运行方式、验收清单 |
| `script/word_new/6_llm_resovler/demo_resolver.py` | resolver MVP demo |
| `script/word_new/6_llm_resovler/test_resolver_smoke.py` | resolver smoke test |

**修改文件**：

| 文件 | 修改 |
|------|------|
| `script/PxFquery/core.py` | 新增 `enable_resolver()`；`query()` 优先走 resolver |
| `script/PxFquery/index/__init__.py` | 导出 `CellLineIndex` |
| `script/PxFquery/index/function_index.py` | 兼容两种 JSON 格式（legacy/new） |
| `script/PxFquery/query/__init__.py` | 导出 resolver 相关类 |
| `script/PxFquery/llm/__init__.py` | 导出 `LLMClient` |

**API key 约定（重要）**：

- Resolver 默认从 `workspace/.env` 读取密钥（demo/test 脚本会自动加载该文件）  
- 支持字段：
  - `MINIMAX_API_KEY`
  - `SILICONFLOW_API_KEY`
- 可选字段：
  - `MINIMAX_BASE_URL`
  - `SILICONFLOW_BASE_URL`

> 说明：`script/word_new/6_llm_resovler` 下当前未发现独立 `.env`，统一以 `workspace/.env` 为准。

**Act-1 本地验证**：

- `test_resolver_smoke.py`：PASS（加载 xpr/sh/cp + resolver 初始化 + forward/reverse 基础路径）
- `demo_resolver.py --provider siliconflow --model Qwen/Qwen2.5-72B-Instruct`：PASS（端到端返回 ForwardResult + summary）
- `demo_resolver.py --provider minimax --model MiniMax-Text-01`：FAIL（历史测试，旧模型名，不再作为默认）
  - 已增加 `MINIMAX_MODEL`/`SILICONFLOW_MODEL` 环境变量覆盖入口
- 新增自动验收脚本：`script/word_new/6_llm_resovler/validate_act1.py`
  - 自动跑 2 个端到端自然语言 case（forward + reverse）
  - 输出：
    - `output/store/resolver_demo/act1_validation.json`
    - `report/6_llm_resovler_act1_validation.md`
  - 2026-04-09 实测结果：2/2 成功（provider=siliconflow, model=Qwen/Qwen2.5-72B-Instruct）
- 新增正向复杂矩阵测试：`script/word_new/6_llm_resovler/test_forward_matrix.py`
  - 覆盖：EXACT / PROXY_PERT / PROXY_CELL / PROXY_BOTH、疾病名输入、未知细胞系输入、药物路径
  - 输出：
    - `output/store/resolver_demo/forward_matrix_results.json`
    - `report/6_llm_resovler_forward_matrix.md`
  - 2026-04-09 实测结果：7/7 通过（mock hooks，确定性）

**Act-1 后续重构（2026-04-09）**：

- `query/resolver.py`：
  - forward 改为四层命中逻辑（L1~L4）
  - 引入 `hit_level` 与代理证据 `resolver_meta`
  - 增加 `provider=mock`，支持无 API 的确定性测试
  - MiniMax 默认模型改为 `MiniMax-M2.7`
  - MiniMax 默认 base_url 改为 `https://api.minimax.io/v1`
- `index/cellline_index.py`：
  - 增加 `get_cell_path()` 与 `proxy_cells_for()`（同 subtype/disease/lineage）
- `llm/prompts.py`：
  - summary 增加 `include_numbers` 开关（默认不报具体分数）
  - summary 提示词改为“科学解释 + 证据质量”，避免纯数字复述
- `core.py`：
  - `enable_resolver()` 增加 `summary_include_numbers` 与 `prompt_hooks` 参数

**MiniMax 实测记录（优先提供）**：

- URL 探测：
  - `https://api.minimax.io/v1`：401（当前 key 在该入口无效）
  - `https://api.minimax.chat/v1`：可调用
- 当前默认已切换到 `https://api.minimax.chat/v1`
- 使用模型：`MiniMax-M2.7`
- `validate_act1.py`（MiniMax）已跑通，见：
  - `report/6_llm_resovler_act1_validation_minimax.md`
  - `output/store/resolver_demo/act1_validation_minimax.json`

**设计落实增强（2026-04-09）**：

- forward 遗传扰动默认双源检索（`xpr + sh`），并输出复合证据：
  - `resolver_meta.composite_mode = genetic_multi_source`
  - `resolver_meta.evidence_bundle = [...]`
- 新增设计对照文档：
  - `report/6_llm_resovler_design_check.md`

---

## 2026-04-08

### 5_function_index 步骤完成（功能基因集索引构建）

**产出文件**：

| 文件 | 内容 |
|------|------|
| `output/store/query_index/function_index.json` | 91 个 var_name、meta（label/source）、243 条 aliases，25.5 KB |
| `script/PxFquery/index/function_index.py` | FunctionIndex 类，lookup/validate/label/for_llm 接口 |

**关键决策**：
- 91 个条目足够小，单文件存储（var_names + meta + aliases）
- hallmark label 保留缩写大写（G2M, MYC, KRAS, TGF 等），MP* 修正 typo、去尾随空格
- aliases = 自动生成（label lowercase）+ curated 手工缩写（EMT, OXPHOS, p53, UPR 等）
- 歧义冲突（hypoxia 同时在 Hallmark 和 MP6）：默认指向 Hallmark，MP6 保留 `mp6 hypoxia` 专用别名
- `for_llm()` 输出 91 行格式化列表（`[H]`/`[M]` 标签），供 `llm_map_function` 直接嵌入 prompt

详见 `report/5_function_index.md`。

---

### 4_cellline_index 步骤完成（细胞系索引构建）

**产出文件**：

| 文件 | 内容 |
|------|------|
| `output/table/cellline_meta_enriched.csv` | cellline_meta_sub.csv + Cellosaurus 补充字段 |
| `output/store/query_index/cellline_index.json` | 240 个 valid_cells，L1 精确验证用 |
| `output/store/query_index/cellline_neighbors.json` | LLM 引导树，lineage→disease→subtype→cells，166 cells |

**关键设计决策**：
- 两条查询路径：精确命中走 cellline_index；未命中统一转生物定位描述走 cellline_neighbors 树遍历
- 树遍历为 LLM 引导式选择题，每步只看当前层选项，单子节点自动跳过不调 LLM
- Cellosaurus API 补充 82 个 unknown lineage，命中 8 个；74 个 LINCS 内部专用名（MCLF*/XC.*）无法补充，仅保留在 valid_cells
- 手工修正两处元数据错误：HME1（disease 错标为 leukemia）、OCILY10（lineage 错标为 placenta）
- subtype 标准化：三种 NSCLC 写法合并为 `non-small cell lung carcinoma`；AML 两种写法合并；孤立 CML 节点合并进 leukemia

详见 `report/4_cellline_index.md`。

---

## 2026-04-07（续）

### 新增 `index/gene_index.py`

实现 `GeneIndex` 类，默认使用 simple 版索引：

- `lookup(name)` — 大小写不敏感，返回 `(canonical_symbol, type_code)` 或 None
- `lookup_candidates(names)` — 依次尝试候选名（为 `llm_map_gene` fallback 准备）
- `in_matrix(symbol)` — 是否有实验数据（基于近邻候选池 7396 基因推断）
- `neighbors(symbol, min_cosine=0.5)` — 余弦近邻，返回 `(symbol, cosine)` 列表
- `gene_type(symbol)` — 返回完整类型名（protein_coding / miRNA / snRNA / misc_RNA）
- `__contains__` — 支持 `"KRAS" in idx` 语法

默认索引文件：`gene_index_simple.json`（25036 条）+ `gene_neighbors_simple.json`（30319 条）
HOTAIR 等 lncRNA 不在 simple 索引中（`lookup("HOTAIR") → None`），走 fallback。

---

## 2026-04-07 (21:20~22:30)

### 3_gene_index 步骤完成（基因索引构建）

**产出文件**：

| 文件 | 大小 | 说明 |
|------|------|------|
| `output/store/genePT/gene_embedding_m3_filtered.npz` | — | 33791×3072 float32，中间产物 |
| `output/store/genePT/gene_names_m3_filtered.csv` | — | 33791 行基因名 |
| `output/store/query_index/gene_index.json` | 6.1 MB | 78061 条，含 gene_type + in_matrix |
| `output/store/query_index/gene_neighbors.json` | 21.8 MB | 33791 个基因，top-50 cosine 近邻 |

**关键设计决策**：
- 使用 GenePT model-3（3072d，蛋白+文本）而非 ada（1536d）
- 过滤 model-3 到 Gencode v49 ∪ 有效矩阵基因（133736 → 33791），去除废弃基因名
- 废弃/拼写变体基因名由 `llm_map_gene()` fallback 处理（见 TODO）
- gene_index 包含 gene_type（Gencode GTF）和 in_matrix 标记，方便 resolver 决策
- cosine 存为整数 ×100（2 位精度），与 drug_neighbors 格式对称
- 发现并修复过滤 bug：`-666` 符号漏网（过滤规则加「必须字母开头」）

**生物学验证**：KRAS→NRAS(1.00), HOTAIR→HOXC10/HOXA5(0.60), BRCA1→BRCA2(0.79)，全部符合预期。

详见 `report/3_gene_index.md`。

---

## 2026-04-07 (19:20~20:30)

### 新增 `index/drug_index.py`

新建 `script/PxFquery/index/` 模块，实现 `DrugIndex` 类：

- `lookup(name)` — alias → BRD-id，大小写不敏感
- `lookup_aliases(names)` — 依次尝试候选名（为 LLM fallback 准备接口）
- `neighbors(brd_id, min_tanimoto=0.3)` — 返回结构近邻列表，`(BRD-id, tanimoto)` 格式

读取约定（drug_neighbors.json 紧凑格式）：
- key 和 neighbor id 均无 `BRD-` 前缀，读时自动补回
- tanimoto 存为整数 ×100，读时 `/100` 还原
- 近邻列表已按 tanimoto 降序排列，`break` 即可截断

TODO 注释已写入文件，说明 `llm_normalize_drug` fallback 的接入位置和完整规范。

---



## 2026-04-06 (17:10) ~ 07 (03:10)

### 2_cp_index 步骤完成（药物索引构建）

**产出文件**：

| 文件 | 大小 | 说明 |
|------|------|------|
| `output/table/cp_meta_enriched.csv` | — | 6647行，smiles命中79.9% |
| `output/store/query_index/drug_index.json` | 176 KB | 5958条别名倒排 |
| `output/store/query_index/drug_neighbors.json` | 4.4 MB | 5314个药物 top-50 Tanimoto近邻 |

**脚本修复**（`script/word_new/2_cp_index/build_drug_index.py`）：
- PubChem URL 去掉非法 property `CID`
- 响应 key 从 `IsomericSMILES` 改为 `SMILES`
- 输出格式优化：去 BRD- 前缀 + tanimoto 整数化（16.1 MB → 4.4 MB）

详见 `report/2_cp_index.md`。

## 2026-04-10

### Act-1 追加：Forward 性能与验证可见性增强

**问题定位（按用户要求只做单条诊断）**
- 脚本：`script/word_new/6_llm_resovler/run_forward_question_suite.py`
- 旧单条（Q1, no-summary）约 79.8s，用户反馈不可接受。
- 诊断结论：
  - 一部分来自 LLM 延迟（`llm_parse_intent` / `llm_map_cell_line`）
  - 更大问题来自 resolver 证据收集阶段反复全表扫描（pair 检查频繁）

**核心修复**
- 文件：`script/PxFquery/query/resolver.py`
  - 新增 engine 级 pair lookup 缓存：`(cell, pert|cmap) -> query_name`
  - `_has_pair` / `_query_name_for_pair` 改为字典查找，避免重复 DataFrame 全表筛选
  - 新增证据预算默认值（避免候选无限堆积）：
    - `max_forward_evidence=15`
    - `forward_budget_exact=1`
    - `forward_budget_proxy_pert=4`
    - `forward_budget_proxy_cell=4`
    - `forward_budget_proxy_both=6`
  - `resolver_meta` 增加 `evidence_policy`，便于解释策略

- 文件：`script/word_new/6_llm_resovler/run_forward_question_suite.py`
  - 支持参数：`--limit`、`--ids`、`--no-summary`、`--output-tag`
  - 默认 `--limit=3`，避免误跑大批量
  - 增加每条 query 总耗时与 prompt 分项耗时统计
  - 扩展问题集，加入“未知细胞系/疾病背景/不存在基因/不存在药物”等场景

**实测结果（MiniMax-M2.7）**
- 单条 Q1（no-summary）
  - 修复前：~79.8s
  - 修复后：~9-12s
  - 输出：
    - `output/store/resolver_demo/forward_question_suite_minimax_single_fastcheck.json`
    - `report/6_llm_resovler_forward_question_suite_minimax_single_fastcheck.md`

- 小批量 3 条（no-summary）
  - 输出：
    - `output/store/resolver_demo/forward_question_suite_minimax_quick3.json`
    - `report/6_llm_resovler_forward_question_suite_minimax_quick3.md`
  - 观察：疾病背景 / 模糊细胞上下文仍主要受 `llm_map_cell_line` 延迟影响

**新增/补跑演示（用户点名）**
- `demo_cellline_stepwise.py` 已补跑多场景（4 个 context）
  - `report/6_llm_resovler_cellline_stepwise_demo.md`
- `demo_external_apis.py` 已实跑 PubChem + Cellosaurus
  - `report/6_llm_resovler_external_api_demo.md`

**文档更新**
- `script/word_new/6_llm_resovler/README.md` 已重写为中文详细版：
  - 运行顺序、参数说明、性能解释、外部 API demo、默认证据策略、Plan-Act 建议


## 2026-04-10（追加）

### 性能优化第二轮：5 秒目标对齐

**新增优化**
- `script/PxFquery/query/resolver.py`
  - 新增本地快速意图解析 `_fast_parse_intent()`（forward 常见句式优先）
  - 新增生物上下文快速节点选择 `_fast_choose_option()` + `_smart_choose_cell_node()`（LLM 兜底）
  - 新增 prompt 级缓存 `_prompt_cache` 与 intent 缓存 `_intent_cache`
  - 缩写词支持：`NSCLC`、`TNBC`

- `script/PxFquery/llm/prompts.py`
  - 轻任务（intent/map）默认 `use_reasoning=False`
  - summary 任务保留 `use_reasoning=True`
  - `llm_parse_intent` 增加失败重试（先快后稳）
  - 分任务收紧 `max_tokens`，降低延迟

**关键结果**
- `run_forward_question_suite.py --limit 3 --no-summary`
  - 输出：`output/store/resolver_demo/forward_question_suite_minimax_quick3_fastv2.json`
  - 实测：Q1/Q2/Q3 分别约 `0.63s/0.09s/0.09s`
  - `prompt_timing_total` 为空，表示此批问题走本地快速路径，无需 LLM 往返

**过程文件**
- 新增任务看板：`report/todolist.md`


## 2026-04-10（追加2）

### 语义一致性与可追踪性修复

- 修复 `stepwise demo` 与生产路径不一致问题：
  - `demo_cellline_stepwise.py` 改为复用 resolver 的实际选择逻辑（fast_rule + LLM fallback），并在 trace 中标记 `source`。
  - 修复 NSCLC/colorectal 上下文映射偏差：
    - 增加上下文归一化（`NSCLC`/`TNBC`/`colorectal`/`colon`）
    - 对 `carcinoma` 等泛词降权，避免误选。

- 修复扰动类别误判：
  - `resolver.py` 新增 `_infer_pert_class_and_desc()`，使用关键词 + drug index 命中进行 `drug/genetic` 判定。
  - 结果：药物 query 不再误走 `xpr/sh`，可正确走 `cp`。

- 增强鲁棒性：
  - `prompts.py::_chat_text` 增加 3 次重试（应对 MiniMax 偶发 5xx/520）。

- 可复现实验脚本：
  - 新增 `script/word_new/6_llm_resovler/verify_resolver_cases.py`，覆盖基因/疾病背景/药物 query。

- suite 归档整理：
  - `run_forward_question_suite.py` 输出改为时间戳文件名并写入统一目录：
    - `report/6_llm_resovler_suite_runs/`
    - `output/store/resolver_demo/suite_runs/`
  - 并生成索引：`report/6_llm_resovler_suite_runs/README.md`


## 2026-04-10（追加3，收敛更新）

### 用户关切对齐
- 引入 resolver 双模式：
  - `always_llm`（默认）
  - `hybrid_fast`（容灾/低成本）
- `hybrid_fast` 下，当 LLM 调用失败会 warning 并自动降级（非静默）。
- 新增每次查询真实 LLM 调用统计：`resolver_meta.llm_call_stats`（query/total 计数 + 耗时）。
- 新增 logger 基础能力：`log_level` 可配，输出解析开始/结束、命中层、分流信息。

### 药物/遗传分流修复
- 修复“药物 query 误走 xpr/sh”问题。
- 典型验证：
  - `erlotinib treatment` -> `pert_type=cp`
  - `EGFR inhibitor` -> `pert_type=cp`
  - `l-theanine-like perturbation` -> drug 语义路径优先（无命中则 `NOT_FOUND`）

### 交互式验证
- 新增 `script/word_new/6_llm_resovler/Resolver_Workbench.ipynb`（按 block 验证）。
- 新增 `check_llm_stability.py`（LLM 稳定性检查）。

### Stepwise 与文档一致性
- `demo_cellline_stepwise.py` 复用生产选择逻辑并记录 `source`。
- 修复 NSCLC / colorectal 上下文选择偏差（归一化 + 泛词降权）。

### Suite 归档
- `run_forward_question_suite.py` 输出统一到：
  - `report/6_llm_resovler_suite_runs/`
  - `output/store/resolver_demo/suite_runs/`
- 文件名加时间戳，保证新对话可追踪顺序。

### MiniMax highspeed 实测
- 中国区 `https://api.minimaxi.com/v1` 已测：
  - `MiniMax-M2.7-highspeed` 返回 token plan 不支持（2061）
  - `M2.7-highspeed` 返回未知模型（2013）
  - `MiniMax-M2.7` 可用

## 2026-04-10（logger 系统重构）

### 目标对齐（本轮只做 logger）

- 统一日志模块/级别/格式/开关；
- 增加 `verbosity`（`quiet`/`normal`/`debug`）；
- 增加 LLM 输入输出内容暴露开关（默认关闭，debug 可开）；
- 支持按日期命名写日志文件；
- 保留 `resolver_meta.llm_call_stats` 并在日志中加入 `query_id` 追踪。

### 代码变更

- `script/PxFquery/logging_utils.py`（新增）
  - `LoggingSettings` + `configure_logger()` 统一配置
  - 日志格式统一为：`time | level | module | qid | message`
  - 文件日志命名：`<prefix>_YYYY-MM-DD.log`

- `script/PxFquery/query/resolver.py`
  - 替换为统一 logger
  - 新增 query 级 `query_id`（写入日志 + `resolver_meta.query_id`）
  - 保留并打印 `resolver_meta.llm_call_stats`
  - 新增配置字段：
    - `verbosity`
    - `log_enabled`
    - `log_to_file`
    - `log_dir`
    - `log_file_prefix`
    - `log_llm_io`（默认 `None`，debug 自动开启）
  - `log_llm_io=True` 时可在 debug 级记录 LLM 入参与返回摘要

- `script/PxFquery/core.py`
  - `enable_resolver()` 新增参数透传：
    `verbosity/log_enabled/log_to_file/log_dir/log_llm_io`
  - 保留原 API，不移除旧参数
  - 统一核心输出到 logger（替换 print）

- `script/PxFquery/llm/client.py`
  - 统一到 `pxfquery.llm` logger
  - health_check 与异常路径改为结构化日志输出

### 最小验证命令与结果摘要

1) 语法编译  
`D:\Softwares\s4_code\anaconda\envs\pxfquery\python.exe -m compileall script\PxFquery`  
结果：PASS（`logging_utils.py`、`resolver.py`、`llm/client.py` 编译成功）

2) resolver 四层命中回归（mock，无外部 API）  
`D:\Softwares\s4_code\anaconda\envs\pxfquery\python.exe script\word_new\6_llm_resovler\test_forward_matrix.py`  
结果：PASS（7/7 用例通过，日志输出包含 `qid=...`）

3) 文件日志与日期命名验证  
在 `provider=mock` + `log_to_file=True` 条件下执行单次 query。  
结果：生成 `workspace/report/04_management/logs/pxfquery_2026-04-10.log`，内容包含 `qid=q20260410-...`。

