

I need to understand this task and its dependencies before writing the check handoff. Let me first check the CyHex API and then examine the T-021 predecessor task outputs since this task depends on them
Good. Now I have the full context. Let me check the current task's protocol and asset situation more carefully, then write the handoff check report.
Now I have full context. This is a **Yellow Repair** case: `zero_assets: true` but the task clearly needs T-021 standard-resource inputs, and the protocol is empty. Let me repair it.
Now I have all the information I need. Let me repair the task configuration: register T-021's standard-resource outputs, populate the protocol, and
Now let me repair all three files and create the execution step folders. The T-021 standard-resource outputs are at:
`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`

M1-relevant assets: 10 index JSON files + data_description.yaml. The h5ad matrices and CSVs are background context, not M
Now let me quickly verify the T-021 assets exist
All 11 assets exist. Now write the handoff
---

### 一、我准备如何遵守 CyHex
- **本 task 实际路径:** `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1`
- **允许写入目录:** `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为:** T-021 standard_resources (只读), `8_functional_query` legacy root, raw `2_project_asset/`, T-021 的 `.h5ad` 和 `.csv` 文件, 重写或修改任何索引
- **执行阶段必须先读的文件:** `1_asset/registration.yaml`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`
- **触发 `5_report/blocked.md` 的条件:** 任意 required 索引不可读, function_index.json 不是 91 terms, 核心索引缺失 M1 所需 key, JSON 解析失败无法恢复

### 二、我准备如何达成任务目标
- **目标复述:** 审计 T-021 产出的 10 个 M1 相关查询索引，验证 JSON schema 有效性、forward/reverse demo 所需 key、邻居图完整性和 demo 覆盖缺口。产出机读健康摘要 + 人读报告 + 缺口记录。不修改任何索引，仅报告和推荐补丁。
- **7 步执行策略:**
  1. 加载 4 个核心索引 + data_description，验证 JSON 可解析性
  2. 验证每个核心索引的 M1 必需 key
  3. 检查 6 个可选邻居/树索引的可用性
  4. 对照 T-042 M1 demo 需求检查索引覆盖度
  5. 产出 `index_health_summary.json`（机读）
  6. 产出 `index_health_report.md`（人读）
  7. 产出 `gap_notes.md`（缺口叙述）
- **保守起步/试跑建议:** 先用 `function_index.json`（17 KB，最小核心索引）做 smoke test
- **预期交付物和验收信号:** 3 个文件 — health_summary.json 含 per-index status，health_report.md 含 pass/warn/block + T-047 交接建议，gap_notes.md 含 severity + demo case + resolution path

### 三、检查与修复
- **资产预检结论:** 原始配置 `zero_assets: true`，但任务明确需要 T-021 索引作为输入 → 已修复，注册了 11 个 T-021/D-004 资产
- **计划质量结论:** 原始 protocol.md 完全空白 → 已修复为 7 步执行计划，含每步输入/输出/中间产物
- **修复了什么:**
  - `1_asset/registration.yaml`: 空白 → 11 个 T-021 资产注册
  - `2_protocol/3_asset_rule/asset_rule.yaml`: 空白 → 5 required / 6 optional / 6 forbidden / 3 output / 1 non_modifiable
  - `2_protocol/2_protocol_split/protocol.md`: 空白 → 7 步 protocol + deliverables 表
  - `3_execution/`: 空目录 → 创建了 step1~step4 子目录
- **`handoff_check_before_exec.md` 是否已写:** 是
- **是否避免调用下游 prompt 生成:** 是，未调用任何 `/prompt/generate*` API
- **剩余阻断:** 无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
