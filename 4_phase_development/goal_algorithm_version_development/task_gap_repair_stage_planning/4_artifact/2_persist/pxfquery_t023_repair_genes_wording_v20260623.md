# PxFquery 缺口修复方案与 Genes 措辞对照

生成时间: 2026-06-23
来源任务: T-023 gap_repair_stage_planning
参考数据: T-012 Genes 论文可交付物措辞库

---

## 一、工具整体定位措辞

| 阶段 | 修复内容 | 论文措辞建议 | Genes 参照模式 |
|------|----------|-------------|---------------|
| 修复前 | 现状 | 不声称 PxFquery 有任何可用性 | — |
| 第1阶段后 | 索引恢复 + resolver 基础链路 | "PxFquery integrates pre-built indexes covering cell lines, drugs, genes, and 91 functional gene sets to enable perturbation-to-function query." | 模仿 software_package_or_tool 的 "we developed a ... tool" 模式；强调索引覆盖度 |
| 第2阶段后 | 未命中安全返回 | "The system returns explicit not-found results for unsupported (perturbation, cell) pairs, avoiding misleading false positives." | 参考 T-012 样本中常见的 limitation 声明模式："limitations include..." |
| 第3阶段后 | 反向查询稳健性 | "Reverse queries compute cosine similarity between target functions and all candidate perturbations, ranked with numerical stability safeguards." | algorithm_method 模式："we propose a computational framework...; the method identifies/ranks..." |

---

## 二、功能模块措辞

### 2.1 正向查询（Forward Query）

**功能描述:** 给定扰动（药物/基因）和生物学背景（细胞系），返回关联的功能程序变化

| 修复状态 | 措辞建议 |
|----------|----------|
| 当前可声称 | "Forward query maps a perturbation in a given cell context to a ranked list of activated and suppressed functional programs, based on precomputed LINCS-derived functional matrices." |
| 修复后增强 | "Forward query supports deterministic exact matching as well as proxy matching via cell-line similarity and perturbation neighbor indices." |

**Genes 可模仿句式:**
- "The system enables users to query which functional pathways are affected by a given perturbation in a specified biological context."
- "Results are serialized as structured tables with found/not-found status labels."

### 2.2 反向查询（Reverse Query）

**功能描述:** 给定希望激活/抑制的功能目标，返回候选扰动排序

| 修复状态 | 措辞建议 |
|----------|----------|
| 当前（partial） | "Reverse query identifies candidate perturbations whose functional profiles are closest to a desired target profile, computed via cosine similarity." |
| 修复后（CAP-06完成） | "Reverse query employs cosine similarity ranking with zero-norm filtering and numerical stability checks, producing reproducible candidate lists." |

**Genes 可模仿句式:**
- "To identify perturbations that may induce a desired functional response, the system computes pairwise cosine similarity between the target functional vector and all perturbation vectors in the matrix."

### 2.3 索引与解析层（Resolver/Index Layer）

**功能描述:** 自然语言解析 + 索引匹配 + 四层命中

| 修复状态 | 措辞建议 |
|----------|----------|
| 第1阶段后 | "The resolver layer maps natural-language queries to structured (cell, perturbation) pairs through a multi-stage index lookup: exact cell-perturbation match, perturbation-neighbor proxy, cell-neighbor proxy, and combined proxy." |
| 第2阶段后 | "When no valid (cell, perturbation) pair is found, the resolver returns a not-found status with a clear explanation, preventing spurious matches." |

**Genes 可模仿句式:**
- "The index system covers N cell lines, M drugs, G genes, and 91 functional gene sets, enabling rapid exact and near-neighbor retrieval."
- "Coverage statistics demonstrate that X% of cell-perturbation queries can be resolved within the first two hit levels."

### 2.4 自然语言入口（NL/LLM）

**谨慎措辞（当前 blocked）:**

| 阶段 | 措辞建议 |
|------|----------|
| 第1阶段后 | "Natural-language query parsing is provided as an optional convenience layer. The deterministic retrieval core operates independently of LLM availability." |
| LLM 验证后 | "An LLM-assisted intent parser converts free-text queries into structured (query_type, bio_context, pert_desc) triples, falling back to fast deterministic parsing when LLM is unavailable." |

**关键 Genes 模式:** 将 LLM/AI 功能描述为 "optional"、"convenience"、"assisted" 而非核心声称。参考 T-012 样本中 AI_agent_or_LLM_tool 类的谨慎措辞。

---

## 三、弱但可容忍的验证模式（参考 T-012）

根据 T-012 对 103 篇 Genes 论文的分析，以下是 PxFquery 可采用的验证程度（按投入递增）：

| 验证级别 | 典型做法 | PxFquery 适配 |
|----------|----------|--------------|
| 1. 功能演示 | 展示 1-2 个 case study 的输入输出 | 适配：EGFR/A549 forward + A549 apoptosis reverse |
| 2. 覆盖率统计 | 报告索引覆盖的细胞系/药物/基因/功能数量 | 适配：91 功能 × N 细胞系 × M 基因 × K 药物 |
| 3. 对比基准 | 与 1-2 个已有工具/方法做对比 | 可选：与原始 LINCS L1000 查询对比 |
| 4. 用户评测 | 用户试用反馈 | 不可行（非公开服务） |
| 5. 基准数据集评测 | 在标准数据集上做性能评估 | 可选但投入大 |

**建议:** 采用级别 1+2 即可满足 Genes 投稿要求。T-012 中许多被收录的工具类论文仅展示 1-2 个 case 加覆盖率统计。

---

## 四、常见局限声明句式（Genes 论文模式）

以下句式来自 T-012 措辞库，适合 PxFquery 在论文 Discussion 或 Limitations 中使用：

1. "The current version relies on precomputed functional matrices derived from a specific LINCS data release; results may differ with updated data."
2. "The natural-language parser is optional and its accuracy depends on the underlying LLM model; deterministic query paths remain available as fallback."
3. "Not all (perturbation, cell) combinations are represented in the current index; unmatched queries return explicit not-found status."
4. "The functional coverage is limited to 91 gene set programs (50 MSigDB Hallmark, 41 3CA MPS); broader functional annotation would require additional matrix columns."
5. "The system has been validated on the A549 lung cancer cell line as a representative case; generalization to other cancer types requires further testing."

---

## 五、交付物命名与描述模式

参考 T-012 中带命名交付物（如 DTVF、CrossMP、OHDLF、TExCNN 等）的论文模式：

**PxFquery 命名策略:**
- PxFquery 本身即为工具名，不需要另起 acronym
- 论文标题建议："PxFquery: A LINCS-Based Perturbation-to-Function Query Workflow for Interpreting Drug and Gene Induced Functional Programs"

**Genes 投稿中可量化的描述:**
> "PxFquery integrates 3 functional matrices covering 201,014 (CP), 189,365 (SH), and 132,464 (XPR) perturbation records across 91 functional gene set programs, enabling both forward and reverse perturbation-to-function queries through a deterministic index-based resolver."

---

*措辞仅描述当前已验证或规划修复后可验证的能力，不声称未经运行的 LLM/AI agent 能力。*