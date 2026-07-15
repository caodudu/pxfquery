from __future__ import annotations

import json
import os
import sys
import textwrap
import time
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
TASK_ROOT = PROJECT_ROOT / "5_phase_translation" / "G-011_paper_figure_planning" / "T-149_figure5_forward_drug_query_notebook_figure_workb"
PKG_ROOT = TASK_ROOT / "3_execution" / "t144_package_source_for_figure5a_round5"
SRC_ROOT = PKG_ROOT / "src"

ROUND_ID = "round5_clean_route_graph_v0522"
OUT_PICTURE = TASK_ROOT / "4_artifact" / "4_picture" / "figure5" / "panel_a_iter" / ROUND_ID
OUT_TABLE = TASK_ROOT / "4_artifact" / "5_table" / "figure5" / "panel_a_iter" / ROUND_ID
OUT_TMP = TASK_ROOT / "4_artifact" / "1_tmp" / "panel_a_iter" / ROUND_ID

CASES = [
    {
        "case_id": "R5C01_CLEAN_TAMOXIFEN_BREAST",
        "drug_theme": "tamoxifen-like anti-estrogen treatment in breast cancer",
        "why_test": "Clean disease + drug-family query; tests whether SERM/tamoxifen structural neighbors produce a readable drug-to-function route graph.",
        "query": "In breast cancer models, what functional programs change after tamoxifen-like anti-estrogen treatment?",
    },
    {
        "case_id": "R5C02_CLEAN_GEMCITABINE_PDAC",
        "drug_theme": "gemcitabine-like nucleoside chemotherapy in pancreatic cancer",
        "why_test": "Clean disease + chemotherapy-family query; tests whether nucleoside analog drug neighbors give the clearest bridge to Figure 5 drug-similarity evidence.",
        "query": "In pancreatic cancer models, what functional programs change after gemcitabine-like nucleoside chemotherapy?",
    },
    {
        "case_id": "R5C03_CLEAN_BRAF_MEK_MELANOMA",
        "drug_theme": "BRAF/MEK inhibitor treatment in melanoma",
        "why_test": "Clean targeted-therapy query; tests whether a canonical MAPK drug example gives an intuitive route graph and functional answer.",
        "query": "In melanoma models, what functional programs change after BRAF or MEK inhibitor treatment such as vemurafenib or trametinib?",
    },
    {
        "case_id": "R5C04_CLEAN_EGFR_LUNG",
        "drug_theme": "EGFR inhibitor treatment in lung cancer",
        "why_test": "Clean RTK inhibitor query; tests whether a familiar lung-cancer targeted therapy produces a direct reader-friendly Figure 5A route graph.",
        "query": "In lung cancer models, what functional programs change after EGFR inhibitor treatment such as gefitinib or erlotinib?",
    },
]


def load_env() -> None:
    sys.path.insert(0, str(SRC_ROOT))
    os.environ["PYTHONPATH"] = str(SRC_ROOT) + os.pathsep + os.environ.get("PYTHONPATH", "")
    for env_path in [
        Path.home() / ".env",
        PROJECT_ROOT / ".env",
        PROJECT_ROOT / "4_phase_development" / "G-035_goal_ms8_human_usable_package" / "T-144_ms8_14_user_value_l5_output_rework" / "1_asset" / ".env",
    ]:
        if not env_path.exists():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())


def write_table(rows: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False)


