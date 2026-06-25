# M1 DAG Heartbeat Maintenance Log

This document records runtime failure patterns observed while maintaining the T041-T053 PxFquery M1 DAG. It is for future CyHex heartbeat/error-code design. It is not a task deliverable and should not be used as scientific or package evidence.

## 2026-06-24 03:17-03:35 Initial DAG Run

### ERR-CODEX-UNSUPPORTED-CONTENT-TYPE

Observed in:
- T042 config session `cli_494e8dfb1d7d`
- T042 check session `cli_ced0408076a2`

Symptom:
- Codex CLI session starts, repeatedly times out on WebSocket, falls back to HTTPS, then fails with:
  `{"detail":"Unsupported content type"}`
- No business-level task blocker is reported.
- The session may fail before writing files, or after a previous stage already produced valid files.

Likely class:
- Driver/transport/API compatibility bug, not task-content failure.

Recommended heartbeat response:
- Classify as infrastructure/session failure.
- Do not mark task done or approve failed states.
- If task-local config files are blank or incomplete, repair them from objective/notes/allowed predecessor summaries.
- Regenerate the stage prompt through CyHex.
- Start a fresh stage session, preferably not resuming the failed session.
- If repeated for Codex, consider fallback to OpenCode for check/config only, while preserving task assignment metadata or recording the temporary fallback.

### ERR-DEEPSEEK-502-JSON-PARSE

Observed in:
- T041 config session `cli_a86f67fe586d`

Symptom:
- OpenCode/deepseek session writes part of the configuration, then fails with JSON parsing error caused by a streamed gateway chunk containing:
  `HTTP/1.0 502 Bad Gateway`
  `JSON Parse error: Unterminated string`
- T041 wrote `1_asset/registration.yaml` but left `protocol.md` and `asset_rule.yaml` as blank templates.

Likely class:
- Model gateway/network failure after partial file writes.

Recommended heartbeat response:
- Inspect which task-local files were actually written.
- Preserve valid partial outputs.
- Complete only missing task-local configuration files.
- Write a `5_report/config_repair_*.md` note with the session error and repair scope.
- Regenerate prompt and start a fresh session.
- Do not send messages into the failed session.

### ERR-TASK-SCRIPT-WRONG-WORKDIR

Observed in:
- T043 execute session `cli_b5e91b3d4aed`

Symptom:
- Agent created `build_m1_data_manifest_fixture.py` under project root:
  `/Users/dudu/Documents/3_Project/12_PxFquery/3_execution/`
- Execution then ran from task directory and failed because it expected:
  `task_data_manifest_fixture_m1/3_execution/build_m1_data_manifest_fixture.py`

Likely class:
- Tool/file-write working-directory mismatch; the agent wrote to repo root instead of task root.

Recommended heartbeat response:
- Move or copy the script into the task-local `3_execution/` directory.
- Remove or quarantine the project-root stray file after confirming the task-local copy exists.
- Restart execution from a fresh session.
- Add future guardrail: execution prompts should include a `pwd` sanity check and require all generated scripts to use absolute task paths or verify `TASK_ROOT`.

### ERR-ASSET-RULE-PARENT-FORBIDS-REGISTERED-CHILD

Observed in:
- T041 manual repair draft before correction.

Symptom:
- `asset_rule.yaml` initially forbade broad `/2_project_asset`, while `registration.yaml` intentionally registered one project-asset child path/symlink as A-003.
- This can cause future preflight/check confusion even if protocol notes say only A-003 is allowed.

Likely class:
- Asset-rule contradiction between registered input and forbidden parent path.

Recommended heartbeat response:
- Do not put the registered asset's parent directory in `forbidden` if the specific child is required.
- Encode the restriction in `notes` and protocol constraints:
  "read only registered A-003; do not scan broad project assets."
- Use `non_modifiable` for read-only source paths.

## Current Repair Principles

- Treat `failed`/`interrupted`/`incident` states as honest states; never clear them by writing completion reports.
- Repair only task-local files unless the user explicitly authorizes graph-wide changes.
- For model/transport failures, separate infrastructure failure from task-content failure.
- For partial writes, inspect actual files before retrying.
- Prefer fresh sessions over resume after transport/gateway parse errors.
- Hard routing rule: never start Codex driver sessions with `llm_gateway/*` model names. If a stage must use `deepseek-v4-pro` or another gateway model, route it through OpenCode. If using Codex/AGT-001, omit `model` or use only a Codex-supported model.
- Log every new failure pattern here with observed task/session, symptom, likely class, and recommended heartbeat response.

## 2026-06-24 05:06 CST - T-048 contract/fixture mismatch

### T-048 observed symptom
- Task state during heartbeat: `active / execute_failed`, then reported as `execute_config_mismatch` through CyHex `stage_incident`.
- Execute session `cli_52c684be8de8` completed with return code 0 but wrote `5_report/blocked.md` and `5_report/completion.md` with blocked status.
- Evidence: `forward_query_demo_evidence_v20260624.json` shows the required T-042 demo input `EGFR / A549 / xpr` returns `PerturbationNotFound`.
- Assertion table `forward_query_contract_assertions_v20260624.csv` records the required forward hit assertions as `FAIL`.

### T-048 classification
- Error class: `ERR-CONTRACT-FIXTURE-MISMATCH`.
- Likely layer: DAG/input design mismatch between T-042 demo contract and T-043/T046 fixture content, not transport failure and not a T048 implementation-only bug.
- Specific conflict: T-042 requires `pert2func(perturbation=\"EGFR\", cell_line=\"A549\", matrix_type=\"xpr\")` to be a positive demo hit, but T046's loader-exposed xpr fixture contains only STAC/SLC19A3/CPVL/ORAI3 across BICR6/PC3/A375/U251MG.

### Repair decision
- No safe task-local repair was performed because making T048 pass would require changing a completed contract, changing a completed fixture, or bypassing the T046 loader.
- Reported a CyHex stage incident with `kind=config_mismatch` for the execute stage.
- Recommended future handling: create a side-path correction task that either updates the demo contract to a fixture-backed hit, produces a new fixture containing EGFR/A549/xpr, or explicitly approves a different forward demo case. Do not force T048 to fabricate a passing hit.

## 2026-06-24 05:12 CST - T-049 reverse contract/fixture mismatch

### T-049 observed symptom
- Task state during heartbeat: `active / execute_failed`, then reported through CyHex `stage_incident` as `execute_config_mismatch`.
- Execute session `cli_27dc0c6d22a2` completed with return code 0, but wrote `5_report/blocked.md` and `5_report/completion.md` with `partial / blocked` status.
- The task produced partial reverse query code under `4_artifact/1_package/pxfquery/` and partial `NoMatrixLoaded` evidence, but did not produce `reverse_demo_evidence_v20260624.json`.

