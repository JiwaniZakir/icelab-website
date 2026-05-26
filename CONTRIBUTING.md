# Contributing to the ICE Lab Website

Thank you for contributing to the ICE Lab website! This guide will help you
make changes smoothly.

For a lab-member-friendly guide (no coding background required), see [CONTENT.md](CONTENT.md).

## Quick Start

### Adding Content (No Coding Required)

| Content Type     | Where to Add               | File Format           |
| ---------------- | -------------------------- | --------------------- |
| News item        | `_news/`                   | `YYYY-MM-DD-title.md` |
| Blog post        | `_posts/`                  | `YYYY-MM-DD-title.md` |
| Project          | `_projects/`               | `name.md`             |
| Team member      | `_team/`                   | `slug.md` + photo in `assets/img/team/` |
| Publication      | `_bibliography/papers.bib` | BibTeX entry + PDF in `assets/pdf/` |
| Static page      | `_pages/`                  | Markdown with `nav: true` |

### Workflow

1. **Create a branch** from `main`:

   ```bash
   git checkout -b content/your-change-name
   ```

2. **Make your changes** (add/edit markdown files)

3. **Test locally** (recommended):

   ```bash
   docker compose pull && docker compose up
   # Visit http://localhost:8080
   ```

4. **Commit and push**:

   ```bash
   git add .
   git commit -m "content: add news about new paper"
   git push origin content/your-change-name
   ```

5. **Open a Pull Request** on GitHub
   - The CI will automatically:
     - Build the site and check for errors
     - Validate your markdown formatting
     - Check for broken links
     - Validate BibTeX syntax
     - Generate a preview artifact

6. **Get a review** and merge!

## Commit Message Convention

Use prefixes to categorize your commits:

| Prefix     | Use For                                            |
| ---------- | -------------------------------------------------- |
| `content:` | Adding/editing news, posts, projects, publications |
| `feat:`    | New features or pages                              |
| `fix:`     | Bug fixes                                          |
| `style:`   | CSS/design changes                                 |
| `chore:`   | Config, dependencies, CI/CD                        |
| `docs:`    | Documentation updates                              |

Examples:

```
content: add ISCAS 2026 paper to publications
content: add Jane Doe as new PhD student
feat: add research areas page
fix: broken image on projects page
style: update theme color to Drexel blue
chore: update Ruby dependencies
```

## Adding a News Item

Create a file in `_news/` with this template:

```markdown
---
layout: post
date: 2026-05-22
inline: true
related_posts: false
---

Your news text here. You can use **bold**, _italic_, and [links](https://example.com).
```

## Adding a Publication

Add a BibTeX entry to `_bibliography/papers.bib`:

```bibtex
@inproceedings{AuthorYear,
  title     = {Your Paper Title},
  author    = {Last, First and Last2, First2},
  booktitle = {Conference Name},
  year      = {2026},
  abbr      = {ISCAS},
  selected  = {true},
  pdf       = {assets/pdf/conferences/your-paper.pdf},
}
```

Upload the PDF to `assets/pdf/` (subfolders: `journals/`, `conferences/`, `dissertations/`, `tutorials/`).

## Adding a Project

Create a file in `_projects/` with this template:

```markdown
---
layout: page
title: Project Name
description: A short description of the project
importance: 1
category: active
---

Your project description in markdown...
```

Use `category: active` or `category: completed`.

## Adding a Team Member

Create a file in `_team/` with this template:

```markdown
---
layout: page
title: First Last
description: Ph.D. Student | email@drexel.edu
img: assets/img/team/first-last.jpg
importance: 1
category: phd
---

Bio and research interests...
```

Categories: `faculty`, `phd`, `alumni`.

## Image conventions

- Team photos: `assets/img/team/{slug}.jpg`
- Research figures: `assets/img/research/{topic}.jpg`
- Project thumbnails: `assets/img/projects/{slug}.jpg` (optional)
- Publication PDFs: `assets/pdf/{journals,conferences,dissertations,tutorials}/`

## Maintenance scripts

- `bin/check_pdf_paths.py` — verify every `pdf = {...}` entry in `papers.bib` has a file under `assets/pdf/`

## Formatting

Before committing, format your files:

```bash
npx prettier . --write
```

## Questions?

Open an issue or reach out to the lab admin.
