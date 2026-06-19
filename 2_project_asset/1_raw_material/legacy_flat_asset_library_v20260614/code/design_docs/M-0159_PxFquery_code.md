> 说明（2026-04-10）：本文件保留为来源设计稿。
> 工作区主版本请优先阅读：`workspace/context/deep_dive/02_code_design_workspace.md`

# PxFquery — 包开发指南

> 给 Claude Code 用的上下文文件  
> 语言：Python，面向对象（OOP）

---

## 包结构

```
PxFquery/
├── __init__.py
├── core.py             # PxFquery 主类，统一入口
├── utils.py            # 基础工具（fuzzy_match, cosine_similarity）
├── pyproject.toml
│
├── data/
│   └── loader.py       # 加载 h5ad 矩阵，支持1-3个同时加载
│
├── index/              # 查询索引模块【待实现】
│   ├── cellline_index.py    # 细胞系层次树查找
│   ├── gene_index.py   # 基因索引 + genePT近邻
│   └── drug_index.py   # 药物别名索引 + Morgan指纹近邻
│
├── query/
│   ├── resolver.py     # 三元组解析器（核心流程）【待实现】
│   ├── forward.py      # pert2func 查询逻辑（基础版已完成）
│   └── reverse.py      # func2pert 查询逻辑（基础版已完成）
│
├── llm/
│   └── prompts.py      # 所有LLM调用，每个独立函数【待实现】
│
└── viz/
    └── plots.py        # 可视化（条形图、热图、排名表）
```

---

## 三元组解析架构（核心设计）

查询本质是补齐三元组 `(B, P, F)`：
- 正向查询：已知 `(B, P)` → 查 `F`
- 反向查询：已知 `(B, F)` → 查 `P`

分两层：

### 层1：意图解析（LLM，1次调用）

```
用户自然语言
  → {query_type, B描述, P描述, F描述, pert_class}

pert_class 判断规则（LLM执行）：
  "EGFR" / "knockdown" / "knockout" / "overexpression" → genetic（查xpr+sh合并）
  药物名 / "inhibitor" / 化合物名 → drug（查cp）
```

### 层2：键定位（索引，保证落到库内键）

**B（细胞系）定位**：

```
cellline_tree.json（lineage → disease → subtype → [cell_inames]）

用户描述 → LLM选lineage/disease节点 → 候选细胞系列表

命中优先级：
  L1: 精确匹配 cell_iname → EXACT
  L2: 同 subtype 的细胞系
  L3: 同 primary_disease 的细胞系
  L4: 同 lineage 的细胞系
```

**P（遗传扰动/基因）定位**：

```
gene_index.json（symbol/alias → pert_id）
gene_neighbors.json（genePT预计算近邻）

genePT近邻计算规则：
  - 18080个人类基因，各自在"矩阵内存在的基因"（~6959个）里找top-50近邻
  - 近邻按cosine similarity排序
  - 预计算一次，离线存JSON

命中优先级：
  L1: (指定细胞系, 指定基因) 存在 → EXACT
  L2: (指定细胞系, genePT近邻基因[1..50]) 依次检查是否存在
  L3: (相似细胞系L2-L4, 指定基因) 是否存在
  L4: (相似细胞系L2-L4, genePT近邻基因) 组合检查

注意：对于L2-L4命中的，全部汇总提供给LLM，LLM说明用了哪些代理及理由
不做单一"最优"选择，提供所有命中的证据，由LLM综合总结
```

**P（药物）定位**：

```
drug_index.json（别名倒排索引）
drug_neighbors.json（Morgan指纹预计算近邻）

drug_neighbors计算规则（需要cp_meta_enriched.csv）：
  1. 从cp_meta_unique.csv出发，批量查PubChem获取SMILES
  2. 用RDKit计算Morgan指纹（ECFP4，radius=2）
  3. 两两Tanimoto系数，每个药物保留top-50近邻
  4. 只保留"有真实名字"的药物（过滤BRD-only）

药物名解析流程（在进入命中优先级之前）：
  Step1: user_input.lower() → 查 drug_index.json → 找到 BRD-id → 直接进入命中检查
  Step2: 未找到 → llm_normalize_drug(user_input) → 返回标准化候选名列表
           → 依次查 drug_index.json → 找到则继续
  Step3: 仍未找到 → 实时查 PubChem（候选名 → InChIKey）
           → 与 cp_meta_enriched.csv 的 inchikey 列做精确匹配 → 找到 BRD-id
  Step4: 全部失败 → 返回 not_found，LLM总结说明

命中优先级（与基因类似）：
  L1: (指定细胞系, 指定药物) 存在 → EXACT
  L2: (指定细胞系, Morgan近邻药物[1..50]) 依次检查，tanimoto阈值 > 0.3
  L3: (相似细胞系, 指定药物)
  L4: (相似细胞系, Morgan近邻药物) 组合检查

同样汇总所有命中，交给LLM综合
```

### hit_level（命中级别，传递给LLM总结用）

- `EXACT`：精确命中
- `PROXY_CELL`：细胞系做了替代
- `PROXY_PERT`：扰动做了近邻替代（基因近邻或药物近邻）
- `PROXY_BOTH`：两个维度都做了替代

LLM总结时需标注是精确结果还是近似证据，并说明替代理由。

---

## LLM 调用设计（每个独立函数，方便修改prompt）