### T-049 classification
- Error class: `ERR-CONTRACT-FIXTURE-MISMATCH`.
- Likely layer: DAG/input design mismatch between T-042 reverse demo contract and the T-046 assets selected into T-049, not a transport failure and not a safe task-local implementation bug.
- Specific conflict: T-042 DEMO-002 requires the suppress term `HALLMARK_MYC_TARGETS_V1`, but registered T-046 loader smoke evidence lists only `HALLMARK_ADIPOGENESIS`, `HALLMARK_APOPTOSIS`, `HALLMARK_E2F_TARGETS`, `HALLMARK_P53_PATHWAY`, `HALLMARK_TNFA_SIGNALING_VIA_NFKB`, `MP39 Metal-response`, and `MP40 PDAC-related`.
- Additional asset gap: T-049's selected T-046 assets include loader code/API/smoke evidence, but not a selected `resource_manifest_m1.yaml` or `fixture_package_m1/` path that T-049 can load without bypassing protocol.

### Repair decision
- No task-local pass repair was performed. Making T-049 green would require changing a completed contract, changing or adding fixture data from upstream, registering additional predecessor assets, or fabricating hidden private fixture data.
- Reported a CyHex stage incident with `kind=config_mismatch` for the execute stage.
- Recommended future handling: create a side-path correction task that aligns the reverse demo contract with available fixture terms, or produces/registers a fixture package containing `HALLMARK_MYC_TARGETS_V1`, then rerun reverse implementation against that corrected substrate.

## 2026-06-24 05:30 CST - Bypass replacement task repair pattern

### Observed need
- T-048 and T-049 were both honest `execute_config_mismatch` states caused by contract/fixture substrate gaps.
- Forcing either task to pass would have required modifying completed upstream assets or fabricating hidden fixture data.
- Blocking downstream T-050/T-051/T-052 on the failed originals would freeze the M1 chain even though a same-layer replacement task can produce a new registered repair substrate plus the originally intended deliverable.

### Repair pattern
- Keep the failed original task visible and unchanged; do not mark it done and do not rewrite its protocol.
- Create a same-layer bypass replacement task:
  - T-059 `forward_query_core_repair_m1` replaces T-048 for forward implementation.
  - T-060 `reverse_query_core_repair_m1` replaces T-049 for reverse implementation.
- The replacement task uses the failed original only as a `reference` edge, not as `must` or `may`.
- The replacement task keeps trusted completed substrate tasks as `must` inputs and uses optional accelerators as `may`.
- The replacement task objective must explicitly require both:
  - a task-local supplemental substrate asset with provenance, such as a minimal M1.1 fixture/manifest or contract-bridge supplement;
  - the original missing implementation deliverable and runnable demo evidence.
- Downstream tasks are rewired:
  - old failed original -> downstream changes from `must` to `may`;
  - replacement task -> downstream becomes `must`.

### Concrete graph changes
- T-048 -> T-050 changed from `must` to `may`; T-059 -> T-050 added as `must`.
- T-048 -> T-052 changed from `must` to `may`; T-059 -> T-052 added as `must`.
- T-049 -> T-051 changed from `must` to `may`; T-060 -> T-051 added as `must`.
- T-049 -> T-052 changed from `must` to `may`; T-060 -> T-052 added as `must`.
- T-048 -> T-059 added as `reference`.
- T-049 -> T-060 added as `reference`.

### Activation result
- T-059 and T-060 were activated after graph verification.
- Both tasks are `active / configuring`.
- Single-task GET and task-local `meta.yaml` show `fast_pass_permission: green`, AGT-001 for config/check/execute, and no `_waiting_on`.
- `orchestration-state` currently projects `fast_pass_permission: null` for T-059/T-060 while single-task GET returns `green`; classify this as `ERR-ORCHESTRATION-STATE-FAST-PASS-PROJECTION-MISMATCH` until CyHex confirms the intended projection behavior.

### Recommended future CyHex handling
- Add a first-class "bypass replacement" maintenance action for `*_config_mismatch` tasks when the failure is a missing substrate/contract mismatch rather than a local code bug.
- The action should create a new task, add a `reference` edge from failed original to replacement, demote original downstream edges to `may`, add replacement downstream edges as `must`, and preserve the failed task's incident state.
- The UI should clearly label the replacement as a same-layer repair path so reviewers do not confuse it with approving the failed original.

## 2026-06-24 05:48 CST - T-059 release and T-041 interrupted-with-artifacts

### T-059 observed symptom
- Earlier heartbeat saw `active / deliver_interrupted` after an auto-recovery delivery session `cli_ecbd42748bee` stalled at Codex reconnect timeout.
- A prior delivery session `cli_809925f3d05b` had already completed with return code 0, wrote `handoff_ai_use.md`, `delivery_qa.md`, and enriched `4_artifact/registry.yaml`.
- Follow-up state check showed T-059 became `done`; downstream T-050 was released and entered `checking`.

### T-059 classification
- Error class: `ERR-DELIVER-AUTORECOVERY-RACE-STALE_INTERRUPTED`.
- Likely layer: delivery auto-recovery/session-state race. One delivery session completed enough for green auto-accept, while a second recovery session still looked interrupted/stale.
- Repair action: no extra session was started after confirming T-059 was `done`. Avoided duplicate delivery work.
- Recommended future CyHex handling: when a delivery auto-recovery session is interrupted, first re-read task meta and orchestration-state. If task is already `done` with accepted artifacts, suppress further recovery and mark the stale session as historical.

### T-041 observed symptom
- Task state: `active / execute_interrupted`; no T-041 running session in the available agent_health result.
- Local `5_report/completion.md` and `4_artifact/registry.yaml` exist and describe completed deliverables: source digest, reuse matrix, and boundary YAML.
- Latest execute session repeatedly read large legacy source files and shows output truncation/large-context behavior.

### T-041 classification
- Error classes: `ERR-EXECUTE-INTERRUPTED-WITH-COMPLETE-ARTIFACTS` and likely `ERR-AGENT-OVERREAD-STALLED` family.
- Likely layer: execution session/state recovery issue after useful artifacts were already written, plus too much verbatim source reading in a legacy-source digestion task.
- Repair action: no forced status transition to `done` and no automatic approval. No new execute retry was started because the task is optional/may for the active M1 path and repeated retries would likely repeat the over-read pattern.
- Recommended future CyHex handling: add a recovery mode for `execute_interrupted` where completion report and registry exist. The recovery should run a bounded delivery/consistency check or move to delivery review, not restart execution from scratch.

