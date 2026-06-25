I’ll do the checking stage from the live CyHex protocol again, then verify the current task config against the selected assets without executing the task body.
The CyHex API is reachable and version-matched. I’m reading the protocol file from the returned path, then I’ll inspect the prompt/config/assets.
The checking rules require the latest prompt, protocol, registration, asset rule, project protocol/state, and key registered assets. I’m reading those now and will only inspect the selected asset paths, not redo predecessor discovery.
The project context is consistent with the package-core milestone and current workspace rules. Next I’m reading the latest action prompt and the selected task config files, then I’ll resolve each registered asset path and check it is non-empty and relevant.
The task is active, and the generated action prompt matches the current protocol at the sections I checked. I’m now verifying that each selected required asset directory resolves, is non-empty, and contains the specific package/loader/engine/guard files the protocol relies on.
The required assets resolve and contain the expected task-relevant files. I found one configuration mismatch: the protocol named `3_execution/verify_package_core.py`, while the generated prompt requires numbered step organization under `3_execution/`; I’m repairing that path and creating only empty execution step folders, not any task deliverables.
The verification driver path now matches the numbered execution layout. I’m creating only the execution workspace folders needed for the steps and then regenerating the action prompt because protocol/rules changed.
The step folders are in place and contain no deliverable content. I’m validating YAML and regenerating the prompt now.
The repaired config parses and no stale `3_execution/verify_package_core.py` reference remains. I’m calling the prompt-generation API now and will verify the new prompt exists.
The new action prompt was generated at `18:19`. I’m doing final consistency checks against that prompt path and confirming the execution folders are still just scaffolding, with no task outputs written.
### 一、我准备如何遵守 CyHex
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1`
- Uses selected assets A-001..A-004 from T-024/T-026/T-029/T-031, plus optional A-005 project protocol.
- Execution may call `GET /api/version`; only if needed, `stage_incident` for blockers or `durable_jobs` for long jobs. It must not PATCH task `done`.
- Forbidden: T-038, T-039 as input, archived T-037, reverse-query branches, `6_project_deliverable/`, predecessor task mutation, and `2_project_asset/` mutation.
- Trigger `5_report/blocked.md` if required predecessor files are unreadable, package-core assembly cannot be made importable, verification cannot run in `pxfquery`, or evidence cannot be written truthfully.

### 二、我准备如何达成任务目标
- Objective: build a T-040 package-core branch from package workspace, loader, deterministic forward query, and no-hit guard, independent of T-038.
- Plan: verify A-001..A-004 metadata and key files, assemble `4_artifact/2_persist/pxfquery-T-040/`, integrate loader/forward/guard components, write `3_execution/05_run_verification/verify_package_core.py`, run import/compile/loader/forward/no-hit checks, then write JSON evidence, lineage, T-039 handoff, registry, completion, and two Chinese HTML reports.
- Expected outputs include `pxfquery_T040_test_results.json`, `pxfquery_T040_demo_summary.json`, `pxfquery_T040_lineage.md`, `pxfquery_T040_handoff.md`, `execution_report_vYYYYMMDD.html`, and `result_report_vYYYYMMDD.html`.
- The plan is executable because all required asset directories resolve, are non-empty, and contain the expected package, loader, forward-engine, and no-hit guard files.

### 三、检查与修复
- Problems found: verification driver path was not aligned with numbered `3_execution/` step-folder layout.
- Repairs made: revised `protocol.md` and `asset_rule.yaml` to use `3_execution/05_run_verification/verify_package_core.py`; created empty step folders under `3_execution/`.
- Empty/placeholder check: required asset dirs are non-empty; current `4_artifact/registry.yaml` and `5_report/completion.md` are still pre-execution placeholders, which is correct at checking stage.
- Regenerated action prompt: `4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/2_protocol/0_prompt/2026-06-23_1819_action_prompt.md`
- Remaining blockers: none.

检查完成。请确认：检查通过，开始执行 / 提出修改意见
