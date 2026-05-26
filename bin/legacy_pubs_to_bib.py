#!/usr/bin/env python3
"""Convert legacy publications JSON to BibTeX for al-folio."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBS_JSON = ROOT / "_data" / "legacy-publications.json"
OUT_BIB = ROOT / "_bibliography" / "papers.bib"

SECTION_TYPE = {
    "Dissertations": "phdthesis",
    "Journal Papers": "article",
    "Conference Papers": "inproceedings",
    "Book": "book",
    "Book Chapter": "incollection",
    "Tutorials": "inproceedings",
    "Workshop Presentations": "misc",
    "Conference Presenter": "misc",
    "Technical Industrial Presentations": "misc",
}

ABBR_PATTERNS = [
    (r"\bISSCC\b", "ISSCC"),
    (r"\bJSSC\b", "JSSC"),
    (r"\bTVLSI\b", "TVLSI"),
    (r"\bTCAS\b", "TCAS"),
    (r"\bCICC\b", "CICC"),
    (r"\bISCAS\b", "ISCAS"),
    (r"\bDAC\b", "DAC"),
    (r"\bICCD\b", "ICCD"),
    (r"\bGLSVLSI\b", "GLSVLSI"),
    (r"\bGOMACTech\b", "GOMACTech"),
    (r"\bVLSI\b", "VLSI"),
    (r"\bICCAD\b", "ICCAD"),
    (r"\bDATE\b", "DATE"),
    (r"\bASP-DAC\b", "ASP-DAC"),
    (r"\bS3S\b", "S3S"),
    (r"\bSOCC\b", "SOCC"),
    (r"\bISQED\b", "ISQED"),
    (r"\bMLCAD\b", "MLCAD"),
    (r"\bVMIC\b", "VMIC"),
]

SELECTED_YEARS = {2024, 2025}
SELECTED_KEYWORDS = ("career", "obfuscation", "hardware trojan", "3-d", "3d", "ntc")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "", text.lower())
    return text[:24] or "entry"


def clean_text(value: str) -> str:
    value = value.replace("\u2013", "-").replace("\u2014", "-")
    value = re.sub(r"\s+", " ", value)
    return value.strip(" .,")


def extract_quoted_title(text: str) -> str | None:
    if not text:
        return None
    for pattern in (r"[\u201c\"]([^\u201d\"]+)[\u201d\"]", r'"([^"]+)"'):
        match = re.search(pattern, text)
        if match:
            title = clean_text(match.group(1))
            if len(title) > 4 and not title.lower().startswith("presented"):
                return title
    return None


def title_needs_fix(title: str | None) -> bool:
    if not title:
        return True
    title = title.strip()
    if len(title) < 12:
        return True
    broken_prefixes = ("and ", "S. ", "I. ", "Presented", "\u2022", '"', "\u201d")
    return title.startswith(broken_prefixes)


def resolve_title(entry: dict) -> str:
    title = clean_text(entry.get("title") or "")
    title = title.lstrip('"').lstrip("\u201c").lstrip("\u201d").strip()
    venue = entry.get("venue") or ""
    authors = entry.get("authors") or ""
    if title_needs_fix(title):
        for source in (venue, authors):
            quoted = extract_quoted_title(source)
            if quoted:
                return quoted
    if entry["section"] == "Book":
        match = re.search(
            r",\s*(Three-Dimensional Integrated Circuit Design[^,]+)",
            venue,
            re.I,
        )
        if match:
            return clean_text(match.group(1))
    return title or "Untitled"


def extract_journal(venue: str) -> str:
    match = re.search(
        r"[\u201c\"][^\u201d\"]+[\u201d\"]\s*,?\s*(.+?)\s*,\s*(?:Vol\.|Volume|pp\.|No\.)",
        venue,
        re.I,
    )
    if match:
        journal = clean_text(match.group(1))
        if journal.lower() not in {"journal", "untitled"}:
            return journal
    for pattern in (
        r"(IEEE Transactions on [^,]+)",
        r"(IEEE Journal on [^,]+)",
        r"(Journal of Hardware and Systems Security)",
        r"(Microelectronics Journal)",
        r"(University of Rochester Journal)",
    ):
        match = re.search(pattern, venue, re.I)
        if match:
            return clean_text(match.group(1))
    return "Journal"


def extract_booktitle(venue: str, title: str) -> str:
    match = re.search(r"(Proceedings of the [^,]+(?:\([^)]+\))?)", venue, re.I)
    if match:
        return clean_text(match.group(1))
    match = re.search(r"(Proceedings of [^,]+(?:\([^)]+\))?)", venue, re.I)
    if match:
        return clean_text(match.group(1))
    if title and title in venue:
        rest = venue.split(title, 1)[-1].lstrip(" ,")
        event = rest.split(",")[0].strip()
        if event and len(event) > 8:
            return clean_text(event.rstrip("."))
    return clean_text(venue.split(",")[0])


def extract_booktitle_for_chapter(venue: str) -> str:
    match = re.search(
        r"[\u201c\"][^\u201d\"]+[\u201d\"]\s*,\s*(On-Chip [^,]+|[^,]+Interconnect[^,]*)",
        venue,
        re.I,
    )
    if match:
        return clean_text(match.group(1))
    return clean_text(venue)


def parse_misc(entry: dict) -> tuple[str, str, str]:
    venue = normalize_venue(entry.get("venue") or "")
    title = resolve_title(entry)
    authors = clean_text(entry.get("authors") or "I. Savidis")
    if authors.startswith(("Presented", "\u2022", "•")) or "Presented" in authors[:24]:
        authors = "I. Savidis"
    howpublished = extract_howpublished(venue, title)
    return title, authors, howpublished


def resolve_year(entry: dict) -> int | None:
    venue = entry.get("venue") or ""
    raw_year = entry.get("year")
    pdf_url = entry.get("pdf_url") or ""

    if pdf_url:
        stem = Path(pdf_url).stem
        match = re.search(r"_(\d{4})", stem)
        if match:
            return int(match.group(1))
        match = re.search(r"_(\d{2})(?:_|$)", stem)
        if match:
            short_year = int(match.group(1))
            return 2000 + short_year if short_year < 50 else 1900 + short_year

    month_year_match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})",
        venue,
        re.I,
    )
    month_year = int(month_year_match.group(2)) if month_year_match else None

    if raw_year and re.search(rf"pp\.\s*{raw_year}\s", venue):
        return month_year or raw_year

    if month_year:
        return month_year

    if isinstance(raw_year, int) and 1990 <= raw_year <= 2035:
        return raw_year
    return raw_year if isinstance(raw_year, int) else None


def normalize_venue(venue: str) -> str:
    venue = venue.replace("\\}", ")")
    venue = re.sub(r"\)\s*\}", ")", venue)
    return venue


def extract_howpublished(venue: str, title: str) -> str:
    quoted = extract_quoted_title(venue)
    if quoted:
        title = quoted
    if title and title in venue:
        rest = venue.split(title, 1)[-1].lstrip(" ,")
        rest = rest.lstrip('"').lstrip("\u201c").lstrip("\u201d").lstrip(",").strip()
        return clean_text(rest.rstrip("."))
    match = re.search(
        r"(?:Presented|presented)\s+[\u201c\"][^\u201d\"]+[\u201d\"],?\s*(.+)",
        venue,
        re.I | re.S,
    )
    if match:
        return clean_text(match.group(1))
    return clean_text(venue)


def infer_bib_type(entry: dict) -> str:
    section = entry["section"]
    venue = normalize_venue(entry.get("venue") or "")
    if section == "Conference Papers" and "Proceedings" not in venue and "Journal" in venue:
        return "article"
    return SECTION_TYPE[section]


def bib_key(entry: dict, used: set[str]) -> str:
    authors = entry.get("authors") or ""
    first_author = authors.split(" and ")[0].split(",")[0].strip()
    first_author = re.sub(r"[^A-Za-z]", "", first_author.split()[-1] if first_author else "anon")
    year = resolve_year(entry) or entry.get("year") or "0000"
    title_word = slugify(resolve_title(entry))[:12]
    base = f"{first_author.lower()}{year}{title_word}"
    key = base
    n = 2
    while key in used:
        key = f"{base}{n}"
        n += 1
    used.add(key)
    return key


def escape_bib(value: str) -> str:
    return value.replace("{", "\\{").replace("}", "\\}")


def infer_abbr(venue: str) -> str | None:
    for pattern, abbr in ABBR_PATTERNS:
        if re.search(pattern, venue, re.I):
            return abbr
    return None


def local_pdf_path(pdf_url: str | None, section: str) -> str | None:
    if not pdf_url:
        return None
    filename = pdf_url.rstrip("/").split("/")[-1]
    folder = {
        "Journal Papers": "journals",
        "Conference Papers": "conferences",
        "Dissertations": "dissertations",
        "Tutorials": "tutorials",
        "Book Chapter": "books",
        "Book": "books",
        "Workshop Presentations": "workshops",
        "Conference Presenter": "presentations",
        "Technical Industrial Presentations": "presentations",
    }.get(section, "misc")
    return f"{folder}/{filename}"


def should_select(entry: dict) -> bool:
    year = resolve_year(entry) or 0
    title = resolve_title(entry).lower()
    if year in SELECTED_YEARS and "savidis" in (entry.get("authors") or "").lower():
        return True
    return any(keyword in title for keyword in SELECTED_KEYWORDS) and year >= 2015


def field_line(name: str, value: str | int | None, indent: str = "  ") -> str | None:
    if value is None or value == "":
        return None
    if isinstance(value, int):
        return f"{indent}{name} = {{{value}}},"
    return f'{indent}{name} = {{{escape_bib(str(value))}}},'


def entry_to_bib(entry: dict, key: str) -> str:
    section = entry["section"]
    bib_type = infer_bib_type(entry)
    lines = [f"@{bib_type}{{{key},"]
    title = resolve_title(entry)
    authors = entry.get("authors") or "Savidis, Ioannis"
    venue = normalize_venue(entry.get("venue") or "")
    year = resolve_year(entry)

    if bib_type == "misc":
        title, authors, howpublished = parse_misc(entry)
        for line in [
            field_line("title", title),
            field_line("author", authors),
            field_line("howpublished", howpublished),
        ]:
            if line:
                lines.append(line)
    else:
        for line in [
            field_line("title", title),
            field_line("author", authors),
        ]:
            if line:
                lines.append(line)

        if bib_type == "article":
            lines.append(field_line("journal", extract_journal(venue)))
        elif bib_type == "inproceedings":
            lines.append(field_line("booktitle", extract_booktitle(venue, title)))
            if section == "Tutorials":
                lines.append(field_line("note", "Tutorial"))
        elif bib_type == "phdthesis":
            lines.append(field_line("school", "Drexel University"))
            lines.append(field_line("address", "Philadelphia, PA, USA"))
        elif bib_type == "book":
            lines.append(field_line("publisher", "Morgan Kaufmann Publishers"))
        elif bib_type == "incollection":
            lines.append(field_line("booktitle", extract_booktitle_for_chapter(venue)))

    if year:
        lines.append(field_line("year", year))

    abbr = infer_abbr(venue)
    if abbr:
        lines.append(field_line("abbr", abbr))

    pdf = local_pdf_path(entry.get("pdf_url"), section)
    if pdf:
        lines.append(field_line("pdf", pdf))

    if should_select(entry):
        lines.append("  selected = {true},")

    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    pubs = json.loads(PUBS_JSON.read_text())
    used: set[str] = set()
    blocks = [
        "---",
        "---",
        "",
        "@string{ieee_jssc = {IEEE Journal of Solid-State Circuits}}",
        "@string{ieee_tvlsi = {IEEE Transactions on Very Large Scale Integration Systems}}",
        "@string{isscc = {IEEE International Solid-State Circuits Conference (ISSCC)}}",
        "@string{cicc = {IEEE Custom Integrated Circuits Conference (CICC)}}",
        "@string{iscas = {IEEE International Symposium on Circuits and Systems (ISCAS)}}",
        "",
    ]

    for entry in pubs:
        key = bib_key(entry, used)
        blocks.append(entry_to_bib(entry, key))
        blocks.append("")

    OUT_BIB.write_text("\n".join(blocks) + "\n")
    print(f"Wrote {len(pubs)} entries to {OUT_BIB}")


if __name__ == "__main__":
    main()