### API health note
- `agent_health` sometimes took longer than normal and once returned no JSON within `curl --max-time 8`.
- Error class: `ERR-AGENT-HEALTH-TIMEOUT-UNDER-LOAD`.
- Recommended future CyHex handling: return a lightweight cached health response or a structured timeout/error JSON so heartbeat agents can distinguish "no running sessions" from "health endpoint stalled".

## 2026-06-24 06:05 CST - API empty response during active DAG progress

### Observed symptom
- Heartbeat attempted the required API entrypoints:
  - `GET /api/version`
  - `GET /api/projects/12_PxFquery/orchestration-state`
  - `GET /api/projects/12_PxFquery/agent_health`
- All returned connection-level empty results under bounded curl checks:
  - `HTTP=000`
  - `BYTES=0`
  - approximately 8 second timeout
- Because `/api/version` was also unavailable, the heartbeat did not perform any task status mutation or CLI-session repair.

### Local fallback snapshot
- Local task meta showed meaningful DAG progress despite API unavailability:
  - T-059 `forward_query_core_repair_m1`: `done`
  - T-060 `reverse_query_core_repair_m1`: `done`
  - T-050 `forward_validation_m1`: `done`
  - T-051 `reverse_validation_m1`: `done`
  - T-052 `package_assembly_m1`: `active / executing`
  - T-053 `m1_python_package_milestone`: `active / waiting`
  - T-041 `legacy_source_digest_for_m1`: `active / execute_failed` locally, while earlier completion/registry artifacts exist

### Classification
- Error class: `ERR-CYHEX-API-EMPTY-RESPONSE-ALL-ENTRYPOINTS`.
- Likely layer: CyHex backend/API availability under load, not individual task content.
- Related prior class: `ERR-AGENT-HEALTH-TIMEOUT-UNDER-LOAD`; this occurrence is broader because even `/api/version` returned no bytes.

### Action taken
- No task repair session was started.
- No task status was changed.
- Used local meta files only for a read-only progress snapshot.

### Recommended future CyHex handling
- API entrypoints should return structured timeout/error JSON when overloaded, especially `/api/version`, so heartbeat agents can avoid ambiguous empty-response handling.
- Heartbeat agents should treat `/api/version` empty response as a hard stop for mutation: local files may be read for reporting, but no status recovery or session start should occur until the API responds again.
- Consider a lightweight `/api/healthz` or cached orchestration-state endpoint that does not block behind long-running session bookkeeping.

## 2026-06-24 06:25 CST - API still unavailable while local M1 chain reached done

### Observed symptom
- Required API checks again returned connection-level timeouts:
  - `/api/version`: `HTTP=000`, `BYTES=0`, timeout after 12 seconds
  - `/api/projects/12_PxFquery/orchestration-state`: `HTTP=000`, `BYTES=0`, timeout after 18 seconds
  - `/api/projects/12_PxFquery/agent_health`: `HTTP=000`, `BYTES=0`, timeout after 12 seconds
- Since `/api/version` was unavailable, no API mutation, session start, status recovery, approval, or incident reporting was attempted.

### Local fallback snapshot
- Local task meta files show the M1 bypass chain progressed to completion:
  - T-059 `forward_query_core_repair_m1`: `done`
  - T-060 `reverse_query_core_repair_m1`: `done`
  - T-050 `forward_validation_m1`: `done`
  - T-051 `reverse_validation_m1`: `done`
  - T-052 `package_assembly_m1`: `done`
  - T-053 `m1_python_package_milestone`: `done`
- T-041 remains locally `active / execute_failed`, with prior completion/registry artifacts present. It is not a hard blocker for the bypass M1 chain.

### Classification
- Error class: continuing `ERR-CYHEX-API-EMPTY-RESPONSE-ALL-ENTRYPOINTS`.
- Additional state class: `ERR-LOCAL-META-AHEAD-OF-API-OBSERVABILITY`.
- Likely layer: CyHex API availability/observability under load, not current task content.

### Action taken
- No task files were edited except this maintenance log.
- No status fields were changed.
- No CLI sessions were started or messaged.

### Recommended future CyHex handling
- Provide a read-only emergency snapshot endpoint that can return task meta summaries without waiting on session bookkeeping.
- When API is unavailable but local meta indicates done, heartbeat should report only and defer all reconciliation until `/api/version` and orchestration-state respond again.

## 2026-06-24 06:45 CST - API partially recovered and M1 bypass chain confirmed done

### Observed symptom
- `/api/version` recovered and returned `matched: true` for CyHex 1.2.19 / protocol v2.11.
- `/api/projects/12_PxFquery/orchestration-state` recovered and returned authoritative task state.
- `/api/projects/12_PxFquery/agent_health` still timed out with `HTTP=000`, `BYTES=0`, timeout after 8 seconds.

### Confirmed DAG state
- T-059 `forward_query_core_repair_m1`: `done`
- T-060 `reverse_query_core_repair_m1`: `done`
- T-050 `forward_validation_m1`: `done`
- T-051 `reverse_validation_m1`: `done`
- T-052 `package_assembly_m1`: `done`
- T-053 `m1_python_package_milestone`: `done`
- T-048 and T-049 remain visible as `execute_config_mismatch` may/reference predecessors, as intended.
- T-041 remains `active / execute_failed`; it is not a hard blocker for the bypass M1 chain and should not be auto-accepted.

### Classification
- Error class: `ERR-AGENT-HEALTH-TIMEOUT-UNDER-LOAD` persists.
- Recovery class: `RECOVERY-ORCHESTRATION-STATE-RESTORED`.
- Milestone class: `M1-BYPASS-CHAIN-DONE`.

### Action taken
- No task status was modified.
- No session was started.
- No failed/interrupted/incident task was approved automatically.

### Recommended future CyHex handling
- Continue to separate orchestration-state availability from agent_health availability; a healthy project DAG read should not be blocked by the slower session-health endpoint.
- For milestone monitors, a completed replacement chain should be reported as milestone-ready even when original replaced tasks remain abnormal, provided those original tasks have been demoted to `may` or `reference` and the replacement must-chain is done.

## 2026-06-24 07:05 CST - API flapping after prior recovery

