I’ll load the CyHex protocol from the local API first, then read the required project/task/predecessor files and configure only the task protocol and asset rules.
The local CyHex API is reachable and returned protocol version `v2.11`. I’m reading that protocol file now and will treat it as the workflow authority for this configuration.
I have the CyHex configuration requirements: register inputs, write task-only `protocol.md`, write minimal executable `asset_rule.yaml`, generate the prompt, then report evidence. Next I’m reading the project/task/predecessor files and only directory-level asset indexes unless a candidate needs detail.
Project rules confirm this should stay inside the current project tree, prefer migrated assets and predecessor outputs, and keep legacy roots read-only. I’m reading the selected predecessor protocols and registries next so the new task can reuse those outputs without depending on T-038.
The predecessor outputs provide exactly the package workspace, loader, forward engine evidence, and no-hit guard that this milestone should aggregate. I’m checking the current task’s existing config and asset directory now, then I’ll register the selected inputs and write the task-specific protocol.
The current task already has a preliminary configuration and even some downstream output files present. I’m going to validate the config against the requested scope, tighten the asset paths if needed, and avoid touching `4_artifact/` or task status.
The current `4_artifact/registry.yaml` is empty and `completion.md` is pending, so the task is not actually completed. I’m reading the CyHex task format reference before editing the registration and asset rule files, because this configuration stage writes those formats directly.
The format reference confirms the current registration structure is usable, but I’m going to make it more explicit and execution-ready: predecessor artifacts stay required and read-only, while project raw assets remain optional/reference-only because this milestone should consume the task-versioned outputs.
I’m revising the task configuration now. The changes are confined to `1_asset/registration.yaml`, `2_protocol/2_protocol_split/protocol.md`, and `2_protocol/3_asset_rule/asset_rule.yaml`; no execution artifacts or completion status will be changed.
Asset registration now names the four required predecessor deliverable bundles explicitly and adds the project protocol as a read-only reference. I’m tightening the execution protocol around package-core assembly, verification, and T-039 handoff.
The protocol now spells out the exact package-core assembly and verification contract, including the T-038 independence check and T-039 handoff. I’m aligning the asset rule with the same boundary and output list.
One asset-rule item was too broad: forbidding all `2_project_asset/` would block documented reference reads if an executor hits a justified asset question. I’m narrowing that to read-only/non-modifiable instead of forbidden.
The editable configuration files are now revised. I’m validating the YAML and then will call the CyHex prompt-generation API required by the configuration workflow.
The system Python lacks PyYAML, so I’m validating with the project conda interpreter using a direct `-c` command rather than stdin.
The YAML files parse cleanly. I’m generating the downstream action prompt through the CyHex API and then checking where it landed.
Prompt generation succeeded and returned an action prompt path. I’m checking the file exists on disk before giving the evidence report.
**Evidence Report**
1. Files read:
- CyHex: `/Applications/CyHex.app/Contents/Frameworks/cyhex_protocol.md`, `cyhex_task_format_reference.md`
- Project protocol/state: `0_overview.md`, `1_goal.md`, `2_rule.md`, `3_environment.md`, `state.yaml`, `current_state.md`
- Current task: `meta.yaml`, `registration.yaml`, existing `protocol.md`, existing `asset_rule.yaml`, pending `4_artifact/registry.yaml`, pending `5_report/completion.md`
- Project assets browsed: raw-material README files and legacy package directory listing

2. Predecessor tasks read:
- T-024 `workspace_package_v1`: protocol, asset registration, artifact registry, completion
- T-026 `matrix_loader_v1`: protocol, asset registration, artifact registry, completion
- T-029 `forward_query_engine_v1`: protocol, asset registration, artifact registry, completion
- T-031 `no_hit_guard_v1`: protocol, asset registration, artifact registry, completion

3. Assets selected/registered:
- Required: A-001 T-024 pxfquery workspace package
- Required: A-002 T-026 matrix/resource loader
- Required: A-003 T-029 forward query engine
- Required: A-004 T-031 no-hit guard
- Optional/reference: A-005 current project protocol
- Missing assets: none
- Intentionally not used: T-038, T-039, T-030/T-032/T-035/T-036, archived T-037, direct legacy raw package assets except for browsing candidate context

4. Files revised:
- `1_asset/registration.yaml`
- `2_protocol/2_protocol_split/protocol.md`
- `2_protocol/3_asset_rule/asset_rule.yaml`

5. Generated action prompt:
- `4_phase_development/goal_package_milestone_merge_v1/task_milestone_package_core_parallel_v1/2_protocol/0_prompt/2026-06-23_1815_action_prompt.md`

6. Validation/blockers:
- YAML parsed successfully for registration and asset rule.
- Prompt generation API succeeded.
- No blockers.

配置完成。请确认：配置通过 / 提出修改意见
