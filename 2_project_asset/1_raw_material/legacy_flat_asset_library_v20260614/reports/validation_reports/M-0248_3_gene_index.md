# 3_gene_index 运行分析报告

**时间**: 2026-04-07
**执行步骤**: extract → index → neighbors → simplify
**总耗时**: ~92s（主任务 84.5s + simplify 7.6s）

---

## 输出文件总览

| 文件 | 路径 | 规模 | 磁盘 | 说明 |
|------|------|------|------|------|
| 嵌入矩阵（中间产物）| `output/store/genePT/gene_embedding_m3_filtered.npz` | 33791×3072 float32 | — | 一次性生成，可重复使用 |
| 基因名列表（中间产物）| `output/store/genePT/gene_names_m3_filtered.csv` | 33791 行 | — | |
| 完整基因索引 | `output/store/query_index/gene_index.json` | 78061 条 | 6.1 MB | 含 gene_type + in_matrix，lowercase key |
| 完整语义近邻 | `output/store/query_index/gene_neighbors.json` | 33791 个基因 | 21.8 MB | 含所有 Gencode 基因类型 |
| **简化基因索引** | `output/store/query_index/gene_index_simple.json` | 25036 条 | **356 KB** | pc/mir/snr/misc，uppercase key |
| **简化语义近邻** | `output/store/query_index/gene_neighbors_simple.json` | 30319 个基因 | **19.5 MB** | 排除 lncRNA query 基因 |

---

## Step 0：model-3 过滤提取

| 指标 | 数值 |
|------|------|
| model-3 原始基因数 | 133736（含大量废弃历史基因名） |
| 过滤目标（Gencode v49 ∪ 有效矩阵基因）∩ model-3 | **33791** |
| Gencode v49 基因数 | 77078 |
| 有效矩阵基因数 | 7965 |

---

## Step 1：gene_index.json（完整版）

**来源与条目数：**

| 来源 | 基因数 | 新增条目 |
|------|--------|----------|
| 有效矩阵基因（优先级1，in_matrix=True）| 7965 | 7965 |
| Gencode v49（优先级2）| 77078 | 69915 |
| gene_info_beta（优先级3）| 12327 | 181 |
| 合计 | — | **78061** |

**gene_type 分布（top-8）：**

| gene_type | 数量 |
|-----------|------|
| lncRNA | 34509 |
| protein_coding | 20047 |
| processed_pseudogene | 9479 |
| miRNA | 1877 |
| snRNA | 1837 |
| misc_RNA | 1275 |
| unprocessed_pseudogene | 1948 |
| transcribed_unprocessed_pseudogene | 1567 |

---

## Step 2：gene_neighbors.json（完整版）

| 指标 | 数值 |
|------|------|
| 近邻候选池 = 有效矩阵基因 ∩ model-3 | **7396** |
| 候选池 gene_type：protein_coding | 7126（96.3%） |
| 候选池 gene_type：lncRNA | 2（可忽略） |
| gene_neighbors 总条目 | 33791 |
| 满 50 个近邻 | 33791/33791（100%） |
| cosine_int 范围 | 43 ~ 100（即 0.43 ~ 1.00） |
| cosine ≥ 0.80 的近邻对 | 53119（3.1%） |
| cosine ≥ 0.60 的近邻对 | 672540（39.8%） |

**近邻生物学验证：**

| 基因 | top-3 近邻（cosine） | 生物学含义 |
|------|----------------------|------------|
| KRAS | NRAS(1.00), HRAS(0.76), SOS1(0.74) | RAS 家族 |
| TP53 | TP53BP2(0.73), TP53TG1(0.72), MDM4(0.71) | TP53 调控网络 |
| EGFR | EGF(0.73), EREG(0.73), AREG(0.73) | EGF 配体家族 |
| BRCA1 | BRCA2(0.79), RBBP8(0.72), BRD7(0.68) | DNA 修复同源基因 |
| HOTAIR | HOXC10(0.61), HOXA5(0.60), HOXA10(0.60) | HOTAIR 调控 HOX 基因 ✓ |

---

## Step 3：简化索引

**gene_index_simple.json（356 KB，原来 6.1 MB 的 5.7%）**

- Key：UPPERCASE symbol（resolver 查询前需 `.upper()`）
- Value：短类型码（pc / mir / snr / misc）
- 保留类型：protein_coding 20047、miRNA 1877、snRNA 1837、misc_RNA 1275
- 排除：lncRNA（34509）、pseudogenes（~15000）、snoRNA（792）、TEC（1017）等

**gene_neighbors_simple.json（19.5 MB）**

- 排除 lncRNA query 基因（3472 条）
- 保留 30319 个基因的近邻列表
- 近邻候选池不变（本就几乎全为 protein_coding）

---

## 有效矩阵基因过滤说明

| 过滤条件 | 类型 | 数量 |
|----------|------|------|
| 非字母开头（含 `-666`）| 异常符号 | 1 |
| `^[ACGTN]{4,8}$` | shRNA guide 序列 | 3816 |
| 含 `_` 或 `/` | 实验对照 | 7 |
| **过滤后有效** | | **7965** |

**关于 569 个无近邻的矩阵基因**：均为 `TRCN0000XXXXXX` shRNA 试剂 ID，非基因 symbol，无 model-3 嵌入，支持精确匹配但无法代理查询。

---

## 读取约定

```python
import json

# 完整版（小写 key，含 in_matrix）
idx = json.load(open("output/store/query_index/gene_index.json"))
entry = idx.get(user_input.lower())
# {"symbol": "KRAS", "gene_type": "protein_coding", "in_matrix": True}

# 简化版（大写 key，仅 pc/mir/snr/misc）
idx_s = json.load(open("output/store/query_index/gene_index_simple.json"))
entry_s = idx_s.get(user_input.upper())
# "pc"

# 近邻（两版格式相同）
nbrs = json.load(open("output/store/query_index/gene_neighbors.json"))
neighbors = nbrs.get(canonical_symbol, [])
# [["NRAS", 100], ["HRAS", 76], ...]  cosine = cosine_int / 100
```

---

## 下一步

- `index/gene_index.py`：实现 `GeneIndex` 类，封装查询接口
- `query/resolver.py`：三元组解析器，接入 GeneIndex
- `llm/prompts.py`：实现 `llm_map_gene()`，处理废弃基因名/拼写变体 fallback