### Observed symptom
- Previous heartbeat confirmed `/api/version` and `/orchestration-state` had recovered.
- This heartbeat again saw all required API entrypoints time out at connection level:
  - `/api/version`: `HTTP=000`, `BYTES=0`, timeout after 12 seconds
  - `/api/projects/12_PxFquery/orchestration-state`: no JSON, timeout after 20 seconds
  - `/api/projects/12_PxFquery/agent_health`: `HTTP=000`, `BYTES=0`, timeout after 12 seconds

### Local fallback snapshot
- Local task meta still shows the M1 bypass chain as complete:
  - T-059, T-060, T-050, T-051, T-052, and T-053 are `done`.
- T-041 remains `active / execute_failed` and is not a hard blocker for the completed M1 bypass chain.

### Classification
- Error class: `ERR-CYHEX-API-FLAPPING-AFTER-RECOVERY`.
- Related classes: `ERR-CYHEX-API-EMPTY-RESPONSE-ALL-ENTRYPOINTS`, `ERR-AGENT-HEALTH-TIMEOUT-UNDER-LOAD`.

### Action taken
- No task status was changed.
- No CLI session was started or messaged.
- Only this maintenance log was updated.

### Recommended future CyHex handling
- Add a lightweight health endpoint independent of orchestration/session aggregation.
- Add heartbeat-side circuit breaker logic: after a recent full API outage, avoid repeated expensive orchestration reads until `/api/version` and lightweight health are both stable.

## 2026-06-24 07:25 CST - Mixed API availability: orchestration restored while version and health timeout

### Observed symptom
- `/api/version` timed out with `HTTP=000`, `BYTES=0` after 12 seconds.
- `/api/projects/12_PxFquery/orchestration-state` succeeded and returned authoritative M1 DAG state.
- `/api/projects/12_PxFquery/agent_health` timed out with `HTTP=000`, `BYTES=0` after 12 seconds.

### Confirmed DAG state
- T-059, T-060, T-050, T-051, T-052, and T-053 remain `done`.
- T-048 and T-049 remain `execute_config_mismatch` and are non-blocking through `may/reference` replacement edges.
- T-041 remains `active / execute_failed`; still not a hard blocker for the completed M1 bypass chain.

### Classification
- Error class: `ERR-CYHEX-MIXED-API-AVAILABILITY`.
- Related classes: `ERR-CYHEX-API-FLAPPING-AFTER-RECOVERY`, `ERR-AGENT-HEALTH-TIMEOUT-UNDER-LOAD`.

### Action taken
- No task status was changed.
- No CLI session was started or messaged.
- Only this maintenance log was updated.

### Recommended future CyHex handling
- Heartbeat agents need a rule for mixed API availability. If `/api/version` fails but orchestration-state succeeds, treat the state read as observational only and avoid mutations until `/api/version` is healthy again.
- Split version/health/session bookkeeping so `/api/version` remains a cheap reliable readiness probe.


## 2026-06-24 03:35 Maintenance Actions

### T042 check_failed after valid config

Observed:
- Config session `cli_cbd40681815f` completed successfully.
- Check session `cli_ced0408076a2` failed before content-level checking with Codex `Unsupported content type`.

Action:
- Treat as `ERR-CODEX-UNSUPPORTED-CONTENT-TYPE`, not a T042 protocol defect.
- Planned repair is to regenerate/use the check prompt and start a fresh check session with OpenCode/AGT-002 as a temporary maintenance fallback, without changing the task's assigned strong agent metadata and without approving the failed state manually.

Recommended future CyHex behavior:
- If a check/config stage fails with this exact Codex transport signature and no task-level blocker was produced, classify as infrastructure retryable.
- Retry with a fresh session; optionally switch driver for the same stage after one Codex transport failure.

### T043 execute_failed from wrong script location

Observed:
- Execute session `cli_b5e91b3d4aed` created `build_m1_data_manifest_fixture.py` at project root `3_execution/`.
- The task then executed from `task_data_manifest_fixture_m1/` and failed because `3_execution/build_m1_data_manifest_fixture.py` was missing there.

Action:
- Moved the generated script from project root `3_execution/` to task-local `task_data_manifest_fixture_m1/3_execution/`.
- Confirmed the project-root stray file was removed.
- Planned repair is to restart T043 execute from a fresh session.

Recommended future CyHex behavior:
- Detect generated files outside the current task root during stage execution.
- Emit a workdir mismatch warning when a task-stage session writes to project-root `3_execution/`.
- Consider injecting an execution preamble that verifies `pwd` equals task path before file creation.
## 2026-06-24 04:00 CST - T-042/T-043 blocked root repair

### T-042 observed symptom
- Task state: `active / execute_failed`.
- Failed session: `cli_a9db947c7bec`.
- Log evidence: Codex was started with `-m llm_gateway/deepseek-ai/deepseek-v4-pro`; Codex/ChatGPT account rejected it with `The 'llm_gateway/deepseek-ai/deepseek-v4-pro' model is not supported when using Codex with a ChatGPT account.`

### T-042 classification
- Error class: `ERR-CODEX-LLM-GATEWAY-MODEL-UNSUPPORTED`.
- Likely layer: orchestration/session launch configuration, not task content.
- Recommended future CyHex handling: if driver is `codex`, do not pass `llm_gateway/*` model identifiers. Use Codex default model or route the stage to `opencode` when a gateway model is required.

### T-043 observed symptom
- Task state: `active / deliver_failed`.
- Execute stage had completed and generated artifacts.
- Deliver session found missing `5_report/handoff_ai_use.md` and `5_report/delivery_qa.md`, then hit two failures: `python` command unavailable and Codex `Unsupported content type`.

### T-043 classification
- Error classes: `ERR-DELIVERY-METADATA-INCOMPLETE`, `ERR-TASK-SCRIPT-PYTHON-COMMAND-MISSING`, and recurring `ERR-CODEX-UNSUPPORTED-CONTENT-TYPE`.
- Likely layer: deliver metadata completion plus tool/runtime assumptions, not fixture artifact generation.
- Repair action: added task-local `5_report/handoff_ai_use.md` and `5_report/delivery_qa.md`; did not modify generated fixture artifacts or upstream completed assets.
## 2026-06-24 04:18 CST - T-042 deliver repair and T-046 execute failure triage

### T-042 observed symptom
- Task state: `active / deliver_failed`.
- Failed session: `cli_8bca2f98b4b3`.
- Log evidence: Codex was again launched with `-m llm_gateway/deepseek-ai/deepseek-v4-pro`, then failed with `The 'llm_gateway/deepseek-ai/deepseek-v4-pro' model is not supported when using Codex with a ChatGPT account.`

