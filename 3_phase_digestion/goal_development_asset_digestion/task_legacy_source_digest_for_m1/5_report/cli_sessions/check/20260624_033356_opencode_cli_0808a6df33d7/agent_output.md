

I'll start by understanding the task structure and then
All assets verified, symlinks intact, protocol well-structured. Writing the handoff report now.
### 一、我准备如何遵守 CyHex

- **Task 实际路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1`
- **允许写入目录**: `4_artifact/`, `5_report/`, `2_protocol/` (协议/资产规则), `1_asset/registration.yaml`
- **禁止目录/行为**: 不得扫描 `2_project_asset/` 整棵树；不得读取 T024-T040；不得修改 legacy 源或已完成 task 的产出；不得写 M1 实现代码
- **执行阶段必须先读**: A-001 (source map) 确认 A-003 路径 → A-003 包源码目录
- **触发 `blocked.md` 的条件**: A-003 symlink 断裂或目标不存在；A-001 报告的路径与 A-003 实际路径矛盾

### 二、我准备如何达成任务目标

**复述目标**: 对 T-007 source map 注册的唯一 migrated package source (A-003) 做源分析，输出 M1 可用模块/函数/模式、不可用/风险部分，以及下游任务的引用边界规则。

**执行策略 (7 步)**:
1. 读 A-001 确认 A-003 路径与优先级规则
2. 遍历 A-003 目录树，盘点顶层文件/模块
3. 读核心文件识别 entry points、loader API、forward/reverse query、index 访问、no-hit 行为
4. 读 A-005 交叉检查风险项；必要时读 A-002/A-004
5. 产出 `legacy_source_digest_m1.md` + `legacy_module_reuse_matrix_m1.csv` + `legacy_reference_boundaries_m1.yaml`
6. 注册到 `4_artifact/registry.yaml`
7. 写 `5_report/completion.md`

**保守起步**: 先确认 A-003 结构是否匹配预期模块清单，再做逐文件阅读。

**预期交付物与验收信号**: 3 份文件 (digest/reuse matrix/boundary YAML) + 1 completion note + registry 登记；所有产出必须映射到 T046/T048/T049/T052 任务。

### 三、检查与修复

- **资产预检结论**: ✅ 通过 — 5 个 assets 全部 `ok`，symlink 全部指向有效目标文件
- **计划质量结论**: ✅ 通过 — 6 个执行步骤 + 4 个具体交付物 + 明确 scope 边界 + 低成本风险评估到位
- **修复了什么**: 无修复需要
- **`handoff_check_before_exec.md`**: ✅ 已写入 `5_report/handoff_check_before_exec.md`
- **是否避免调用下游 prompt 生成**: ✅ 是，没有调用任何 `/prompt/generate*` 端点
- **剩余阻断**: 无

---

检查完成。请确认：检查通过，开始执行 / 提出修改意见
