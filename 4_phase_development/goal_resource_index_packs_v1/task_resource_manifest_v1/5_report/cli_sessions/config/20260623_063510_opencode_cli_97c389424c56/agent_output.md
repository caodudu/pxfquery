I'll execute the CyHex configuration prompt. Let me start by reading the mandatory protocol and required project files.
Now I have a clear picture. T-021 produced `standard_resources/` bundle at D-004. My task T-025 is to create a "resource manifest" from that bundle. Let me inspect the standard resources bundle to understand what's in it.
Let me also peek at the existing standard_resources guide and cell line index to round out my understanding of the bundle, plus look at the lineage endpoint for context.
I now have a thorough understanding. The T-021 bundle has 19 files: 3 H5AD matrices, 10 JSON indexes, 5 CSV metadata, 1 data_description YAML. T-025 is to build a `pxfquery-{task_id}` standard resource manifest from D-004, with manifest, schema summary, and usage notes.

Let me also look at the whitelist symlinks in the T-021 task and the project asset layout for the 1_asset structure within the current task.
Now I have everything I need to configure T-025. Let me write the three required artifacts: `registration.yaml`, `protocol.md`, and `asset_rule.yaml`.

First, register the T-021 standard_resources bundle (D-004) and its companion deliverable (D-001 resource guide) as input assets — those are the explicit required predecessor artifacts named in the meta.yaml objective.
Now write `protocol.md`. The task is a configuration-task/configuration-only step: produce the standard resource manifest, schema summary, and usage notes from the T-021 D-004 bundle.
Now let me call the CyHex API to generate the
Prompt generated successfully at `2_protocol/0_prompt/2026-06-23_0645_action_prompt.md`.

---

## 配置完成报告

**1. 已读文件:**
- CyHex 协议: `/Applications/CyHex.app/Contents/Frameworks/cyhex_protocol.md`
- 项目协议: `0_overview.md`, `1_goal.md`, `2_rule.md`, `3_environment.md`
- 项目状态: `state.yaml`, `current_state.md`
- 当前 task 元信息: `meta.yaml` (T-025, active, configuring)
- 当前 task 资产: `registration.yaml` (原为空)
- 当前 task 协议: `protocol.md` (原为空壳), `asset_rule.yaml` (原为空壳)

**2. 已读前置任务 T-021:**
- `meta.yaml` (done, 2026-06-23)
- `registration.yaml` (A-001~A-008)
- `protocol.md` (完整 7-step 协议)
- `asset_rule.yaml` (含 forbidden/output 规则)
- `4_artifact/registry.yaml` (D-001~D-005, core=D-004)
- `5_report/completion.md` (全部 7 step 完成, 19 文件, float32 lossless)

**3. 资产选择与注册:**
- A-001: T-021 D-004 标准资源包 (19 文件, required)
- A-002: T-021 D-001 资源指南 (required)
- A-003~A-006: T-021 交付物 (optional reference)
- 无缺失资产

**4. 已写入/修订文件:**
- `1_asset/registration.yaml` — 6 资产注册
- `2_protocol/2_protocol_split/protocol.md` — 完整 7-step 协议
- `2_protocol/3_asset_rule/asset_rule.yaml` — 含 required/forbidden/output/modifiable 规则

**5. Action Prompt 生成:**
- 已生成: `2_protocol/0_prompt/2026-06-23_0645_action_prompt.md`

**6. 阻断:** 无

配置完成。请确认：**配置通过 / 提出修改意见**