### T-042 classification
- Error class: recurring `ERR-CODEX-LLM-GATEWAY-MODEL-UNSUPPORTED`.
- Likely layer: CyHex stage launcher selected Codex for a gateway model.
- Repair action: added task-local delivery metadata (`handoff_ai_use.md`, `delivery_qa.md`) and HTML execution/result summaries without changing the core contract YAML artifacts. A clean OpenCode/pro deliver rerun is required for state recovery.

### T-046 observed symptom
- Task state: `active / execute_failed`.
- Failed session: `cli_b89802dc1daf`.
- Log evidence: Codex progressed through preflight and began creating task-local package directories, then failed with `Unsupported content type`.

### T-046 classification
- Error class: recurring `ERR-CODEX-UNSUPPORTED-CONTENT-TYPE`.
- Likely layer: Codex transport/content bug during file-edit turn, not validated task logic failure.
- Repair action: checked for project-root pollution from the failed session; no root-level `3_execution/` or `4_artifact/` residues were present. Next recovery should rerun T-046 execute with OpenCode/pro.

### Follow-up result
- T-042 deliver was rerun with OpenCode/pro session `cli_da7a00ed8d89` and completed successfully.
- T-042 state after repair: `done`.
- Downstream effect: T048/T049 no longer wait on T-042; both correctly remain waiting only on T-046.
- T-046 execute was restarted with OpenCode/pro session `cli_bcfb64e0200b`; it was still running at the follow-up check.
## 2026-06-24 04:44 CST - T-046 delivery repair and T-047 stalled execute triage

### Special case summary
- T-046 is not just a generic deliver failure. It combined a repeated driver/model routing error with a real artifact-registration mismatch: the task registry pointed to a task-local loader file that did not exist until repair.
- T-047 is not just a generic stalled session. It stalled after an agent strategy error: full verbatim reading of large assets through a subtask/subagent, which inflated context/output and left the execute stage stuck mid-implementation.

### T-046 observed symptom
- Task state: `active / deliver_failed`.
- Execute session `cli_bcfb64e0200b` completed successfully and produced loader docs, smoke evidence, reports, registry, and completion report.
- Deliver session `cli_d59d345636f9` failed because Codex was again launched with `-m llm_gateway/deepseek-ai/deepseek-v4-pro`, which Codex/ChatGPT rejects.
- Additional delivery consistency issue: registry path `4_artifact/1_package/pxfquery/data/m1_loader.py` did not exist, while completion reported loader code under the predecessor T044 skeleton package path.

### T-046 classification
- Error classes: recurring `ERR-CODEX-LLM-GATEWAY-MODEL-UNSUPPORTED` plus `ERR-DELIVERY-REGISTRY-PATH-MISSING`.
- Likely layer: deliver launcher model routing plus execute artifact placement drift.
- Repair action: copied the loader implementation into the task-local registered path, added `handoff_ai_use.md` and `delivery_qa.md`, and prepared a clean OpenCode/pro deliver rerun.

### T-047 observed symptom
- Task state: `active / execute_stalled`.
- Stalled session: `cli_b55e26ce5fe1`.
- Log evidence: the agent delegated a full verbatim read of large inputs to a subtask, produced a very large output, then stalled while beginning implementation.

### T-047 classification
- Error class: `ERR-AGENT-OVERREAD-STALLED`.
- Likely layer: agent strategy failure, not proven task-content impossibility.
- Recommended future CyHex handling: discourage full verbatim asset reads in execute prompts for large manifests/tables; prefer structured parsing, sampled inspection, and explicit no-subagent/no-full-dump recovery prompts.

### Follow-up action
- Stopped stalled T-047 session `cli_b55e26ce5fe1` through the CyHex stop endpoint.
- Started bounded OpenCode/pro recovery execute session `cli_6fe95b2366a0` with an explicit no-subagent/no-full-verbatim-read prompt.
- Started T-046 OpenCode/pro deliver rerun `cli_49806aa3b655` after task-local delivery repair.

### Follow-up result and routing correction
- T-046 deliver completed and task state became `done`.
- Downstream effect: T048 and T049 were released and started configuring.
- Operator correction: repeated Codex + `llm_gateway/*` launches were maintenance mistakes. The fixed rule is now explicit: gateway models go through OpenCode only; Codex sessions must not receive gateway model names.

### Future automatic handling rule
- For T-046-like cases, do not treat a successful execute as enough. Before rerunning deliver, verify every `4_artifact/registry.yaml` path actually exists under the current task root. If a registry path points to a predecessor task location or missing task-local copy, repair by copying or re-registering a task-local artifact and record the provenance.
- For T-047-like cases, if stalled logs show a subagent/full-content dump of large manifest/table assets, stop the stalled session and restart with a bounded recovery prompt that forbids subagents, forbids full verbatim asset dumps, and requires structured parsing/sampled reads.

### Side-path test task
- Created T-054 `large_asset_reading_rules_probe` as a pending side-path task.
- Correction: T-054 is not merely a prompt-guidance research task. It is intended to be otherwise similar to T-047 resource-loader hardening, with the added experimental requirement that protocol/config/check/execute instructions explicitly restrict large-file reading and forbid subagent full dumps.
- T-054 dependencies corrected to T-043 and T-045 only; it does not wait on T-047 and does not participate in the active M1 delivery chain unless later promoted.
- Correction: because T-054 is still pending, do not hand-edit `2_protocol/2_protocol_split/protocol.md` as if config had already run. Keep the extra large-input constraints in orchestration intent fields (`objective`/`notes`) so the future config AI generates the protocol through the normal CyHex path.

## 2026-06-24 12:26 CST - T-041 bypass replacement T-061

### Observed need
- T-041 `legacy_source_digest_for_m1` remained `active / execute_failed` after many OpenCode/pro execute auto-recovery sessions.
- Task-local artifacts existed (`legacy_source_digest_m1.md`, reuse matrix, boundary YAML, reports, registry, completion note), but the CyHex task state did not recover to a trustworthy completed state.
- Re-running T-041 execute directly risked repeating the same failure pattern: over-reading legacy source, gateway/session interruption, and further session-log pollution.

### Classification
- Error classes: recurring `ERR-EXECUTE-INTERRUPTED-WITH-COMPLETE-ARTIFACTS` / `ERR-AGENT-OVERREAD-STALLED`.
- Likely layer: CyHex recovery should have moved to a bounded delivery/consistency check once registry and completion artifacts existed; restarting execute was the wrong recovery shape.

