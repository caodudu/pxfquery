# 5_function_index 执行日志

**执行时间**：2026-04-08

---

## 产出文件

| 文件 | 大小 | 说明 |
|------|------|------|
| `output/store/query_index/function_index.json` | 25.5 KB | 91 个功能基因集索引 |
| `script/PxFquery/index/function_index.py` | — | FunctionIndex 类 |

---

## 关键统计

| 指标 | 数值 |
|------|------|
| var_names 总数 | 91 |
| MSigDB Hallmark | 50 |
| 3CA MPS v1 | 41 |
| aliases 条目总数 | 243（自动 180 + curated 96） |

---

## 设计决策

### 单一 JSON 结构

与 drug/gene/cellline 索引不同，function_index 将 var_names、meta、aliases 合为一个文件（25.5 KB）。91 个条目足够小，无需拆分。

### labels 规范化

- **HALLMARK_\*** ：去掉前缀，下划线分词，保留既有缩写大写（G2M, E2F, MYC, KRAS, TGF, TNFA, PI3K, AKT, MTORC1, ROS, UV, DNA, WNT, IL2, IL6）
- **MP\*** ：提取 `MP(\d+)\s+(.*)` 中的描述部分，修正 typo（"Cylce" → "Cycle"），去首尾空格
- MP* 原始 var_name 含冗余空格（如 `"MP4  Chromatin "`），保留精确原文作为 key，label 层做清洁展示

### aliases 优先级

自动生成（低优先级）被 curated 覆盖（高优先级）。
歧义处理：`"hypoxia"` → `HALLMARK_HYPOXIA`（Hallmark 更通用）；MP6 专用别名 `"mp6 hypoxia"` → `MP6 Hypoxia`。

### FunctionIndex 类接口

```python
idx.lookup("emt")              # → 'HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION'
idx.lookup("cell cycle g2/m")  # → 'MP1  Cell Cycle - G2/M'
idx.validate(var_name)         # → bool
idx.label(var_name)            # → human-readable label
idx.source(var_name)           # → 'hallmark' | '3ca_mps'
idx.for_llm()                  # → 91 行格式化列表，供 llm_map_function 使用
```

`for_llm()` 输出格式（`[H]`=hallmark，`[M]`=3ca_mps）：
```
  1. [H] Adipogenesis                              |  HALLMARK_ADIPOGENESIS
...
 51. [M] Cell Cycle - G2/M                         |  MP1  Cell Cycle - G2/M
```

---

## 验证

11 项 lookup 测试全部 PASS，覆盖：
- emt / apoptosis / oxphos / p53 / myc / g2m / hypoxia / upr
- MP 条目（cell cycle g2/m、respiration）
- 直接传入 var_name 的回查

---

## 后续接入（6_llm_resolver TODO）

- `FunctionIndex.lookup(user_input)` → 命中则直接用
- 未命中 → `llm_map_function(user_desc, idx.for_llm())` → 返回 var_name（或多个，多功能目标）
- 反向查询结果过滤：展示时用 `idx.label(vn)` 替代原始 var_name，更可读
