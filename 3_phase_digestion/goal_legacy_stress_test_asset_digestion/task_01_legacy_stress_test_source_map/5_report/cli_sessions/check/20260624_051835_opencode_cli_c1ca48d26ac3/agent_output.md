Now I have all the information needed to write the check handoff report. All 9 assets resolve, the flat library directories are populated, the protocol has 7 concrete steps, and the deliverables are well
### 一、我准备如何遵守 CyHex
- 本 task 实际路径: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map`
- 允许写入目录: `3_execution/`, `4_artifact/`, `5_report/`
- 禁止目录/行为: 禁止扫描 legacy root `/Users/dudu/Documents/3_Project/8_functional_query`，禁止修改 flat asset library，禁止修改 predecessor 产物
- 执行阶段必须先读的文件: A-005/A-006/A-007（T-007 交接）、A-002/A-009（迁移清单和未迁移清单）
- 触发 `5_report/blocked.md` 的条件: flat asset library 不可访问或为空；>10% 的 validation report 引用文件在 flat library 中找不到

### 二、我准备如何达成任务目标
- 目标: 创建迁移 legacy stress test 相关素材的源地图和 CSV 索引，供后续任务使用，不执行不验证
- 7 步执行策略: (1) 读 T-007 交接文件了解已有验证全景 → (2) 读迁移清单过滤 stress-test 相关条目 → (3) 浏览 flat library 7 个高优先级目录 → (4) 逐候选资产记录分类和评估 → (5) 写 markdown 源地图 → (6) 写 CSV 索引 → (7) 注册交付物、写 completion
- 保守起步: 先读 A-006（仅 15 行）和 A-002 建立基线，扫描单个目录（validation_reports）产 2-3 候选行验证 schema 后全量扫描
- 无计算/API 开销，纯读文件编目工作
- 预期交付物: `4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md` 和 `4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv`

### 三、检查与修复
- 资产预检结论: 9/9 ok，所有 symlink 解析正确，flat library 7 个目标目录均存在且有内容
- 计划质量结论: 协议有 7 步具体操作、明确的产出物、验收标准和停止条件，符合质量门要求
- 修复了什么: 无需修复，green check
- `5_report/handoff_check_before_exec.md` 已写
- 未调用下游 prompt 生成
- 剩余阻断: 无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
