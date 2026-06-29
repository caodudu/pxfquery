from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, TimeoutError
from time import perf_counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import pickle

from pxfquery.l3_execution import execute_route_plan
from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l4_evidence.annotation import default_annotation_providers
from pxfquery.l1_intent import parse_intent
from pxfquery.l2_routing import route_intent
from pxfquery.l5_presentation.answer import build_answer
from pxfquery.l5_presentation.chat import build_chat_response
from pxfquery.l5_presentation.figures import write_figure_files
from pxfquery.utils.events import EventLog, PxFQueryEvent
from pxfquery.version import __version__


QDATA_PICKLE_SCHEMA = "pxfquery-qdata-pickle/v1"


@dataclass
class PxFQueryData:
    """Mutable query object used by the scanpy-style user interface."""

    text: str
    obs: dict[str, Any] = field(default_factory=dict)
    uns: dict[str, Any] = field(default_factory=dict)

    def save(self, path: str | Path) -> Path:
        """Serialize this query object to a local pickle file."""
        return save_qdata(self, path)

    @classmethod
    def load(cls, path: str | Path) -> "PxFQueryData":
        """Restore a query object from a local pickle file."""
        return load_qdata(path)


def save_qdata(qdata: PxFQueryData, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": QDATA_PICKLE_SCHEMA,
        "pxfquery_version": __version__,
        "qdata": qdata,
    }
    with target.open("wb") as handle:
        pickle.dump(payload, handle, protocol=pickle.HIGHEST_PROTOCOL)
    qdata.uns["pickle_path"] = str(target)
    return target


def load_qdata(path: str | Path) -> PxFQueryData:
    source = Path(path)
    with source.open("rb") as handle:
        payload = pickle.load(handle)
    if isinstance(payload, PxFQueryData):
        qdata = payload
    elif isinstance(payload, dict) and payload.get("schema_version") == QDATA_PICKLE_SCHEMA and isinstance(payload.get("qdata"), PxFQueryData):
        qdata = payload["qdata"]
    else:
        raise ValueError("pickle file does not contain a PxFquery query object")
    qdata.uns["pickle_path"] = str(source)
    return qdata


class ReadNamespace:
    def query(self, text: str) -> PxFQueryData:
        return PxFQueryData(text=text.strip())

    def save(self, qdata: PxFQueryData, path: str | Path) -> Path:
        return save_qdata(qdata, path)

    def load(self, path: str | Path) -> PxFQueryData:
        return load_qdata(path)


class PreprocessingNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def parse(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = parse_intent(target.text, provider=self._client.llm_providers.get())
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent"] = intent
        return target if copy else None

    def route(self, qdata: PxFQueryData, *, copy: bool = False, auto_download: bool = True) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = _require_intent(target)
        if auto_download:
            self._client.resources.ensure("l2_core_indexes", auto_download=True)
            self._client.resources.ensure("l2_proxy_neighbors", auto_download=True)
            if self._client.resources.manifest():
                self._client.resources.ensure("l3_functional_scores", kinds=("obs",), auto_download=True)
        route_plan = route_intent(
            intent,
            assets=self._client.assets,
            index_dir=self._client._index_dir,
            llm_provider=self._client.llm_providers.get(),
        )
        target.uns["route_plan"] = route_plan.to_dict()
        target.uns["_route_plan"] = route_plan
        target.uns["route_status"] = route_plan.route_status
        return target if copy else None


class ToolsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def parse(
        self,
        text: str,
        *,
        synthesize: bool = True,
        literature_provider: Any | None = None,
        auto_download: bool = True,
        top_n: int = 20,
        debug: bool = False,
        annotate: bool = False,
        annotation_sources: list[str] | tuple[str, ...] = ("chembl",),
        annotation_timeout: float = 5.0,
        progress: bool | EventLog = True,
        copy: bool = False,
    ) -> PxFQueryData:
        qdata = self._client.read.query(text)
        events = progress if isinstance(progress, EventLog) else EventLog(enabled=bool(progress), style="text")
        qdata.uns["progress_events"] = events.to_list()
        try:
            stage_start = perf_counter()
            events.stage("parse", "parse_start", "start")
            self._client.pp.parse(qdata)
            intent = qdata.uns.get("intent", {})
            events.stage(
                "parse",
                "parse_done",
                "done",
                mode=intent.get("query_type"),
                context=intent.get("bio_context"),
                perturbation=intent.get("pert_desc"),
                function=intent.get("function_desc"),
                time=_elapsed(stage_start),
            )

            stage_start = perf_counter()
            events.stage("match", "match_start", "start")
            self._client.pp.route(qdata, auto_download=auto_download)
            selected = ((qdata.uns.get("route_plan") or {}).get("combination_route") or {}).get("selected_routes") or []
            events.stage("match", "match_done", "done", matches=len(selected), time=_elapsed(stage_start))

            stage_start = perf_counter()
            events.stage("matrix", "matrix_start", "start")
            self.execute(qdata, auto_download=auto_download, top_n=top_n)
            execution = qdata.uns.get("execution") or {}
            events.stage(
                "matrix",
                "matrix_done",
                "done",
                profiles=len(execution.get("executed_routes") or []),
                skipped=len(execution.get("skipped_routes") or []),
                time=_elapsed(stage_start),
            )

            stage_start = perf_counter()
            events.stage("evidence", "evidence_start", "start")
            self.assemble(qdata, synthesize=synthesize, literature_provider=literature_provider, debug=debug)
            dossier = qdata.uns.get("evidence_dossier") or {}
            events.stage("evidence", "evidence_done", "done", status=_public_status(dossier.get("dossier_status")), time=_elapsed(stage_start))

            if annotate:
                stage_start = perf_counter()
                if _should_auto_annotate(qdata):
                    events.stage("annotation", "annotation_start", "start", sources=",".join(annotation_sources), timeout=annotation_timeout)
                    self.anno(qdata, sources=annotation_sources, timeout=annotation_timeout)
                    annotation = qdata.uns.get("annotation_evidence") or {}
                    events.stage(
                        "annotation",
                        "annotation_done",
                        "done",
                        status=annotation.get("status"),
                        records=sum(len(block.get("records") or []) for block in annotation.get("records") or []),
                        diagnostics=len(annotation.get("diagnostics") or []),
                        time=_elapsed(stage_start),
                    )
                else:
                    events.stage("annotation", "annotation_skipped", "skipped", reason="drug_aliases_available_or_no_compound_routes", time=_elapsed(stage_start))
        except Exception as exc:
            events.error("pipeline", "failed", "failed", error=f"{type(exc).__name__}: {exc}")
            qdata.uns["progress_events"] = events.to_list()
            raise
        qdata.uns["progress_events"] = events.to_list()
        return _copy_qdata(qdata) if copy else qdata

    def execute(
        self,
        qdata: PxFQueryData,
        *,
        copy: bool = False,
        resource_dir: str | None = None,
        auto_download: bool = True,
        top_n: int = 20,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        route_plan = _require_route_plan(target)
        execution = execute_route_plan(
            route_plan,
            resources=self._client.resources,
            resource_dir=resource_dir,
            auto_download=auto_download,
            top_n=top_n,
        )
        target.uns["execution"] = execution.to_dict()
        target.uns["_execution"] = execution
        return target if copy else None

    def assemble(
        self,
        qdata: PxFQueryData,
        *,
        copy: bool = False,
        synthesize: bool = True,
        literature_provider: Any | None = None,
        debug: bool = False,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        execution = _require_execution(target)
        result = assemble_evidence(
            execution,
            intent=target.uns.get("intent"),
            route_plan=target.uns.get("route_plan"),
            llm_provider=self._client.llm_providers.get(),
            synthesize=synthesize,
            literature_provider=literature_provider,
            debug=debug,
        )
        target.uns["evidence_dossier"] = result
        target.uns["result"] = result
        return target if copy else None

    def anno(
        self,
        qdata: PxFQueryData,
        *,
        providers: list[Any] | tuple[Any, ...] | None = None,
        sources: list[str] | tuple[str, ...] | None = None,
        timeout: float = 5.0,
        copy: bool = False,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        dossier = _require_evidence(target)
        active_providers = list(providers) if providers is not None else default_annotation_providers(sources, timeout=timeout)
        records: list[dict[str, Any]] = []
        diagnostics: list[dict[str, Any]] = []
        for provider in active_providers:
            name = getattr(provider, "name", provider.__class__.__name__)
            if not hasattr(provider, "annotate"):
                diagnostics.append({"provider": name, "status": "unavailable", "reason": "provider does not expose annotate(...)"})
                continue
            provider_start = perf_counter()
            try:
                payload = _run_provider_with_timeout(provider, query=target.text, evidence_dossier=dossier, timeout=timeout)
            except TimeoutError:
                diagnostics.append({"provider": name, "status": "timed_out", "reason": f"annotation exceeded {timeout:.1f}s"})
                continue
            except Exception as exc:
                diagnostics.append({"provider": name, "status": "failed", "reason": f"{type(exc).__name__}: {exc}"})
                continue
            elapsed = perf_counter() - provider_start
            if elapsed > timeout:
                diagnostics.append({"provider": name, "status": "timed_out", "reason": f"annotation exceeded {timeout:.1f}s", "elapsed": round(elapsed, 3)})
                continue
            records.append({"provider": name, "status": "completed", "elapsed": round(elapsed, 3), "records": _json_safe_list(payload)})
        status = "completed" if records else "unavailable"
        annotation = {"status": status, "records": records, "diagnostics": diagnostics}
        dossier.setdefault("evidence_layer", {})["annotation_evidence"] = annotation
        target.uns["evidence_dossier"] = dossier
        target.uns["result"] = dossier
        target.uns["annotation_evidence"] = annotation
        return target if copy else None

    def answer(
        self,
        qdata: PxFQueryData,
        *,
        mode: str = "python",
        output: str | Path | None = None,
        progress: bool | EventLog = False,
        copy: bool = False,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        dossier = _require_evidence(target)
        events = progress if isinstance(progress, EventLog) else EventLog(enabled=bool(progress), style="text")
        existing = target.uns.get("progress_events") or []
        for item in existing:
            event = _event_from_dict(item)
            if event is not None:
                events.events.append(event)
        stage_start = perf_counter()
        events.stage("answer", "answer_start", "start", mode=mode)
        answer = build_answer(target.text, dossier, mode=mode)
        if mode == "html" and output is not None:
            path = Path(output)
            path.write_text(answer.html or "", encoding="utf-8")
            target.uns["answer_output"] = str(path)
        target.uns["_answer"] = answer
        target.uns["answer"] = answer.to_dict()
        events.stage("answer", "answer_done", "done", mode=mode, time=_elapsed(stage_start))
        target.uns["progress_events"] = events.to_list()
        return target if copy else None

    def chat(
        self,
        qdata: PxFQueryData,
        message: str,
        *,
        copy: bool = False,
        llm_provider: Any | None = None,
        print_response: bool = True,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        dossier = _require_evidence(target)
        answer = target.uns.get("_answer")
        if answer is None:
            answer = build_answer(target.text, dossier, mode="python")
            target.uns["_answer"] = answer
            target.uns["answer"] = answer.to_dict()
        provider = llm_provider if llm_provider is not None else self._client.llm_providers.get()
        history = target.uns.setdefault("chat", [])
        turn = build_chat_response(
            target.text,
            dossier,
            message,
            answer=answer,
            history=history,
            llm_provider=provider,
        )
        history.append(turn)
        target.uns["last_chat"] = turn
        if print_response:
            print(turn["assistant"])
        return target if copy else None

    def figures(
        self,
        qdata: PxFQueryData,
        *,
        output_dir: str | Path,
        prefix: str = "pxfquery",
        format: str = "pdf",
        copy: bool = False,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        answer = target.uns.get("_answer")
        if answer is None:
            dossier = _require_evidence(target)
            answer = build_answer(target.text, dossier, mode="python")
            target.uns["_answer"] = answer
            target.uns["answer"] = answer.to_dict()
        paths = write_figure_files(answer.figures, output_dir, prefix=prefix, fmt=format)
        target.uns["figure_outputs"] = paths
        return target if copy else None

    def save(self, qdata: PxFQueryData, path: str | Path) -> Path:
        return save_qdata(qdata, path)

    def load(self, path: str | Path) -> PxFQueryData:
        return load_qdata(path)


class GetNamespace:
    def intent(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["intent"]

    def route(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["route_plan"]

    def result(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["result"]

    def evidence(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["evidence_dossier"]

    def execution(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["execution"]

    def answer(self, qdata: PxFQueryData):
        if "_answer" not in qdata.uns:
            raise RuntimeError("qdata has no L5 answer; call pxf.tl.answer(qdata) before pxf.get.answer(qdata)")
        return qdata.uns["_answer"]

    def chat(self, qdata: PxFQueryData) -> str:
        if "last_chat" not in qdata.uns:
            raise RuntimeError("qdata has no L5 chat turn; call pxf.tl.chat(qdata, message) before pxf.get.chat(qdata)")
        return qdata.uns["last_chat"]["assistant"]

    def chat_history(self, qdata: PxFQueryData) -> list[dict[str, Any]]:
        return qdata.uns.get("chat", [])


def run_scanpy_style_pipeline(client, text: str) -> PxFQueryData:
    return client.tl.parse(text)


def _copy_qdata(qdata: PxFQueryData) -> PxFQueryData:
    return PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns))


def _should_auto_annotate(qdata: PxFQueryData, *, limit: int = 5) -> bool:
    dossier = qdata.uns.get("evidence_dossier") or {}
    matrix = ((dossier.get("evidence_layer") or {}).get("matrix_evidence") or {})
    routes = [route for route in matrix.get("executed_routes") or [] if route.get("modality") == "cp"]
    if not routes:
        return False
    top = routes[:limit]
    return all(not route.get("perturbation_alias") for route in top)


def _run_provider_with_timeout(provider: Any, *, query: str, evidence_dossier: dict[str, Any], timeout: float) -> Any:
    executor = ThreadPoolExecutor(max_workers=1)
    future = executor.submit(provider.annotate, query=query, evidence_dossier=evidence_dossier)
    try:
        return future.result(timeout=timeout)
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


def _require_intent(qdata: PxFQueryData):
    if "_intent" not in qdata.uns:
        raise RuntimeError("qdata has no l1_intent result; call pxf.pp.parse(qdata) before downstream tools")
    return qdata.uns["_intent"]


def _require_route_plan(qdata: PxFQueryData):
    if "_route_plan" not in qdata.uns:
        raise RuntimeError("qdata has no l2 routing result; call pxf.pp.route(qdata) before downstream tools")
    return qdata.uns["_route_plan"]


def _require_execution(qdata: PxFQueryData):
    if "_execution" not in qdata.uns:
        raise RuntimeError("qdata has no execution result; call pxf.tl.execute(qdata) before assembly")
    return qdata.uns["_execution"]


def _require_evidence(qdata: PxFQueryData) -> dict[str, Any]:
    if "evidence_dossier" not in qdata.uns:
        raise RuntimeError("qdata has no L4 evidence dossier; call pxf.tl.assemble(qdata) before annotation")
    return qdata.uns["evidence_dossier"]


def _json_safe_list(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe_list(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe_list(item) for item in value]
    if isinstance(value, tuple):
        return [_json_safe_list(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    return str(value)


def _event_from_dict(value: Any) -> PxFQueryEvent | None:
    if not isinstance(value, dict):
        return None
    try:
        return PxFQueryEvent(
            timestamp=str(value.get("timestamp") or ""),
            layer=str(value.get("layer") or ""),
            stage=str(value.get("stage") or ""),
            level=str(value.get("level") or "stage"),
            message=str(value.get("message") or ""),
            details=value.get("details") if isinstance(value.get("details"), dict) else {},
        )
    except Exception:
        return None


def _public_status(value: Any) -> str:
    text = str(value or "")
    if text in {"evidence_found", "partial_evidence"}:
        return "ready"
    if text in {"unresolved_route", "no_executable_route", "no_matrix_hit"}:
        return "no_match"
    if text in {"resource_unavailable", "invalid_upstream_schema"}:
        return "blocked"
    return text or "unknown"


def _elapsed(start: float) -> str:
    return f"{perf_counter() - start:.2f}s"
