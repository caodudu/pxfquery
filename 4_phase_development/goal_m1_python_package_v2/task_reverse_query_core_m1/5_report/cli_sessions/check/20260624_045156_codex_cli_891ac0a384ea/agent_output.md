我会按 Green Check 处理：只验证配置可执行性并写交接检查报告，不进入实现、不生成下游 prompt。接下来只查看必要的当前任务文件和报告目录状态。
配置本身是可执行的：资产预检干净，协议、注册表、asset_rule 三者一致，步骤也已经足够具体。我只需要补写执行前 handoff，让执行 AI 不去重新发现上下文或越界读取。
我已写入 `5_report/handoff_check_before_exec.md`，接下来快速核对文件结构是否符合指定模板，然后结束检查。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不读 `2_project_asset/`、不读历史源 `/Users/dudu/Documents/3_Project/8_functional_query`、不依赖 T024-T040、不得写私有 ad hoc loader、不得执行任务本体
- 执行阶段必须先读的文件：A-001/A-002 合同与 demo；A-004/A-005 loader 代码与 API 文档
- 触发 `5_report/blocked.md` 的条件：loader 无法暴露 T-042 所需数据、需要 raw asset/legacy root、必须猜测合同字段或阈值、必须绕过 loader

### 二、我准备如何达成任务目标
- 目标复述：让执行 AI 基于 T-042 合同和 T-046 loader 实现 M1 reverse query core，并产出确定性排序/评分、demo JSON 证据和报告
- 4-8 步执行策略：先抽取合同；再做 loader smoke check；实现 task-local package code；实现确定性 ranking/tie-break；跑 reverse demo；按需跑 no-hit/error；登记 artifacts；写 completion
- 保守起步/试跑建议：先用 `pxfquery` conda 环境做最小 loader smoke check，确认无需私有解析后再写 reusable 输出
- 预期交付物和验收信号：`4_artifact/1_package/` 代码、`reverse_demo_evidence_v20260624.json`、条件性 no-hit/error JSON、报告、registry、completion；验收看合同字段、loader-only 数据访问、demo assertions 和确定性排序

### 三、检查与修复
- 资产预检结论：干净，6 个资产均 ok，required 资产齐全
- 计划质量结论：通过，步骤、边界、交付物、stop conditions 都足够具体
- 修复了什么：无；按 Green Check 只补写 handoff
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/handoff_check_before_exec.md` 是否已写：已写
- 是否避免调用下游 prompt 生成：已避免
- 剩余阻断：无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
