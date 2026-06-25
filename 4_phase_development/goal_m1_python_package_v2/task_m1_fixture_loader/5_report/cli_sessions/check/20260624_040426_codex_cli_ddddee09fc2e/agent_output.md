我会按 Green Check 只做可执行性检查，不进入 loader 实现。先确认 CyHex 服务状态，然后只写规定的 handoff 报告。
CyHex 本地服务已响应，版本与任务 meta 中的 1.2.19 一致。配置资产预检是干净的，所以我会信任预检结果，不再展开检查 T-043 内容。
检查结论是可执行，且不需要 Yellow Repair。接下来只在 `5_report/` 写执行前 handoff，内容会聚焦执行策略、边界、交付物和停止条件。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不读 `2_project_asset/`、不读 legacy root、不扫描无关 task、不调用下游 prompt 生成、不执行 loader 实现本体
- 执行阶段必须先读的文件：`1_asset/resource_manifest_m1.yaml`、`1_asset/fixture_package_m1/`、`1_asset/expected_shapes_keys_columns_m1.csv`，以及当前 package/module layout
- 触发 `5_report/blocked.md` 的条件：T-043 注册资产缺失/矛盾、需要 raw asset 或 legacy root、无法识别 package layout、必须发明 schema 才能继续

### 二、我准备如何达成任务目标
- 目标：实现一个小而稳定的 M1 fixture loader，严格使用 T-043 manifest/fixture/expected-shapes 合同，并用 smoke evidence 证明稳定 matrix/index access API
- 4-8 步执行策略：先检查注册资产和 package layout；读取 manifest/expected table 提炼合同；加入最小 public loader API；做窄范围验证；写 `3_execution/` smoke 脚本；用 `pxfquery` conda 环境试跑；把可复用证据移入 `4_artifact/`；更新 registry 和 completion report
- 保守起步/试跑建议：先做只读 smoke inspection，再写最小 loader；试跑命令使用 `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`
- 预期交付物和验收信号：loader code 可被下游调用；API 文档说明输入/输出/限制；smoke evidence 记录 keys、shapes、columns、index access，并与 A-003 对齐；`4_artifact/registry.yaml` 和 `5_report/completion.md` 完成

### 三、检查与修复
- 资产预检结论：干净，3 个注册资产均为 `ok`
- 计划质量结论：通过，步骤具体，边界清楚，有保守试跑、停止条件和明确交付物
- 修复了什么：未修复配置，保持 Green Check
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/5_report/handoff_check_before_exec.md` 是否已写：已写
- 是否避免调用下游 prompt 生成：已避免
- 剩余阻断：无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
