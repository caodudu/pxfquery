from __future__ import annotations

from pathlib import Path

from pxfquery.l1_intent import ProviderRegistry, provider_from_env
from pxfquery.l3_execution.assets import AssetRegistry
from pxfquery.resources import ResourceManager
from pxfquery.settings import SettingsNamespace
from pxfquery.version import __version__
from pxfquery.workflow import (
    GetNamespace,
    PreprocessingNamespace,
    ReadNamespace,
    ToolsNamespace,
)


class PxFQuery:
    """Main user-facing PxFquery client."""

    def __init__(self, *, llm_provider=None) -> None:
        self.assets: AssetRegistry | None = None
        self.llm_providers = ProviderRegistry()
        initial_provider = llm_provider if llm_provider is not None else provider_from_env(required=False)
        if initial_provider is not None:
            if hasattr(initial_provider, "config"):
                self.llm_providers.register(initial_provider.config, default=True)
            else:
                self.llm_providers.register_provider("injected", initial_provider, default=True)
        self._index_dir: Path | None = None
        self.forward_proxy_direction_calibration = {
            "enabled": True,
            "genetic": True,
            "drug": False,
            "min_common_cells": 3,
            "flip_threshold": -0.10,
            "keep_threshold": 0.10,
            "uncertain_proxy_weight": 0.35,
        }
        self.resources = ResourceManager(self)
        self.settings = SettingsNamespace(self)
        self.read = ReadNamespace()
        self.pp = PreprocessingNamespace(self)
        self.tl = ToolsNamespace(self)
        self.get = GetNamespace()

    @property
    def version(self) -> str:
        return __version__

    def query(self, text: str) -> dict:
        qdata = self.tl.parse(text)
        return {
            "schema_version": "pxfquery-l4-query/v1",
            "intent": self.get.intent(qdata),
            "route_plan": self.get.route(qdata),
            "execution": self.get.execution(qdata),
            "evidence_dossier": self.get.evidence(qdata),
            "resource_pack": self.resources.status().to_dict(),
        }

    def ask(self, text: str, *, mode: str = "python"):
        qdata = self.tl.parse(text)
        self.tl.answer(qdata, mode=mode)
        return self.get.answer(qdata)