def build_pick_sheet(summary_df: pd.DataFrame, output_path: Path) -> None:
    from PIL import Image, ImageDraw, ImageFont

    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
        font_case = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 17)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        font_header = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
    except Exception:
        font_title = font_case = font_small = font_header = ImageFont.load_default()

    cols = [
        ("01_evidence_match_map", "Evidence map"),
        ("02_forward_route_graph", "Route graph"),
        ("03_function_match_heatmap", "Heatmap"),
        ("04_function_consensus_bar", "Consensus"),
    ]
    thumb_w = 380
    thumb_h = 300
    label_w = 440
    pad = 20
    header_h = 96
    row_h = thumb_h + 70
    sheet_w = label_w + len(cols) * thumb_w + (len(cols) + 2) * pad
    sheet_h = header_h + len(summary_df) * row_h + pad
    canvas = Image.new("RGB", (sheet_w, sheet_h), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text((pad, 18), "Figure 5A clean-query route graph candidates (T144 0.5.22)", fill=(0, 0, 0), font=font_title)
    for j, (_, title) in enumerate(cols):
        x = label_w + pad + j * (thumb_w + pad)
        draw.text((x + 6, 62), title, fill=(0, 0, 0), font=font_header)

    for i, row in summary_df.reset_index(drop=True).iterrows():
        cid = row["case_id"]
        y = header_h + i * row_h
        if i % 2 == 0:
            draw.rectangle((0, y, sheet_w, y + row_h), fill=(248, 248, 248))
        draw.line((0, y, sheet_w, y), fill=(220, 220, 220), width=1)
        draw.text((pad, y + 14), cid, fill=(0, 0, 0), font=font_case)
        text = f"{row['drug_theme']}\n{row['query']}\nRoutes={row['route_rows']} Functions={row['function_rows']} Error={bool(row['error'])}"
        lines: list[str] = []
        for part in text.split("\n"):
            lines.extend(textwrap.wrap(part, width=52))
        for k, line in enumerate(lines[:9]):
            draw.text((pad, y + 42 + k * 17), line, fill=(35, 35, 35), font=font_small)
        for j, (suffix, _) in enumerate(cols):
            matches = sorted((OUT_PICTURE / cid / "png").glob(f"*_{suffix}.png"))
            if not matches:
                continue
            img = Image.open(matches[0]).convert("RGB")
            img.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            x = label_w + pad + j * (thumb_w + pad) + (thumb_w - img.width) // 2
            yy = y + 48 + (thumb_h - img.height) // 2
            canvas.paste(img, (x, yy))
            draw.rectangle((x, yy, x + img.width, yy + img.height), outline=(210, 210, 210), width=1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=95)


def score_row(row: dict) -> dict:
    pert_types = str(row.get("perturbation_match_types") or "")
    aliases = [x for x in str(row.get("perturbation_aliases") or "").split("|") if x]
    route_rows = int(row.get("route_rows") or 0)
    function_rows = int(row.get("function_rows") or 0)
    route_graph_score = min(5, 1 + route_rows // 3)
    if "structural_neighbor" in pert_types or "mechanism_representative" in pert_types:
        route_graph_score = min(5, route_graph_score + 1)
    if len(aliases) >= 2:
        route_graph_score = min(5, route_graph_score + 1)
    heatmap_score = 4 if function_rows >= 64 else 3 if function_rows >= 32 else 1
    answer_score = 4 if function_rows >= 64 else 3 if function_rows >= 32 else 1
    return {
        "route_graph_score": route_graph_score,
        "heatmap_score": heatmap_score,
        "answer_score": answer_score,
        "overall_score": round((route_graph_score + heatmap_score + answer_score) / 3, 2),
    }


def main() -> None:
    load_env()
    from pxfquery import PxFQuery
    import pxfquery

    OUT_PICTURE.mkdir(parents=True, exist_ok=True)
    OUT_TABLE.mkdir(parents=True, exist_ok=True)
    OUT_TMP.mkdir(parents=True, exist_ok=True)
    manifest = {
        "round_id": ROUND_ID,
        "package_root": str(PKG_ROOT),
        "pxfquery_file": str(Path(pxfquery.__file__).resolve()),
        "version": pxfquery.__version__,
        "cases": CASES,
        "started_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    (OUT_TMP / "run_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    summary_rows = []
    for case in CASES:
        cid = case["case_id"]
        case_picture = OUT_PICTURE / cid
        case_table = OUT_TABLE / cid
        case_tmp = OUT_TMP / cid
        case_picture.mkdir(parents=True, exist_ok=True)
        case_table.mkdir(parents=True, exist_ok=True)
        case_tmp.mkdir(parents=True, exist_ok=True)
        started = time.perf_counter()
        route_rows: list[dict] = []
        function_rows: list[dict] = []
        ranked_rows: list[dict] = []
        error = ""
        try:
            client = PxFQuery()
            qdata = client.tl.parse(case["query"], top_n=8, progress=False)
            client.tl.answer(qdata, progress=False)
            answer = client.get.answer(qdata)
            route_rows = list(answer.tables.get("route_summary", []))
            function_rows = list(answer.tables.get("route_function_results", []))
            ranked_rows = list(answer.tables.get("ranked_results", []))
            write_table(route_rows, case_table / "route_summary.csv")
            write_table(function_rows, case_table / "route_function_results.csv")
            write_table(ranked_rows, case_table / "ranked_results.csv")
            (case_table / "answer.txt").write_text(str(answer), encoding="utf-8")
            for fmt in ["png", "pdf"]:
                client.tl.figures(qdata, output_dir=case_picture / fmt, prefix=cid.lower(), format=fmt)
        except Exception as exc:
            error = repr(exc)
            (case_tmp / "error.txt").write_text(error, encoding="utf-8")
        elapsed = time.perf_counter() - started
        route_df = pd.DataFrame(route_rows)
        fn_df = pd.DataFrame(function_rows)
        row = {
            **case,
            "elapsed_seconds": round(elapsed, 3),
            "error": error,
            "route_rows": len(route_rows),
            "function_rows": len(function_rows),
            "ranked_rows": len(ranked_rows),
            "unique_cells": "|".join(sorted(route_df["cell"].dropna().astype(str).unique())) if "cell" in route_df else "",
            "unique_perturbations": "|".join(sorted(route_df["perturbation"].dropna().astype(str).unique())) if "perturbation" in route_df else "",
            "perturbation_aliases": "|".join(sorted(route_df["perturbation_alias"].dropna().astype(str).unique())) if "perturbation_alias" in route_df else "",
            "cell_match_types": "|".join(sorted(route_df["cell_match_type"].dropna().astype(str).unique())) if "cell_match_type" in route_df else "",
            "perturbation_match_types": "|".join(sorted(route_df["perturbation_match_type"].dropna().astype(str).unique())) if "perturbation_match_type" in route_df else "",
            "top_activated": "|".join(fn_df.loc[fn_df.get("direction", "") == "activated", "label"].head(5).astype(str)) if "direction" in fn_df and "label" in fn_df else "",
            "top_suppressed": "|".join(fn_df.loc[fn_df.get("direction", "") == "suppressed", "label"].head(5).astype(str)) if "direction" in fn_df and "label" in fn_df else "",
        }
        row.update(score_row(row))
        summary_rows.append(row)
        print(f"{cid}: routes={len(route_rows)} functions={len(function_rows)} ranked={len(ranked_rows)} error={bool(error)} elapsed={elapsed:.1f}s", flush=True)

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(OUT_TABLE / f"{ROUND_ID}_summary.csv", index=False)
    build_pick_sheet(summary_df, OUT_PICTURE / f"{ROUND_ID}_pick_sheet.png")
    (OUT_TMP / "run_complete.json").write_text(
        json.dumps(
            {
                "completed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "summary_path": str(OUT_TABLE / f"{ROUND_ID}_summary.csv"),
                "picture_dir": str(OUT_PICTURE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

