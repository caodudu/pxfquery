from __future__ import annotations

from pxfquery._version import __version__
from pxfquery.execution.assets import AssetRegistry
from pxfquery.execution.resources import ResourceManager
from pxfquery.evidence.pipeline import run_query_pipeline
from pxfquery.nlu import parse_query
from pxfquery.presentation import build_answer
from pxfquery.presentation.model import PxFQueryAnswer


class PxFQuery:
    """Main user-facing PxFquery client."""

    def __init__(self) -> None:
        self.assets: AssetRegistry | None = None
        self.resources = ResourceManager(self)

    @property
    def version(self) -> str:
        return __version__

    def parse(self, text: str) -> dict:
        return parse_query(text).to_dict()

    def query(self, text: str) -> dict:
        result = run_query_pipeline(text)
        if self.assets is not None:
            result["resource_pack"] = self.resources.status().to_dict()
        return result

    def ask(self, text: str) -> PxFQueryAnswer:
        structured = self.query(text)
        return build_answer(text, structured, resources_status=self.resources.status().to_dict())