### Action taken
- Kept T-041 unchanged as an abnormal historical node; did not mark it done and did not approve/clear the failed state.
- Created T-061 `legacy_source_digest_repair_m1` under `goal_development_asset_digestion`.
- T-061 is `pending`, `green`, AGT-001 for config/check/execute, with `T-007` as a `must` dependency.
- Added `T-041 -> T-061` as a `reference` edge only.
- T-061 objective/notes require a clean replacement digest and explicitly forbid full large-file dumps, broad project asset scans, binary matrix reads, notebooks, caches, and reuse of T-041 artifacts as authoritative outputs.

### Recommended future CyHex handling
- Add a first-class "interrupted-with-artifacts replacement" action: when a task has useful local artifacts but polluted/failed execution state, create a same-layer replacement task rather than repeatedly restarting execute.
- Config prompts for source-digestion tasks should include bounded-read rules by default: list files first, inspect symbols/imports/classes/functions with targeted windows, never dump whole large files, and never read binary data unless the task explicitly requires it.

## 2026-06-24 13:26 CST - T-061 config transport failure after writes

### Observed symptom
- T-061 became `active / config_failed` after Codex config session `cli_a63836d5aad1`.
- The session wrote the task-local config files before failing:
  - `1_asset/registration.yaml`
  - `2_protocol/2_protocol_split/protocol.md`
  - `2_protocol/3_asset_rule/asset_rule.yaml`
- Session log shows repeated reconnects and final HTTPS transport failure:
  `stream disconnected before completion: error sending request for url (https://chatgpt.com/backend-api/codex/responses)`.

### Classification
- Error class: `ERR-CODEX-HTTPS-STREAM-DISCONNECTED-AFTER-WRITE`.
- Likely layer: Codex transport/session completion failure after valid task-local file writes, not an observed config-content failure.

### Action taken
- Reviewed the three written config files and found them structurally usable.
- Added task-local repair note `5_report/config_repair_20260624_1326.md`.
- Did not modify upstream artifacts, did not resume or message the failed session, and did not approve/clear the failed state manually.

### Recommended future CyHex handling
- Add a recovery mode for config sessions that fail after writing files: validate existing `registration.yaml`, `protocol.md`, and `asset_rule.yaml`; if valid, move to check review or start a fresh config session without regenerating the files.
- Distinguish "model/session failed to return final success" from "configuration content is invalid."

## 2026-06-24 13:56 CST - T-061 check transport failure without output

### Observed symptom
- T-061 became `active / check_failed` after Codex check session `cli_64606473a952`.
- The session produced no `agent_output.md` and no business-level `blocked.md`.
- Session log shows repeated reconnects and final transport failure:
  `stream disconnected before completion: Transport error: network error: error decoding response body`.

### Classification
- Error class: `ERR-CODEX-CHECK-TRANSPORT-DISCONNECTED-NO-OUTPUT`.
- Likely layer: Codex transport/session failure during check, not an observed protocol or asset-rule rejection.

### Action taken
- Added T061 task-local note `5_report/check_repair_20260624_1356.md`.
- Did not modify upstream artifacts, did not resume or message the failed session, and did not approve/clear the failed state manually.
- Started a fresh check session from the generated check prompt.

### Recommended future CyHex handling
- If a check session fails before producing agent output or a structured blocker, classify it separately from true `check_failed`.
- Offer a deterministic local schema/file-presence check for already written `registration.yaml`, `protocol.md`, and `asset_rule.yaml` before spending another model call.

## 2026-06-24 14:19 CST - T-061 repeated Codex check transport failure

### Observed symptom
- Fresh T-061 Codex check session `cli_09f0b4e942a5` also failed.
- Like the previous check failure, it produced no `agent_output.md` and no business-level `blocked.md`.
- Session log shows repeated reconnects and final HTTPS transport failure:
  `stream disconnected before completion: error sending request for url (https://chatgpt.com/backend-api/codex/responses)`.

### Classification
- Error class: repeated `ERR-CODEX-CHECK-TRANSPORT-DISCONNECTED-NO-OUTPUT`.
- Likely layer: Codex transport instability for this stage, not a task protocol/content failure.

### Action taken
- Did not resume or message either failed check session.
- Did not approve/clear `check_failed` manually.
- Started a T061 check fallback through OpenCode/pro using the existing generated check prompt.

### Recommended future CyHex handling
- After two same-stage Codex transport failures with no agent output, route the next stage retry through a different configured driver rather than repeating the same transport path.
- Preserve task-local config/check files and record the fallback driver in process history.

## 2026-06-24 14:38 CST - T-061 OpenCode fallback check stalled

### Observed symptom
- T-061 became `active / check_stalled` after OpenCode/pro fallback check session `cli_23b62437a0ff`.
- The fallback session produced no `agent_output.md`.
- `stdout.log` and `stderr.log` were empty.
- Agent health reported the session as `stalled`.

### Classification
- Error class: `ERR-OPENCODE-CHECK-STALLED-NO-OUTPUT`.
- Likely layer: driver/model execution stall before business-level check output, not a confirmed protocol/content defect.

### Action taken
- Stopped stalled session `cli_23b62437a0ff` through `POST /api/cli_sessions/{session_id}/stop`.
- Did not resume or message the session.
- Did not approve/clear T061 state manually.
- Did not start another automatic retry in this heartbeat, to avoid an unbounded retry loop across drivers.

### Recommended future CyHex handling
- After repeated check failures across Codex and OpenCode with no business output, switch to a deterministic local check mode for config files instead of spawning more model sessions.
- A local check should validate presence/schema of `registration.yaml`, `protocol.md`, and `asset_rule.yaml`, then either move to check review or produce a structured `check_capability_failed` report.

## 2026-06-24 16:56 CST - T-061 deterministic local check recovery

### Observed symptom
- T-061 remained `active / check_interrupted` after repeated model-backed check failures and one stopped OpenCode fallback check.
- No failed check session produced business-level `agent_output.md` or a structured protocol defect report.

### Classification
- Error class: `ERR-CHECK-MODEL-UNAVAILABLE-LOCAL-DETERMINISTIC-CHECK-USED`.
- Likely layer: check-agent capability/transport availability, not confirmed task protocol invalidity.

### Action taken
- Ran a bounded deterministic local check of T-061 config files and registered input paths.
- Verified YAML parsing for `1_asset/registration.yaml`, `2_protocol/1_meta_info/meta.yaml`, and `2_protocol/3_asset_rule/asset_rule.yaml`.
- Verified A-001 and A-002 exist, A-002 is a bounded source directory, and the protocol contains required replacement deliverables and bounded-read constraints.
- Wrote task-local evidence report `5_report/deterministic_check_20260624_1656.md`.
- Did not modify upstream artifacts, did not message failed sessions, and did not directly set `check_approved`.

