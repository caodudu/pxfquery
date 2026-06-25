# task_llm_flash_adapter_v1 — Protocol

## Objective
Produce an optional `pxfquery-T-034` LLM adapter layer that exposes DeepSeek v4 flash as an extra provider through the existing `pxfquery.llm.LLMClient` interface, while running through the active CyHex `llm_gateway` configuration (no model switch from this task). The adapter must degrade gracefully when the flash endpoint is unavailable, ship a reproducible endpoint/config smoke record, and produce documentation explaining how the deterministic forward/reverse pipeline remains runnable without this layer.

## Inputs
- A-001: Current project protocol — Defines environment (pxfquery conda env), runtime rules, and legacy asset boundaries; this task must not violate any boundary.
- A-002: T-024 `pxfquery-T-024` workspace LLM module — Read-only reference for legacy `client.py` / `prompts.py` / `__init__.py` that defines `LLMClient`. The T-034 adapter must preserve that public interface.
- A-003: T-013 MVP capability review deliverables — Capability contract and test inventory; used to keep the adapter strictly within the optional/LLM-gated bucket.
- A-004: CyHex `llm_gateway` runtime metadata — Confirms the active provider/model for this run so the adapter targets DeepSeek v4 flash as an *additional* route rather than flipping the project default.

## Steps
1. Record the active `llm_gateway` configuration snapshot by calling `GET http://localhost:47291/api/version` and saving the trimmed response to `3_execution/llm_gateway_snapshot.json`. Do **not** modify the `llm_gateway` provider from this task.
2. Read `client.py` and `__init__.py` from A-002 to capture the current `LLMClient` constructor signature, `health_check`, `parse_query`, and `summarize_*` method contracts.
3. Create `4_artifact/2_persist/workspace/src/pxfquery/llm/adapters/deepseek_flash.py`. Implement `DeepSeekFlashAdapter`, a subclass/composer of `LLMClient`, that:
   - accepts `api_key`, `base_url` (default `https://api.deepseek.com/v1`), and `model` (default `deepseek-v4-flash`);
   - uses the same `litellm`-compatible pattern as the legacy client;
   - on connection, auth, or HTTP failure, returns a structured `AdapterUnavailable` result (`{"ok": False, "reason": "...", "latency_ms": N}`) instead of raising, and exposes `health_check()` returning the same shape.
4. Update only this task's `4_artifact/2_persist/workspace/src/pxfquery/llm/__init__.py` to re-export `DeepSeekFlashAdapter` alongside `LLMClient`. Do not touch A-002 or any sibling task artifact.
5. Write the workspace-level `pyproject.toml` amendment under `4_artifact/2_persist/workspace/pyproject.toml` adding an optional dependency marker `; python_version >= "3.10" and extra == "llm-flash"` for `litellm>=1.40` (already pulled in by the legacy package; re-pin only if missing).
6. Run deterministic smoke checks in the `pxfquery` conda environment:
   - `python -c "from pxfquery.llm import LLMClient, DeepSeekFlashAdapter; print('imports OK')"`
   - `python -m py_compile` over every module under `4_artifact/2_persist/workspace/src/pxfquery/llm/`
   - `python 3_execution/smoke_endpoint.py --provider deepseek-flash` which calls `DeepSeekFlashAdapter.health_check()` without sending real traffic and writes the JSON record to `4_artifact/2_persist/deepseek_flash_smoke_vYYYYMMDD.json`. If the runtime cannot reach the endpoint, the script must record `status=unavailable` with `reason` and exit 0 — the task uses this as graceful fallback evidence, not a failure.
7. Produce `4_artifact/3_document/pxfquery_T-034_adapter_notes_v20260623.md` documenting:
   - how to enable the optional exposure (`pip install pxfquery-T-034[llm-flash]`);
   - how the deterministic forward/reverse pipeline continues to run when `DeepSeekFlashAdapter` is absent or unreachable;
   - the exact smoke record path and what `unavailable` vs `ok` mean.
8. Produce `4_artifact/3_document/execution_report_v20260623.html` and `4_artifact/3_document/result_report_v20260623.html`. Register all artifacts via `4_artifact/registry.yaml`.
9. Write `5_report/completion.md` summarizing the smoke outcome, the fallback path, and the downstream consumers (T-037) that can ignore this layer without functional regression.

### Required Bug-Repair Handling
- If a bug blocks a runnable deliverable, repair within this task boundary and emit the corrected output as `pxfquery-T-034`. Document the source asset / task id, changed files, validation evidence, and which downstream task should consume the corrected version.
- Do not overwrite A-002 or other upstream artifacts. Corrections must live under T-034's own `4_artifact/`.

## Constraints
- CyHex `llm_gateway` is the runtime for this session; T-034 does **not** flip the project default model to deepseek-flash.
- Do not modify `2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/` or any sibling task's `4_artifact/`.
- All Python execution must use the project `pxfquery` conda env.
- The adapter must be **optional**: import, smoke, and report paths must still succeed when the endpoint is unreachable.
- Smoke evidence must come from a `python` invocation inside this task; do not fabricate endpoint availability.
- Endpoint unavailability is a valid outcome; record it explicitly and continue.

## Deliverables
- Adapter source: `4_artifact/2_persist/workspace/src/pxfquery/llm/adapters/deepseek_flash.py`
- Adapter re-export: `4_artifact/2_persist/workspace/src/pxfquery/llm/__init__.py` (T-034-owned copy, not overwriting A-002)
- Workspace pyproject amendment: `4_artifact/2_persist/workspace/pyproject.toml`
- llm_gateway snapshot: `3_execution/llm_gateway_snapshot.json`
- Smoke script: `3_execution/smoke_endpoint.py`
- Smoke record: `4_artifact/2_persist/deepseek_flash_smoke_vYYYYMMDD.json`
- Adapter documentation: `4_artifact/3_document/pxfquery_T-034_adapter_notes_v20260623.md`
- Execution report: `4_artifact/3_document/execution_report_vYYYYMMDD.html`
- Result report: `4_artifact/3_document/result_report_vYYYYMMDD.html`
- Artifact registry: `4_artifact/registry.yaml`
- Completion note: `5_report/completion.md`

## Acceptance
- `import pxfquery.llam` (T-034 workspace) returns both `LLMClient` and `DeepSeekFlashAdapter`.
- `python -m py_compile` passes on the new adapter module.
- `DeepSeekFlashAdapter.health_check()` returns a structured dict in both reachable and unreachable scenarios without raising.
- T-034 failure or endpoint unavailability does not block T-037 deterministic forward/reverse runs.
- Reports and `5_report/completion.md` are written, and registries are populated.
