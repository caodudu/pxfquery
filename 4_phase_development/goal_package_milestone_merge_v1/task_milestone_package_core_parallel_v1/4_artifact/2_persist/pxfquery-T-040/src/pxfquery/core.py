"""
core.py — PxFquery main entry point.

Provides the PxFquery class that ties together data loading,
querying, LLM summarization, and visualization.
"""

from __future__ import annotations
import logging
from pathlib import Path
from typing import List, Optional

from .data.loader import DataLoader
from .logging_utils import LoggingSettings, configure_logger
from .query.forward import ForwardQuery, ForwardResult
from .query.reverse import ReverseQuery, ReverseResult
from .query.resolver import QueryResolver, ResolverConfig


class PxFquery:
    """
    PxFquery — Perturbation × Function Query Toolkit.

    Wraps data loading, forward/reverse query, LLM summarization,
    and visualization into a single convenient interface.

    Parameters
    ----------
    None

    Examples
    --------
    >>> pxf = PxFquery()

    # Load data (one or more perturbation types)
    >>> pxf.load_data("xpr", "/path/to/xpr_func_ad.h5ad")

    # Or load all from a directory
    >>> pxf.load_data_dir("/path/to/gsea_anndata/")

    # Optionally set up LLM
    >>> pxf.load_llm(api_key="sk-...", base_url="https://api.siliconflow.cn/v1",
    ...              model="Qwen/Qwen2.5-72B-Instruct")

    # Forward query
    >>> result = pxf.pert2func("EGFR", cell_line="A549")
    >>> pxf.plot(result)

    # Reverse query
    >>> result = pxf.func2pert(
    ...     activate=["HALLMARK_APOPTOSIS"],
    ...     suppress=["HALLMARK_MYC_TARGETS_V1"],
    ...     cell_line="MCF7",
    ... )
    >>> pxf.plot(result)

    # Natural language interface (requires LLM)
    >>> result = pxf.query("A549里敲掉EGFR会影响哪些通路")
    """

    def __init__(self):
        self._loader = DataLoader()
        self._forward_engines: dict = {}   # pert_type → ForwardQuery
        self._reverse_engines: dict = {}   # pert_type → ReverseQuery
        self._llm = None
        self._resolver: Optional[QueryResolver] = None
        self._logger = configure_logger(
            "pxfquery.core",
            LoggingSettings(verbosity="normal"),
        )

    # ------------------------------------------------------------------
    # Data loading
    # ------------------------------------------------------------------

    def load_data(self, pert_type: str, path: str) -> "PxFquery":
        """
        Load a single matrix from a local h5ad file.

        Parameters
        ----------
        pert_type : str
            One of 'xpr', 'sh', 'cp'.
        path : str
            Path to the .h5ad file.

        Returns
        -------
        self (for chaining)
        """
        self._loader.load_local(pert_type, path)
        adata = self._loader.get(pert_type)
        self._forward_engines[pert_type] = ForwardQuery(adata)
        self._reverse_engines[pert_type] = ReverseQuery(adata)
        return self

    def load_data_dir(self, directory: str) -> "PxFquery":
        """
        Load all matrices (xpr/sh/cp) from a directory.

        Expects files: xpr_func_ad.h5ad, sh_func_ad.h5ad, cp_func_ad.h5ad

        Parameters
        ----------
        directory : str

        Returns
        -------
        self (for chaining)
        """
        self._loader.load_all_local(directory)
        for pert_type in self._loader.list_loaded():
            adata = self._loader.get(pert_type)
            self._forward_engines[pert_type] = ForwardQuery(adata)
            self._reverse_engines[pert_type] = ReverseQuery(adata)
        return self

    # ------------------------------------------------------------------
    # LLM
    # ------------------------------------------------------------------

    def load_llm(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: str = "gpt-4o-mini",
        test: bool = True,
    ) -> "PxFquery":
        """
        Set up LLM client.

        Parameters
        ----------
        api_key : str, optional
            Falls back to OPENAI_API_KEY / SILICONFLOW_API_KEY env vars.
        base_url : str, optional
            API base URL for non-OpenAI providers.
        model : str
            Model name.
        test : bool
            Run health_check() immediately after setup.

        Returns
        -------
        self (for chaining)
        """
        from .llm.client import LLMClient
        self._llm = LLMClient(api_key=api_key, base_url=base_url, model=model)
        if test:
            self._llm.health_check()
        return self

    def enable_resolver(
        self,
        *,
        index_dir: str = "output/store/query_index",
        provider: str = "minimax",
        model: Optional[str] = None,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        default_top_n: int = 20,
        summary_include_numbers: bool = False,
        must_answer: bool = True,
        use_fast_path: bool = False,
        verbosity: str = "normal",
        log_level: Optional[str] = None,
        log_enabled: bool = True,
        log_to_file: bool = False,
        log_dir: str = "report/04_management/logs",
        log_file_prefix: str = "pxfquery",
        log_llm_io: Optional[bool] = None,
        log_human_readable: bool = False,
        prompt_hooks: Optional[dict] = None,
    ) -> "PxFquery":
        """
        Enable MVP resolver pipeline for natural-language queries.

        Parameters
        ----------
        index_dir : str
            Directory containing query index JSON files.
        provider : str
            'minimax' (default) or 'siliconflow'.
        model : str, optional
            Override model name. Provider-specific default is used if None.
        api_key : str, optional
            Explicit API key. Falls back to provider env vars.
        base_url : str, optional
            Explicit API base URL.
        default_top_n : int
            Default retrieval size for resolver pipeline.
        verbosity : str
            Log verbosity: 'quiet' | 'normal' | 'debug'.
        log_to_file : bool
            Whether to append logs to date-based file.
        log_dir : str
            Log directory when log_to_file=True.
        log_human_readable : bool
            Use simplified human-readable log format.
        """
        cfg = ResolverConfig(
            provider=provider,
            model=model,
            api_key=api_key,
            base_url=base_url,
            default_top_n=default_top_n,
            summary_include_numbers=summary_include_numbers,
            must_answer=must_answer,
            use_fast_path=use_fast_path,
            verbosity=verbosity,
            log_level=log_level,
            log_enabled=log_enabled,
            log_to_file=log_to_file,
            log_dir=log_dir,
            log_file_prefix=log_file_prefix,
            log_llm_io=log_llm_io,
            log_human_readable=log_human_readable,
        )
        self._resolver = QueryResolver(
            forward_engines=self._forward_engines,
            reverse_engines=self._reverse_engines,
            index_dir=index_dir,
            config=cfg,
            prompt_hooks=prompt_hooks,
        )
        return self

    # ------------------------------------------------------------------
    # Forward query
    # ------------------------------------------------------------------

    def pert2func(
        self,
        perturbation: str,
        pert_type: Optional[str] = None,
        cell_line: Optional[str] = None,
        top_n: int = 20,
        summarize: bool = False,
    ) -> ForwardResult:
        """
        Forward query: given a perturbation, retrieve functional changes.

        Parameters
        ----------
        perturbation : str
            Gene/drug name. Fuzzy matched.
        pert_type : str, optional
            One of 'xpr', 'sh', 'cp'. If None, uses the first loaded type.
        cell_line : str, optional
            Cell line filter. If None, aggregates across all cell lines.
        top_n : int
            Number of top terms to show.
        summarize : bool
            If True, generate LLM summary (requires load_llm() first).

        Returns
        -------
        ForwardResult
        """
        engine = self._get_forward_engine(pert_type)
        result = engine.query(perturbation, cell_line=cell_line, top_n=top_n)

        if summarize:
            if self._llm is None:
                self._logger.warning("LLM not loaded. Call load_llm() first.")
            else:
                result.summary = self._llm.summarize_forward(result)
                self._logger.info("LLM summary generated.")

        return result

    # ------------------------------------------------------------------
    # Reverse query
    # ------------------------------------------------------------------

    def func2pert(
        self,
        activate: Optional[List[str]] = None,
        suppress: Optional[List[str]] = None,
        pert_type: Optional[str] = None,
        cell_line: Optional[str] = None,
        top_k: int = 20,
        summarize: bool = False,
    ) -> ReverseResult:
        """
        Reverse query: given a functional target, recommend perturbations.

        Parameters
        ----------
        activate : list of str, optional
            Pathways to activate.
        suppress : list of str, optional
            Pathways to suppress.
        pert_type : str, optional
            One of 'xpr', 'sh', 'cp'. If None, uses the first loaded type.
        cell_line : str, optional
            Cell line filter.
        top_k : int
            Number of candidates to return.
        summarize : bool
            Generate LLM summary if True.

        Returns
        -------
        ReverseResult
        """
        engine = self._get_reverse_engine(pert_type)
        result = engine.query(
            activate=activate, suppress=suppress,
            cell_line=cell_line, top_k=top_k,
        )

        if summarize:
            if self._llm is None:
                self._logger.warning("LLM not loaded. Call load_llm() first.")
            else:
                result.summary = self._llm.summarize_reverse(result)
                self._logger.info("LLM summary generated.")

        return result

    # ------------------------------------------------------------------
    # Natural language interface
    # ------------------------------------------------------------------

    def query(
        self,
        user_input: str,
        pert_type: Optional[str] = None,
        top_n: int = 20,
    ):
        """
        Natural language query interface.

        Requires load_llm() to be called first.

        Parameters
        ----------
        user_input : str
            Free-form query, e.g. "A549里敲掉EGFR会影响哪些通路".
        pert_type : str, optional
        top_n : int

        Returns
        -------
        ForwardResult or ReverseResult
        """
        if self._resolver is not None:
            return self._resolver.resolve_and_query(
                user_input=user_input,
                pert_type=pert_type,
                top_n=top_n,
                summarize=True,
            )

        if self._llm is None:
            raise RuntimeError(
                "LLM not loaded. Call load_llm() first, or call enable_resolver()."
            )

        term_names = self._loader.term_names
        intent = self._llm.parse_query(user_input, available_terms=term_names)
        self._logger.info("Parsed intent: %s", intent)

        if intent.get("query_type") == "forward":
            return self.pert2func(
                perturbation=intent.get("perturbation", ""),
                pert_type=pert_type,
                cell_line=intent.get("cell_line"),
                top_n=intent.get("top_n") or top_n,
                summarize=True,
            )
        elif intent.get("query_type") == "reverse":
            return self.func2pert(
                activate=intent.get("activate", []),
                suppress=intent.get("suppress", []),
                pert_type=pert_type,
                cell_line=intent.get("cell_line"),
                top_k=intent.get("top_n") or top_n,
                summarize=True,
            )
        else:
            self._logger.warning("Could not determine query type. Please be more specific.")
            return None

    # ------------------------------------------------------------------
    # Visualization
    # ------------------------------------------------------------------

    def plot(
        self,
        result,
        kind: Optional[str] = None,
        backend: str = "plotly",
        top_n: int = 20,
        save: Optional[str] = None,
        **kwargs,
    ):
        """
        Plot a query result.

        Parameters
        ----------
        result : ForwardResult or ReverseResult
        kind : str, optional
            'bar', 'heatmap', or 'table'. Auto-detected from result type if None.
        backend : 'plotly' or 'matplotlib'
        top_n : int
        save : str, optional
            File path to save the figure (e.g. 'output/picture/fig1.png').

        Returns
        -------
        Figure
        """
        from .viz.plots import plot_forward_bar, plot_reverse_table

        if isinstance(result, ForwardResult):
            fig = plot_forward_bar(result, top_n=top_n, backend=backend, **kwargs)
        elif isinstance(result, ReverseResult):
            fig = plot_reverse_table(result, top_k=top_n, backend=backend, **kwargs)
        else:
            raise TypeError(f"Unknown result type: {type(result)}")

        if save:
            _save_figure(fig, save, backend)

        return fig

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    def list_loaded(self) -> List[str]:
        """Return list of loaded perturbation types."""
        return self._loader.list_loaded()

    def list_terms(self) -> List[str]:
        """Return all functional term names."""
        return self._loader.term_names

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _get_forward_engine(self, pert_type: Optional[str]) -> ForwardQuery:
        loaded = self._loader.list_loaded()
        if not loaded:
            raise RuntimeError("No data loaded. Call load_data() or load_data_dir() first.")
        pt = pert_type or loaded[0]
        if pt not in self._forward_engines:
            raise KeyError(f"'{pt}' not loaded. Available: {loaded}")
        return self._forward_engines[pt]

    def _get_reverse_engine(self, pert_type: Optional[str]) -> ReverseQuery:
        loaded = self._loader.list_loaded()
        if not loaded:
            raise RuntimeError("No data loaded. Call load_data() or load_data_dir() first.")
        pt = pert_type or loaded[0]
        if pt not in self._reverse_engines:
            raise KeyError(f"'{pt}' not loaded. Available: {loaded}")
        return self._reverse_engines[pt]


def _save_figure(fig, path: str, backend: str) -> None:
    """Save figure to disk."""
    from pathlib import Path
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    if backend == "plotly":
        if path.endswith(".html"):
            fig.write_html(path)
        else:
            fig.write_image(path)
    else:
        fig.savefig(path, dpi=300, bbox_inches="tight")
    logger = logging.getLogger("pxfquery.core")
    logger.info("Saved figure: %s", path)
