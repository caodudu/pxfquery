我会按 green check 只做可执行性检查和 handoff 编写，不进入任务实现，也不扫描资产内容。先确认任务目录里的协议文件是否足够完整，然后写 `5_report/handoff_check_before_exec.md`。
协议、资产规则和注册表彼此一致，CyHex 版本也可访问。配置已经具备执行 AI 所需的边界、输入、步骤、交付物和停机条件；我现在只写检查交接文件，不改协议或资产登记。
检查交接文件已写入，未进行 yellow repair，也没有触发下游 prompt 生成。最后我会快速确认文件存在并包含要求结构，然后给你中文检查结论。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不得改 predecessor task；不得读/用 `2_project_asset/`；不得用 T024-T040 blocked assets；不得把 T049 标绿；不得执行任务本体
- 执行阶段必须先读：A-001/T042 contract、A-002/T042 demo cases，然后读 T043/T046 注册资产
- 触发 `5_report/blocked.md` 的条件：需要 forbidden raw assets、blocked assets、修改 upstream、削弱 T042 contract、或无法诚实标注 synthetic/repair provenance

### 二、我准备如何达成任务目标
- 目标复述：T060 是 T049 的旁路替代交付；先创建 task-local reverse repair substrate 支撑 `HALLMARK_MYC_TARGETS_V1` demo，再实现 reverse query core、JSON evidence、deterministic ranking、no-hit/error behavior 和 provenance。
- 执行策略：按 T042 contract 抽取要求；用注册资产确认 fixture/manifest 缺口；创建 task-local repair fixture/manifest；基于 T044 skeleton + T046 loader API 实现 reverse core；跑 positive demo 与 no-hit/error smoke；登记 `4_artifact/registry.yaml` 并写报告。
- 保守起步/试跑建议：先做 contract extraction 和 loader smoke check，再创建可复用 `4_artifact/` 输出；demo 必须在 `pxfquery` conda 环境实际运行并重复验证 ranking 稳定。
- 预期交付物和验收信号：package code、repair fixture/manifest、provenance report、demo JSON、error/no-hit JSON、ranking CSV、HTML reports、artifact registry、completion report；验收看 T042 JSON contract、`HALLMARK_MYC_TARGETS_V1`、稳定排名、结构化错误和 provenance。

### 三、检查与修复
- 资产预检结论：15 个注册资产均为 `ok`，无 missing/empty/forbidden anomaly。
- 计划质量结论：通过；已有明确步骤、输入、输出、保守起步、成本风险和 stop conditions。
- 修复了什么：未修复任何配置，保持 green check。
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/handoff_check_before_exec.md` 是否已写：已写。
- 是否避免调用下游 prompt 生成：已避免。
- 剩余阻断：无。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
