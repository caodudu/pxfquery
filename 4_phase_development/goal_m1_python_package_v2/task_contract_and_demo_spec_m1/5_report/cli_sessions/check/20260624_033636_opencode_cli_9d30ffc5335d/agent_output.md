

I'll execute this CyHex check prompt for T-042. Let me start by reading the required
Let me verify the primary required assets have substantive content:
All four primary assets have substantive content. Configuration is sound. Let me now write the handoff report.
检查完成。

### 一、我准备如何遵守 CyHex
- **Task 路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `1_asset/registration.yaml`
- **禁止目录/行为**: `2_project_asset/`, legacy root `8_functional_query`, T024-T040 五个 goal 目录；禁止实现代码、索引重建、矩阵分析、T024-T040 作为权威引用
- **执行阶段必须先读的文件**: A-001, A-002, A-004, A-005（主资产）；A-003, A-006, A-007（可选交叉验证）
- **触发 `blocked.md` 的条件**: 必需资产缺失/空文件；开发任务需要 `2_project_asset/`；T-007/T-013 互相矛盾无法产生确定性合约；工作超出 spec 范围进入实现/索引重建

### 二、我准备如何达成任务目标
- **目标复述**: 基于 T-007 开发状态和 T-013 MVP 能力契约，交付 M1 API/CLI 合约、正向/反向 demo 用例、JSON Schema、no-hit/error 行为、pass/fail 标准；不下沉实现代码，不扩大产品设计
- **执行策略** (7 步):
  1. 读 A-001/A-002/A-004/A-005 主资产，提取 (B,P,F) 模型、forward/reverse 意图、确定性边界
  2. 写 `4_artifact/2_persist/m1_api_contract.yaml`（函数名、参数、返回 JSON、error 结构）
  3. 同 YAML 中定义 CLI 合约（命令、标志、demo 调用、退出码）
  4. 写 `4_artifact/2_persist/m1_demo_cases.yaml`（正向 + 反向各一例，含 pass/fail 断言）
  5. 定义 no-hit/ambiguous/missing-index/low-confidence 的合约级输出
  6. 写 `4_artifact/3_document/m1_contract_summary.md`
  7. 注册输出到 `4_artifact/registry.yaml`，写 `5_report/completion.md`
- **保守起步**: 先读 A-001 + A-004 锚定包身份和 M1 边界；草图输出 JSON 再写 YAML
- **预期交付物**: m1_api_contract.yaml / m1_demo_cases.yaml / m1_contract_summary.md / registry.yaml / completion.md
- **验收信号**: 函数签名精确、demo 用例可追溯、no-hit/error 行为确定、无 T024-T040 引用

### 三、检查与修复
- **资产预检结论**: 7 项资产全部 `ok`，symlink 同步正确，无 missing/empty/forbidden
- **计划质量结论**: 7 步执行步骤，每步有操作名+输入+输出；有停止条件；交付物路径明确；不要求重发现 predecessor 上下文；不留在 `3_execution/`
- **修复了什么**: 无（配置已在上一轮 config_repair 修复完成）
- **handoff_check_before_exec.md**: ✅ 已写入 `5_report/handoff_check_before_exec.md`
- **是否避免调用下游 prompt 生成**: ✅ 未调用任何 `/prompt/generate*`
- **剩余阻断**: 无

检查完成。请确认：**检查通过，开始执行**
