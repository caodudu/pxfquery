I'll execute this CyHex configuration prompt step by step.
Protocol read. Now read task format reference and project protocol files in parallel.
Now read current task files and predecessor tasks in parallel.
Now read predecessor tasks T-007 and T-013
Now read T-013 predecessor task files in parallel:
Now let me also read T-013's completion report
Now let me browse the project asset library structure to understand the package code
Good. The package has a real `core.py` (referenced from `__init__.py`) and a historical `main.py` (placeholder class). Let me check the `core.py` and understand the package top-level interface
The legacy package has a flat layout with `__init__.py` and submodules at root. The current task wants "pyproject/src layout" — meaning a src-layout (`src/pxfquery/...`) package. Let me check 4_artifact and existing 1_asset directories in T-024
Now I have enough understanding. Let me also quickly check what `pxfquery_package/core.py` actually imports and the package data dirs to understand
I have enough context. Let me also confirm where the `0_prompt` file is and the existing `__init__.py` files have body content:
Now generate the action prompt:
Action prompt generated and stored at the indicated path. Now produce the final evidence report:
## Final Evidence Report

### 1. Files Actually Read
- `~/.cyhex/protocols/cyhex_protocol.md` (CyHex system protocol, v2.11)
- `~/.cyhex/protocols/cyhex_task_format_reference.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/0_overview.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/1_goal.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/2_rule.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/3_environment.md`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/state.yaml`
- `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/current_state.md`
- `legacy_flat_asset_library_v20260614/README.md`, `code/pxfquery_package/README.md`, `__init__.py`, `pyproject.toml`, `main.py`, `core.py` (first 60 lines), `data/__init__.py`, full module tree listing

### 2. Predecessor Tasks Actually Read
- **T-007** `task_digest_pxfquery_development_state`: `meta.yaml`, `1_asset/registration.yaml`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`
- **T-013** `task_mvp_algorithm_run-through_review`: `meta.yaml`, `1_asset/registration.yaml`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `4_artifact/registry.yaml`, `5_report/completion.md`

### 3. Assets Selected / Registered / Missing / Not Used
- **A-001** (registered): Legacy PxFquery package code (raw, local, read-only) — primary input.
- **A-002** (registered): T-013 MVP capability review deliverables (deliverable, local) — used to set realistic smoke-test expectations.
- **A-003** (registered): Current project protocol (deliverable, local, symlinked) — governance and runtime env.
- **A-004** (registered, optional): Migrated code design documents (reference, local).
- No external web/download needed; no missing assets.

### 4. Files Written or Revised
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/2_protocol/2_protocol_split/protocol.md` (Objective/Inputs/Steps/Constraints/Deliverables/Acceptance filled)
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/2_protocol/3_asset_rule/asset_rule.yaml` (replaced empty stub with full required/optional/forbidden/output/modifiable/non_modifiable structure)
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/1_asset/registration.yaml` (replaced `assets: []` with 4 assets)

### 5. Generated Action Prompt Path
- `4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/2_protocol/0_prompt/2026-06-23_0649_action_prompt.md` (generated via `POST /api/projects/12_PxFquery/tasks/goal_package_foundation_v1/task_workspace_package_v1/prompt/generate`)

### 6. Blockers
- None. Configuration completed cleanly. The task objective / name are correct and do not require revision.

配置完成。任务目标：在 T-024 下创建当前 `pxfquery` 包工作区（pyproject.toml + src/ 布局），从迁移代码仅复制、不修改，提供 import/compile smoke 证据与报告。已生成下游 action prompt。提示词路径：`4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/2_protocol/0_prompt/2026-06-23_0649_action_prompt.md`。请确认：配置通过 / 提出修改意见。
