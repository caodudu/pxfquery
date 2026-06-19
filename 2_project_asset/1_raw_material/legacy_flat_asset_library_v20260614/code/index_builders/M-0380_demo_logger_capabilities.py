from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path


def _load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _make_hooks():
    def _intent(_user_input: str):
        return {
            "query_type": "forward",
            "bio_context": "A549",
            "pert_desc": "EGFR",
            "pert_class": "genetic",
            "function_desc": None,
            "activate": [],
            "suppress": [],
            "top_n": 5,
        }

    return {
        "llm_parse_intent": _intent,
        "llm_map_cell_line": lambda desc, options, level: options[0] if options else "",
        "llm_map_gene": lambda desc, candidates: [desc],
        "llm_map_drug": lambda desc: [],
        "llm_normalize_drug": lambda name: [name],
        "llm_map_function": lambda desc, options, max_items=3: [],
        "llm_summarize_forward": lambda result, include_numbers=False: "mock summary",
        "llm_summarize_reverse": lambda result, include_numbers=False: "mock summary reverse",
    }


def _tail(path: Path, n: int = 12) -> list[str]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return lines[-n:]


def _run_case(
    workspace: Path,
    *,
    case_id: str,
    title: str,
    verbosity: str,
    log_human_readable: bool,
    log_llm_io: bool | None,
):
    from PxFquery import PxFquery

    day = datetime.now().strftime("%Y-%m-%d")
    log_dir = workspace / "report/04_management/logs"
    prefix = f"loggerdemo_{case_id}"
    log_path = log_dir / f"{prefix}_{day}.log"
    if log_path.exists():
        log_path.unlink()

    pxf = PxFquery()
    pxf.load_data("xpr", str(workspace / "output/store/gsea_anndata/xpr_func_ad.h5ad"))
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="mock",
        model="mock-model",
        prompt_hooks=_make_hooks(),
        verbosity=verbosity,
        log_to_file=True,
        log_dir=str(log_dir),
        log_file_prefix=prefix,
        log_human_readable=log_human_readable,
        log_llm_io=log_llm_io,
    )
    res = pxf.query("logger demo", top_n=5)
    meta = getattr(res, "resolver_meta", {}) or {}
    tail = _tail(log_path, n=14)
    return {
        "id": case_id,
        "title": title,
        "verbosity": verbosity,
        "log_human_readable": log_human_readable,
        "log_llm_io": log_llm_io,
        "query_id": meta.get("query_id"),
        "hit_level": meta.get("hit_level"),
        "llm_call_stats": meta.get("llm_call_stats"),
        "log_path": str(log_path),
        "log_tail": tail,
    }


def _has_non_empty_env(workspace: Path, key: str) -> bool:
    env_path = workspace / ".env"
    if not env_path.exists():
        return False
    for line in env_path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        if k.strip() == key and bool(v.strip().strip('"').strip("'")):
            return True
    return False


