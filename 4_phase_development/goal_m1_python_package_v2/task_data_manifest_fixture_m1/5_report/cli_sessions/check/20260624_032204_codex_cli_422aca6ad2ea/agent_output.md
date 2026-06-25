我会按 Green Check 处理：只使用已给出的快照和干净的资产预检结论，不进入任务本体，也不读取后续 prompt。接下来只确认 CyHex 服务可用并写检查交接文件。
CyHex 返回版本 `1.2.19`，与任务元信息一致。检查文件尚不存在；我现在只写 `5_report/handoff_check_before_exec.md`，不碰 `4_artifact/`。
我会把执行建议限定在已注册的 T-014/T-021 资产和当前 task 可写目录内。交接文件会明确停止条件，避免执行 AI 为了补数据去扫 `2_project_asset/` 或失败任务输出。
交接文件已经写入。最后我会做一次轻量读取确认结构完整，不检查任务资产内容。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不读 `2_project_asset/`，不扫无关前置任务目录，不使用 T024-T040 输出，不读后续 prompt，不执行任务本体，不写交付物
- 执行阶段必须先读的文件：当前 task registry/rules，以及注册的 A-001 到 A-006
- 触发 `5_report/blocked.md` 的条件：注册资产缺失/不可读、需要 raw `2_project_asset/`、需要伪造数据、需要失败任务输出、或无法从 T-014/T-021 追溯 fixture 内容

### 二、我准备如何达成任务目标
- 目标：确认该配置足够让执行 AI 基于 T-014/T-021 生成 M1 resource manifest、fixture package、shape/key/column 表和 sample record 表，不扩范围、不猜数据
- 执行策略已写为 8 步：先读授权说明/表格，再小范围检查 A-001，交叉核对 A-003/T-014，生成 manifest、fixture、CSV、README、报告和 registry
- 保守起步/试跑建议：先做小范围 schema/path survey，再用 `conda run -n pxfquery python ...` 做 fixture 加载与 shape/key/column smoke validation
- 预期交付物和验收信号：已在 handoff 表格中列出，包括 `resource_manifest_m1.yaml`、`fixture_package_m1/`、两个 CSV、README、两个 HTML 报告和 `4_artifact/registry.yaml`

### 三、检查与修复
- 资产预检结论：干净，6 个注册资产均 `ok`
- 计划质量结论：可执行，步骤具体，边界清楚，交付物明确，有停止条件和保守试跑建议
- 修复了什么：未修复配置；仅创建检查交接文件
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/handoff_check_before_exec.md` 是否已写：已写
- 是否避免调用下游 prompt 生成：已避免
- 剩余阻断：无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
