Now I have sufficient context. Let me write the configuration files.
所有三个配置文件都已写入。以下是最终证据报告：

---

## 配置完成

**判定：** `yellow_expand` – 因为所有三个前驱任务（T-001、T-002、T-007）的 `handoff_ai_use.md` 均缺失，所以进入黄色扩展模式。阅读了完成报告和 T-007 关键产出物，收集了足够信息，返回以写入配置。

**实际读取的文件：**
- T-001: `meta.yaml`、`registry.yaml`、`completion.md`
- T-002: `meta.yaml`、`registry.yaml`、`completion.md`
- T-007: `meta.yaml`、`registry.yaml`、`completion.md`、`pxfquery_development_state_report_v20260617.md`、`pxfquery_module_asset_status_matrix_v20260617.csv`、`pxfquery_validation_evidence_index_v20260617.csv`
- 目标层级：`goal_meta.yaml`、`goal_protocol.md`、`shared_protocol.md`
- 同级任务：`T-055 meta.yaml`、`T-056 meta.yaml`
- 项目资产：`M-0386 test_forward_matrix.py`、`M-0389 verify_resolver_cases.py`
- T-041 状态（通过子代理确认——仍处于活跃状态，未完成）

**实际读取的前驱任务：** T-001、T-002、T-007

**已选资产：** 注册了 12 个资产（A-001 至 A-012），包含 1 个可选资产（针对 T-041 的 MAY-001，前提是它已完成）。
- 4 个来自 T-007（开发状态报告、模块状态矩阵、验证索引、风险列表）
- 1 个来自 T-001（旧资产结构报告）
- 2 个来自 T-002（库结构指南、未迁移资产报告）
- 5 个来自项目资产（测试脚本目录、验证报告目录、解析器源代码、JSON 跟踪、源代码映射）

**已写/已修订的文件：**
- `2_protocol/2_protocol_split/protocol.md` — 完整协议，包含目标、位置、输入、步骤、约束条件、交付物和验收标准
- `2_protocol/3_asset_rule/asset_rule.yaml` — 结构化的必填/可选/禁止/输出/可修改/不可修改规则
- `1_asset/registration.yaml` — 包含来源元数据和就绪状态的 12 个资产注册记录

**未调用下游提示端点。** 未调用 `/prompt/generate`、`/prompt/generate-check` 或 `/prompt/generate-delivery`。

**阻塞器：** 无。T-041 为活跃状态，因此已被省略（如其现有状态所要求）。T-055/T-056 为待处理状态，不构成阻塞——此任务直接基于 T-001/T-002/T-007 构建。

**关键配置决策：**
- 测试脚本目录（`code/index_builders/`）注册为单个代码类型资产（A-008），因为执行人工智能需要枚举并单独检查每个脚本
- 验证报告目录注册为单个文档类型资产（A-009），原因同上
- 解析器源代码已注册（A-010），因为理解目标逻辑是区分脚本与实际压力测试行为的关键
- 未迁移资产报告（A-007）已包含，以防止评估被故意排除在迁移之外的旧版材料

配置完成。请确认：配置通过 / 提出修改意见