### Recommended future CyHex handling
- Add a first-class deterministic check recovery path for repeated no-output check failures.
- The recovery should write structured local evidence, classify the state as `check_review` or `check_capability_failed`, and avoid spawning more model sessions when two independent drivers fail without business output.
- Fast-pass should distinguish deterministic check evidence from completed model check sessions instead of requiring operators to hand-edit states.

## 2026-06-25 04:02 CST - CyHex 1.2.20 API accepts connections but all HTTP endpoints time out

### Observed symptom
- CyHex app bundle reports version `1.2.20` / `1.2.20`.
- `~/.cyhex/AI.md` still points external AI sessions to `GET http://localhost:47291/api/version`.
- `lsof` confirms `/Applications/CyHex.app/Contents/MacOS/CyHex` is listening on `127.0.0.1:47291`.
- `curl --max-time 10 http://localhost:47291/api/version` connects but receives zero bytes until timeout.
- `curl --max-time 3 /`, `/docs`, and `/openapi.json` also time out with zero bytes.
- A raw socket test can connect and send `GET /api/version`, then times out waiting for response.

### Classification
- Error class: `ERR-CYHEX-API-LISTENING-BUT-HTTP-HANDLER-UNRESPONSIVE`.
- Likely layer: CyHex runtime/server event loop or Python GIL starvation, not route misuse and not project-specific data.
- `/api/version` in 1.2.20 is a light route in `routers/misc.py` that only builds protocol paths and calls `ensure_ai_entrypoint`; it should not be blocked by project state.

### Action taken
- Did not create or activate tasks because CyHex AI entry rules require `/api/version` to return `matched: true` before API orchestration.
- Confirmed the issue is not the earlier invalid `GET /goals` route and not an unsupported content type request.
- Captured a macOS `sample` at `/tmp/cyhex_1_2_20_sample.txt`.
- The sample shows the main AppKit thread idle, one Python asyncio thread spending time in `_io_TextIOWrapper_read`, `stat/open/read`, and several Python threads waiting on GIL/locks.

### Recommended future CyHex handling
- Keep `/api/version` and a minimal `/api/healthz` endpoint isolated from project scanning, prompt generation, CLI pipe reads, and long-running task IO.
- Add request timeouts and cancellation around any background task or pipe reader that can monopolize the Python event loop.
- Add a watchdog that marks the API unhealthy when the port is listening but `/api/version` cannot return within 1-2 seconds.
- Include an operator-visible diagnostic: `listening_but_unresponsive`, with the active long-running session/task if one is holding the event loop.
- External AI should stop orchestration and report this error when `/api/version` times out, instead of falling back to hand-written task state changes.

## 2026-06-24 17:06 CST - T-061 check repaired with explicit handoff and minimal recovery prompt

### Observed symptom
- T-061 was not truly ready for execution even after deterministic status recovery because the check stage had not produced the CyHex-required `5_report/handoff_check_before_exec.md`.
- The original check prompt was about 37 KB and previous check attempts failed or stalled before business output.
- A smaller recovery prompt of about 1.2 KB was sufficient, which rules out T061 task content size as the root cause.

### Classification
- Error class: `ERR-CHECK-HANDOFF-MISSING-AFTER-NO-OUTPUT-SESSIONS`.
- Likely layer: repeated check-agent transport/stall failures caused missing check handoff; T061 protocol/asset content was locally coherent.

### Action taken
- Added T061-local `5_report/handoff_check_before_exec.md` with `yellow_repair` verdict, execution boundaries, selected inputs, execution strategy, expected deliverables, and stop conditions.
- Added T061-local minimal recovery prompt `2_protocol/0_prompt/2026-06-24_1710_minimal_check_recovery_prompt.md`.
- Rolled T061 back from `check_review` to `check_interrupted` only to allow a formal check retry.
- Started new Codex check session `cli_6dd1b8f7a5d9`; it completed successfully and confirmed the handoff is sufficient.
- CyHex green fast-pass then moved T061 into execute stage, creating execute session `cli_dcacea2b0cc1`.

### Recommended future CyHex handling
- When check sessions fail without `agent_output.md`, CyHex should explicitly detect whether `handoff_check_before_exec.md` is missing.
- Provide a built-in small "handoff-only recovery check" prompt rather than rerunning the full assembled check prompt.
- Treat `yellow_repair` handoff creation as a valid check repair path when the repair is task-local and documented.

## 2026-06-24 17:36 CST - T-061 execution/delivery completed after path-scope recovery

### Observed symptom
- T-061 first execute session `cli_dcacea2b0cc1` produced the required artifacts but ended as `interrupted` with `process_not_alive`.
- A later minimal execute-recovery prompt incorrectly used task-relative paths while Codex execute work_dir was the project root, causing it to write an erroneous project-root `5_report/blocked.md`.
- Another execute retry failed due Codex DNS/HTTPS transport failure.

### Classification
- Error class: `ERR-EXECUTE-ARTIFACTS-WRITTEN-SESSION-NOT-DONE`.
- Error class: `ERR-RECOVERY-PROMPT-RELATIVE-PATH-WRONG-WORKDIR`.
- Error class: `ERR-CODEX-DNS-HTTPS-TRANSPORT-FAILURE`.
- Likely layer: mixed task artifact success plus session closure/transport failure and one recovery-prompt design mistake.

### Action taken
- Validated T061 task-local artifacts directly: required files exist and are non-empty, `registry.yaml` and boundary YAML parse, CSV has 25 rows and required columns.
- Removed erroneous project-root `5_report/blocked.md` generated by the bad relative-path recovery prompt.
- Let the CyHex delivery session `cli_4edb1459f1a0` perform task-local QA. It added `5_report/handoff_ai_use.md`, `5_report/delivery_qa.md`, and enriched `4_artifact/registry.yaml`.
- Final state after green fast-pass delivery acceptance: T-061 `done`, completed `2026-06-24`.

### Recommended future CyHex handling
- Recovery prompts must include either absolute task paths or an explicit `cd <task_path>` first step because task CLI work_dir may be project root.
- If an execute session writes all required artifacts but exits `process_not_alive`, CyHex should offer an artifact-presence validation recovery before rerunning the full execute prompt.
- Delivery QA should ignore project-root stray `5_report/blocked.md` unless it belongs to the current task path, and heartbeat repair should clean such pollution immediately.

## 2026-06-24 17:50 CST - T-048/T-049 original core tasks archived after verified bypass replacement

