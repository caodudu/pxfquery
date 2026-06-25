

I'll execute the CyHex configuration protocol step by step. Let me start by fetching the CyHex
Now let me read the CyHex protocol and the predecessor
Now I have a complete understanding. Let me also check the task directory structure to see existing files and confirm asset paths exist.
Now let me check the T-013 capability data and the existing README, plus the T-014 precomputed data path (since it's the standard_resources bundle that the forward query needs). Let me also check which task produced the xpr
Now I have a comprehensive understanding of the task context. Let me now check a few more important things about the query forward module and the T-026 loader's ability to load actual matrices that the forward query
Now I have a complete picture. The forward query engine requires a `unique()` perturbation ID column `cmap_name`. The T-013 capability matrix is right, and T-026 already created a loader. Let me also check the existing T-026 loader JSON to understand the actual data structure that we'll need to load.
Excellent! I now have full understanding of:
- The T-029 task is configuring a forward query engine
- T-024 (workspace package, done) delivers the pxfquery package with `ForwardQuery` and `ForwardResult` classes
- T-026 (matrix_loader, done) delivers a loader that loads xpr/sh/cp H5AD matrices and indexes
- T-013 (MVP review, done) provides gap analysis: forward query is feasible, fuzzy match has known issue, index naming broken
- The xpr H5AD matrix has 132464 obs x 91 vars (functional terms), with cmap_name/pert_id/cell_iname columns

The T-029 task is to build a runnable forward query engine deliverable. Let me now write the configuration files.
The `protocol.md` is already populated with a reasonable objective and structure — let me revise it for clarity and precision based on what I've learned from all
Prompt generated successfully. Let me verify it was written to
---

## 最终证据报告

### 1. 实际读取的文件
- `cyhex_protocol.md`（通过 `/api/version` 获取路径后读取）
- 项目协议：`0_overview.md`, `1_goal.md`, `2_rule.md`, `3_environment.md`
- 项目状态：`state.yaml`, `current_state.md`
- T-029 元信息：`meta.yaml`
- T-029 现有文件：`protocol.md`（已存在但需修订）, `asset_rule.yaml`（空白）, `registration.yaml`（空白）
- T-024 predecessor：`meta.yaml`, `registration.yaml`, `protocol.md`, `asset_rule.yaml`, `registry.yaml`, `completion.md`
- T-026 predecessor：`meta.yaml`, `registration.yaml`, `protocol.md`, `asset_rule.yaml`, `registry.yaml`, `completion.md`
- T-013 predecessor：`meta.yaml`, `registration.yaml`, `protocol.md`, `asset_rule.yaml`, `registry.yaml`, `completion.md`
- T-026 数据文件：`loader/__init__.py`, `loader/validate_loader.py`, `loader_validation_summary.md`
- T-024 源码：`__init__.py`, `core.py`, `query/forward.py`
- T-013 能力文件：`capability_contract.md`, `failure_missing_capability_list.md`

### 2. 已读的前置任务
- **T-024** workspace_package_v1（done）：提供 `ForwardQuery`/`ForwardResult` + `src/pxfquery/` 工作区
- **T-026** matrix_loader_v1（done）：提供 `load_matrix()` / `load_bundle()` loader + xpr/sh/cp 矩阵验证证据
- **T-013** MVP algorithm run-through review（done）：能力差距分析，确认 forward query 可行、fuzzy match 有FP风险、resolver 被阻断

### 3. 资产选择与注册
- **A-001** T-024 workspace package（required）→ symlink 已创建
- **A-002** T-026 matrix loader package（required）→ symlink 已创建
- **A-003** T-021 standard_resources bundle D-004（required）→ symlink 已创建
- **A-004** T-013 MVP capability contract D-001（required）→ symlink 已创建
- **A-005** T-013 failure/missing capability list D-005（required）→ symlink 已创建
- **A-006** Current project protocol（required）→ symlink 已创建
- **A-007** T-026 loader validation record D-003（optional）→ symlink 已创建
- **A-008** T-026 loader validation summary D-004（optional）→ symlink 已创建
- **A-009** T-013 capability status matrix D-003（optional）→ symlink 已创建
- 无缺失资产

### 4. 写入/修改的文件
- `2_protocol/2_protocol_split/protocol.md` — 修订为完整 T-029 前向查询引擎协议
- `2_protocol/3_asset_rule/asset_rule.yaml` — 从空白配置为完整资产规则（6 required, 3 optional, 5 forbidden）
- `1_asset/registration.yaml` — 从空白 `assets: []` 配置为 9 项资产登记
- `1_asset/` 下创建 9 个 symlink 指向相应资产

### 5. 生成的 action prompt 路径
`2_protocol/0_prompt/2026-06-23_0816_action_prompt.md`（22,753 bytes，生成成功）

### 6. 阻断项
无。配置完整可执行。

---

配置完成。请确认：配置通过 / 提出修改意见
