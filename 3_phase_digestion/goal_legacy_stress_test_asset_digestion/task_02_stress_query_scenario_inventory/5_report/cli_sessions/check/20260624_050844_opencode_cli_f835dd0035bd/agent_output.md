### 一、我准备如何遵守 CyHex
- **本 task 实际路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: 前驱 task 目录、`2_project_asset/`（只读 symlink）、不可修改资产；禁止执行测试代码、运行查询、读取 T-041
- **执行阶段必须先读的文件**: `1_asset/` 下全部 8 个已注册资产
- **触发 `5_report/blocked.md` 条件**: 资产缺失/空、超出 8 个已注册资产的信息需求、LLM 稳定性导致矛盾分类无法解决

### 二、我准备如何达成任务目标
- **目标复述**: 从 8 个 T-007 资产中提取并分类压力测试场景（9 个维度），产出叙述文档 + CSV 表 + 注册到 artifact registry。不实现、不执行、不读旧脚本。
- **执行策略（4-8 步）**:  
  1. 读取全部 8 个注册输入资产  
  2. 按 9 个维度推导并分类场景  
  3. 为每个场景记录完整字段（ID、类别、参数、期望命中级别、期望结果、理由、来源证据）  
  4. 编写叙述文档  
  5. 编写 CSV 表  
  6. 更新 `4_artifact/registry.yaml`
- **保守起步**: 先读 A-001 + A-007（覆盖面最广），写 5 个代表性场景作为 smoke draft 验证模式，确认后再扩展到全部
- **预期交付物**: narrative inventory (md), scenario table (csv), registry update
- **验收信号**: 9 维度全覆盖，每场景有完整字段和来源引用，CSV 可解析

### 三、检查与修复
- **资产预检结论**: 全部 8 个资产 symlink 存在且目标文件可达，preflight 全部 ok
- **计划质量结论**: 协议含 6 个具体步骤，明确输入/输出/交付物，接受标准清晰。缺少显式 stop conditions（已在 handoff 中补全），但不构成阻断
- **修复了什么**: 无修复 — 资产和协议均一致可用
- **`handoff_check_before_exec.md`**: 已写入 `5_report/handoff_check_before_exec.md`
- **是否避免调用下游 prompt 生成**: 是，未调用任何 `/prompt/generate*` 端点
- **剩余阻断**: 无

---

**检查完成。请确认：检查通过，开始执行**