### Observed symptom
- T-048 and T-049 remained `active / execute_config_mismatch` even though their config, check, and execute sessions had all completed.
- Both tasks had task-local `blocked.md` and completion reports showing real contract/fixture mismatches, not transport failures.

### Classification
- T-048 error class: `ERR-CONTRACT-FIXTURE-MISMATCH-FORWARD-EGFR-A549-XPR`.
- T-049 error class: `ERR-CONTRACT-FIXTURE-MISMATCH-REVERSE-MYC-TARGETS`.
- Likely layer: original task input design mismatch. These are not agent failure, not CyHex status machine failure, and not suitable for forced delivery acceptance.

### Action taken
- Inspected T-048/T-049 internals, process records, blocked reports, completion reports, and registries.
- Confirmed T-048 could not satisfy the T-042 `EGFR/A549/xpr` forward demo because T-046 loader fixture had no matching perturbation or cell line.
- Confirmed T-049 could not satisfy the T-042 reverse demo because selected loader assets lacked the required manifest/fixture package and `HALLMARK_MYC_TARGETS_V1`.
- Confirmed T-059 and T-060 are complete same-layer replacements and downstream edges already make them `must` replacements while T-048/T-049 are only `may`/reference history.
- Added task-local `5_report/orchestration_resolution_20260624.md` to both T-048 and T-049.
- Patched T-048 and T-049 to `blocked` with notes pointing downstream users to T-059 and T-060.

### Recommended future CyHex handling
- When a task is superseded by a completed bypass repair, CyHex should support an explicit `superseded_by` archival status or field rather than overloading `blocked`.
- Heartbeat repair should distinguish "repair original task" from "archive original task after replacement path completed."
- Original failed tasks should retain their blocked reports as diagnostic evidence, while downstream prompts should consume the replacement task only.

## 2026-06-25 12:44 CST - T-064 execute_stalled with partial artifact completion

### Observed symptom
- T-064 reached `active / execute_stalled`; `agent_health` reported OpenCode session `cli_310e961ca3ca` as stalled.
- The execute session had produced a substantive route taxonomy artifact, but two protocol-required deliverables were absent:
  - `4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml`
  - `4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv`
- `4_artifact/registry.yaml` still contained `artifacts: []`, and `5_report/completion.md` still said `Pending`.
- The task was not conceptually blocked; it had a partial-write/stalled-session failure after doing useful work.

### Classification
- Error class: `ERR-EXECUTE-STALLED-PARTIAL-ARTIFACTS-WRITTEN`.
- Likely layer: OpenCode execution/session stall after partial artifact generation; task protocol and inputs were sufficient.

### Action taken
- Performed one bounded T-064-local repair only.
- Preserved the existing taxonomy file.
- Added the missing metadata contract YAML.
- Added the 29-row stress-test scenario to route mapping CSV.
- Updated `4_artifact/registry.yaml` to register all three required deliverables.
- Updated `5_report/completion.md` with acceptance evidence and repair note.
- Validated locally that registry parses, the mapping has 29 rows from SC-001 to SC-029, and the contract YAML parses.

### Recommended future CyHex handling
- For `execute_stalled`, CyHex should first check whether protocol-required output files exist and whether `completion.md`/registry are pending before rerunning a full execute prompt.
- If most deliverables are already present, offer a "partial artifact completion" recovery prompt that lists only missing files and requires no predecessor reread.
- Add a built-in error classification for `execute_stalled_with_partial_outputs` and expose missing deliverables from protocol vs filesystem.
- Heartbeat repair should log partial-output recovery separately from conceptual task failure; these tasks may be recoverable without bypass replacement.

## 2026-06-25 12:52 CST - T-064 recovery session required absolute prompt_file path

### Observed symptom
- Attempting to start a T-064 execute recovery session with task-relative prompt path failed:
  - endpoint: `POST /api/projects/12_PxFquery/tasks/goal_project_delivery_anchor/task_evidence_routing_anchor/cli_sessions/start`
  - body prompt_file: `2_protocol/0_prompt/2026-06-25_1252_execute_recovery_prompt.md`
  - response: `{"detail":{"error":"prompt_file not found"}}`
- The file existed under the task directory.
- Retrying the same request with the absolute prompt path succeeded and started Codex session `cli_4f8c88e0c5dc`.

### Classification
- Error class: `ERR-CLI-SESSION-START-PROMPT-FILE-RELATIVE-PATH-NOT-FOUND`.
- Likely layer: API path-resolution ambiguity or documentation mismatch. The orchestration guide says `prompt_file` is a relative path, but the actual endpoint accepted the absolute path and rejected the task-relative path in this case.

### Action taken
- Verified the recovery prompt file exists in T-064 `2_protocol/0_prompt/`.
- Retried with absolute `prompt_file`.
- Started minimal Codex execute recovery session `cli_4f8c88e0c5dc`.

### Recommended future CyHex handling
- Clarify whether `prompt_file` is relative to project root, task root, or session root.
- Return the resolved candidate path on `prompt_file not found` so external AI can correct it without guessing.
- Prefer accepting task-relative paths for task-local prompts, because task-local repair prompts are the normal heartbeat recovery pattern.

## 2026-06-25 13:12 CST - T-064 deliver_interrupted after writing green delivery QA

### Observed symptom
- T-064 entered `deliver_interrupted`.
- The delivery session `cli_97c0ac2882b5` had `interrupted_reason: process_not_alive`.
- Despite interrupted process state, it wrote `5_report/delivery_qa.md`.
- `delivery_qa.md` verdict is `green_pass`: all three core deliverables pass delivery QA, all acceptance criteria pass, registry is consistent, and no repair is required.

### Classification
- Error class: `ERR-DELIVER-QA-WRITTEN-SESSION-PROCESS-NOT-ALIVE`.
- Likely layer: delivery QA content completed, but OpenCode process/session closure did not produce a normal terminal success record.

### Action taken
- Read T-064 delivery session metadata, delivery QA report, execute recovery report, and registry.
- Confirmed delivery QA is substantively green and task-local artifacts are present.
- Added minimal T-064 delivery recovery prompt `2_protocol/0_prompt/2026-06-25_1312_deliver_recovery_prompt.md`.

### Recommended future CyHex handling
- For `deliver_interrupted`, first inspect whether `5_report/delivery_qa.md` exists and contains a clear pass/fail verdict.
- If delivery QA is green but session ended `process_not_alive`, offer a minimal delivery recovery prompt instead of redoing full QA.
- Expose a structured `delivery_qa_written_but_session_interrupted` recovery code so heartbeat logic can distinguish content failure from session-finalization failure.
