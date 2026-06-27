# T138 L1/L2 接续与资源格式审计

日期：2026-06-28

## 工作副本

T138 已从 T137 复制 package 工作副本：

```text
T137 source:
4_phase_development/goal_goal_ms8_human_usable_package/task_ms8_09_l1_real_llm_gate_repair/3_execution/03_package_source

T138 work copy:
4_phase_development/goal_goal_ms8_human_usable_package/task_ms8_10_l2_resource_routing_repair/3_execution/03_package_source_v2_l2
```

T137 原目录没有修改。T138 工作副本版本号已从 `0.5.1` 改为：

```text
0.5.2.dev0
```

## L1 当前接口

T137 的 L1 输出类型是 `pxfquery.l1_intent.schema.QueryIntent`。

主要字段：

```text
raw_query
normalized_query
query_type: forward | reverse
bio_context
pert_desc
pert_class: genetic | drug | None
genetic_modality
function_desc
activate
suppress
top_n
extracted_phrases
ambiguity_flags
missing_fields
parse_confidence
parse_method
provider_evidence
```

`QueryIntent.to_resolver_intent()` 会保留：

```text
query_type
bio_context
pert_desc
pert_class
function_desc
activate
suppress
top_n
```

L2 应承接 `QueryIntent`，不能让 L1 直接输出 route、candidate、score、evidence 等非 L1 字段。T137 已在 parser 中禁止这类字段。

## 当前 L2 状态

当前 `pxfquery.l2_routing.router.route_intent()` 仍是浅层占位：

```text
缺字段 -> needs-intent-completion
否则 -> requires-resource-routing
```

它不读取 cell/drug/gene/function index，不生成候选，不做 pair availability，也不产生可交给 L3 的真实 RoutePlan。

这正是 T138 要替换的部分。

## 资源 JSON 实际格式

T021 标准资源包路径：

```text
4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources
```

实际 JSON 结构：

| 文件 | 实际结构 | 数量 | 当前兼容性 |
|---|---|---:|---|
| `cellline_index.json` | `{valid_cells}` | 240 cells | 当前 `CellLineIndex` 可读 |
| `cellline_neighbors.json` | `lineage -> disease -> subtype -> [cells]` | 19 lineage roots | 当前 `CellLineIndex` 可读 |
| `cellline_tree.json` | `{tree, cell_index, meta}` | 452 cell aliases / 240 meta | 当前 L2 未使用 alias tree |
| `drug_index.json` | `lowercase_alias -> BRD ID` | 5,958 aliases | 当前 `DrugIndex` 可读 |
| `drug_neighbors.json` | `BRD without prefix -> [[neighbor without prefix, tanimoto_int], ...]` | 5,312 drugs | 当前 `DrugIndex` 可读 |
| `gene_index.json` | `lowercase_symbol -> {symbol, gene_type, in_matrix}` | 78,061 keys | 当前 `GeneIndex` 不读 full index |
| `gene_index_simple.json` | `UPPER_SYMBOL -> type_code` | 25,036 keys | 当前 `GeneIndex` 可读 |
| `gene_neighbors.json` | `symbol -> [[neighbor_symbol, cosine_int], ...]` | 33,791 keys | 当前 `GeneIndex` 不默认读 full neighbors |
| `gene_neighbors_simple.json` | `symbol -> [[neighbor_symbol, cosine_int], ...]` | 30,319 keys | 当前 `GeneIndex` 可读 |
| `function_index.json` (T021) | `{var_names, meta, aliases}` where `aliases` is `lowercase_alias -> var_name` | 91 var_names | 当前 `FunctionIndex` 可读 |
| legacy original `function_index.json` | `{functions, note, score_note}` | 91 functions | 当前 `FunctionIndex` 可读 via legacy branch |

## 必须处理的兼容风险

1. T138 不做多 schema 兼容；已固定使用 `4_artifact/2_persist/l2_runtime_resources/function_index.json` 作为 canonical runtime file。该文件从 T021 字节复制，schema 固定为 `aliases: lowercase_alias -> var_name`。

2. `GeneIndex` 现在只使用 simple gene index，因此会丢掉完整 `gene_index.json` 里的 lncRNA、pseudogene 等广覆盖信息。T138 要实现非编码基因 proxy prediction 亮点，必须读取 full `gene_index.json` 和 full `gene_neighbors.json`，或新增 full index reader。

3. `CellLineIndex` 现在只用 `cellline_index.json` + `cellline_neighbors.json`，没有使用 `cellline_tree.json` 的 `cell_index` alias 和 `meta`。T138 要做严谨细胞路由，应接入 `cellline_tree.json`，否则 cell alias 支持不足。

4. 当前 `tl.route` 没有资源参数，也没有绑定 client resource registry。T138 需要让 `tl.route` 能从 client 资源包或显式 `index_dir` 读取索引。

5. 当前 `tl.execute` 仍调用 legacy `QueryResolver.execute_intent(...)`，真实 routing 仍藏在 execute 内部。T138 应把 resource routing 前移到 `tl.route`。
