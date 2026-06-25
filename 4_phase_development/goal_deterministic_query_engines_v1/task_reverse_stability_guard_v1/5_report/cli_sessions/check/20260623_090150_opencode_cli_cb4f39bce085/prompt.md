# Checking Prompt
Generated: 2026-06-23 09:01

## 1. Mandatory CyHex Protocol Read
Before any checking work:

1. Call `GET http://localhost:47291/api/version`.
2. Read `cyhex_protocol.md` from the returned `protocol_path`.
3. Use the Checking Stage rules from that file as the workflow authority.
4. Do not rely on memory or on a summary of CyHex.

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/cyhex_protocol.md

## 2. Checking Assignment
You are in the CyHex checking stage. Do not execute the task deliverable.

Your job is to decide whether the current task configuration can actually achieve the objective under CyHex rules. You must repair fixable configuration defects directly, then report evidence for human approval.

Required work:
1. Read the latest action prompt, current protocol, asset registry, and asset rule.
2. Treat the configuration-stage asset registry and asset rules as the selected source of truth.
3. Read key registered/required assets only when needed to judge whether the selected configuration is real and executable.
4. Verify that protocol Steps can achieve the Objective with the selected assets.
5. If Steps are vague, impossible, fake, or disconnected from assets, revise `protocol.md`.
6. If asset paths/rules are missing, unreachable, or overclaiming, revise `asset_rule.yaml` and/or `registration.yaml`.
7. Regenerate the downstream action prompt after any repair.
8. Stop and report blockers if a critical asset is missing and cannot be acquired by the task.

## 3. Project Reads
Project: PxFquery (P-012)
Phase: development | Status: active

Read project protocol:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/0_overview.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/1_goal.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/2_rule.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/3_environment.md

Read project state:
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/state.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/current_state.md

## 4. Current Task Reads
ID: T-032 | Name: reverse_stability_guard_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} reverse-query numerical stability guard for zero-norm/abnormal similarity warnings. Deliver patch, tests, and ranking sanity evidence.
Notes / User Natural-Language Intent: 
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1

Read these files before judging readiness:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/2_protocol_split/protocol.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/1_asset/registration.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/3_asset_rule/asset_rule.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/0_prompt/2026-06-23_0858_action_prompt.md
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/3_execution

## 5. Configuration-Selected Asset Scope
The configuration stage has already selected the task's assets and rules. Do not repeat the full predecessor-task discovery workflow from the configuration stage.

Use the current task's `registration.yaml` and `asset_rule.yaml` to decide what to read. If a registered asset points into another task, read that specific asset path and enough nearby metadata to verify it is the correct file. Do not browse unrelated predecessor-task material unless the selected asset path or current protocol explicitly requires it.

## 6. Checks To Perform
You must explicitly check:
1. Status is active. If not active, PATCH it to active.
2. Every registered/required asset path resolves to a readable file or directory, or has a clear acquisition action.
3. Local registered/required assets are not empty shells: files must have nonzero content and directories must contain task-relevant files unless the protocol explicitly says the asset is a placeholder to be acquired later.
4. `protocol.md` has concrete executable Steps, not only a goal statement.
5. `protocol.md` has a concrete non-empty deliverable list with expected file type/path or acceptance criteria. If no real deliverable can be named, checking fails.
6. Each Step is grounded in selected assets, project protocol, or a permitted acquisition action.
7. The protocol does not overclaim what the selected assets prove.
8. The latest action prompt is consistent with the current protocol and asset rules.
9. `3_execution/` step folders are appropriate for the Steps, or create/update them if CyHex protocol requires it.
10. The task can produce the required deliverables without changing scope, and the planned deliverables are not blank placeholder files or empty directories.

## 7. Repair Rules
If a problem is fixable, fix it now:
- Revise `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/2_protocol_split/protocol.md`
- Revise `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/2_protocol/3_asset_rule/asset_rule.yaml`
- Revise `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/1_asset/registration.yaml` if asset registration is missing or wrong
- Regenerate action prompt with:
  `POST http://localhost:47291/api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/prompt/generate`

Do not execute the task body. Do not write deliverables under `4_artifact/`.

## 8. Final Evidence Report
Output a concise checking report with exactly these sections:

### 一、我准备如何遵守 CyHex
- Actual files and directories this task will use
- Actual API calls needed during execution
- Forbidden directories or actions
- Conditions that would trigger `5_report/blocked.md`

### 二、我准备如何达成任务目标
- Restate the task objective in your own words
- Step-by-step execution plan tied to actual assets
- Expected outputs and report path
- Why the plan is now executable

### 三、检查与修复
- Problems found
- Repairs made
- Empty or placeholder assets/deliverables checked
- Action prompt path after regeneration, if regenerated
- Remaining blockers, if any

End with exactly one of:
- `检查完成。请确认：检查通过，开始执行 / 提出修改意见`
- `检查发现问题，无法进入执行。需要补充：...`

## Hard Stops
- 不执行任务本体
- 不写 4_artifact/ 交付物
- 不把 task 标记为 done
- 不跳过人类检查确认点
