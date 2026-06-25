I'll execute the CyHex check per the prompt. Let me start by verifying the API and reading the
API ok. Now read all required current-task files and
Now let me verify the key assets: A-001 (T-021 bundle) and A-002 (T-021 guide) exist and are non
The shell didn't resolve `../../../`. Let me check absolute paths and verify all assets resolve cleanly:
The actual depth is `goal_resource_index_packs_v1` and `goal_precomputed_data_exploration/task_standard_resources_optimal_formats/` are siblings in `4_phase_development/`. The relative path `../../../task_standard_resources_optimal_formats/...` resolves correctly: from `task_resource_manifest_v1/` go `../../../` = `4_phase_development/`, then `task_standard_resources_optimal_formats/...`. Let me use the absolute path the bundle
19 files confirmed. The relative path I wrote `../../../task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` from `/Users/dudu/.../task_resource_manifest_v1/` correctly resolves to `/Users/dudu/.../4_phase_development/` then siblings. Let me verify the literal relative path resolution with Python:
Now let me verify the exact path to the T-021 bundle from the T-025 task directory:
From T-025's directory, we need to go up 1 level (to `goal_resource_index_packs_v1`), then up 1 level (to `4_phase_development`
The correct relative path is `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/...`, NOT `../../../task_standard_resources_optimal_formats/...`. The `../../../` overshoots one directory (goes to `12_PxFquery/`). This is a real defect in the configuration that must be repaired per the protocol update directive (use task-id temporary versions, record lineage, do not
Now repair the protocol.md `source_bundle.path` line and `asset_rule.yaml` forbidden path:
Prompt
Generated. Final verification — read the repaired registrations back to confirm:
All 6 assets resolve to real, non-empty paths with 19 files in the bundle, 13KB guide, 7KB and 14KB reports, 9 entry process records, and a 2.8KB registry.

---

### 一、我准备如何遵守 CyHex

- **Task 目录**: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_resource_manifest_v1`
- **使用的 API**: `POST /api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_resource_manifest_v1/prompt/generate`（prompt 再生）；`POST .../artifacts/auto_register`（执行阶段输出登记，可选）；`POST .../stage_incident`（阻断时故障上报）
- **禁止写入的目录**: T-021 bundle 及其全部产出（`goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/`），项目资产根目录，`8_functional_query`，当前 task 的 `1_asset/` 和 `2_protocol/`，`4_artifact/` 中非 `2_persist/` 的其他子目录
- **触发 blocked.md 的条件**: A-001 bundle 不可读或文件数 ≠ 19；manifest 生成后 Python 验证发现文件名与 bundle 不一致；无法调用 anndata/pandas 库（capability_failed）；prompt 与 protocol 不一致且无法再生

### 二、我准备如何达成任务目标

从 T-021 标准资源包（A-001, 19 个文件）中，构建 **pxfquery-T025 标准资源 manifest**（YAML 格式的完整索引）、**schema 摘要**（Markdown 可读参考）和**使用手册**（Markdown, 含加载示例和验证规范）。具体步骤：

1. `os.listdir(A-001)` 枚举 bundle 内容 → 内嵌到 manifest 草稿中  
2. 按 H5AD/JSON/CSV/description 分类推导每个文件的 schema → 写入 manifest YAML  
3. 构建一份 19-entry manifest YAML（写入 `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml`）  
4. 编写 schema summary（写入 `...pxfquery_T025_schema_summary_v20260623.md`）  
5. 编写 usage notes（写入 `...pxfquery_T025_usage_notes_v20260623.md`）  
6. Python 验证：文件计数匹配、bundle 大小在 manifest 中 ±5%、data_description.yaml 存在  
7. 登记 4 个新 artifact，编写 `completion.md`

**预期产出**: 3 个 Markdown/YAML 文件存入 `4_artifact/2_persist/`，1 个 validation JSON 存入 `3_execution/`，更新后的 `4_artifact/registry.yaml` 和 `5_report/completion.md`。不产生新数据，不复制 bundle 字节。

### 三、检查与修复

1. **配置阶段 bug 已修复**：T-025 配置 AI 使用的相对路径 `../../../task_standard_resources_optimal_formats/...` 多下探了一个 `../../../`，解析目标位于 `/12_PxFquery/task_standard_resources_optimal_formats/`（不存在）。正确路径应为 `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/...`。
2. **修复范围**：`registration.yaml`（A-001 至 A-006 路径）、`protocol.md`（step 1 位置描述和 manifest 模板路径）、`asset_rule.yaml`（forbidden path）。均已重写为正确的 `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/...`。
3. **修复后验证**：所有 6 个资产路径指向真实存在的非空文件/目录（A-001 目录含 19 个文件，A-002 文档 13KB，A-003/A-004 HTML 报告 7.4KB/13.7KB，A-005 目录含 9 个条目，A-006 文件 2.8KB）。
4. **再生 prompt 已生成**：`2_protocol/0_prompt/2026-06-23_0655_action_prompt.md`。
5. **状态**：`active` / sub_status `checking`, `fast_pass_permission: green` — 配置阶段后已自动推进至检查阶段。
6. **无剩余阻断**。

检查完成。请确认：**检查通过，开始执行 / 提出修改意见**
