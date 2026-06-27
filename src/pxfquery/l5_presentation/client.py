from __future__ import annotations

from pxfquery.l5_presentation.version import __version__
from pxfquery.l3_execution.assets import AssetRegistry
from pxfquery.l3_execution.resources import ResourceManager
from pxfquery.l1_nlu import parse_query
from pxfquery.l5_presentation.model import PxFQueryAnswer
from pxfquery.l5_presentation.workflow import (
    GetNamespace,
    PreprocessingNamespace,
    ReadNamespace,
    ToolsNamespace,
    run_scanpy_style_pipeline,
)


class PxFQuery:
    """Main user-facing PxFquery client."""

    def __init__(self) -> None:
        self.assets: AssetRegistry | None = None
        self.resources = ResourceManager(self)
        self.read = ReadNamespace()
        self.pp = PreprocessingNamespace()
        self.tl = ToolsNamespace()
        self.get = GetNamespace()

    @property
    def version(self) -> str:
        return __version__

    def parse(self, text: str) -> dict:
        return parse_query(text).to_dict()

    def query(self, text: str) -> dict:
        qdata = run_scanpy_style_pipeline(self, text)
        result = self.get.result(qdata)
        if self.assets is not None:
            result["resource_pack"] = self.resources.status().to_dict()
        return result

    def ask(self, text: str) -> PxFQueryAnswer:
        qdata = run_scanpy_style_pipeline(self, text)
        return self.get.answer(qdata, resources_status=self.resources.status().to_dict())
