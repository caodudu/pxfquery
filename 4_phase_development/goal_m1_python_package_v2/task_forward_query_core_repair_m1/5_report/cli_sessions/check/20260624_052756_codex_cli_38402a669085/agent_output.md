我会只做检查层工作：补足快照里被截断的协议/输出规则信息，确认执行边界和交付要求，然后写 handoff 检查报告；不会运行任务代码或写 `4_artifact/`。
协议和资产规则已经足够具体：9 个执行步骤、明确输出路径、禁用 raw asset/web/T048 产物复用，并有停止条件。资产预检干净，唯一需要在 handoff 里提醒的是 A-013/A-014 在规则中是可选参考，执行时不应把它们当成必读前置。
我现在写检查 handoff，只记录执行策略、风险控制和停机条件；不会创建执行产物或触碰 `4_artifact/`。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不读 `2_project_asset/`，不读 T024-T040 blocked 资产，不修改 T-042/T-043/T-044/T-046/T-047/T-048 产物，不执行任务本体，不生成下游 prompt
- 执行阶段必须先读的文件：A-001/A-002 合同与 demo 规范；A-003 到 A-012 fixture、schema、包骨架、loader 与 smoke evidence；A-015 仅作 T-048 incident reference
- 触发 `5_report/blocked.md` 的条件：合同 JSON/API 语义不清、需要 raw asset 或 blocked asset、必须修改 upstream 才能通过、无法诚实标注 synthetic/repair provenance、需要扩大读取未注册 predecessor context

### 二、我准备如何达成任务目标
- 目标复述：T-059 是 T-048 的同层旁路修复/替代交付，必须做出 forward query core，并用 task-local repair substrate 补齐 `EGFR/A549/xpr` positive demo case，不能伪装成原始数据。
- 4-8 步执行策略：先搭 `3_execution/` 工作包；提取 T-042 contract；确认 T-043/T-046 baseline gap；创建 synthetic repair fixture/manifest；实现 loader-compatible forward query；跑 import、positive demo、no-hit demo；保存 JSON/table/report/registry 到 `4_artifact/`；写 completion。
- 保守起步/试跑建议：先做 import smoke 和 loader compatibility check，再跑 `EGFR/A549/xpr` demo 和一个 no-hit demo。
- 预期交付物和验收信号：`4_artifact/1_package/`、repair manifest/fixture、positive/no-hit JSON、assertion CSV、provenance report、HTML reports、`4_artifact/registry.yaml`；验收信号是 JSON 可见且符合 T-042，positive found，no-hit 不崩溃，provenance 清楚，upstream 未改。

### 三、检查与修复
- 资产预检结论：15 个注册资产均 `ok`，无需重复逐项扫描。
- 计划质量结论：通过；协议有明确步骤、输入、输出、保守试跑、成本边界和 stop conditions。
- 修复了什么：未修复配置；仅补写检查 handoff。
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md` 是否已写：已写。
- 是否避免调用下游 prompt 生成：已避免。
- 剩余阻断：无。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
