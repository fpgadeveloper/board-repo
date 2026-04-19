#!/usr/bin/env python3
"""Regenerate the vendor tables in README.md from vendors.json.

The README contains two auto-generated blocks delimited by HTML comment
markers — one for board vendors and one for silicon vendors. This script
reads vendors.json, renders a sorted `| Key | Name |` table for each
section, and replaces the content between the markers. Run after editing
vendors.json and commit the README change. CI enforces that the committed
README matches what this script produces.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
VENDORS = ROOT / "vendors.json"

BLOCKS = [
    ("board_vendors", "BOARD-VENDORS-BEGIN", "BOARD-VENDORS-END"),
    ("silicon_vendors", "SILICON-VENDORS-BEGIN", "SILICON-VENDORS-END"),
]


def render_table(section: dict) -> str:
    lines = ["| Key | Name |", "|-----|------|"]
    for key in sorted(section):
        lines.append(f"| `{key}` | {section[key]['name']} |")
    return "\n".join(lines)


def replace_block(text: str, begin: str, end: str, content: str) -> str:
    begin_idx = text.find(f"<!-- {begin}")
    end_idx = text.find(f"<!-- {end}")
    if begin_idx == -1 or end_idx == -1 or end_idx < begin_idx:
        print(f"ERROR: markers {begin}/{end} not found or misordered in README.md", file=sys.stderr)
        sys.exit(1)
    begin_line_end = text.find("\n", begin_idx)
    return text[: begin_line_end + 1] + content + "\n" + text[end_idx:]


def main() -> None:
    vendors = json.loads(VENDORS.read_text(encoding="utf-8"))
    readme = README.read_text(encoding="utf-8")
    for section_key, begin, end in BLOCKS:
        readme = replace_block(readme, begin, end, render_table(vendors[section_key]))
    README.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
