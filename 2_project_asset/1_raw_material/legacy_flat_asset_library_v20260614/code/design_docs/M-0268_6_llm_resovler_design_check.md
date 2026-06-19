# 6_llm_resovler 设计点提取与验证（Forward 优先）

更新时间：2026-04-09

## 1. 项目设计点提取（你关心的核心）

1. 三元组目标：把用户自然语言映射到 `(B, P, F)`，并在稀疏矩阵中找到可用证据。
2. AI 的必要性：AI 负责意图解析、标准化映射、层级选择与证据整合说明；不负责数值计算。
3. 数字资产的作用：`cellline/gene/drug/function` 索引用于“可落库”的键定位与近邻代理。
4. 正向查询关键策略：先精确命中，再按层级代理（而不是简单查表）。
5. 遗传扰动特殊性：应并行使用 `xpr + sh` 两种来源，输出复合证据。

## 2. 当前实现状态（代码层）

1. Forward 四层命中：
   - `EXACT`：精确 cell + 精确 perturbation
   - `PROXY_PERT`：精确 cell + perturbation 近邻
   - `PROXY_CELL`：代理 cell + 精确 perturbation
   - `PROXY_BOTH`：代理 cell + perturbation 近邻
2. Cellline LLM 引导树：
   - 已实现按 `lineage -> disease -> subtype` 逐层选择
   - 单分支自动跳过
   - 支持疾病名/未知细胞系输入转 proxy cell
3. 遗传扰动双源复合：
   - 已实现 `xpr + sh` 双源检索（默认）
   - `resolver_meta.evidence_bundle` 输出两个来源的证据摘要
4. 输出风格：
   - summary 默认不强制包含数字（可开关）
   - 强调证据等级与代理来源

## 3. 验证方式与结果

1. `test_forward_matrix.py`（确定性 mock hooks）：
   - 覆盖 `EXACT/PROXY_PERT/PROXY_CELL/PROXY_BOTH`
   - 覆盖疾病名输入、未知细胞系输入、药物路径
   - 最新结果：7/7 通过
   - 见 `report/6_llm_resovler_forward_matrix.md`
2. `validate_act1.py`（真实 API）：
   - MiniMax 当前报 `401 invalid api key`
   - 该错误属于认证配置，不属于算法逻辑错误
   - 见 `report/6_llm_resovler_act1_validation_minimax.md`

## 4. 仍需继续确认（下一步）

1. 用有效 MiniMax key 跑真实 forward 多场景（不是 mock）并导出报告。
2. 在 summary 中加入“明确代理原因模板句”（例如：为何用 disease 级别 cell 代理）。
3. 对 `evidence_bundle` 增加“冲突证据处理策略”（xpr 与 sh 方向不一致时如何陈述）。

