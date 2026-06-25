I’ll first load the local CyHex protocol from the API, then read the project/task/predecessor files and inspect candidate assets before editing the current task configuration.
The CyHex API is reachable and protocol `matched: true`. I’m now reading the task format reference and the specific project/task files so the configuration matches the required file schema and upstream assets.
The project protocol confirms this is a current-workspace development task, with migrated flat assets preferred over old source roots. I’m checking the current task state and the four allowed predecessor tasks before deciding what to register.
The current task already has a substantive configuration. I’m validating it against the required predecessors now, especially whether the registered assumptions about empty or usable artifacts are true.
The project asset library has only general package and legacy indexes relevant at this stage; the current task’s scoped inputs are clearly the four predecessor task roots rather than broad raw data. I’m reading those predecessor registries and reports next.
The predecessor reads show an important inconsistency: T-030 and T-036 are marked done in metadata, but their visible artifact registries are empty and completion reports are pending. I’m doing a shallow file inventory to distinguish missing registration from missing files, without executing anything.
The shallow inventory confirms T-030 and T-036 have no concrete execution or artifact files beyond empty registries and pending completion stubs, while T-032 and T-035 have concrete JSON, scripts, reports, and registries. I’m making small revisions so the task configuration states that evidence precisely and preserves the T-040/T-037 exclusions.
I’m checking the project task graph only for the current task’s dependency edges, not changing it. That helps verify the configuration does not accidentally introduce the forbidden branches.
I’m revising only the current task’s configuration files: asset registration, protocol, and asset rule. The edits are narrow: they record the verified predecessor evidence state and keep execution focused on packaging, summaries, and T-039 handoff.
The configuration files are updated. I’m validating the YAML shape and then calling the CyHex prompt generation endpoint required by the workflow.
One duplicated note appeared in `asset_rule.yaml` after the revision. I’m cleaning that up, then I’ll re-run schema validation with a direct local Python call and generate the action prompt.
The YAML validation command had a quoting issue, not a file issue. I’m rerunning it in a simpler form and checking file modification state.
This repository appears untracked at this task path, so `git diff` is not useful for these files. I’m using Ruby’s built-in YAML parser instead of Python’s missing PyYAML module.
YAML parses cleanly. I’m now generating the downstream action prompt and verifying that CyHex wrote it under the task’s `0_prompt/` directory.
**Evidence Report**

1. Files read:
- CyHex API/version and `/Applications/CyHex.app/Contents/Frameworks/cyhex_protocol.md`
- CyHex task format reference
- Project protocol: `0_overview.md`, `1_goal.md`, `2_rule.md`, `3_environment.md`
- Project state: `state.yaml`, `current_state.md`
- Project asset READMEs and shallow asset indexes under `2_project_asset/`
- Current T-038 `meta.yaml`, `registration.yaml`, `protocol.md`, `asset_rule.yaml`, prompt list
- Required predecessor files for T-030, T-032, T-035, T-036: meta, asset registration, protocol, asset rule, artifact registry, completion report
- Shallow file inventories for T-030/T-032/T-035/T-036

2. Predecessor tasks read:
- T-030 `reverse_query_engine_v1`
- T-032 `reverse_stability_guard_v1`
- T-035 `smoke_tests_v1`
- T-036 `demo_cli_v1`

3. Assets selected / missing / not used:
- Selected and registered: A-001 T-030 task record, A-002 T-032 reverse stability artifacts, A-003 T-035 smoke artifacts, A-004 T-036 task record.
- Missing/weak evidence recorded: T-030 and T-036 have empty visible artifact registries, pending completion stubs, and no concrete shallow-inventory deliverables beyond registry files.
- Intentionally forbidden/not used: T-040, archived old T-037, final deliverable directory, legacy source root.

4. Files revised:
- `task_milestone_reverse_demo_reports_v1/1_asset/registration.yaml`
- `task_milestone_reverse_demo_reports_v1/2_protocol/2_protocol_split/protocol.md`
- `task_milestone_reverse_demo_reports_v1/2_protocol/3_asset_rule/asset_rule.yaml`

5. Generated action prompt:
- `4_phase_development/goal_package_milestone_merge_v1/task_milestone_reverse_demo_reports_v1/2_protocol/0_prompt/2026-06-23_1846_action_prompt.md`

6. Blockers:
- None for configuration. YAML parsed successfully via Ruby. Note: project task registration text contains stale references to old T-037, but T-038 meta/protocol/asset rules and task graph now enforce T-030/T-032/T-035/T-036 only, with T-039 as the aggregation point.

配置完成。请确认：配置通过 / 提出修改意见
