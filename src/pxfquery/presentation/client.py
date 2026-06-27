from __future__ import annotations

from pathlib import Path

from pxfquery._version import __version__
from pxfquery.execution.assets import AssetRegistry
from pxfquery.execution.resources import ResourceManager
from pxfquery.presentation import build_answer
from pxfquery.presentation.model import PxFQueryAnswer
from pxfquery.presentation.workflow import (
    GetNamespace,
    PreprocessingNamespace,
    ReadNamespace,
    SettingsNamespace,
    ToolsNamespace,
    one_shot_parse,
    one_shot_query,
)


class PxFQuery:
    """Main user-facing PxFquery client."""

    def __init__(self) -> None:
        self.assets: AssetRegistry | None = None
        self.resources = ResourceManager(self)
        self.settings = SettingsNamespace(self)
        self.read = ReadNamespace(self)
        self.pp = PreprocessingNamespace(self)
        self.tl = ToolsNamespace(self)
        self.get = GetNamespace(self)

    @property
    def version(self) -> str:
        return __version__

    def parse(self, text: str) -> dict:
        return one_shot_parse(self, text)

    def query(self, text: str) -> dict:
        return one_shot_query(self, text)

    def ask(self, text: str) -> PxFQueryAnswer:
        structured = self.query(text)
        return build_answer(text, structured, resources_status=self.resources.status().to_dict())

    def register_assets(
        self,
        *,
        root: str | Path | None = None,
        manifest: str | Path | dict | None = None,
        strict: bool = True,
    ) -> AssetRegistry:
        return self.settings.register_assets(root=root, manifest=manifest, strict=strict)
