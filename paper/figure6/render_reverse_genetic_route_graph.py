from __future__ import annotations

"""Historical renderer for the old RG15 diagnostic set.

Do not use this as the Figure 6 next-round execution entry. The current
next-round path uses multicell-only top5 queries and is documented in
figure6_next_round_reverse_genetic_query_proposals_zh.md.
"""

import csv
import json
import sys
from pathlib import Path


TASK_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = TASK_ROOT.parents[2]
WORKCOPY_SRC = TASK_ROOT / "3_execution" / "t144_reverse_layered_route_workcopy" / "src"
T137_RECORDS = PROJECT_ROOT / "4_phase_development" / "G-035_goal_ms8_human_usable_package" / "T-140_ms8_12_l4_evidence_dossier_plan" / "4_artifact" / "5_table" / "t137_60_l1_to_l4_parallel_latest.json"
OUT_ROOT = TASK_ROOT / "4_artifact" / "4_picture" / "figure6" / "rg15_reverse_layered_route"
TABLE_ROOT = TASK_ROOT / "4_artifact" / "5_table" / "figure6" / "rg15_reverse_layered_route"


def _load_rg_records() -> list[dict]:
    data = json.loads(T137_RECORDS.read_text())
    records = [record for record in data["records"] if record.get("category") == "reverse_genetic"]
    return sorted(records, key=lambda item: item.get("case_id") or "")


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _write_summary(rows: list[dict]) -> None:
    TABLE_ROOT.mkdir(parents=True, exist_ok=True)
    path = TABLE_ROOT / "rg15_reverse_layered_route_summary.csv"
    fieldnames = [
        "case_id",
        "query",
        "status",
        "figure_count",
        "first_figure_kind",
        "top_candidates",
        "target_functions",
        "executed_route_count",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _make_contact_sheet(png_paths: list[Path], output: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont

    if not png_paths:
        return
    thumbs = []
    for path in png_paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((460, 360), Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", (500, 410), "white")
        canvas.paste(img, ((500 - img.width) // 2, 18))
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("Arial.ttf", 16)
        except Exception:
            font = ImageFont.load_default()
        draw.text((18, 382), path.parent.parent.name, fill=(17, 24, 39), font=font)
        thumbs.append(canvas)
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 500, rows * 410), "white")
    for idx, thumb in enumerate(thumbs):
        x = (idx % cols) * 500
        y = (idx // cols) * 410
        sheet.paste(thumb, (x, y))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def main() -> None:
    sys.path.insert(0, str(WORKCOPY_SRC))
    from pxfquery.l5_presentation.figures import build_figure_specs, write_figure_files

    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    TABLE_ROOT.mkdir(parents=True, exist_ok=True)
    records = _load_rg_records()
    summary_rows: list[dict] = []
    layered_pngs: list[Path] = []

    for record in records:
        case_id = str(record["case_id"])
        case_prefix = case_id.lower()
        dossier = record["evidence_dossier"]
        specs = [
            spec
            for spec in build_figure_specs(dossier, max_items=12)
            if spec.get("kind") == "reverse_layered_route_graph"
        ]
        case_dir = OUT_ROOT / case_id
        (case_dir / "png").mkdir(parents=True, exist_ok=True)
        (case_dir / "pdf").mkdir(parents=True, exist_ok=True)
        png_paths = [Path(path) for path in write_figure_files(specs, case_dir / "png", prefix=case_prefix, fmt="png")]
        pdf_paths = [Path(path) for path in write_figure_files(specs, case_dir / "pdf", prefix=case_prefix, fmt="pdf")]
        _write_json(case_dir / f"{case_prefix}_figure_specs.json", specs)
        _write_json(case_dir / f"{case_prefix}_record_compact.json", {
            "case_id": case_id,
            "query": record.get("query"),
            "status": record.get("status"),
            "compact_summary": record.get("compact_summary"),
            "png_paths": [str(path) for path in png_paths],
            "pdf_paths": [str(path) for path in pdf_paths],
        })
        layered = [path for path in png_paths if "reverse_layered_route_graph" in path.name]
        if layered:
            layered_pngs.append(layered[0])
        first = specs[0] if specs else {}
        top_candidates = (record.get("compact_summary") or {}).get("top_perturbations") or []
        target_functions = []
        for function in first.get("functions") or []:
            label = function.get("label")
            if label and label not in target_functions:
                target_functions.append(label)
        summary_rows.append({
            "case_id": case_id,
            "query": record.get("query"),
            "status": record.get("status"),
            "figure_count": len(specs),
            "first_figure_kind": first.get("kind"),
            "top_candidates": "; ".join(str(item.get("label")) for item in top_candidates[:5]),
            "target_functions": "; ".join(target_functions),
            "executed_route_count": (record.get("compact_summary") or {}).get("executed_route_count"),
        })

    _write_summary(summary_rows)
    _make_contact_sheet(layered_pngs, OUT_ROOT / "rg15_reverse_layered_route_contact_sheet.png")
    print(f"Rendered {len(records)} reverse genetic cases")
    print(OUT_ROOT)
    print(TABLE_ROOT / "rg15_reverse_layered_route_summary.csv")


if __name__ == "__main__":
    main()

