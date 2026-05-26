# Adding Content to the ICE Lab Website

This guide is for lab members who want to add news, team profiles, projects, or publications **without writing code**. Changes go live automatically after a pull request is merged to `main`.

## How the site is organized

| What you see on the site | Where the content lives |
| ------------------------ | ----------------------- |
| Homepage mission & PI info | `_pages/about.md` |
| Research overview | `_pages/research.md` |
| Project cards | `_projects/*.md` |
| Team page | `_team/*.md` |
| Homepage announcements | `_posts/` with `inline: true`, or `_news/` for brief-only items |
| Homepage featured slider | `_data/featured_slides.yml` |
| Full news archive (blog) | `_posts/YYYY-MM-DD-title.md` |
| Publications list | `_bibliography/papers.bib` |
| PDF reprints | `assets/pdf/` |
| Photos | `assets/img/team/`, `assets/img/research/`, `assets/img/projects/` |

**Homepage vs blog**

- `_posts/` — full archive on the [blog](/icelab-website/blog/). Add `inline: true` to also show the item in the homepage news table.
- `_news/` — optional for short announcements that do not need a full blog entry (e.g. recruiting blurbs).

---

## Step-by-step workflows

### Add a homepage announcement (and blog archive entry)

1. Create `_posts/2026-06-01-your-title.md`:

```markdown
---
layout: post
title: Paper Accepted at ISCAS 2026
date: 2026-06-01
inline: true
related_posts: false
description: Brief summary for search and previews.
tags: news
---

Full announcement text here. Include authors, venue, and links if helpful.
```

2. Open a pull request. CI will build the site and check formatting.

### Add a brief homepage-only note

Use `_news/` when you do not need a separate blog page:

```markdown
---
layout: post
date: 2026-06-01
inline: true
related_posts: false
---

**PhD openings** — We are recruiting students for Fall 2026. [Contact us]({{ '/contact/' | relative_url }}).
```

### Update the homepage featured slider

Configure slides in `_data/featured_slides.yml`:

```yaml
- image: assets/img/banners/your-banner.jpg
  title: Paper Accepted at ISCAS 2026
  caption: Our work on hardware obfuscation was accepted.
  link: /blog/2026/your-title/
```

### Add a team member

1. Save a headshot to `assets/img/team/first-last.jpg` (roughly square, ≥400×400 px).
2. Create `_team/first-last.md` with `layout: page`, bio, `img`, `importance`, and `category` (`faculty`, `phd`, or `alumni`).

### Add a research project

Create `_projects/project-slug.md` with `category: active` or `category: completed`.

### Add a publication

1. Add a BibTeX entry to `_bibliography/papers.bib`.
2. Upload the PDF under `assets/pdf/` (`journals/`, `conferences/`, etc.).
3. Set `selected = {true}` only for papers to highlight on the homepage.

---

## Review process

1. Branch → commit → pull request
2. Wait for CI (build + BibTeX validation)
3. Merge to `main` → deploys to https://jiwanizakir.github.io/icelab-website/

See [CONTRIBUTING.md](CONTRIBUTING.md) for developer setup.
