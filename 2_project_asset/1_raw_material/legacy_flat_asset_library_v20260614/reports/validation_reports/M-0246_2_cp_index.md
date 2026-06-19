# 2_cp_index 运行分析报告

**时间**: 2026-04-06 ~ 2026-04-07 02:51  
**执行步骤**: pubchem → fingerprint → index (all)  
**总耗时**: 14842.5s（约 4.1 小时）  
**退出码**: 0（成功）

---

## 输出统计

| 文件 | 路径 | 规模 |
|------|------|------|
| 药物元数据增强版 | `output/table/cp_meta_enriched.csv` | 6647 行 |
| 别名倒排索引 | `output/store/query_index/drug_index.json` | 5958 条 |
| Tanimoto 近邻 | `output/store/query_index/drug_neighbors.json` | 5314 个药物 |

---

## Step 1+2: PubChem 查询

| 指标 | 数值 |
|------|------|
| cp_meta_unique.csv 总药物 | 34,419 |
| 有真实名字（非 BRD-only） | 6,647 (19.3%) |
| PubChem SMILES 命中 | 5,314 (79.9%) |
| 查询失败（404/网络） | 1,333 (20.1%) |

命中率 79.9%，高于预期区间 60–80% 上限，数据质量良好。

**异常区段**：[2400→2700] 共 300 条仅新增 17 个 SMILES（命中率约 6%），
推测是一批命名规范特殊的化合物（立体化学前缀、非标准命名），PubChem 无法识别。

**耗时说明**：理论 6647×0.2s≈22min，实际 4.1h。
差距来自国内网络访问 PubChem 延迟高，实际每条约 2.2s。

---

## Step 3+4+5: Morgan 指纹 + Tanimoto 近邻

| 指标 | 数值 |
|------|------|
| 有效 SMILES 输入 | 5,314 |
| 指纹计算成功 | 5,314 (100%) |
| Tanimoto 矩阵规模 | 5314×5314 |
| 矩阵最大值 | 1.000（存在完全相同结构） |
| 有近邻的药物 | 5314/5314 (100%) |

所有药物均找到至少 1 个 tanimoto > 0 的近邻，覆盖率完整。

---

## Step 6: 别名倒排索引

| 指标 | 数值 |
|------|------|
| 索引条目数 | 5,958 |
| 同名冲突（保留先出现）| 868 |

冲突率约 14.6%，说明有相当数量别名被多个 BRD-id 共用（化合物命名不唯一）。

---

## Bug 修复记录（运行前已修复）

本次运行前第一次尝试因脚本两处 bug 导致全量写入 smiles=None：

1. **PubChem URL 含非法 property `CID`** → URL 改为只请求 `IsomericSMILES,InChIKey`
2. **响应 key 不匹配**：脚本写 `props.get("IsomericSMILES")`，但 API 实际返回 key 为 `SMILES` → 改为 `props.get("IsomericSMILES") or props.get("SMILES")`

## 运行后优化（脚本已同步）

`drug_neighbors.json` 输出格式经三步压缩，已同步回 `build_drug_index.py`：

| 版本 | 变更 | 大小 |
|------|------|------|
| 初始输出 | `{"brd":..., "name":..., "tanimoto":0.5357}` | 16.1 MB |
| 去掉 name 字段 | `{"brd":..., "t":0.54}` | 8.9 MB |
| 去 BRD- 前缀 + t 整数化 | `["K62309135", 54]` | **4.4 MB** |

读取约定：key/neighbor_id 补回 `"BRD-"` 前缀；`t / 100` 还原 tanimoto 值。

---

## 输入

- `input/cp_meta_unique.csv`: 34419 行，80.7% 为 BRD-only

---

## 数字资产后探索

### 文件格式与内存

| 文件 | 磁盘 | Python 内存（估算）| 说明 |
|------|------|--------------------|------|
| `drug_index.json` | 176 KB | ~3 MB | name→BRD 正查字典 |
| `drug_neighbors.json` | 8.9 MB（优化后）| ~45 MB | BRD→近邻列表 |
| `cp_meta_enriched.csv` | — | 按需加载 | 不常驻内存 |

`drug_neighbors.json` 经两轮压缩：
- 初版（含 name 字段）: 16.1 MB
- 去掉 name 字段: 8.9 MB
- 去掉 BRD- 前缀 + tanimoto 存整数×100: **4.4 MB**（最终版）

最终格式：`{"A08715367": [["K62309135", 54], ...]}` （key/value 均去掉 BRD- 前缀，读时补回；54 表示 tanimoto=0.54）

### drug_index.json 的别名覆盖能力

`drug_index.json` 本身就是**所有已知别名的倒排索引**（包括商品名、研究代号等），
查询时只需 `user_input.lower()` 直接命中，无需 LLM 标准化。

覆盖不到的边缘情况（需要 LLM fallback 模块，待实现）：
- 拼写错误
- 用靶点描述代替药名（如"EGFR inhibitor"）
- 极冷僻别名、缩写

**设计决策**：在 resolver 中，当 `drug_index` 查不到时，增加可选的 LLM+PubChem fallback：
LLM 将用户输入标准化为规范名 → 再次查 PubChem → 获取 BRD-id。此为增强功能，非当前瓶颈。

### Tanimoto 值的实际意义

tanimoto 不只是排序用，有药学意义：

| 阈值 | 占比（当前50邻居内）| 含义 |
|------|---------------------|------|
| > 0.3 | 24.6% | 弱相似，可作为代理参考 |
| > 0.5 | 6.3% | 中等相似 |
| > 0.7 | 2.3% | 结构高度相似，可信代理 |

resolver 使用时建议设阈值过滤（如 > 0.3），避免将完全不相关的化合物作为代理。
tanimoto 值同时作为 hit_level 置信度的辅助信号。

### 邻居数分布

- 5313/5314 个药物满 50 个邻居（k=50），几乎全满
- 最低 48 个邻居
- 原因：化学空间密集，tanimoto > 0 的邻居远超 50，截断 k=50 是合理上限
