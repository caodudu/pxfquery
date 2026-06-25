Now let me write the handoff check report. All 12 assets are `ok`, protocol has clear steps, deliverables are concrete, no blocking issues.
---

### 一、我准备如何遵守 CyHex
- **任务实际路径**: `.../goal_m1_python_package_v2/task_m1_python_package_milestone`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: `2_project_asset/`、所有前驱任务目录（T-050/T-051/T-052）、修改前驱产物、重新执行验证或装配
- **执行阶段必须先读的文件**: `1_asset/registration.yaml`, `2_protocol/3_asset_rule/asset_rule.yaml`, `2_protocol/2_protocol_split/protocol.md`
- **触发 blocked.md 的条件**: 任一必需资产缺失/空、前置证据流出现 FAIL、协议与资产规则无法自洽

### 二、我准备如何达成任务目标
- **目标复述**: 将三个已完成的前驱证据流（前向验证11/11 PASS、反向验证42/42 PASS、包装配9项通过）汇总为 M1 里程碑交付，输出最终包路径/版本/演示命令/证据索引/分层资产地图/已知缺口报告。不修复任何下层代码。
- **8步策略**: （1）确认三个证据流全 PASS；（2）读取演示与包证据；（3）构建分层资产地图 CSV；（4）编写证据索引 JSON；（5）编写演示命令参考；（6）编写已知缺口报告；（7）编写里程碑总报告；（8）注册交付物。
- **保守起步**: 先读 A-001/A-003/A-007 确认绿灯；用 `import pxfquery; print(pxfquery.__version__)` 做只读冒烟。
- **交付物**: milestone_report.md, evidence_index.json, layered_asset_map.csv, known_gaps.md, demo_commands.md, completion.md。

### 三、检查与修复
- **资产预检**: 12/12 ok，symlink 12/12 linked，无 missing/empty/forbidden
- **计划质量**: 协议有 9 步执行计划，6 个交付物，硬停止条件和禁止规则明确
- **修复**: 无。无需修复。
- **handoff_check_before_exec.md**: 已写
- **下游 prompt 生成**: 未调用，仅写了检查报告
- **剩余阻断**: 无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
