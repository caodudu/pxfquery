"""adapters package — optional DeepSeek v4 flash adapter for pxfquery (T-034).

This package exists so the T-034 deliverable does not have to be grafted onto
the legacy pxfquery tree to be importable. Each adapter is a self-contained
PXFQUERY-style client that:

- exposes the same public method names as ``pxfquery.llm.LLMClient``;
- never raises on connectivity, auth, or HTTP failure — instead returns a
  structured ``{"ok": False, ...}`` dict that downstream callers must treat as
  "adapter unavailable";
- works under the project's default conda environment without requiring a
  CyHex llm_gateway switch.
"""
