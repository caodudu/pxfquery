我会只做执行前检查，不进入实现、不写 `4_artifact/`，并把执行 AI 需要的边界、策略和停机条件写入指定 handoff 文件。配置快照和资产预检已经足够干净，我只会在必要处补足执行建议。
我现在写入检查 handoff。内容会明确：只允许执行 AI 使用已注册资产，必须通过 T-046 loader 访问 fixture，发现 loader 接口不足时停止并报告接口缺口。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不得读写 `2_project_asset/`、legacy root、任意 predecessor task folder；不得执行任务本体；不得写 `4_artifact/` 交付物；不得调用下游 prompt 生成
- 执行阶段必须先读的文件：A-001、A-002、A-004、A-005，即 contract/demo cases 和 T-046 loader/API docs
- 触发 `5_report/blocked.md` 的条件：必需资产不可读、loader 无法提供所需数据、必须绕过 loader 才能实现、需要 raw assets/legacy root、T-042 contract 与 loader 能力不可调和

### 二、我准备如何达成任务目标
- 目标复述：执行 AI 应实现 M1 forward query core，严格遵守 T-042 API/demo/no-hit contract，并且所有 fixture 数据访问必须通过 T-046 loader。
- 4-8 步执行策略：先抽取 contract；再确认 loader API；做 loader-only smoke；实现 forward query；实现 no-hit；跑 demo/no-hit JSON；生成 assertion CSV；写报告和 handoff。
- 保守起步/试跑建议：先用 `pxfquery` conda 环境跑 loader-only smoke，不要先写排名逻辑。
- 预期交付物和验收信号：package code 在 `4_artifact/1_package/pxfquery/`；demo/no-hit JSON 符合 contract；CSV 明确 pass/fail；HTML/report/handoff/registry 完整。

### 三、检查与修复
- 资产预检结论：clean，6 个注册资产均 ok，无缺失、空文件、forbidden scope。
- 计划质量结论：可执行，边界明确，步骤和 deliverables 足够具体。
- 修复了什么：未进入 yellow repair；只创建/写入检查 handoff。
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md` 是否已写：已写。
- 是否避免调用下游 prompt 生成：已避免。
- 剩余阻断：无。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
