# pxfquery-T-034 — Optional DeepSeek v4 flash adapter notes (T-034)

Ad-hoc task-level documentation complementing the package-level `README.md`. It explains the adapter choices, the graceful-fallback contract and the deterministic pipeline decoupling as they were actually exercised on 2026-06-23.

## 1. Why this layer exists

T-034 is the **optional adapter layer** of `goal_resolver_optional_layer_v1`. The deterministic forward/reverse pipeline (T-024 workspace + T-013 review) does not depend on any external LLM. This task adds a non-mandatory adapter that exposes DeepSeek v4 flash as **one more** LLM provider that downstream resolvers can opt into. CyHex `llm_gateway` remains the active runtime for this session; T-034 must not flip the active model.

## 2. Adapter contract

The adapter mirrors the public surface of `pxfquery.llm.LLMClient` so resolvers can swap providers without touching call sites:

| Method | Returns | Behaviour on failure |
| --- | --- | --- |
| `health_check()` | `dict` with `ok`, `model`, `reply`, `latency_ms`, `error_type`, `error_message`, `reason` | Never raises. Returns `{"ok": False, "reason": "<missing_api_key|client_build_failed|endpoint_unreachable|unexpected_reply>", "latency_ms": N}`. |
| `parse_query(user_input, available_terms=None)` | intent dict (`query_type`, `perturbation`, `cell_line`, `activate`, `suppress`, `top_n`) plus `ok` and `reason` | Empty intent + `ok=False, reason="missing_api_key"` or `reason="endpoint_unreachable"`. |
| `summarize_forward(result, max_words=200)` | `str` | On failure returns a one-liner beginning with `[DeepSeekFlashAdapter unavailable: ...]`. The deterministic result stays in `result`. |
| `summarize_reverse(result, max_words=200)` | `str` | Same as above. |

## 3. Degraded-fallback rules

The adapter is **always** reachable in a structural sense: imports succeed and `health_check()` always returns a dict. The four fallback reasons cover every observable failure mode:

| `reason` | Trigger | Pipeline impact |
| --- | --- | --- |
| `missing_api_key` | `DEEPSEEK_API_KEY` / `OPENAI_API_KEY` / `PXFQUERY_API_KEY` not set and no `api_key=` passed in. | None. Resolver switches to deterministic summarization. |
| `client_build_failed` | openai SDK fails to construct (e.g. older SDK). | None. |
| `endpoint_unreachable` | TCP connect / TLS handshake fails or HTTP error. | None. |
| `unexpected_reply` | Endpoint reachable but reply ≠ "OK". | Optional retry policy — currently returns `ok=False` once. |

None of these raise exceptions, so the deterministic pipeline never blocks on the adapter.

## 4. What was actually exercised on 2026-06-23

Three smoke runs were captured in `4_artifact/2_persist/`:

| File | Scenario | Outcome |
| --- | --- | --- |
| `deepseek_flash_smoke_v20260623.json` | Real endpoint probe, default base URL. | `status=unavailable, reason=missing_api_key, tcp_ok=true` (real API key was not provided; TCP handshake to `api.deepseek.com:443` succeeded in 365 ms). |
| `deepseek_flash_smoke_notraffic_v20260623.json` | `--no-traffic` (TCP-only probe). | `status=reachable_no_traffic, reason=skipped_by_flag` |
| `deepseek_flash_smoke_unreachable_v20260623.json` | `--base-url http://127.0.0.1:1` (forced unreachable). | `status=unavailable, reason=endpoint_unreachable, tcp_ok=false` (`ConnectionRefusedError` after 1 ms) |

The `-` imports were also verified:

```text
>>> from pxfquery.llm import DeepSeekFlashAdapter
>>> from pxfquery.llm.adapters.deepseek_flash import AdapterUnavailable
imports OK
```

…and `python -m py_compile` passed on all four new modules.

## 5. Coupling (and decoupling) with the legacy `LLMClient`

- T-024 ships the canonical `pxfquery.llm.LLMClient` under `goal_package_foundation_v1/task_workspace_package_v1/4_artifact/2_persist/workspace/src/pxfquery/llm/`. T-034 does **not** modify it.
- T-034's own `__init__.py` keeps `DeepSeekFlashAdapter` as the primary export and re-exports the legacy `LLMClient` only **lazily** through `adapters.legacy_compat.py`. The compat shim reads `PXFQUERY_LEGACY_PATH` or falls back to the T-024 workspace hard-coded path; if neither exists, it sets `LLMClient = None` and the adapter package still imports cleanly.
- This decoupling guarantees that the deterministic pipeline does not need either workspace to be installed.

## 6. Failure stops encountered

- **import shadowing** — `pyxfquery` (conda env name) and `pxfquery` substrings both appear in sys.path; the original purge was too aggressive. Fixed by restricting the purge to actual legacy workspaces, not conda prefixes.
- **IPv4 vs IPv6** — `urllib.request` failed with 502 once because `localhost` resolved to `::1` while the CyHex app listens on `127.0.0.1`. Switched the snapshot capture to `curl`/`subprocess` for transport stability.

Both were repaired in place; no upstream artifact was modified.

## 7. Downstream consumers

- **T-037 (deterministic pipeline task)** — can ignore this layer. `from pxfquery.query.forward import run_forward` and the reverse equivalent continue to work; only summarisation, if used, will see `[DeepSeekFlashAdapter unavailable: ...]` placeholders when the endpoint is down. That is the design.
- **Future tasks that want to opt into flash** — call `DeepSeekFlashAdapter(base_url=..., model=..., api_key=...)` explicitly and route the result through summarising wrappers.

## 8. Side effects for the CyHex state machine

- No `4_artifact/` in T-024 was touched.
- `1_project_init/`, `2_project_asset/1_raw_material/`, `3_project_state/` were not modified.
- No status change was made; T-034 remains `active` until CyHex records the acceptance gate.
