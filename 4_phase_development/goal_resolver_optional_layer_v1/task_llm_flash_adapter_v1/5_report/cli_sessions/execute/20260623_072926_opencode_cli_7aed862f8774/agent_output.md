I see this is now the **execution stage** prompt. I need to actually execute the task body: build the DeepSeek v4 flash adapter, run sm
Step 1: Record llm_gateway snapshot
Some sockets block urllib's default User-Agent; let me retry with a proper request to confirm:
curl works fine. The 502 from urllib was likely IPv6 lookup glitch. Let me write the snapshot using curl-parsed JSON:
Step 2: Read T-024 workspace LLM module to capture the interface contract.
I notice **client.py** uses the `openai` library (not litellm as the docstring says) and depends on `..logging_utils` and `..query.forward/.reverse`. I need to verify those exist (they're sibling packages) and whether `openai` is actually installed in the `pxfquery` env.
The `pxfquery` conda env has `openai` 2.30.0 and the T-024 workspace `LLMClient` imports successfully. Now I understand the design clearly:

- `LLMClient` uses `openai.OpenAI()` with `api_key` and `base_url` — not `litellm`. 
- The adapter should replicate this pattern (not litellm), use the same constructor signature, and return the graceful `AdapterUnavailable` dict.

Let me now create the adapter workspace structure:
Wait — I copy/pasted T-024's `prompts.py` into the T-034 workspace. Per the protocol, the T-034 workspace is NEW (a corrected downstream version). But it depends on imports `from .client import LLMClient` which need `..logging_utils` and `..query.forward/.reverse`. The cleanest approach for the **adapter** is to make `DeepSeekFlashAdapter` a standalone composition over the OpenAI SDK with graceful fallback — it must NOT depend on the legacy `LLMClient`'s sibling-package import chain at import-time.

Let me actually NOT copy `prompts.py` (it's a separate concern). The T-034 mission is the **adapter layer** — it must be importable without the legacy pxfquery package. I'll remove `prompts.py` and design the adapter so it does not import the heavy `LLMClient` at construction time:
Now design decision: T-034's adapter workspace must be **importable independently** (without the legacy sibling-package chain). The cleanest is to ship the adapter as a standalone package that:

1. Re-exports `LLMClient` only via a lazy optional import (so `from pxfquery.llm import LLMClient` keeps working when the full legacy workspace is installed, but the adapter workspace itself doesn't need it for its own smoke).
2. `DeepSeekFlashAdapter` is fully self-contained — just `openai.OpenAI(...)` with `base_url` pointed at DeepSeek, latency logging, structured adapter-unavailable dict on failure.

This matches the protocol's "the adapter must be **optional**: import, smoke, and report paths must still succeed when the endpoint is unreachable" requirement.
I just referenced `.adapters.legacy_compat` for the optional LLMClient re-export. Let me create that module so the import works correctly and the optional fallback unit-test for the smoke is meaningful:
Now write `pyproject.toml` amendment and
Now write the smoke script:
Now run smoke checks in proper order: (a) import, (b) py_compile, (c) endpoint smoke.
The `py_compile` passes for all 4 files. The import failure is because the T-024 workspace is on PYTHONPATH first and shadows the T-034 workspace. I need the T-034 workspace *first*. Also, the T-024 workspace's own `llm/__init__.py` only contains `from .client import LLMClient`, so the T-034 workspace must take priority. Let me fix:
Good — `DeepSeekFlashAdapter` is importable from the T-034 workspace and the file resolves to T-034's source. Now run the endpoint smoke check via the script:
TCP probe to api.deepseek.com:443 succeeded (574 ms). The script's `from pxfquery.llm import DeepSeekFlashAdapter` failed because `3_execution/` is on sys.path and the conda env also imports T-024's `pxfquery`. I need to fix the script to clean sys.path before importing:
Also need to handle the `p` reference correctly in
A strange Python 3.10 stdlib issue with `locale`/`gettext` — that suggests the `_purge_existing_pxfquery()` accidentally broke stdlib sys.path.
This stdlib issue happens when too much of **sys.path** is purged. The current path includes conda's `lib/python3.10.zip` or other stdlib paths. Let me limit the purge more surgically — only drop the specific legacy paths, not all `pxfquery`-containing entries:
The T-024 workspace is already on sys.path (because PYTHONPATH was set earlier). Wait — the test only had `export PYTHONPATH` in the previous test session, not this one. Let me dig in:
There's a `__editable__.pxfquery_t_024-0.1.0.pth` pointing to T-024's workspace. That means T-024 is installed as `pip install -e .` in the conda env. So the deep `purge()` was right, but it removed too much (the stdlib `site-packages` contains `pxfquery-0.1.0` editable, which the regex matched — and the package `gettext` is also from `site-packages` — wait no, gettext is stdlib).

The real issue is that `idx = "pxfquery" not in str(p).lower()` removes any path that mentions "pxfquery" — including `site-packages` (which doesn't mention pxfquery, so safe) — but it then ALSO seems to cause `locale` to fail. The `locale` failure is from gettext trying `_expand_lang` which calls `import locale` — and `locale` is a C-extension that's been **side-effected** by removing some path. Actually, the real culprit is that I purged too late, after the import system already kicked off `argparse` which uses `gettext` which transitively tries to import `locale` — but the fact that `locale` fails means locale.so isn't on the path.

Let me look more carefully. The `sys.path` shown above does include:
- `python310.zip`
- `python3.10/lib`
- `python3.10/lib-dynload`
- `python3.10/site-packages` ← but this is NOT in the printed list!

So actually 3 of the standard prefix paths are missing — when env var is unset, normally Python adds its prefix but here they're missing because the conda activation added them via `os.pathsep` in `site.py`. My purge must've removed them.

Actually re-reading: the cure is `sys.path[:] = [p for p in sys.path if "pxfquery" not in str(p).lower()]`. None of the standard paths contain "pxfquery" so they shouldn't be touched … unless the regex matches something I'm missing. Let me inspect more carefully:
Found the bug! The conda env is installed at **`/Users/dudu/Softwares/miniconda/envs/pxfquery/`** — the literal path contains "pxfquery"! My regex was too aggressive and removed all conda env paths. I need a smarter filter — only drop paths pointing to T-024 or other pxfquery workspaces:
Excellent. Status=`unavailable`, reason=`missing_api_key`. This is a valid graceful-fallback outcome — the script imported DeepSeek, the TCP probe may have succeeded, and the adapter returns `missing_api_key` since no DEEPSEEK_API_KEY is set.
This is a valid smoke outcome:
- **TCP probe**: succeeded (`tcp_ok: true`, `api.deepseek.com:443`, 365 ms).
- **Adapter call**: returned `ok: false, reason: missing_api_key` because no real DeepSeek API key is configured in this environment, which is exactly the graceful-fallback path the protocol asks for.
- **No exception raised** — the adapter degrades properly.

Now let me also run a `--no-traffic` smoke (pure TCP probe) and a positive control to demonstrate the structure works when a fake key is present:
The test suite confirms all three scenarios are handled correctly. Smoke check step is complete. Now I move on
Now check the smoke records were recorded under 4_artifact/, then write the two HTML reports:
