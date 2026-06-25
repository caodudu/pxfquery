

I'll execute this CyHex checking prompt. Let me start by reading the required files and assessing the
Good. Now let me verify the asset paths actually exist to confirm the preflight anomaly: the prompt shows `zero_assets: true` but the registration has 5 assets with explicit paths. Let me check the actual symlink/asset directory layout.
Now let me verify the actual source asset files exist at
All 5 registered assets exist and are non-empty files. The preflight `zero_assets: true` is an anomaly because the registration clearly has 5 assets — but since this is a digestion-phase task and the assets exist at their source paths (not symlinked into the task's `1_asset/` directory), the preflight is reporting on the task's own `1_asset/` directory which has no symlink copies. The registration paths point to predecessor artifact locations which all exist. This is not a blocker — the paths in registration.yaml are correct.

Now let me also verify the two key requirements: that the `5_report/` directory exists (it does), and the `check` directory exists for the cli session context. Let me also quickly verify the target output
All checks are complete. The configuration is clean. Here is the checking result:

---

### 一、我准备如何遵守 CyHex

- **Task 路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: 不扫描 predecessor 协议/资产/执行目录；不操作 legacy source root；不写 Python 实现代码；不运行 stress tests；不做 web search
- **执行阶段必须先读的文件**: `1_asset/registration.yaml` 中列出的 A-001～A-005（5 份 predecessor 产出）
- **触发 `blocked.md` 的条件**: 任一 required asset 缺失/空文件且无法修复；protocol 步骤或交付物不可修复的模糊/缺失；task 缺少必要执行能力

### 二、我准备如何达成任务目标

- **复述目标**: 定义 PxFquery 证据路由行为契约，产出 6 种路由类型（exact/proxy/no-hit/ambiguous/context-missing/transfer）的 taxonomy + acceptance cases、evidence metadata contract、以及 29 个 T-058 stress-test 场景的路由映射表。
- **执行策略** (6 步):
  1. 读取 A-001～A-005，提取当前 exact/proxy/no-hit 实际行为、gap 和风险
  2. 依据 protocol 定义 6 种路由类型的具体语义，引用 T-021 标准资源
  3. 为每类路由写 acceptance case（含输入、解析路径、metadata 字段、pass condition）
  4. 定义 evidence metadata contract schema（8 个必填字段 + 类型/取值范围）
  5. 将 29 个 T-058 场景映射到路由类型，标注预期 pass/fail/borderline
  6. 写入 3 个交付物并注册到 `4_artifact/registry.yaml`
- **保守起步**: 先读 A-003 (standard resource guide) 确认可用的 index/matrix 集合，作为后续路由定义的基准确认；再读 A-004 掌握 29 个场景的分类
- **预期交付物**:
  - `4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md` — 含 acceptance cases
  - `4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml` — schema + 字段定义
  - `4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv` — 29 场景路由映射
- **验收信号**: 6 种路由全定义、每个 case 含 resolution path 和 pass condition、metadata contract 覆盖 8 个字段、29 场景全部映射、no-hit 要求 thresholding、transfer 有用户可见语义

### 三、检查与修复

- **资产预检结论**: 绿色。preflight 报告 `zero_assets: true` 是因为 task 自身的 `1_asset/` 目录无 symlink，但 `registration.yaml` 中的 5 个资产路径都指向真实存在的 predecessor 文件，内容非空。这是 CyHex 的 symlink-check 状态标记，不影响可执行性。
- **计划质量结论**: 通过 — 6 步具体执行步骤，输入/输出明确，有保守起步策略，有停止条件，交付物路径和类型清晰
- **修复了什么**: 无（资产路径正确，protocol 完整，无需修复）
- **`handoff_check_before_exec.md`** 已写入
- **避免调用下游 prompt 生成**: 是
- **剩余阻断**: 无

---

检查完成。请确认：**检查通过
**检查完成。请确认：检查通过，开始执行 / 提出修改意见**
