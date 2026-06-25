# pxfquery-T-034 — Optional DeepSeek v4 flash adapter

This package is the CyHex **T-034** optional adapter layer for
[PxFquery](https://github.com/) (P-012, `goal_resolver_optional_layer_v1`).
It exposes `DeepSeekFlashAdapter`, a thin OpenAI-compatible client that targets
`https://api.deepseek.com/v1` with `deepseek-v4-flash` by default and matches
the public surface of `pxfquery.llm.LLMClient`.

The adapter is **optional**: imports, smoke tests, and downstream projections
continue to succeed when the DeepSeek endpoint is unreachable or no API key is
configured. T-034 is not allowed to flip the active CyHex `llm_gateway`
default — it only registers DeepSeek v4 flash as an _additional_ provider that
downstream code can opt into by instantiating the adapter explicitly.

## Install

```bash
pip install pxfquery-T-034[llm-flash]
```

The base install already pulls in `openai>=1.40`. The `llm-flash` extra is a
documented opt-in marker; it does not currently add any new dependency.

## Use

```python
from pxfquery.llm import DeepSeekFlashAdapter

adapter = DeepSeekFlashAdapter()                # reads DEEPSEEK_API_KEY / OPENAI_API_KEY
probe = adapter.health_check()                  # never raises
if probe["ok"]:
    intent = adapter.parse_query("MCF7里敲掉EGFR会激活哪些通路")
```

If the endpoint is unreachable or the key is missing, `health_check()` returns
`{"ok": False, "reason": "...", "latency_ms": N}` and adapters downstream
treat that as graceful fallback.

## Deterministic pipeline

The optional layer does not change the deterministic forward/reverse flow.

```python
from pxfquery.query.forward import run_forward    # unaffected
from pxfquery.query.reverse import run_reverse    # unaffected
```

If `DeepSeekFlashAdapter` is unavailable, summarisation layers receive the
structured `unavailable` shape and the deterministic result stands on its own.

## Layout

| Path                                              | Purpose                                         |
|---------------------------------------------------|-------------------------------------------------|
| `src/pxfquery/llm/__init__.py`                    | Re-export shim (`DeepSeekFlashAdapter` + optional legacy `LLMClient`). |
| `src/pxfquery/llm/adapters/deepseek_flash.py`     | Adapter implementation.                         |
| `src/pxfquery/llm/adapters/legacy_compat.py`      | Optional, lazy re-export of the legacy `LLMClient`. |
| `pyproject.toml`                                  | Optional install metadata.                      |
| `../3_document/pxfquery_T-034_adapter_notes_v20260623.md` | Long-form adapter documentation.       |
| `../deepseek_flash_smoke_v20260623.json`          | Reproducible endpoint smoke record.             |

## Smoke record format

```jsonc
{
  "status": "ok" | "unavailable",
  "provider": "deepseek-flash",
  "model": "deepseek-v4-flash",
  "latency_ms": 1234,
  "ok": true | false,
  "reason": "<missing_api_key|endpoint_unreachable|client_build_failed|unexpected_reply|null>",
  "error_type": "<ExceptionName|null>",
  "error_message": "<str|null>",
  "reply": "<str|null>",
  "recorded_at": "2026-06-23T07:55:00"
}
```
