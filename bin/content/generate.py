#!/usr/bin/env python3
"""Generate repo files from validated content intake JSON."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

from common import (
    INTAKE_DIR,
    ROOT,
    blog_url,
    make_bib_key,
    normalize_pdf_bib_path,
    pdf_disk_path,
    render_template,
    slugify,
)
from pending import plan_is_approved, resolve_pending_from_intake, set_status
from intake import validate_intake


def enforce_plan_approval(intake_path: Path, dry_run: bool, force: bool) -> None:
    if dry_run or force:
        return
    pending = resolve_pending_from_intake(intake_path)
    if pending is None:
        raise ValueError(
            "Generate requires pending workflow. Save intake under content-intake/pending/{thread}/ "
            "or pass --force (maintainer only)."
        )
    if not plan_is_approved(pending):
        raise ValueError(
            f"Plan not approved for {pending.name}. User must reply APPROVE PLAN; "
            f"run: python3 bin/content/approve.py plan {pending.name}"
        )


def escape_bib(value: str) -> str:
    return value.replace("{", "\\{").replace("}", "\\}")


def format_authors_bib(authors: list[str]) -> str:
    return " and ".join(escape_bib(a.strip()) for a in authors)


def infer_ice_type(entry_type: str, data: dict[str, Any]) -> str:
    note = str(data.get("note", ""))
    howpublished = str(data.get("howpublished", "")).lower()
    if "tutorial" in note.lower():
        return "tutorials"
    mapping = {
        "book": "book",
        "incollection": "book_chapter",
        "phdthesis": "dissertations",
        "article": "journal_papers",
        "inproceedings": "conference_papers",
    }
    if entry_type in mapping:
        return mapping[entry_type]
    if entry_type == "misc":
        if any(x in howpublished for x in ("to qualcomm", "to samsung", "to kodak", "cisco", "award number")):
            return "technical_industrial"
        if any(x in howpublished for x in ("technology showcase", "lincoln laboratory", "best paper award contest")):
            return "workshop_presentations"
        if howpublished.startswith("at the") or " at the " in howpublished:
            return "conference_presenter"
        return "workshop_presentations"
    return "conference_papers"


def build_bib_entry(data: dict[str, Any]) -> tuple[str, str]:
    key = data.get("bib_key") or make_bib_key(data["authors"], data["year"], data["title"])
    lines = [f"@{data['entry_type']}{{{key},"]
    lines.append(f"  title = {{{escape_bib(data['title'])}}},")
    lines.append(f"  author = {{{format_authors_bib(data['authors'])}}},")

    entry_type = data["entry_type"]
    venue = data.get("venue", "")
    if entry_type == "article":
        lines.append(f"  journal = {{{escape_bib(venue)}}},")
    elif entry_type == "inproceedings":
        lines.append(f"  booktitle = {{{escape_bib(venue)}}},")
    elif entry_type == "incollection":
        lines.append(f"  booktitle = {{{escape_bib(venue)}}},")
    elif entry_type == "phdthesis":
        lines.append("  school = {Drexel University},")
        lines.append("  address = {Philadelphia, PA, USA},")

    lines.append(f"  year = {{{data['year']}}},")
    if data.get("abbr"):
        lines.append(f"  abbr = {{{data['abbr']}}},")
    if data.get("pdf_file"):
        lines.append(f"  pdf = {{{normalize_pdf_bib_path(data['pdf_file'])}}},")
    if data.get("selected"):
        lines.append("  selected = {true},")
    if data.get("note"):
        lines.append(f"  note = {{{escape_bib(str(data['note']))}}},")

    ice_type = data.get("ice_type") or infer_ice_type(entry_type, data)
    lines.append(f"  ice_type = {{{ice_type}}},")

    if lines[-1].endswith(","):
        lines[-1] = lines[-1][:-1]
    lines.append("}")
    return key, "\n".join(lines) + "\n"


def append_featured_slide(data: dict[str, Any], date: str, slug: str) -> None:
    slide = data.get("featured_slide")
    if not slide:
        return
    path = ROOT / "_data" / "featured_slides.yml"
    block = (
        f"\n- image: {slide['image']}\n"
        f"  title: {slide['title']}\n"
        f"  caption: >\n"
        f"    {slide.get('caption', slide['title'])}\n"
        f"  link: {slide.get('link') or blog_url(date, slug)}\n"
    )
    path.write_text(path.read_text().rstrip() + block)


def generate(data: dict[str, Any], dry_run: bool = False) -> dict[str, Any]:
    data = validate_intake(data)
    content_type = data["type"]
    created: list[str] = []
    meta: dict[str, Any] = {"type": content_type, "files": [], "urls": []}

    if content_type == "news_post":
        date, slug = data["date"], data["slug"]
        out = ROOT / "_posts" / f"{date}-{slug}.md"
        inline_block = "inline: true\n" if data["show_on_homepage"] else ""
        tags = ", ".join(data["tags"])
        body = render_template(
            "post.md.tpl",
            title=data["title"],
            date=date,
            inline_block=inline_block,
            description=data["description"],
            tags=tags,
            body_markdown=data["body_markdown"],
        )
        if not dry_run:
            out.write_text(body)
            append_featured_slide(data, date, slug)
        created.append(str(out.relative_to(ROOT)))
        meta["urls"].append(blog_url(date, slug))

    elif content_type == "news_brief":
        date, slug = data["date"], data["slug"]
        out = ROOT / "_news" / f"{date}-{slug}.md"
        body = render_template(
            "news_brief.md.tpl",
            date=date,
            body_markdown=data["body_markdown"],
        )
        if not dry_run:
            out.write_text(body)
        created.append(str(out.relative_to(ROOT)))

    elif content_type == "publication":
        bib_path = ROOT / "_bibliography" / "papers.bib"
        key, entry = build_bib_entry(data)
        if not dry_run:
            bib_path.write_text(bib_path.read_text().rstrip() + "\n\n" + entry)
            if data.get("pdf_source") and data.get("pdf_file"):
                dest = pdf_disk_path(data["pdf_file"])
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(data["pdf_source"], dest)
        created.append("_bibliography/papers.bib")
        if data.get("pdf_file"):
            created.append(f"assets/pdf/{normalize_pdf_bib_path(data['pdf_file'])}")
        meta["bib_key"] = key
        meta["urls"].append("/publications/")

    elif content_type == "team_member":
        out = ROOT / "_team" / f"{data['slug']}.md"
        body = render_template(
            "team.md.tpl",
            name=data["name"],
            role=data["role"],
            email=data["email"],
            photo_path=data["photo_path"],
            importance=data["importance"],
            category=data["category"],
            bio_markdown=data["bio_markdown"],
        )
        if not dry_run:
            out.write_text(body)
            if data.get("photo_source"):
                dest = ROOT / data["photo_path"]
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(data["photo_source"], dest)
        created.extend([str(out.relative_to(ROOT)), data["photo_path"]])
        meta["urls"].append("/team/")

    elif content_type == "project":
        out = ROOT / "_projects" / f"{data['slug']}.md"
        img_line = f"img: {data['image']}\n" if data.get("image") else ""
        body = render_template(
            "project.md.tpl",
            title=data["title"],
            description=data["description"],
            img_line=img_line,
            importance=data["importance"],
            category=data["category"],
            body_markdown=data["body_markdown"],
        )
        if not dry_run:
            out.write_text(body)
        created.append(str(out.relative_to(ROOT)))
        meta["urls"].append("/projects/")

    meta["files"] = created
    return meta


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate site files from intake JSON")
    parser.add_argument("intake_file", type=Path, nargs="?", help="Intake JSON path")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--force", action="store_true", help="Skip plan approval gate (maintainer)")
    args = parser.parse_args()

    intake_path = args.intake_file
    if intake_path is None:
        candidates = sorted(INTAKE_DIR.glob("pending/*/intake.json"))
        if not candidates:
            candidates = sorted(INTAKE_DIR.glob("*.json"))
        if not candidates:
            print("No intake file specified and content-intake/ is empty.", file=sys.stderr)
            return 1
        intake_path = candidates[-1]

    try:
        enforce_plan_approval(intake_path, args.dry_run, args.force)
    except ValueError as exc:
        print(f"Generate blocked: {exc}", file=sys.stderr)
        return 1

    data = json.loads(intake_path.read_text())
    try:
        meta = generate(data, dry_run=args.dry_run)
        if not args.dry_run:
            pending = resolve_pending_from_intake(intake_path)
            if pending:
                set_status(pending.name, "await_pr_approval")
    except (ValueError, OSError) as exc:
        print(f"Generate failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(meta, indent=2))
    if args.dry_run:
        print("Dry run — no files written.")
    else:
        print("Generated files successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
