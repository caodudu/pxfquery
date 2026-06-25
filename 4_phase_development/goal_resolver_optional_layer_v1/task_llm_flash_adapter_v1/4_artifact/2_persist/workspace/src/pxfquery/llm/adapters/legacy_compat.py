"""legacy_compat.py — Optional re-export shim for ``pxfquery.llm.LLMClient``.

T-024's ``LLMClient`` lives in a sibling ``pxfquery`` workspace and pulls in
``..logging_utils`` / ``..query.forward / .reverse`` at import time. T-034
must not modify that workspace, but should let downstream code write
``from pxfquery.llm import LLMClient`` without breaking when the legacy
package is unavailable (which is the common case during smoke tests and on
fresh installs).

This module is the *only* place T-034 mentions LLMClient. The lookup uses
``sys.path`` injection (no install required) and falls back to ``None`` when
the legacy workspace is not on disk.
"""

from __future__ import annotations

import os
import sys
from types import ModuleType
from typing import Any, Optional

__all__ = ["LLMClient"]


def _resolve_legacy_workspace() -> Optional[ModuleType]:
    """Best-effort import of ``pxfquery.llm`` from the T-024 workspace."""
    # Explicit override: ``PXFQUERY_LEGACY_PATH`` can point directly at the
    # T-024 ``src/`` directory.
    candidates = []
    env_path = os.environ.get("PXFQUERY_LEGACY_PATH")
    if env_path:
        candidates.append(env_path)
    candidates.append(
        "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
        "goal_package_foundation_v1/task_workspace_package_v1/4_artifact/"
        "2_persist/workspace/src"
    )
    for cand in candidates:
        if not cand or cand in sys.path:
            continue
        if not os.path.isdir(cand):
            continue
        sys.path.insert(0, cand)
        try:
            return __import__("pxfquery.llm", fromlist=["LLMClient"])
        except Exception:
            sys.path.pop(0, None)
            continue
    return None


_resolved = _resolve_legacy_workspace()

if _resolved is not None and hasattr(_resolved, "LLMClient"):
    LLMClient: Any = _resolved.LLMClient
else:  # pragma: no cover - legacy workspace not on disk
    LLMClient = None
