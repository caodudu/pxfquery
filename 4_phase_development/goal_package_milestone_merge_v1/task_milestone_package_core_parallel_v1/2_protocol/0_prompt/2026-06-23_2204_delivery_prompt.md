# Delivery QA Prompt
Generated: 2026-06-23 22:04

## 1. Mandatory CyHex Protocol Read
Before delivery QA:

1. Call `GET http://localhost:47291/api/version`.
2. Read `cyhex_protocol.md` from the returned `protocol_path`.
3. Use that file as the workflow authority.

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/cyhex_protocol.md

## 2. Delivery QA Assignment
You are reviewing the finished execution output for this one CyHex task.

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

Task:
- Project: PxFquery (P-012)
- Phase: development
- ID: T-040 | Name: milestone_package_core_parallel_v1
- Objective: Create a parallel pxfquery package-core milestone: assemble package workspace, loader/resource access, deterministic forward query, no-hit guard, and minimal package-core verification. This branch must not depend on T-038; T-039 is the only aggregation point.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1

## 3. Read Scope
Read only these local task records unless a listed artifact/report path is broken:
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/2_protocol/1_meta_info/meta.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/2_protocol/2_protocol_split/protocol.md
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/2_protocol/3_asset_rule/asset_rule.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/1_asset/registration.yaml
- [required; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/4_artifact/registry.yaml
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/4_artifact/3_document
- [optional; exists] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/5_report/completion.md
- [optional; missing] /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/5_report/reuse_summary.md

Do not scan predecessor tasks. Do not scan project-level raw assets.

## 4. QA Checks
Check whether:
1. Deliverables promised by protocol exist under `4_artifact/`.
2. Reusable outputs are registered in `4_artifact/registry.yaml`.
3. Results are not misplaced under `3_execution/` if they are meant for acceptance or downstream reuse.
4. Required HTML reports exist under `4_artifact/3_document/` when required by this CyHex version.
5. Reports explain what was done, what was produced, limitations, and how downstream tasks should reuse the output.
6. `5_report/completion.md` and/or `5_report/reuse_summary.md` gives a concise summary usable by later config stages.

## 5. Allowed Repairs
You may repair only delivery metadata and reports:
- Update `4_artifact/registry.yaml` if outputs are present but under-registered.
- Write or revise `5_report/completion.md`.
- Write or revise `5_report/reuse_summary.md`.
- Add a short delivery QA note under `5_report/delivery_qa.md`.

Do not rewrite core deliverables unless the human explicitly asks. If the deliverable itself is wrong, stop and report that execution must be revised.

## 6. Final Report
Return a concise delivery QA report:

### 一、交付物真实性
- Existing deliverables checked
- Missing or misplaced deliverables

### 二、后续复用性
- Registry/reuse summary status
- What downstream config can safely read

### 三、修复与结论
- Metadata/report repairs made
- Remaining blockers

End with exactly one of:
- `交付质检通过。可以验收。`
- `交付质检未通过。需要退回执行：...`

## Hard Stops
- 不进入全局资产扫描
- 不读取前置任务目录
- 不把 task 标记为 done
- 不把执行临时文件当成交付物
