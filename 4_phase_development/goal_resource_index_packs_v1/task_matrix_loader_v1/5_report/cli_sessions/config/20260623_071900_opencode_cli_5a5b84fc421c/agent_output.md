

I'll execute this CyHex configuration prompt. Let me start by reading the CyHex protocol and all
Protocol read. Now let me load all required files in parallel.
Now let me read the predecessor tasks for context on T-025 and T-021 (these provide the standard resources and manifest).
Now let me verify the T-021 standard_resources bundle exists and inspect it, then check if T-025 manifests have been generated and are available.
Good, both T-021 bundle and T-025 manifest exist. Now let me quickly check the T-025 manifest to understand what resources this task needs
Now I have all the context I need. Let me also check if the T-025 symlinked assets path works from the T-026 task's perspective, and verify the T-021 symlinks inside
All context is gathered. Now I'll configure the task. Let me write the three configuration files: registration.yaml, protocol.md, and asset_rule.yaml
All symlinks resolved. Now let me run the prompt generation API.
Prompt generation succeeded. Let me verify the prompt file was created.
Configuration complete. Final evidence report:

---

## Configuration Evidence Report — T-026 matrix_loader_v1

### 1. Files Read
- `/Users/dudu/.cyhex/protocols/cyhex_protocol.md` (via `GET /api/version`)
- Project protocol: `1_project_init/1_project_protocol/0_overview.md`, `1_goal.md`, `2_rule.md`, `3_environment.md`
- Project state: `1_project_init/3_project_state/state.yaml`, `current_state.md`
- Current task: `2_protocol/1_meta_info/meta.yaml` (status: `active`, sub_status: `configuring`), `1_asset/registration.yaml` (empty), `2_protocol/2_protocol_split/protocol.md` (existing), `2_protocol/3_asset_rule/asset_rule.yaml` (empty), `2_protocol/0_prompt/` (only `2026-06-23_0719_config_prompt.md`)
- Verified existing T-021 bundle at `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` (19 files, 323.47 MB)
- Verified existing T-025 deliverables at `task_resource_manifest_v1/4_artifact/2_persist/` (manifest YAML, schema summary, usage notes)

### 2. Predecessor Tasks Read
- **T-025 resource_manifest_v1** (status: `done`) — meta.yaml, registration.yaml (A-001..A-006), protocol.md (157 lines, 7 steps + repair handling + scoped repair constraints), asset_rule.yaml, registry.yaml (D-006..D-011), completion.md
- **T-021 standard_resources_optimal_formats** (status: `done`) — meta.yaml, registration.yaml (A-001..A-008), protocol.md (169 lines), asset_rule.yaml, registry.yaml (D-001..D-005), completion.md. Confirmed canonical bundle is `{cp,sh,xpr}_func_ad.h5ad` float32 + 10 JSON indexes + 5 CSV metadata + `data_description.yaml`.

### 3. Assets Selected / Registered
9 assets registered in `1_asset/registration.yaml`, symlinked under `1_asset/`:
- **A-001** (required): T-025 resource manifest (D-006) — source-of-truth inventory
- **A-002..A-003** (optional): T-025 schema summary, T-025 usage notes
- **A-004** (required, core): T-021/D-004 bundle — the actual data to load
- **A-005..A-009** (optional): T-021 std resource guide, execution/result reports, process records, artifact registry
- **Intentionally not used**: legacy flat library, `/Users/dudu/Documents/3_Project/8_functional_query`, project-level raw materials — all marked `forbidden` in asset_rule.yaml
- **No missing assets**: upstream T-021 bundle + T-025 manifest exist on disk; no external acquisition needed

### 4. Files Written or Revised
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/1_asset/registration.yaml` — 9 assets (rewritten)
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/2_protocol/2_protocol_split/protocol.md` — full CyHex §3.1 / §3.3-style protocol (rewritten: Objective, Inputs A-001..A-009, 6 Steps including repair handling, Constraints including scoped-repair + loader discipline, Deliverables, Acceptance)
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/2_protocol/3_asset_rule/asset_rule.yaml` — version 1 with required/optional/forbidden/output/modifiable/non_modifiable lists (rewritten)
- 9 symlinks under `1_asset/` created pointing to T-025 / T-021 upstream files

### 5. Generated Action Prompt Path
- `POST http://localhost:47291/api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_matrix_loader_v1/prompt/generate` → HTTP 200
- Written to: `4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/2_protocol/0_prompt/2026-06-23_0725_action_prompt.md` (20,435 bytes)

### 6. Blockers
None. Name/objective in `meta.yaml` are consistent with protocol and predecessor intent (. `objective: Create pxfquery-{task_id} matrix/resource loader using T021 xpr/sh/cp standard resources.`) — no correction needed.

---

**配置完成。任务目标：构建 `pxfquery-T-026` 矩阵/资源 loader，从 T-021 xpr/sh/cp 标准资源与 T-025 manifest 出发，运行时发现并验证资源结构（不硬编码 schema），交付 loader 代码、验证脚本与报告。提示词路径：`4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/2_protocol/0_prompt/2026-06-23_0725_action_prompt.md`。请确认：配置通过 / 提出修改意见**
