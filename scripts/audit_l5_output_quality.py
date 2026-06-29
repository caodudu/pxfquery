from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import matplotlib.image as mpimg


INTERNAL_HTML_PATTERNS = [
    re.compile(r"\bl[1-5][._-]", re.IGNORECASE),
    re.compile(r"\bsummary_source\b", re.IGNORECASE),
    re.compile(r"\bevidence_dossier\b", re.IGNORECASE),
    re.compile(r"\broute_plan\b", re.IGNORECASE),
    re.compile(r"\bquery_id\b", re.IGNORECASE),
]

CLINICAL_OVERCLAIM_PATTERNS = [
    re.compile(r"\bclinical efficacy\b", re.IGNORECASE),
    re.compile(r"\b治疗有效\b"),
    re.compile(r"\b临床疗效\b"),
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validation-json", required=True)
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--max-cases", type=int)
    args = parser.parse_args(argv)

    validation = json.loads(Path(args.validation_json).read_text(encoding="utf-8"))
    cases = _collect_cases(validation)
    if args.max_cases is not None:
        cases = cases[: args.max_cases]

    findings = []
    stats = {
        "cases_checked": 0,
        "html_checked": 0,
        "png_checked": 0,
        "svg_checked": 0,
        "chat_checked": 0,
    }
    for case in cases:
        stats["cases_checked"] += 1
        findings.extend(_audit_case(case, stats))

    report = {
        "schema_version": "pxfquery-l5-output-quality-audit/v1",
        "validation_json": str(Path(args.validation_json).resolve()),
        "stats": stats,
        "finding_count": len(findings),
        "findings": findings,
    }
    out = Path(args.output_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["schema_version", "stats", "finding_count"]}, ensure_ascii=False, indent=2))
    return 0 if not findings else 1


def _collect_cases(validation: dict[str, Any]) -> list[dict[str, Any]]:
    cases = []
    artifact_dir = Path(validation.get("artifact_dir", ""))
    if artifact_dir.exists():
        for html_path in sorted(artifact_dir.glob("*/*/answer.html")):
            dataset = html_path.parents[1].name
            case_id = html_path.parent.name
            cases.append(
                {
                    "dataset": dataset,
                    "case_id": case_id,
                    "query": None,
                    "html": html_path,
                    "case_dir": html_path.parent,
                    "figure_kinds": [],
                }
            )
        if cases:
            return cases
    for dataset, stats in validation.get("datasets", {}).items():
        for sample in stats.get("samples", []):
            html_path = Path(sample["html"])
            case_dir = html_path.parent
            cases.append(
                {
                    "dataset": dataset,
                    "case_id": sample.get("case_id"),
                    "query": sample.get("query"),
                    "html": html_path,
                    "case_dir": case_dir,
                    "figure_kinds": sample.get("figure_kinds", []),
                }
            )
    return cases


def _audit_case(case: dict[str, Any], stats: dict[str, int]) -> list[dict[str, Any]]:
    findings = []
    html_path = Path(case["html"])
    if not html_path.exists():
        return [_finding(case, "html_missing", "HTML report file is missing.")]

    html_text = html_path.read_text(encoding="utf-8")
    stats["html_checked"] += 1
    required_sections = ["Question", "Main Evidence", "Process Overview", "Figures", "Evidence Limits"]
    for section in required_sections:
        if section not in html_text:
            findings.append(_finding(case, "html_missing_section", f"Missing section: {section}"))
    if "<table" not in html_text:
        findings.append(_finding(case, "html_missing_table", "HTML report has no evidence table."))
    if "<svg" not in html_text:
        findings.append(_finding(case, "html_missing_svg", "HTML report has no embedded SVG figure."))
    if len(_strip_tags(html_text)) < 900:
        findings.append(_finding(case, "html_too_thin", "HTML visible text is too short for a useful report."))
    for pattern in INTERNAL_HTML_PATTERNS:
        if pattern.search(html_text):
            findings.append(_finding(case, "html_internal_label", f"HTML exposes internal label matching {pattern.pattern!r}."))
            break

    png_files = sorted((Path(case["case_dir"]) / "png").glob("*.png"))
    svg_files = sorted((Path(case["case_dir"]) / "svg").glob("*.svg"))
    if not png_files:
        findings.append(_finding(case, "png_missing", "No PNG figures were written."))
    if not svg_files:
        findings.append(_finding(case, "svg_missing", "No SVG figures were written."))
    for path in png_files:
        stats["png_checked"] += 1
        findings.extend(_audit_png(case, path))
    for path in svg_files:
        stats["svg_checked"] += 1
        findings.extend(_audit_svg(case, path))

    chat_path = Path(case["case_dir"]) / "chat.json"
    if chat_path.exists():
        stats["chat_checked"] += 1
        findings.extend(_audit_chat(case, chat_path))
    return findings


def _audit_png(case: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    findings = []
    try:
        image = mpimg.imread(path)
    except Exception as exc:
        return [_finding(case, "png_unreadable", f"{path.name}: {type(exc).__name__}: {exc}")]
    if image.size == 0:
        findings.append(_finding(case, "png_empty", f"{path.name}: image array is empty."))
    if image.shape[0] < 120 or image.shape[1] < 120:
        findings.append(_finding(case, "png_too_small", f"{path.name}: image dimensions are too small: {image.shape!r}."))
    sample = image[..., :3] if image.ndim == 3 else image
    if float(sample.max() - sample.min()) < 0.02:
        findings.append(_finding(case, "png_low_variance", f"{path.name}: image appears visually blank or near-uniform."))
    return findings


def _audit_svg(case: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    findings = []
    if not text.startswith("<svg"):
        findings.append(_finding(case, "svg_bad_root", f"{path.name}: SVG does not start with <svg."))
    shape_count = sum(text.count(tag) for tag in ["<rect", "<circle", "<line", "<path", "<text"])
    if shape_count < 5:
        findings.append(_finding(case, "svg_too_few_elements", f"{path.name}: too few visible SVG elements."))
    if "Figure" in text and len(_strip_tags(text)) < 60:
        findings.append(_finding(case, "svg_thin_text", f"{path.name}: SVG has little explanatory text."))
    return findings


def _audit_chat(case: dict[str, Any], path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    answer = str(payload.get("assistant") or "")
    findings = []
    if len(answer.strip()) < 80:
        findings.append(_finding(case, "chat_too_short", "Chat answer is too short to be useful."))
    if not any(term in answer for term in ["证据", "evidence", "限制", "limit", "confidence", "置信"]):
        findings.append(_finding(case, "chat_missing_evidence_or_limits", "Chat answer does not mention evidence or limitations."))
    for pattern in CLINICAL_OVERCLAIM_PATTERNS:
        if pattern.search(answer):
            findings.append(_finding(case, "chat_clinical_overclaim", f"Chat answer contains possible clinical overclaim: {pattern.pattern!r}."))
            break
    return findings


def _strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text)


def _finding(case: dict[str, Any], code: str, message: str) -> dict[str, Any]:
    return {
        "dataset": case.get("dataset"),
        "case_id": case.get("case_id"),
        "query": case.get("query"),
        "code": code,
        "message": message,
    }


if __name__ == "__main__":
    raise SystemExit(main())
