#!/usr/bin/env python3
"""Assign ice_type to every entry in _bibliography/papers.bib."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "_bibliography" / "papers.bib"

WORKSHOP_MARKERS = (
    "technology showcase",
    "lincoln laboratory",
    "best paper award contest",
)
INDUSTRIAL_MARKERS = (
    "to qualcomm",
    "to samsung",
    "to kodak",
    "cisco",
    "award number",
)


def classify(entry_type: str, fields: dict[str, str]) -> str:
    note = fields.get("note", "")
    howpublished = fields.get("howpublished", "").lower()

    if "tutorial" in note.lower():
        return "tutorials"
    if entry_type == "book":
        return "book"
    if entry_type == "incollection":
        return "book_chapter"
    if entry_type == "phdthesis":
        return "dissertations"
    if entry_type == "article":
        return "journal_papers"
    if entry_type == "inproceedings":
        return "conference_papers"
    if entry_type == "misc":
        if any(marker in howpublished for marker in INDUSTRIAL_MARKERS):
            return "technical_industrial"
        if any(marker in howpublished for marker in WORKSHOP_MARKERS):
            return "workshop_presentations"
        if howpublished.startswith("at the") or " at the " in howpublished:
            return "conference_presenter"
        return "workshop_presentations"
    return "conference_papers"


def parse_entries(text: str) -> list[tuple[str, dict[str, str], str]]:
    entries: list[tuple[str, dict[str, str], str]] = []
    pattern = re.compile(r"^@\w+\{([^,]+),", re.MULTILINE)
    starts = [m.start() for m in pattern.finditer(text)]
    if not starts:
        return entries

    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(text)
        block = text[start:end].rstrip()
        header = re.match(r"^@(\w+)\{([^,]+),", block)
        if not header:
            continue
        entry_type, key = header.group(1), header.group(2)
        fields: dict[str, str] = {}
        for match in re.finditer(r"^\s*(\w+)\s*=\s*\{([^}]*)\}\s*,?\s*$", block, re.MULTILINE):
            fields[match.group(1).lower()] = match.group(2).strip()
        entries.append((key, {"type": entry_type, **fields}, block))
    return entries


def upsert_ice_type(block: str, ice_type: str) -> str:
    if re.search(r"^\s*ice_type\s*=", block, re.MULTILINE):
        return re.sub(r"^\s*ice_type\s*=\s*\{[^}]*\}\s*,?\s*$", f"  ice_type = {{{ice_type}}},", block, count=1, flags=re.MULTILINE)
    lines = block.splitlines()
    insert_at = 1
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() and not line.strip().startswith("%"):
            insert_at = i
            break
    lines.insert(insert_at, f"  ice_type = {{{ice_type}}},")
    return "\n".join(lines) + ("\n" if block.endswith("\n") else "")


def main() -> int:
    text = BIB.read_text(encoding="utf-8")
    preamble, _, body = text.partition("@string")
    if not body:
        body = text
        preamble = ""
    else:
        body = "@string" + body

    entries = parse_entries(body)
    if not entries:
        print("No bibliography entries found.", file=sys.stderr)
        return 1

    rebuilt: list[str] = []
    counts: dict[str, int] = {}
    for _key, meta, block in entries:
        ice_type = classify(meta["type"], meta)
        counts[ice_type] = counts.get(ice_type, 0) + 1
        rebuilt.append(upsert_ice_type(block, ice_type))

    header = preamble.rstrip("\n")
    if header:
        header += "\n\n"
    BIB.write_text(header + "\n\n".join(rebuilt).rstrip() + "\n", encoding="utf-8")

    for ice_type, count in sorted(counts.items()):
        print(f"  {ice_type}: {count}")
    print(f"Tagged {len(entries)} entries in {BIB.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
