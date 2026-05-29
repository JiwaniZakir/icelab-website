# Adding Content to the ICE Lab Website

This guide is for lab members who want to add news, team profiles, projects, or publications **without writing code**. Changes go live automatically after a pull request is merged to `main`.

## Recommended: GitHub issue forms (no JSON, no LLM)

1. Open **[New Issue](https://github.com/JiwaniZakir/icelab-website/issues/new/choose)** on the repo.
2. Choose the right template:
   - **Add News Post** — optional homepage line + **full blog article** (use when the story needs its own page)
   - **Add News Brief** — homepage / news page only (no blog page)
   - **Add Publication** — BibTeX + publications list
   - **Add Team Member** — team profile
   - **Add Research Project** — project page
3. Fill in the form fields and submit.
4. A bot comments with a **plan preview**, then opens a **draft PR**.
5. A maintainer reviews CI, marks the PR ready, and merges → site deploys (~2 minutes).

**Edit the issue** to regenerate the PR if you need to fix something.

### Attachments (photos, PDFs)

Comment on your issue with the file, or note that a maintainer will add it in the PR branch. Publication PDFs go under `assets/pdf/`; team photos under `assets/img/team/`.

---

## Alternative: Inbox JSON drop (maintainers)

Push a validated JSON file to `content-intake/inbox/` on `main`:

```bash
python3 bin/content/intake.py content-intake/examples/pilot-news.json
cp content-intake/examples/pilot-news.json content-intake/inbox/my-news.json
git add content-intake/inbox/my-news.json && git commit -m "content: submit news" && git push
```

See [content-intake/inbox/README.md](content-intake/inbox/README.md).

---

## Advanced: raw JSON issue

Use **Add Content (Advanced JSON)** if you already have intake JSON. Examples: [content-intake/examples/](content-intake/examples/). Schemas: [content-schemas/](content-schemas/).

---

## Maintainer CLI (local)

Full pipeline from a validated intake file:

```bash
INTAKE=content-intake/examples/pilot-news.json
python3 bin/content/cli.py submit $INTAKE --force --skip-build
```

Staged workflow with explicit approvals (optional):

```bash
THREAD=my-submission-001
INTAKE=content-intake/pending/$THREAD/intake.json
python3 bin/content/cli.py plan $INTAKE --thread $THREAD --write
python3 bin/content/cli.py approve plan $THREAD
python3 bin/content/cli.py generate $INTAKE
python3 bin/content/cli.py validate --skip-build
python3 bin/content/cli.py approve pr $THREAD
python3 bin/content/cli.py publish $INTAKE
```

---

## How the site is organized

| What you see on the site | Where the content lives |
| ------------------------ | ----------------------- |
| Homepage mission & PI info | `_pages/about.md` |
| Research overview | `_pages/research.md` |
| Project cards | `_projects/*.md` |
| Team page | `_team/*.md` |
| Homepage & **News** (`/news/`) | `_news/` briefs + `_posts/` with `inline: true` (homepage table) |
| **Blog archive** (`/blog/`) | Full articles only — `_posts/` without `inline: true` still appear here; use **News Brief** or omit `inline` when you do not want a homepage line |
| Homepage featured slider | `_data/featured_slides.yml` |
| Publications list | `_bibliography/papers.bib` (grouped on `/publications/` by `ice_type`) |
| PDF reprints | `assets/pdf/` |
| Photos | `assets/img/team/`, `assets/img/research/`, `assets/img/projects/` |

**Publication PDF paths:** set `pdf_file` relative to `assets/pdf/` (e.g. `conferences/MyPaper_ISCAS_2026.pdf`), not `assets/pdf/conferences/...`.

---

## Review process

1. Submit via issue form (or inbox JSON)
2. Bot opens **draft PR** → CI runs (build, BibTeX, content validation)
3. Maintainer reviews diff + CI
4. Merge to `main` → deploys to https://jiwanizakir.github.io/icelab-website/

See [CONTRIBUTING.md](CONTRIBUTING.md) for developer setup.

---

## Rollback after a bad merge

See [content-snapshots/ROLLBACK.md](content-snapshots/ROLLBACK.md). Each deploy creates a `site-snapshot/*` git tag in [content-snapshots/manifest.json](content-snapshots/manifest.json).

### Maintainer review checklist

- [ ] CI passes (Build, YAML, BibTeX, Content Validation)
- [ ] Download **site-build** artifact and spot-check pages
- [ ] Mark draft PR ready and merge to `main`
- [ ] After deploy: `python3 bin/content/verify_live.py --intake ...`

---

## Intake schemas

| Type | Schema file |
|------|-------------|
| News post (blog + optional homepage) | `content-schemas/news_post.json` |
| Brief homepage note | `content-schemas/news_brief.json` |
| Publication | `content-schemas/publication.json` |
| Team member | `content-schemas/team_member.json` |
| Project | `content-schemas/project.json` |

---

## Optional: Chat agent (legacy)

A Hermes + Google Chat agent was explored for conversational intake. It is **not required** — the GitHub workflow above is the supported path. See [deploy/akash/README.md](deploy/akash/README.md) and [skills/ice-website-content/SKILL.md](skills/ice-website-content/SKILL.md) if you want to experiment.
