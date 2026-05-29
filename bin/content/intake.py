#!/usr/bin/env python3
"""Load and validate content intake JSON against schemas."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from common import DATE_RE, SLUG_RE, load_schema, slugify

CONTENT_TYPES = ("news_post", "news_brief", "publication", "team_member", "project")


def _require(data: dict[str, Any], key: str, typ: type | tuple[type, ...]) -> Any:
    if key not in data or data[key] in (None, ""):
        raise ValueError(f"Missing required field: {key}")
    val = data[key]
    if not isinstance(val, typ):
        raise ValueError(f"Field {key} must be {typ}, got {type(val).__name__}")
    return val


def _optional_str(data: dict[str, Any], key: str, default: str = "") -> str:
    val = data.get(key, default)
    return str(val).strip() if val is not None else default


def validate_intake(data: dict[str, Any]) -> dict[str, Any]:
    content_type = _require(data, "type", str)
    if content_type not in CONTENT_TYPES:
        raise ValueError(f"type must be one of {CONTENT_TYPES}")

    load_schema(content_type)  # ensure schema file exists
    normalized = dict(data)
    normalized["type"] = content_type

    if content_type == "news_post":
        normalized["date"] = _require(data, "date", str)
        normalized["title"] = _require(data, "title", str)
        normalized["body_markdown"] = _require(data, "body_markdown", str)
        if not DATE_RE.match(normalized["date"]):
            raise ValueError("date must be YYYY-MM-DD")
        slug = _optional_str(data, "slug") or slugify(normalized["title"])
        if not SLUG_RE.match(slug):
            raise ValueError(f"invalid slug: {slug}")
        normalized["slug"] = slug
        normalized["show_on_homepage"] = bool(data.get("show_on_homepage", True))
        normalized["tags"] = data.get("tags") or ["news"]
        normalized["description"] = _optional_str(data, "description") or normalized["title"][:160]

    elif content_type == "news_brief":
        normalized["date"] = _require(data, "date", str)
        normalized["body_markdown"] = _require(data, "body_markdown", str)
        if not DATE_RE.match(normalized["date"]):
            raise ValueError("date must be YYYY-MM-DD")
        slug = _optional_str(data, "slug") or slugify(normalized["body_markdown"][:60])
        normalized["slug"] = slug

    elif content_type == "publication":
        normalized["entry_type"] = _require(data, "entry_type", str)
        normalized["title"] = _require(data, "title", str)
        normalized["authors"] = _require(data, "authors", list)
        normalized["year"] = int(_require(data, "year", int))
        if normalized["entry_type"] not in (
            "article",
            "inproceedings",
            "phdthesis",
            "book",
            "incollection",
            "misc",
        ):
            raise ValueError("invalid entry_type")
        if normalized["entry_type"] in ("article", "inproceedings", "incollection"):
            normalized["venue"] = _require(data, "venue", str)
        normalized["abbr"] = _optional_str(data, "abbr")
        normalized["selected"] = bool(data.get("selected", False))
        if data.get("pdf_file"):
            normalized["pdf_file"] = normalize_pdf_path(str(data["pdf_file"]))
        else:
            normalized["pdf_file"] = ""
        normalized["bib_key"] = _optional_str(data, "bib_key")

    elif content_type == "team_member":
        normalized["slug"] = _require(data, "slug", str)
        normalized["name"] = _require(data, "name", str)
        normalized["role"] = _require(data, "role", str)
        normalized["email"] = _require(data, "email", str)
        normalized["category"] = _require(data, "category", str)
        normalized["bio_markdown"] = _require(data, "bio_markdown", str)
        if normalized["category"] not in ("faculty", "phd", "masters", "alumni"):
            raise ValueError("category must be faculty, phd, masters, or alumni")
        normalized["importance"] = int(data.get("importance", 5))
        normalized["photo_path"] = _require(data, "photo_path", str)

    elif content_type == "project":
        normalized["slug"] = _require(data, "slug", str)
        normalized["title"] = _require(data, "title", str)
        normalized["description"] = _require(data, "description", str)
        normalized["body_markdown"] = _require(data, "body_markdown", str)
        normalized["category"] = _require(data, "category", str)
        if normalized["category"] not in ("active", "completed"):
            raise ValueError("category must be active or completed")
        normalized["importance"] = int(data.get("importance", 5))
        normalized["image"] = _optional_str(data, "image")

    return normalized


def normalize_pdf_path(path: str) -> str:
    path = path.strip().lstrip("/")
    if path.startswith("assets/pdf/"):
        return path[len("assets/pdf/") :]
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate content intake JSON")
    parser.add_argument("intake_file", type=Path, help="Path to intake JSON")
    parser.add_argument("--write-normalized", type=Path, help="Write normalized JSON")
    args = parser.parse_args()

    data = json.loads(args.intake_file.read_text())
    try:
        normalized = validate_intake(data)
    except ValueError as exc:
        print(f"Validation error: {exc}", file=sys.stderr)
        return 1

    if args.write_normalized:
        args.write_normalized.write_text(json.dumps(normalized, indent=2) + "\n")
        print(f"Wrote normalized intake to {args.write_normalized}")
    else:
        print(json.dumps(normalized, indent=2))
    print("Intake valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
