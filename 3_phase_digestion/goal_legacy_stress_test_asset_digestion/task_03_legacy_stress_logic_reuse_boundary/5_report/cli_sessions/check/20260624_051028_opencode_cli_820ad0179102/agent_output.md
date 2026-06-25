CyHex API is reachable. Let me now do the checks required. I'll verify the asset preflight and inspect the key protocol/registry files for
All assets confirmed. Symlinks resolve, reports directory has 57 items, test scripts present, artifact directories ready. Now writing the handoff check report.
---

### 一、我准备如何遵守 CyHex

- **Task 路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: `1_project_init/`, `2_project_asset/`（已注册资产路径除外）, `8_functional_query/`, 前序任务目录；禁止修改代码、运行脚本、执行 LLM 查询
- **执行前必须读的文件**: 12 个已注册资产（A-001 ~ A-012），均通过预检
- **触发 `blocked.md` 的条件**: 必需资产缺失/无法解析；验证报告目录为空；资产内容无法分类且无法修复

### 二、我准备如何达成任务目标

- **目标复述**: 对迁移资产库中所有 legacy stress-test 相关脚本、报告、设计文档、trace 逐一判定复用边界：`direct reference` / `rewrite needed` / `historical evidence only` / `not usable` / `unknown`，产出分析文档和决策矩阵 CSV
- **执行策略**（10 步）:
  1. 读权威文档（A-005/A-006/A-007/A-001/A-012）建立分类标准
  2. 读成熟度索引（A-002/A-003/A-004）了解组件状态
  3. 读验证报告（A-009 57 份），覆盖强制性报告集
  4. 读测试脚本（A-008, M-0385~M-0389）
  5. 读 resolver 源码（A-010）
  6. 读验证 trace（A-011）
  7. 构建决策矩阵
  8. 写持久化文档
  9. 写 CSV 矩阵
  10. 注册交付物 + 写 completion/delivery QA
- **保守起步**: 先读权威文档和成熟度索引，再读报告；首份报告读 M-0239 最新索引了解全貌
- **交付物和验收信号**:
  - `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` — 每个资产有明确分类和推理
  - `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` — 机器可读，7 列

### 三、检查与修复

- **资产预检结论**: ✅ 全部 12 个资产 symlink 完好，状态 `ok`
- **计划质量结论**: ✅ 协议有具体步骤、输入输出、停止条件、禁止规则，符合 quality gate
- **修复了什么**: 无修复（green_check）
- **`handoff_check_before_exec.md`**: ✅ 已写入 `5_report/handoff_check_before_exec.md`
- **避免调用下游 prompt 生成**: ✅ 未调用任何 `/prompt/generate*`
- **剩余阻断**: 无

检查完成。请确认：检查通过，开始执行
