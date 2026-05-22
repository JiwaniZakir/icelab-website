# Contributing to the ICE Lab Website

Thank you for contributing to the ICE Lab website! This guide will help you
make changes smoothly.

## Quick Start

### Adding Content (No Coding Required)

| Content Type     | Where to Add               | File Format           |
| ---------------- | -------------------------- | --------------------- |
| News item        | `_news/`                   | `YYYY-MM-DD-title.md` |
| Blog post        | `_posts/`                  | `YYYY-MM-DD-title.md` |
| Project          | `_projects/`               | `name.md`             |
| Publication      | `_bibliography/papers.bib` | BibTeX entry          |
| Team member info | `_pages/`                  | Markdown              |

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
content: add NeurIPS 2026 paper to publications
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
  selected  = {true},
  preview   = {paper-thumbnail.png},
  pdf       = {https://arxiv.org/pdf/XXXX.XXXXX.pdf},
  abstract  = {Your abstract here.}
}
```

## Adding a Project

Create a file in `_projects/` with this template:

```markdown
---
layout: page
title: Project Name
description: A short description of the project
img: assets/img/project-thumbnail.jpg
importance: 1
category: research
---

Your project description in markdown...
```

## Formatting

Before committing, format your files:

```bash
npx prettier . --write
```

## Questions?

Open an issue or reach out to the lab admin.
