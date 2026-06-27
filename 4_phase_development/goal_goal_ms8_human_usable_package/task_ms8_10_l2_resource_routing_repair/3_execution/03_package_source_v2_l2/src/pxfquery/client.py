from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Optional

from pxfquery.l1_intent import ProviderRegistry, provider_from_env
from pxfquery.l3_execution.assets import AssetRegistry
from pxfquery.l3_execution.loader import DataLoader
from pxfquery.l3_execution.resources import ResourceManager
from pxfquery.l5_presentation.model import PxFQueryAnswer
from pxfquery.settings import SettingsNamespace
from pxfquery.version import __version__
from pxfquery.workflow import (
    GetNamespace,
    PreprocessingNamespace,
    ReadNamespace,
    ToolsNamespace,
    run_scanpy_style_pipeline,
)

if TYPE_CHECKING:
    from pxfquery.l2_routing.resolver import QueryResolver
    from pxfquery.l3_execution.forward import ForwardQuery
    from pxfquery.l3_execution.reverse import ReverseQuery


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
        self._loader = DataLoader()
        self._forward_engines: dict[str, "ForwardQuery"] = {}
        self._reverse_engines: dict[str, "ReverseQuery"] = {}
        self._resolver: "QueryResolver | None" = None
        self._index_dir: Path | None = None
        self.resources = ResourceManager(self)
        self.settings = SettingsNamespace(self)
        self.read = ReadNamespace()
        self.pp = PreprocessingNamespace(self)
        self.tl = ToolsNamespace(self)
        self.get = GetNamespace()

    @property
    def version(self) -> str:
        return __version__

    def load_data(self, pert_type: str, path: str | Path) -> "PxFQuery":
        from pxfquery.l3_execution.forward import ForwardQuery
        from pxfquery.l3_execution.reverse import ReverseQuery

        self._loader.load_local(pert_type, path)
        adata = self._loader.get(pert_type)
        self._forward_engines[pert_type] = ForwardQuery(adata)
        self._reverse_engines[pert_type] = ReverseQuery(adata)
        return self

    def load_data_dir(self, directory: str | Path) -> "PxFQuery":
        from pxfquery.l3_execution.forward import ForwardQuery
        from pxfquery.l3_execution.reverse import ReverseQuery

        self._loader.load_all_local(directory)
        for pert_type in self._loader.list_loaded():
            adata = self._loader.get(pert_type)
            self._forward_engines[pert_type] = ForwardQuery(adata)
            self._reverse_engines[pert_type] = ReverseQuery(adata)
        return self

    def enable_resolver(
        self,
        *,
        index_dir: str | Path,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
        default_top_n: int = 20,
        summarize: bool = False,
    ) -> "PxFQuery":
        from pxfquery.l2_routing.resolver import QueryResolver, ResolverConfig

        del summarize
        config = ResolverConfig(
            api_key=api_key,
            base_url=base_url,
            model=model,
            default_top_n=default_top_n,
            must_answer=False,
        )
        self._resolver = QueryResolver(
            forward_engines=self._forward_engines,
            reverse_engines=self._reverse_engines,
            index_dir=index_dir,
            config=config,
        )
        self._index_dir = Path(index_dir).expanduser().resolve()
        return self

    def pert2func(
        self,
        perturbation: str,
        *,
        pert_type: str | None = None,
        cell_line: str | None = None,
        top_n: int = 20,
    ):
        engine = self._get_forward_engine(pert_type)
        return engine.query(perturbation, cell_line=cell_line, top_n=top_n)

    def func2pert(
        self,
        *,
        activate: list[str] | None = None,
        suppress: list[str] | None = None,
        pert_type: str | None = None,
        cell_line: str | None = None,
        top_k: int = 20,
    ):
        engine = self._get_reverse_engine(pert_type)
        return engine.query(activate=activate, suppress=suppress, cell_line=cell_line, top_k=top_k)

    def query(self, text: str) -> dict:
        qdata = run_scanpy_style_pipeline(self, text)
        result = self.get.result(qdata)
        if self.assets is not None:
            result["resource_pack"] = self.resources.status().to_dict()
        return result

    def ask(self, text: str) -> PxFQueryAnswer:
        qdata = run_scanpy_style_pipeline(self, text)
        return self.get.answer(qdata, resources_status=self.resources.status().to_dict())

    def plot(self, result, *, kind: str | None = None, backend: str = "plotly", top_n: int = 20, save: str | None = None):
        from pxfquery.l5_presentation.plots import plot_forward_bar, plot_reverse_table
        from pxfquery.l3_execution.forward import ForwardResult
        from pxfquery.l3_execution.reverse import ReverseResult

        if isinstance(result, ForwardResult):
            fig = plot_forward_bar(result, top_n=top_n, backend=backend)
        elif isinstance(result, ReverseResult):
            fig = plot_reverse_table(result, top_k=top_n, backend=backend)
        else:
            raise TypeError(f"Unknown result type: {type(result)}")
        if save:
            _save_figure(fig, save, backend)
        return fig

    def list_loaded(self) -> list[str]:
        return self._loader.list_loaded()

    def list_terms(self) -> list[str]:
        return self._loader.term_names

    def _get_forward_engine(self, pert_type: Optional[str]) -> ForwardQuery:
        loaded = self._loader.list_loaded()
        if not loaded:
            raise RuntimeError("No data loaded. Call load_data() or load_data_dir() first.")
        pt = pert_type or loaded[0]
        if pt not in self._forward_engines:
            raise KeyError(f"{pt!r} is not loaded. Available: {loaded}")
        return self._forward_engines[pt]

    def _get_reverse_engine(self, pert_type: Optional[str]) -> ReverseQuery:
        loaded = self._loader.list_loaded()
        if not loaded:
            raise RuntimeError("No data loaded. Call load_data() or load_data_dir() first.")
        pt = pert_type or loaded[0]
        if pt not in self._reverse_engines:
            raise KeyError(f"{pt!r} is not loaded. Available: {loaded}")
        return self._reverse_engines[pt]


def _save_figure(fig, path: str, backend: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if backend == "plotly":
        if path.endswith(".html"):
            fig.write_html(path)
        else:
            fig.write_image(path)
    else:
        fig.savefig(path, dpi=300, bbox_inches="tight")
