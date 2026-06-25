# pxfquery-T-028 功能索引包 — 下游使用说明

## 本包包含内容

`pxfquery_T028_function_index/function_index.json` 是 T-028 任务生成的经过验证的功能索引包。

**核心数据：**

| 字段 | 值 |
|---|---|
| 版本 | `pxfquery-T-028` |
| 功能术语数 | 91 个 MSigDB Hallmark 基因集术语 |
| 数据来源 | T-021 标准资源的 H5AD 矩阵（cp_func_ad/sh_func_ad/xpr_func_ad）的 `var_names` |
| 每术语别名数 | 2–3 个（自身、小写形式、可读标签） |
| 总别名字段数 | 273 |

**结构：**
```json
{
  "version": "pxfquery-T-028",
  "n_functions": 91,
  "var_names": ["HALLMARK_ADIPOGENESIS", "HALLMARK_ALLOGRAFT_REJECTION", ...],
  "aliases": {
    "HALLMARK_ADIPOGENESIS": ["HALLMARK_ADIPOGENESIS", "hallmark_adipogenesis", "Adipogenesis"],
    ...
  },
  "meta": { ... }
}
```

## 与上游的差异

| 方面 | 上游（T-021/D-004） | T-028（本包） |
|---|---|---|
| `aliases` | 小写→大写的 1:1 字符串映射 | 每术语含列表 [自身, 小写, 标签] |
| `meta` | 每术语 `{source, label}` 字典 | 任务元数据（谱系、种子来源、备注） |
| 验证 | 无 | 机器可读验证记录 |
| 谱系 | 无 | 记录了任务ID、矩阵来源、loader来源 |

上游 T-021 的 `function_index.json` 存在且结构完整；T-028 对其进行重新切片和增强。T-013 任务标记了迁移后查询索引目录中的 `function_index.json` 为缺失/不完整——此纠正后的本地版本填补了该缺口。

## 查询/解析器任务如何使用

```python
import json

with open("function_index.json") as f:
    fi = json.load(f)

# 遍历所有 91 个功能术语
for term in fi["var_names"]:
    aliases = fi["aliases"][term]  # [大写, 小写, 可读名]
    primary = aliases[0]           # 总是大写的矩阵变量名

# 查询特定术语的别名
aliases = fi["aliases"].get("HALLMARK_ADIPOGENESIS", ["HALLMARK_ADIPOGENESIS"])

# 将用户查询（小写或部分匹配）解析为规范术语
def resolve_term(query: str, fi: dict) -> str | None:
    query_lower = query.lower()
    for term, alias_list in fi["aliases"].items():
        if any(query_lower in a.lower() for a in alias_list):
            return term
    return None
```

## 下游消费者

本包适用于：
- `goal_resource_index_packs_v1` DAG 中需要经过验证的 91 项功能术语列表的查询/解析器任务
- 任何需要将功能术语解析为矩阵 `var` 列的任务
- 替代 T-021 的 `function_index.json` 作为功能术语查找的推荐运行时索引

**不要**直接读取旧的 T-021 `function_index.json` 用于运行时查询——优先使用本 `pxfquery-T-028` 包，它带有显式别名列表、验证证据和谱系信息。

## 验证证据

- `function_index.json`：7/7 项检查通过（JSON 加载、键存在、n=91、变量名匹配全部 3 个矩阵、别名覆盖全部术语、自身优先）
- `pxfquery_t028_function_index_validation.csv`：91 行，全部状态 OK
- `03_validation.json`：结构化机器可读验证记录
- `03_validation_summary.md`：人类可读摘要