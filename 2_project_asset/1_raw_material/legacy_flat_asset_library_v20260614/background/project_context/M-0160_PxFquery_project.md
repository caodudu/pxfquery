> 说明（2026-04-10）：本文件保留为来源设计稿。
> 工作区主版本请优先阅读：`workspace/context/deep_dive/01_project_design_workspace.md`

# PxFquery — 项目总览

> 基于预计算功能矩阵的扰动查询工具，自然语言输入输出  
> 目标：MDPI SCI（毕业要求）| 时间窗口：~1周

---

## 项目阶段

| 阶段 | 状态 | 说明 |
|------|------|------|
| 数据资产（矩阵） | ✅ 完成 | 三个得分矩阵已跑完，h5ad格式 |
| 数字资产（查询索引） | 🔄 进行中 | cellline_tree / gene_index / drug_tree / 嵌入向量 |
| 包开发 | 🔄 进行中 | 框架已建，查询解析模块重构中 |
| 论文图表 | ⬜ 待做 | 见 figures 规划 |
| 论文写作 | ⬜ 待做 | — |

---

## 工具定位

- **本质目标**：发论文，不是给真实用户用
- **读者**：非扰动领域专家，门槛低
- **策略**：AI噱头 + 可视化丰富 + 内容看起来扎实 + 工作量可控

---

## 核心功能（两个查询方向）

**给定扰动 → 了解功能变化（正向查询 pert2func）**  
输入自然语言（如"A549里敲掉EGFR会影响哪些通路"），三元组解析定位数据，LLM总结功能后果。

**给定功能目标 → 推荐扰动候选（反向查询 func2pert）**  
输入自然语言（如"MCF7里抑制细胞周期并增强凋亡有哪些候选药物"），余弦相似度检索矩阵，LLM生成推荐理由。

**原则：LLM只负责解析意图和生成文字，不负责计算。计算全在矩阵层面完成。**

---

## 三元组模型（核心设计）

所有查询本质是三元组的补齐：`(生物背景 B, 扰动 P, 功能 F)`

- 正向查询：已知 `(B, P)` → 查 `F`
- 反向查询：已知 `(B, F)` → 查 `P`

**三元组解析分两层**：
1. **意图解析（LLM）**：自然语言 → 提取 B描述、P描述、F描述、扰动类型
2. **键定位（索引树）**：描述 → 映射到矩阵中存在的实际键（或最近邻代理）
标准化查询+最近邻代理
用户描述 → LLM 解析 → 标准化 → 近邻替代

**命中级别（hit_level）**：
- `EXACT`：直接精确命中
- `PROXY_CELL`：细胞系做了近邻替代
- `PROXY_PERT`：扰动做了近邻替代
- `PROXY_BOTH`：两个维度都做了近邻替代

LLM总结时标注是精确结果还是近似证据。

---

## 数据资产

| 项目 | 内容 |
|------|------|
| 来源 | LINCS L1000 Level 5 |
| 扰动类型 | XPR / SH / CP |
| 矩阵维度 | ~201,014 × 91（perturbation实验 × 功能条目） |
| 矩阵格式 | AnnData h5ad（obs含完整元数据） |
| 功能基因集 | MSigDB Hallmark + 3CA MPS v1，共91个 |
| 富集分析 | fgsea，得分 = NES × -log10(FDR+1e-10) |
| 元数据 | 见下方元数据说明 |

**矩阵的稀疏性**：cell × gene（xpr/sh）和 cell × drug（cp）都是高度稀疏的，
大量组合在矩阵中不存在，这是最近邻代理机制存在的根本原因。

---

## 数字资产（查询索引）

需要预先构建，存于 `output/store/query_index/` 或内置包中：

| 文件 | 内容 | 构建方式 |
|------|------|---------|
| `cellline_tree.json` | lineage→disease→subtype→cell_iname 层次树 | cellline_meta_sub.csv |
| `gene_index.json` | symbol/alias→pert_id，矩阵内存在的基因集合 | gene_info_beta.csv + xpr/sh矩阵 |
| `drug_tree.json` | target/moa/alias 层次树（用于beam search） | cp_meta_unique.csv + 外部知识 |
| `gene_embeddings.npz` | genePT语义向量（仅矩阵内存在的基因） | genePT数据 |
| `drug_embeddings.npz` | 药物语义嵌入（待定方案） | DrugBank/ChEMBL/LLM生成描述 |

---

## 技术选型

| 组件 | 方案 |
|------|------|
| 矩阵存储 | 本地h5ad → 未来Zenodo（有DOI） |
| Python包 | PyPI发布 |
| LLM接入 | openai SDK（兼容SiliconFlow等任意接口） |
| Web demo | Streamlit on HuggingFace Spaces |
| 可视化 | plotly（demo）+ matplotlib（论文） |

---

## 论文图表规划

| Figure | 内容 | 类型 |
|--------|------|------|
| Fig 1 | 工具整体框架示意图（三元组解析流程） | 示意图 |
| Fig 2 | 数据资产概览（三种扰动类型的矩阵分布/规模） | 统计图 |
| Fig 3 | 正向查询示例：给定扰动，Top激活/抑制功能条形图 | 条形图 |
| Fig 4 | 反向查询示例：给定功能目标，候选扰动排名 + 匹配热图 | 热图/表格 |
| Fig 5 | 多扰动比较：扰动×功能热图，展示工具批量分析能力 | 热图 |

---

## 待确认

- [ ] genePT 文件格式和覆盖范围
- [ ] 药物嵌入方案（DrugBank描述 vs 化学结构 vs LLM生成）
- [ ] PyPI包名（pxfquery是否被占用）
- [ ] Zenodo上传并获取DOI
- [ ] 论文投哪个MDPI子刊

---

*v4 | 增加三元组模型、数字资产规划、hit_level设计*

## Resolver Narrative Update (2026-04-10)

- The four-level labels (`EXACT`, `PROXY_PERT`, `PROXY_CELL`, `PROXY_BOTH`) are internal retrieval diagnostics, not the external scientific narrative.
- External narrative should be evidence-centric:
  1. Gather an evidence neighborhood around (B, P) from exact and proxy candidates.
  2. Integrate dual-source genetic evidence (`xpr + sh`) when applicable.
  3. Produce a single scientific interpretation with explicit evidence quality.
- Therefore, paper writing should present this as "neighborhood evidence integration with LLM synthesis", while keeping four-level tags as reproducibility/debug metadata.

## 文档与报告入口（2026-04-10 整理后）

- 工程约定：`D:\\Projects\\7_rush\\3_functional_query\\1_claude\\workspace\\WORKSPACE_CONVENTION.md`
- 报告入口：`D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\README.md`
- 最新有效报告索引：`D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\00_index\latest_reports_index.md`
- Resolver 时间戳归档（唯一事实源）：`D:\Projects\7_rush\3_functional_query\1_claude\workspace\report\03_resolver\06_suite_runs\`