```python
# llm/prompts.py

def llm_parse_intent(client, model, user_input) -> dict
    # 提取 query_type, B描述, P描述, F描述, pert_class(genetic/drug)

def llm_map_cell_line(client, model, bio_desc, lineage_nodes) -> str
    # bio_desc: "非小细胞肺癌" → 选择最匹配的 lineage/disease 节点名

def llm_map_gene(client, model, gene_desc, gene_candidates) -> str
    # gene_desc: "EGFR" / "ErbB1" / "表皮生长因子受体" → 标准gene symbol

def llm_map_drug(client, model, drug_desc) -> list[str]
    # 输入是描述性文本（如"EGFR抑制剂"）→ LLM推断具体药物名列表
    # 用于用户未提供具体名字时，由LLM知识补全候选药物

def llm_normalize_drug(client, model, drug_name) -> list[str]
    # 输入是具体药物名但 drug_index 查不到时的 fallback
    # → 返回该药物的标准化候选名（INN名、英文通用名等）
    # 例：输入"厄洛替尼" → ["erlotinib"]，"Tarceva" → ["erlotinib"]
    # 候选名再依次查 drug_index，或走 PubChem InChIKey 匹配

def llm_summarize_forward(client, model, result) -> str
    # 基于ForwardResult生成≤200字总结，标注hit_level和代理理由

def llm_summarize_reverse(client, model, result) -> str
    # 基于ReverseResult生成≤200字总结，标注hit_level和代理理由
```

---

## 数字资产构建（独立脚本，和包解耦）

脚本位置：`script/build_index/`

| 脚本 | 输入 | 输出 | 状态 |
|------|------|------|------|
| `build_cellline_tree.py` | cellline_meta_sub.csv | cellline_tree.json | ⬜ |
| `build_gene_index.py` | gene_info_beta.csv + xpr/sh h5ad + genePT npz + gene_names.csv | gene_index.json + gene_neighbors.json | ⬜ |
| `build_drug_index.py` | cp_meta_unique.csv + PubChem API | cp_meta_enriched.csv + drug_index.json + drug_neighbors.json | ⬜ |

构建结果存于：`output/store/query_index/`

### build_drug_index.py 流程

```
Step1  读取 cp_meta_unique.csv（34k药物）
Step2  过滤有真实名字的药物（19.3% ≈ 6642个）
Step3  批量查 PubChem API（按药物别名查SMILES）
       写入 cp_meta_enriched.csv（增加smiles, inchikey, pubchem_cid列）
Step4  用 RDKit 计算 Morgan 指纹（ECFP4, radius=2, nBits=2048）
Step5  Tanimoto 系数两两计算（6642×6642，可用矩阵操作加速）
Step6  每个药物保留 top-50 近邻，存 drug_neighbors.json
Step7  别名倒排索引，存 drug_index.json
       格式：{"erlotinib": "BRD-K70301465", "tarceva": "BRD-K70301465", ...}
```

### build_gene_index.py 流程

```
Step1  读 gene_names.csv（注意：第一行是列名，本身也是基因，共18080个）
Step2  读 xpr + sh h5ad，取 union 得到矩阵内基因集合（~6959个）
Step3  从 genePT npz 中提取矩阵内基因的向量
Step4  对18080个基因，在矩阵内6959个基因里各自找 top-50 cosine 近邻
Step5  存 gene_neighbors.json：{"EGFR": ["ERBB2","MET",...], ...}
Step6  读 gene_info_beta.csv，构建 symbol/alias → pert_id 倒排
       存 gene_index.json
```

---

## 数据说明

- 三个 h5ad：obs=扰动实验（n≈201k），var=功能基因集（91个）
- obs字段：`sig_id`, `project_code`, `cell_iname`, `pert_id`, `cmap_name`, `pert_dose`, `pert_time`
- **矩阵稀疏性**：cell × gene 和 cell × drug 大量组合不存在
- genePT：18080基因×1536维（ada-002版），gene_names.csv第一行是列名本身也是基因
- cp矩阵：80.7%药物只有BRD编号，反向查询结果过滤这些，只展示有真实名字的

---

## 开发优先级

1. ✅ 包框架（loader / forward / reverse / viz）
2. ✅ 基础查询跑通（无索引版，已测试）
3. ⬜ `script/build_index/build_drug_index.py`（PubChem + Morgan + Tanimoto）
4. ⬜ `script/build_index/build_gene_index.py`（genePT近邻）
5. ⬜ `script/build_index/build_cellline_tree.py`
6. ⬜ `index/` 模块（加载JSON，提供查询接口）
7. ⬜ `query/resolver.py`（三元组解析器）
8. ⬜ `llm/prompts.py`（独立函数形式）
9. ⬜ 完整自然语言查询跑通
10. ⬜ Streamlit demo
11. ⬜ PyPI打包

---

## 当前实现状态补丁（2026-04-10）

- `index/` 已落地：`cellline_index.py`、`gene_index.py`、`drug_index.py`、`function_index.py`
- `query/resolver.py` 已落地并支持两种模式：
  - `always_llm`（论文叙事）
  - `hybrid_fast`（容灾/速度）
- `llm/prompts.py` 已成为 resolver 主用 LLM 层；`llm/client.py` 作为旧接口兼容保留
- Resolver 报告请优先读：
  - `workspace/report/03_resolver/06_suite_runs/`
  - `workspace/report/00_index/latest_reports_index.md`

---

## 注意事项

- LLM只做意图解析和文字生成，不参与计算
- 每个LLM调用独立函数，集中在 `llm/prompts.py`
- xpr+sh 未明确指定时合并查询；cp 单独
- 近邻命中全部汇总，不做单一最优选择，交LLM综合说明
- 反向查询结果过滤BRD-only药物（80.7%）
- 所有公开接口有docstring

---

*v3 | 修正药物嵌入方案（Morgan指纹+Tanimoto）、基因近邻策略、近邻命中处理方式*


