This is the CyHex check stage for T-033. I need to verify that the configuration produced in the previous config sessions is actually executable against real assets. Let me read the latest action prompt, current protocol/registration/asset_rule, then prove every required asset resolves.
The protocol is unchanged (system protocol is the same version). I already have it from the config session memory, but per the prompt rule I should not rely on memory — I should re-read just what I need. Let me read the parts that bear on checking (§3.2 and §6) plus the current task files
Now I need to verify every required asset path resolves to a real, non-empty file or directory. Let me probe each required asset and key optional ones in parallel
The 4-level `../../../` relative paths don't resolve from this task. The actual depth is 5 levels (task → goal_phase_development → 4_phase_development → project). Let me inspect the actual structure
Files do exist — I just used too few `../`. From T-033 you need to ascend 4 levels: `../../../../`. The paths in asset_rule.yaml and registration.yaml have `../../../` (only 3), which would land in `12_PxFquery/`, not in the sibling goal directory.

Let me confirm with absolute paths first, then write the fix
All required and optional assets exist, are non-empty (files have content, directories have entries). The T-027 directory has 10 entries (the 10 symlinks confirmed in the config stage). 

Now I need to **fix the relative paths** which are wrong (`../../../` should be `../../../../`). Let me calculate the correct path depth:
- From T-033: `../../../../goal_resource_index_packs_v1/...`
- i.e. ascend from `task_hybrid_fast_resolver_v1` → `goal_resolver_optional_layer_v1` → `4_phase_development` → `12_PxFquery` (4 levels up)

Let
OK, the structure differs — there's actually only 3 levels from this task to project root. Let
`../../../` lands in `12_PxFquery/` (project root) — so it's 3 levels, not 4. But the sibling task paths start with `../../../goal_resource_index_packs_v1/...` — meaning they assume `12_PxFquery/goal_resource_index_packs_v1/...`, but the actual goal is under `4_phase_development/goal_resource_index_packs_v1/...`.

Let me verify
Confirmed: the goal directories live under `4_phase_development/goal_resource_index_packs_v1/...`. So the correct relative path from T-033 needs **4** levels up then re-descend into `4_phase_development/`. The current `../../../goal_...` goes up to project root and looks for `goal_resource_index_packs_v1/` directly there — which doesn't exist.

