# 04 组合证据路由：forward 与 reverse

日期：2026-06-28

## 为什么单维度命中还不够

细胞能匹配、扰动能匹配、功能能匹配，不等于三者组合有数据。

例如：

```text
A549 存在
erlotinib 存在
HALLMARK_APOPTOSIS 存在
```

这仍然不能证明 `(A549, erlotinib)` 在对应矩阵里有观测。L2 必须检查组合可用性，否则 L3 会被迫失败，或者更糟糕，系统会用错误 fallback 假装有证据。

## T007 源码资料来源

这部分有 T007 源码依据：

- `Migrated PxFquery package code/query/resolver.py`
- `Migrated PxFquery package code/query/forward.py`
- `Migrated PxFquery package code/query/reverse.py`
- `Migrated PxFquery package code/core.py`

T007 源码里，resolver 会构建类似 forward plan 的结构，包含 pert_type、pert_class、base_pert、pert_neighbors、exact_cell、proxy_cells 等信息。随后 `_collect_forward_evidences` 会按 cell 和 perturbation 的组合去找 evidence。

T007 体现了这些证据等级：

```text
EXACT
PROXY_PERT
PROXY_CELL
PROXY_BOTH
not found
```

## Forward 路由原理

Forward query 是给定扰动和细胞上下文，问功能影响。

L2 forward routing 应按这个顺序展开候选：

```text
exact cell + exact perturbation
exact cell + proxy perturbation
proxy cell + exact perturbation
proxy cell + proxy perturbation
```

每个候选都要检查 pair availability。这里检查的是 metadata 或预计算 pair index，不是读取矩阵数值。L2 输出 route plan 后，L3 才负责读取真实功能分数。

## Reverse 路由原理

Reverse query 是给定功能目标，找可能实现该目标的扰动。

Reverse 的路由对象不同：

```text
cell scope
function target vector
search modality / perturbation class
available perturbation universe
```

也就是说，reverse 不是先指定一个药物再找证据，而是先把功能目标映射到真实功能列和方向，再限定细胞范围和可搜索扰动集合，最后交给 L3 做 ranking。

T007 的 reverse query 已经有从 activate/suppress 到 target vector 的基本思路，但它没有把这一步作为独立 L2 artifact 暴露。

## T007 没有完整给出的部分

T007 把 route 和 execute 混在 resolver/query 里。它有组合证据优先级，但不是独立 `tl.route` 结果。

T007 没有要求 route 阶段必须输出所有被检查但失败的候选。T138 应该补这个，否则用户无法知道为什么最后用了 proxy。

T007 的 `must_answer` 和 fast path 风险很高，因为它可能为了回答而给 forced fallback。T138 的 L2 应禁止这种行为。

## L2 输出应该长什么样

组合路由输出至少要能表达：

- forward 或 reverse 查询方向。
- 每个维度的候选列表。
- 组合候选的 exact/proxy 等级。
- pair availability 检查结果。
- 被拒绝候选的拒绝原因。
- 进入 L3 的 route id。
- 如果没有 route，明确 unresolved/no-hit。

