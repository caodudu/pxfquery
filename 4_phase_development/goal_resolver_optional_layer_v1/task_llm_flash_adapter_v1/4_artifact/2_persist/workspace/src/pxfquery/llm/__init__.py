"""pxfquery.llm — Optional DeepSeek v4 flash adapter layer (T-034 module).

This package is the *T-034-owned* re-export shim. It deliberately does NOT
inherit the legacy state-dependent ``__init__.py`` from T-024's workspace, so
this module is independently importable:

    >>> from pxfquery.llm import DeepSeekFlashAdapter
    >>> DeepSeekFlashAdapter()

If the full ``LLMClient`` (T-024) is on PYTHONPATH, ``LLMClient`` is still
re-exported lazily for backward compatibility, but it is never required to use
``DeepSeekFlashAdapter``. This keeps the deterministic pipeline runnable when
the DeepSeek endpoint is unavailable.
"""

from __future__ import annotations

from .adapters.deepseek_flash import (
    AdapterUnavailable,
    DeepSeekFlashAdapter,
    DEFAULT_BASE_URL,
    DEFAULT_MODEL,
)

# Lazy / optional re-export of the legacy LLMClient. Importing this module
# without the full pxfquery tree installed must still succeed.
try:  # pragma: no cover - optional import
    from .adapters.legacy_compat import LLMClient  # type: ignore
except Exception:  # pragma: no cover - no legacy package available
    LLMClient = None  # type: ignore

__all__ = [
    "DeepSeekFlashAdapter",
    "AdapterUnavailable",
    "DEFAULT_BASE_URL",
    "DEFAULT_MODEL",
    "LLMClient",
]