def _run_case_live_llm(workspace: Path):
    from PxFquery import PxFquery

    day = datetime.now().strftime("%Y-%m-%d")
    log_dir = workspace / "report/04_management/logs"
    prefix = "loggerdemo_05_live_llm"
    log_path = log_dir / f"{prefix}_{day}.log"
    if log_path.exists():
        log_path.unlink()

    pxf = PxFquery()
    pxf.load_data("xpr", str(workspace / "output/store/gsea_anndata/xpr_func_ad.h5ad"))
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="minimax",
        model=os.getenv("MINIMAX_MODEL", "MiniMax-M2.7"),
        verbosity="normal",
        log_to_file=True,
        log_dir=str(log_dir),
        log_file_prefix=prefix,
        log_human_readable=False,
        log_llm_io=False,
        use_fast_path=False,
    )
    res = pxf._resolver.resolve_and_query(  # pylint: disable=protected-access
        "In A549, what pathways are affected by EGFR knockdown?",
        top_n=5,
        summarize=False,
    )
    meta = getattr(res, "resolver_meta", {}) or {}
    tail = _tail(log_path, n=14)
    return {
        "id": "05_live_llm",
        "title": "Real LLM call (MiniMax)",
        "verbosity": "normal",
        "log_human_readable": False,
        "log_llm_io": False,
        "query_id": meta.get("query_id"),
        "hit_level": meta.get("hit_level"),
        "llm_call_stats": meta.get("llm_call_stats"),
        "log_path": str(log_path),
        "log_tail": tail,
    }


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    package_root = workspace / "script"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))
    _load_env(workspace / ".env")

    cases = [
        {
            "case_id": "01_normal_technical",
            "title": "Normal + Technical format",
            "verbosity": "normal",
            "log_human_readable": False,
            "log_llm_io": False,
        },
        {
            "case_id": "02_quiet_minimal",
            "title": "Quiet (minimum logs)",
            "verbosity": "quiet",
            "log_human_readable": False,
            "log_llm_io": False,
        },
        {
            "case_id": "03_debug_with_io",
            "title": "Debug + LLM I/O visible",
            "verbosity": "debug",
            "log_human_readable": False,
            "log_llm_io": True,
        },
        {
            "case_id": "04_normal_human",
            "title": "Normal + Human-readable format",
            "verbosity": "normal",
            "log_human_readable": True,
            "log_llm_io": False,
        },
    ]

    results = [_run_case(workspace, **case) for case in cases]
    if _has_non_empty_env(workspace, "MINIMAX_API_KEY"):
        try:
            results.append(_run_case_live_llm(workspace))
        except Exception as e:  # pragma: no cover - network/provider instability
            results.append(
                {
                    "id": "05_live_llm",
                    "title": f"Real LLM call (MiniMax) - failed: {type(e).__name__}",
                    "verbosity": "normal",
                    "log_human_readable": False,
                    "log_llm_io": False,
                    "query_id": None,
                    "hit_level": None,
                    "llm_call_stats": {},
                    "log_path": "N/A",
                    "log_tail": [str(e)],
                }
            )
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = [
        "# Logger Capabilities Demo (Real Run)",
        "",
        f"- Time: {now}",
        "- Scope: resolver logger (mock provider + real local data/index).",
        "- Query used in all cases: `logger demo` (hooked intent -> A549 + EGFR).",
        "",
        "## 1) 设计总览",
        "",
        "1. 统一入口：`script/PxFquery/logging_utils.py` 提供 `configure_logger()`。",
        "2. verbosity：`quiet`(WARNING+) / `normal`(INFO+) / `debug`(DEBUG+)。",
        "3. query trace：每次 query 生成 `query_id`，写入日志与 `resolver_meta.query_id`。",
        "4. LLM I/O：`log_llm_io=True` 时在 debug 级输出输入/输出摘要。",
        "5. 文件日志：`log_to_file=True` 时写 `prefix_YYYY-MM-DD.log`。",
        "6. 人类可读模式：`log_human_readable=True` 时采用简化格式。",
        "",
        "## 2) 从简单到复杂的真实测试",
        "",
    ]

    for i, item in enumerate(results, start=1):
        lines.extend(
            [
                f"### Case {i}: {item['title']}",
                "",
                f"- verbosity: `{item['verbosity']}`",
                f"- human_readable: `{item['log_human_readable']}`",
                f"- log_llm_io: `{item['log_llm_io']}`",
                f"- query_id: `{item['query_id']}`",
                f"- hit_level: `{item['hit_level']}`",
                f"- llm_call_stats.query: `{item['llm_call_stats'].get('query', {}) if item['llm_call_stats'] else {}}`",
                f"- log file: `{item['log_path']}`",
                "",
                "日志尾部样例：",
                "```text",
            ]
        )
        if item["log_tail"]:
            lines.extend(item["log_tail"])
        else:
            lines.append("(empty)")
        lines.append("```")
        lines.append("")

    lines.extend(
        [
            "## 3) 结论（人类可读 vs AI 可读）",
            "",
            "1. `quiet`：最简，只保留 warning/error，适合只看是否出错。",
            "2. `normal + human_readable=True`：最适合人读，保留关键步骤与状态。",
            "3. `normal + technical`：兼顾追踪，适合开发日常。",
            "4. `debug + log_llm_io=True`：最适合定位复杂问题（信息最多）。",
            "",
            "## 4) 推荐配置（你提到的“人类优先”）",
            "",
            "```python",
            "pxf.enable_resolver(",
            "    ...,",
            "    verbosity=\"normal\",",
            "    log_human_readable=True,",
            "    log_to_file=True,",
            "    log_dir=\"report/04_management/logs\",",
            "    log_llm_io=False,",
            ")",
            "```",
        ]
    )

    out = workspace / "report/04_management/logger_capabilities_demo.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(str(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