Let me also verify the current action prompt generation works correctly (to ensure I haven't broken anything) and then fix the registration.yaml and asset_rule.yaml paths.
Now I'll repair the asset_rule.yaml and registration.yaml by replacing the broken `../../../` paths with the correct `../../../../4_...` paths. This is a fixable configuration defect per the check prompt's §7 (repair rules). Then I'll regenerate the action prompt.
Also fix the forbidden paths which need the same repair (they reference `../../../2_project_asset/` etc.). Project root = `12_PxFquery/`. So `../../../2_project_asset/` actually resolves to `12_PxFquery/2_project_asset/` — correct. But the `../../../6_project_deliverable/` and `../../../1_project_init/`, `../../../3_phase_digestion/` are project-root paths that still work. Let me verify each forbidden path
Forbidden paths are correct (they are project-root level). Only the sibling goal paths needed repair. Now also fix the non_modifiable section (also needs `../../../` → `../../../../4_...` because they're under goals, not project root)
Now fix the same paths in registration.yaml. These use `path:` and `origin:` keys with the same broken `../../../`. I'll do a replaceAll on the broken prefix.
Now verify the repaired paths resolve
Still broken. The shell `cd` is wrong — I'm running from my working directory. Let me
So 4 levels up = `/Users/dudu/Documents/3_Project`, but I need `/Users/dudu/Documents/3_Project/12_PxFquery`. That's 3 levels up. From there, I need to descend into `4_phase_development/goal_...`. So the correct relative path is `../../../4_phase_development/goal_...` (3 levels up to project root, then descend).

The current `../../../` does land at `12_PxFquery/` correctly — but I was searching for the goal under the project *root* (`12_PxFquery/goal_resource_index_packs_v1/`) — that's wrong. The goal lives under `12_PxFquery/4_phase_development/goal_...`.

So the fix I applied (`../../../../4_phase_development/...`) is wrong — it over-corrects (goes to `/Users/dudu/Documents/3_Project/4_phase_development/...` which doesn't exist). The correct fix is `../../../4_phase_development/goal_...`. Let me revert
All paths resolve. The correct pattern is `../../../4_phase_development/goal_...`. Now I need to undo my over-correction in both files and replace `../../../../4_phase_development/` back to `../../../4_phase_development/`. Let me do this with edits to
I need to replace `../../../../4_phase_development/` → `../../../4_phase_development/` in both files. And also `../../../../3_phase_digestion/` → `../../../3_phase_digestion/
Now verify all paths resolve from the actual task directory
One miss left: R-006 (3_phase_digestion) still has 4-up levels. Let me fix it
(The 3_execution/ ones being MISS is expected — they're deliverables to be written by execution, not current assets.) Now check the registration.yaml
All paths now resolve. Note the non-zero content checks:
- `pxfquery_T027_runtime_query_index/` is a directory of 10 symlinks (non-zero meaning — directory has 10 entries, each linking to T-021/D-004 files averaging 17KB–22MB).
- `function_index.json` = 15,513 bytes
- `pxfquery_T031_forward_no_hit_guard.py` = 6,098 bytes
- `reverse_stability_guard /2_persist/` has 3 entries (Guard warnings JSON, positive control candidates, positive control meta — all non-empty files seen earlier)

Now let me regenerate the downstream action prompt
The API returned path but the prompt body had length 0. Let me check what was actually written
The action prompt was actually written at 23,515 bytes (different from previous 25,219 since my repair changed the asset list paths in registration.yaml) — confirming regeneration picked up the repaired paths. Let me peek at the asset list portion to confirm
Important: the regenerated action prompt shows `## Assets (0)` — the registration.yaml parsing by CyHex backend is failing. Let me check whether the YAML is valid
The R-006 entry is misindented — the column spacing is wrong (4 spaces instead of aligning with `- id:`), which causes the sibling items above it (`location: local`, etc.) to be siblings of the `- id: R-006` and breaks the YAML list structure for the asset. Let me fix the indentation for R-006
Now I also need to check and fix A-002's `origin` path (R-006 was also using wrong indentation but let me also verify there's no indentation issues anywhere else). Let me validate full YAML with Python via conda
PyYAML is not available. Let me parse it manually using the structure. Let me read the whole latest state of registration.yaml to verify it's valid YAML (no indent issues)
The `origin` on R-006 line 154 now has the correct `../../../3_phase_digestion/` path. But now the `path:` values are local symlink targets (`1_asset/...`), not direct predecessor paths — this is the intended format per the schema (registering a local symlink with `origin` pointing to the real file). However, the CyHex action prompt generator saw `## Assets (0)` — likely because the backend parses `registration.yaml` but doesn't follow symlinks or its parser is strict about the `type` field matching its internal categories. Let me check whether the `origin` paths are correct for R-006
R-006 origin is correct and exists. The 0-asset detection issue from the previous regenerated prompt must be either: (a) the prompt was generated before my indent fix took effect; (b) the backend stopped treating the YAML for some reason. Let me regenerate the prompt again now that all YAML is structurally clean
Now the action prompt contains `## Assets (10)` with all 10 entries — the YAML indent fix restored backend parsing. The repaired paths are reflected. Configuration is now consistent. 

Let me also confirm the latest generated action prompt persists on disk
Action prompt regenerated with correct Assets (10) and corrected paths. Now let me write the final output.

## 一、我准备如何遵守 CyHex

### Actual files this task will use
- `../../../4_phase_development/goal_resource_index_packs_v1/task_index_name_normalizer_v1/4_artifact/2_persist/pxfquery_T027_runtime_query_index/` — 10 symlinks (7 resolver-required JSON filenames)
- `../../../4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1/4_artifact/2_persist/pxfquery_T028_function_index/function_index.json` — 91 functions, 15KB validated
- `../../../4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1/4_artifact/2_persist/pxfquery_T031_forward_no_hit_guard.py` — 6KB guard module
- `../../../4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/4_artifact/2_persist/` — 3 entries (guard warnings JSON, candidate JSON, meta JSON)

### Actual API calls during execution
- None required by the task protocol beyond `conda run -n pxfquery python ...` for Python scripts.
- CyHex `stage_incident` API if blocked; `durable_jobs` API if long-running.

### Forbidden directories/actions
- `../../../2_project_asset/` (project raw materials), `../../../6_project_deliverable/` (final deliverables), `/Users/dudu/Documents/3_Project/8_functional_query` (legacy root), `../../../1_project_init/` (project protocol/state), all predecessor `4_artifact/` directories (read-only).
- Do not modify any upstream artifact in place. Do not mark task `done`.

### Conditions that trigger `5_report/blocked.md`
- Any required asset (A-001..A-004) not readable or empty-shell.
- Python execution fails in `pxfquery` conda env.
- `example_exact_match.py` cannot produce `hit_level=EXACT`.

## 二、我准备如何达成任务目标

**Objective restatement**: Produce a `pxfquery-T-033` optional hybrid fast resolver that demonstrates EXACT / PROXY / NOT_FOUND resolver behavior over T-027 runtime indexes + T-028 function index + T-031 no-hit guard + T-032 stability guard, with runnable examples and visible metadata.

**Step-by-step plan** (tied to actual assets):
1. Read A-001→A-004 from their resolved paths to understand the resolver+guard surface.
2. Design `3_execution/pxfquery_T033_hybrid_fast_resolver.py` combining index lookups with `NoHitGuardForwardQuery` wrapper.
3. Write `3_execution/example_exact_match.py` (targets A-001 cellline_index + drug_index), `example_proxy_match.py`, `example_not_found.py` (uses T-031 guard semantics).
4. Run all three inside `conda run -n pxfquery python ...`; capture JSON evidence.
5. Write usage notes, HTML reports (execution + result), register in `4_artifact/registry.yaml`.

**Expected outputs**: 13 deliverable files listed in protocol.md's Deliverables section.
**Why executable**: All 4 required asset paths resolve to actual non-empty content. `pxfquery` conda environment is available (per project env). Resolver API surface (QueryResolver etc.) is known from legacy code and T-024 workspace.

## 三、检查与修复

### Problems found
1. **`asset_rule.yaml` and `registration.yaml` had broken relative paths**: All paths used `../../../` to reference sibling goals under `4_phase_development/`, but `../../../` lands at the project root (`12_PxFquery/`). The correct prefix to reference a sibling goal is `../../../4_phase_development/goal_...`. Found for all 10 asset paths in asset_rule.yaml's required/optional blocks, the 6 non_modifiable entries, and all 10 assets in registration.yaml (both `origin:` and `path:`).
2. **`registration.yaml` had a YAML indentation break**: R-006 entry's subfields (`location`, `identity`, etc.) were at the wrong indent level (aligned with `- id:` instead of indented under it), which broke the YAML list and caused the CyHex backend to parse 0 assets.

### Repairs made
- Fixed all path prefixes in `2_protocol/3_asset_rule/asset_rule.yaml` (16 occurrences: 4 required + 6 optional + 6 non_modifiable)
- Fixed all path prefixes in `1_asset/registration.yaml` (10 assets × 2 fields = 20 occurrences)
- Fixed R-006's indentation in `registration.yaml` (removed errant leading space on its `- id:`)

### Empty/placeholder asset checks
- All required assets confirmed non-empty: T-027 runtime index dir has 10 entries (symlinks); T-028 function_index.json is 15KB; T-031 guard module is 6KB; T-032 2_persist/ has 3 files.
- `3_execution/` deliverables are expected to be written by execution, not pre-existing — correct.

### Action prompt path after regeneration
`2_protocol/0_prompt/2026-06-23_1622_action_prompt.md` — 25,399 bytes, shows `## Assets (10)` with corrected paths.

### Remaining blockers
None. All 10 CyHex §3.2 checks pass: status=active, assets exist+non-empty, protocol has concrete steps+deliverables, steps grounded in assets, no overclaiming, action prompt consistent, 3_execution/ structure is appropriate, deliverables are not empty placeholders. The conda environment and file-writing capability are available.

检查完成。请确认：检查通过，开始执行 / 提出修改意见
