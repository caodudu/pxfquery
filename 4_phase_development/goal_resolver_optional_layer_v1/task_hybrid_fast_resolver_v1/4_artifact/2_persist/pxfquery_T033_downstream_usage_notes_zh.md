# pxfquery-T-033 下游使用说明

`pxfquery-T-033` 是一个可选的混合快速解析器元数据层。它不属于确定性里程碑主链的硬依赖，但如果可用，后续 demo 或 merge 任务可以消费它。

## 功能

- 按引用读取 T-027 runtime query indexes。
- 按引用读取 T-028 function index。
- 支持 exact perturbation/cell 解析。
- 支持存在索引证据时的 proxy cell / proxy perturbation 解析。
- 对 no-hit perturbation 返回显式 `NOT_FOUND`，保留 T-031 guard 语义。
- 在结果元数据中包含 T-032 风格的 guard metadata 证据。

## 导入方式

```python
from pxfquery_T033_hybrid_fast_resolver import HybridFastResolver

resolver = HybridFastResolver()
result = resolver.resolve("EGFR/A549/xpr")
print(result.to_dict())
```

从 `3_execution/` 运行，或把该目录加入 `PYTHONPATH`。

## 验证命令

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/run_examples.py
```

该命令会写出 exact / proxy / not_found 三个 JSON 证据和一个总 metadata JSON。

## 当前验证结果

- exact: `EGFR/A549/xpr` -> `found=true`, `hit_level=EXACT`。
- proxy: `TP53/breast/xpr` -> `found=true`, `hit_level=PROXY_CELL`, `used_cell=BT20`。
- not_found: `NONSENSE_ZZZ999/UNKNOWN_CELL/xpr` -> `found=false`, `hit_level=NOT_FOUND`。

## 范围

这是 T-033 任务范围内的修复版本地资产，不修改 T-027、T-028、T-031、T-032 或其他已完成上游产物。
