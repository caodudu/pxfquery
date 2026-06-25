I'll execute the CyHex configuration prompt for task T-032 (reverse_stability_guard_v1).
Now let me read the task-specific files and predecessor tasks in parallel.
Now let me read the T-013 predecessor task files and explore relevant project assets in parallel.
Now let me check the T-030 artifact registry for actual completed artifacts, and explore the existing workspace query module to understand stability-related concerns.
Now I have full context. Let me check the workspace 1_asset (which is a symlinked dir from within the workspace itself).

Now I understand the picture. The T-030 reverse_query_engine_v1 task is the predecessor and its workspace is `pxfquery-T-024`. The current task T-032 needs to add numerical stability guard logic on top. Let me check the existing assets and look at the README for the task.
Now I have a complete picture. T-030 has all the necessary context already configured in its `1_asset` directory (`T-024 workspace package`, `T-026 loader outputs`, `T-021 standard resources`, `T-013 MVP capability review`, `Current project protocol`). My task is to configure T-032 which will consume T-030's reverse query engine output and T-013's warning evidence.

Let me check the existing CyHex orchestrator's guide briefly for proper asset rule format and then write the configuration.
The API works. Now I need to properly configure the task. The generated prompt is using the existing (incomplete) configuration. I need to revise `protocol.md`, `asset_rule.yaml`, and `registration.yaml` to properly define what T-032 needs. Let me now write the proper configuration
Now let me write the registration.yaml. The T-030 task already has all required input assets symlinked, so I'll mirror them and also register seed and the project protocol.
Good. T-030 already has all the assets I need as symlinks. I'll create the same structure for T-032.
Now I need to find the relative path to use inside T-032 for the T-024 symlink target. T-030 uses absolute paths — let me verify and use the same approach.
Now let me write the protocol.md:
Action prompt generated successfully. Let me verify the new prompt includes our updated configuration:
The latest generation at `2026-06-23_0858` contains all the new protocol content, including the 5 registered assets, guard semantics, and `pxfquery-T-032`
**最终证据报告：**

1. **已读文件：**
   - `~/.cyhex/protocols/cyhex_protocol.md`（CyHex 系统协议）
   - T-032 当前 task 的 `meta.yaml`、`registration.yaml`（空）、`protocol.md`（旧版）、`asset_rule.yaml`（空）、`README_TASK.md`
   - T-030 前序任务：`meta.yaml`、`registration.yaml`、`protocol.md`、`asset_rule.yaml`、`artifact/registry.yaml`、`completion.md`
   - T-013 前序任务：`meta.yaml`、`registration.yaml`、`protocol.md`、`asset_rule.yaml`、`artifact/registry.yaml`、`completion.md`
   - 项目 workspace 源码：`core.py`、`query/reverse.py`、`utils.py`（全部 T-024 路径下）

2. **已读前序任务：** T-030 (reverse_query_engine_v1, done)、T-013 (MVP algorithm run-through review, done)

3. **资产选择与登记：**
   - **A-001**: T-024 workspace package (pxfquery-T-024) — 已选，含反向查询/工具函数/DataLoader
   - **A-002**: T-026 loader outputs (pxfquery-T-026) — 已选，运行时 schema 探测
   - **A-003**: T-021 standard resources bundle (D-004) — 已选，cp_func_ad.h5ad 数据
   - **A-004**: T-013 MVP capability review deliverables — 已选，cosine 零分母警告证据
   - **A-005**: Current project protocol — 已选，conda env、workspace 边界规则

4. **已写/修订文件：**
   - `2_protocol/2_protocol_split/protocol.md` — 改写：10 步执行计划、10 个交付物明确清单、guard 语义不变性要求（无回归+异常场景显式告警+NaN/Inf 剪枝）
   - `2_protocol/3_asset_rule/asset_rule.yaml` — 改写：5 required、10 forbidden、10 output、modifiable/non_modifiable 分区、5 条 notes 含 guard 语义+执行纪律
   - `1_asset/registration.yaml` — 改写：5 个资产登记，每个含 symlink 路径和用途说明
   - 同时创建了 5 个 `1_asset/` symlinks，与 T-030 资产链路保持一致

5. **生成的操作提示词路径：** `2_protocol/0_prompt/2026-06-23_0858_action_prompt.md`（22,551 字符，含完整新 protocol/asset rules/assets）

6. **阻断项：** 无。所有 required 资产 symlink 链路经过 T-030 验证且可解析，CyHex API 正常返回，`1_asset/` 已填满。

配置完成。请确认：配置通过 / 提出修改意见
