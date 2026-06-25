"""
pxfquery-T-026 validation driver.

Invokes loader.load_bundle against the T-021 standard_resources bundle,
writes a JSON validation record and a Markdown readable summary.
"""
import os
import sys
import json
import time

# add loader to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from loader import load_bundle


def resolve_bundle_root():
    """Resolve bundle path, preferring A-004 asset symlink."""
    candidates = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "1_asset", "T-021 standard_resources bundle (D-004)"),
    ]
    for p in candidates:
        absp = os.path.abspath(p)
        if os.path.isdir(absp):
            return absp
    raise FileNotFoundError(f"No bundle directory found in candidates: {candidates}")


def write_validation_json(result, path):
    """Write machine-readable validation record."""
    with open(path, "w") as f:
        json.dump(result, f, indent=2, default=str)
    print(f"[WRITTEN] {path}")


def write_validation_summary(result, path):
    """Write human-readable Markdown summary."""
    lines = []
    lines.append("# pxfquery-T-026 Loader Validation Summary")
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"Bundle root: `{result['bundle_root']}`")
    lines.append(f"Total files loaded: {result['summary']['total_files_loaded']}")
    lines.append(f"Failed files: {len(result['summary']['failed_files'])}")
    lines.append("")

    if result["summary"]["failed_files"]:
        lines.append("## Failed Files")
        for f in result["summary"]["failed_files"]:
            lines.append(f"- **{f['filename']}**: {f['error']}")
        lines.append("")

    lines.append("## Loaded By Category")
    for cat, count in result["summary"]["loaded_by_category"].items():
        lines.append(f"- **{cat}**: {count}")
    lines.append("")

    if result["matrices"]:
        lines.append("## Functional Matrices (H5AD)")
        lines.append("| File | Shape | obs_columns | var_count | X_dtype | Load (s) |")
        lines.append("|------|-------|-------------|-----------|---------|----------|")
        for m in result["matrices"]:
            cols = ", ".join(m.get("obs_columns", []))
            lines.append(f"| {m['filename']} | {m['shape']} | {cols} | {m.get('n_var', '?')} | {m.get('X_dtype', '?')} | {m.get('load_sec', '?')} |")
        lines.append("")

    if result["indexes"]:
        lines.append("## Query Indexes (JSON)")
        lines.append("| File | Type | Top-Level Keys | Item Count | Load (s) |")
        lines.append("|------|------|----------------|------------|----------|")
        for idx in result["indexes"]:
            tlk = ", ".join(idx.get("top_level_keys", ["?"])) if idx.get("top_level_keys") else "(list)"
            lines.append(f"| {idx['filename']} | {idx.get('type', '?')} | {tlk} | {idx.get('item_count', '?')} | {idx.get('load_sec', '?')} |")
        lines.append("")

    if result["metadata"]:
        lines.append("## Metadata Tables (CSV)")
        lines.append("| File | Columns | Rows | Load (s) |")
        lines.append("|------|---------|------|----------|")
        for md in result["metadata"]:
            cols = ", ".join(md.get("columns", ["?"]))
            lines.append(f"| {md['filename']} | {cols} | {md.get('n_rows', '?')} | {md.get('load_sec', '?')} |")
        lines.append("")

    if result["description"]:
        lines.append("## Data Description (YAML)")
        d = result["description"]
        tlk = ", ".join(d.get("top_level_keys", ["?"]))
        lines.append(f"| File | Top-Level Keys | Load (s) |")
        lines.append(f"| {d['filename']} | {tlk} | {d.get('load_sec', '?')} |")
        lines.append("")

    lines.append("---")
    lines.append("Validation complete. All files opened with appropriate Python libraries.")

    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[WRITTEN] {path}")


def main():
    bundle_root = resolve_bundle_root()
    print(f"[LOADING] bundle_root={bundle_root}")

    result = load_bundle(bundle_root)

    exec_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(exec_dir, "loader_validation.json")
    md_path = os.path.join(exec_dir, "loader_validation_summary.md")

    write_validation_json(result, json_path)
    write_validation_summary(result, md_path)

    print(f"\n[RESULT] loaded={result['summary']['total_files_loaded']}, failed={len(result['summary']['failed_files'])}")

    if result["summary"]["failed_files"]:
        for f in result["summary"]["failed_files"]:
            print(f"  FAIL: {f['filename']} — {f['error']}")
        sys.exit(1)
    else:
        print("[PASS] All files loaded successfully.")


if __name__ == "__main__":
    main()