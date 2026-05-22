# Deep Research Report: Static Site Generators for Research Lab Websites

## Auto-Updating from Markdown via GitHub

_Compiled 2026-05-22 for ICE Lab, Drexel University_

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Jekyll-Based Academic/Lab Themes](#1-jekyll-based-academiclab-themes)
3. [Other Static Site Generators (SSGs)](#2-other-static-site-generators)
4. [CI/CD & Auto-Deploy Pipelines](#3-cicd--auto-deploy-pipelines)
5. [CMS Connectors for Non-Technical Users](#4-cms-connectors-for-non-technical-users)
6. [Notable Open-Source Lab Website Repos](#5-notable-open-source-lab-website-repos)
7. [Automation Patterns](#6-automation-patterns)
8. [Recommendations for ICE Lab](#7-recommendations-for-ice-lab)

---

## Executive Summary

The goal is a **static website for a research lab** that **automatically rebuilds and deploys when `.md` files are pushed to GitHub**. This is a solved problem with multiple mature approaches. The dominant ecosystem is **Jekyll + GitHub Pages** (native zero-config auto-deploy), but Hugo, Eleventy, and Astro are strong alternatives when paired with GitHub Actions.

**Top 3 recommendations (detailed below):**

| Rank | Solution                                 | Why                                                                                                        |
| ---- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 🥇   | **al-folio** (Jekyll)                    | 15.6k stars, purpose-built for academics, BibTeX integration, auto-deploy, Google Scholar citation updates |
| 🥈   | **Greene Lab Website Template** (Jekyll) | 549 stars, purpose-built for _labs_ (not individuals), auto-citations via Manubot/DOI, team pages          |
| 🥉   | **academicpages** (Jekyll)               | 17k stars, simple fork-and-go, great for getting started fast                                              |

---

## 1. Jekyll-Based Academic/Lab Themes

### 🏆 al-folio -- The Gold Standard

- **Repo:** [alshedivat/al-folio](https://github.com/alshedivat/al-folio)
- **Stars:** ⭐ 15,643 | **Forks:** 13,029
- **License:** MIT
- **Demo:** https://alshedivat.github.io/al-folio/
- **Last updated:** Active daily (May 2026)

**Key Features:**

- **Publications from BibTeX** -- drop a `.bib` file in `_bibliography/papers.bib`, pages auto-generate
- **Google Scholar citation auto-update** -- GitHub Actions cron job (Mon/Wed/Fri) fetches citation counts
- **Team/people pages** via markdown
- **Blog posts** in `_posts/` as `.md` files
- **Projects** in `_projects/` as `.md` files
- **News** in `_news/` as `.md` files
- **CV** from YAML (`_data/cv.yml`) or JSON Resume format, with automatic PDF generation via RenderCV
- **Collections** -- extensible (teachings, books, etc.)
- **Docker support** for local development
- **GitHub Actions deploy workflow** included out of the box
- **GitHub Copilot agent** built-in for customization help
- **Responsive**, dark mode, math (MathJax/KaTeX), code highlighting, Jupyter notebook support

**Content organization:**

```
_bibliography/papers.bib    # Publications (BibTeX)
_data/cv.yml                # CV data
_data/coauthors.yml         # Co-author info
_data/repositories.yml      # GitHub repos to showcase
_news/                      # News items (.md files)
_posts/                     # Blog posts (.md files)
_projects/                  # Project pages (.md files)
_pages/                     # Static pages (.md files)
```

**Pros:**

- Largest community, most mature, extremely well-documented
- BibTeX is the native academic format -- no conversion needed
- Auto Google Scholar citation updates
- Used by hundreds of real academics and ~10 known labs
- No coding experience needed -- just edit config + add markdown

**Cons:**

- Designed for individual academics first, labs second (but works well for both)
- Ruby/Jekyll can be slow for very large sites (500+ pages)
- Jekyll plugin ecosystem is less active than Hugo/Astro

---

### academicpages

- **Repo:** [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io)
- **Stars:** ⭐ 17,022 | **Forks:** 7,005
- **Based on:** Minimal Mistakes theme
- **Demo:** https://academicpages.github.io

**Key Features:**

- Fork-and-go template (fork repo, rename, edit)
- Publications, talks, teaching, portfolio as collections
- Markdown-driven content
- Built on the rock-solid Minimal Mistakes framework

**Pros:**

- Highest star count in academic website space
- Very simple to get started (fork + edit)
- Lots of community examples

**Cons:**

- More individual-focused than lab-focused
- Less sophisticated publication management than al-folio (no BibTeX auto-parsing)
- Less actively maintained than al-folio

---

### Minimal Mistakes (as a base)

- **Repo:** [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes)
- **Stars:** ⭐ 13,504 | **Forks:** 27,293
- **License:** MIT

**Usage for Labs:** Many labs fork Minimal Mistakes directly and customize:

- HenriquesLab, MHM-Lab, DAVAR-Lab, LZ-Lab, TYW-Lab, iPCR-Lab all use this approach
- Very flexible but requires more manual setup for academic features

**Pros:** Maximum flexibility, huge ecosystem, great docs
**Cons:** No academic-specific features built in (publications, BibTeX, etc.)

---

### research-lab-website (by ericdaat)

- **Repo:** [ericdaat/research-lab-website](https://github.com/ericdaat/research-lab-website)
- **Stars:** ⭐ 63
- **Specifically built for:** Research lab groups

**Content organization:**

```
_data/news.yml              # News items
_data/publications.json     # Publications as JSON
_pages/team/_posts/         # Team member bios
_pages/research.md          # Research page
_pages/openings.md          # Open positions
```

**Pros:** Purpose-built for labs, simple structure
**Cons:** Small community, less maintained, fewer features

---

### Other Jekyll Academic Themes

| Theme                                                               | Stars    | Description                              |
| ------------------------------------------------------------------- | -------- | ---------------------------------------- |
| [minimal-light](https://github.com/yaoyao-liu/minimal-light)        | ⭐ 987   | Minimalist single-page academic homepage |
| [academic (LeNPaul)](https://github.com/LeNPaul/academic)           | ⭐ 230   | Simple academic theme                    |
| [Dumbarton](https://github.com/tcbutler320/Jekyll-Theme-Dumbarton)  | ⭐ 77    | Academic-focused with portfolio          |
| [academic-portfolio](https://github.com/ys1998/academic-portfolio)  | ⭐ 55    | Clean mobile-friendly academic theme     |
| [lab_pages (isacofflab)](https://github.com/isacofflab/lab_pages)   | ⭐ 10    | Specifically for academic lab pages      |
| [jekyll-scholar plugin](https://github.com/inukshuk/jekyll-scholar) | ⭐ 1,197 | BibTeX plugin for any Jekyll site        |

---

## 2. Other Static Site Generators

### Comparison Matrix

| SSG                 | Stars     | Language | Build Speed  | Academic Ecosystem                   | GitHub Pages Native | Markdown | Learning Curve |
| ------------------- | --------- | -------- | ------------ | ------------------------------------ | ------------------- | -------- | -------------- |
| **Jekyll**          | 50k+      | Ruby     | Slow         | ⭐⭐⭐⭐⭐ (al-folio, academicpages) | ✅ Native           | ✅       | Low            |
| **Hugo**            | 80k+      | Go       | ⚡ Very Fast | ⭐⭐⭐⭐ (HugoBlox/Wowchemy)         | ❌ (needs Actions)  | ✅       | Medium         |
| **Astro**           | ⭐ 59,484 | JS       | Fast         | ⭐⭐ (emerging)                      | ❌ (needs Actions)  | ✅       | Medium         |
| **Eleventy**        | ⭐ 19,651 | JS       | Fast         | ⭐⭐ (few themes)                    | ❌ (needs Actions)  | ✅       | Medium         |
| **Docusaurus**      | ⭐ 64,979 | React    | Fast         | ⭐⭐ (docs-oriented)                 | ❌ (needs Actions)  | ✅       | Medium-High    |
| **MkDocs Material** | ⭐ 26,777 | Python   | Fast         | ⭐⭐⭐ (docs/wiki-style)             | ❌ (needs Actions)  | ✅       | Low            |
| **Quartz**          | ⭐ 12,238 | JS       | Fast         | ⭐⭐ (knowledge base)                | ❌ (needs Actions)  | ✅       | Low            |
| **Zola**            | ⭐ 17,078 | Rust     | ⚡ Very Fast | ⭐ (few themes)                      | ❌ (needs Actions)  | ✅       | Medium         |
| **Pelican**         | ⭐ 13,302 | Python   | Medium       | ⭐⭐ (some academic)                 | ❌ (needs Actions)  | ✅       | Medium         |

### Hugo + HugoBlox (formerly Wowchemy / Hugo Academic)

- **Repo:** [HugoBlox/kit](https://github.com/HugoBlox/kit)
- **Stars:** ⭐ 9,439 | **Forks:** 2,938
- **Demo:** https://hugoblox.com

The main Hugo competitor to al-folio. Previously called "Hugo Academic" and "Wowchemy."

**Pros:**

- Blazing fast builds (Go-based)
- Rich academic features (publications, talks, courses)
- Jupyter/R Markdown support
- Tailwind CSS based, modern

**Cons:**

- Has gone through multiple rebrandings (Hugo Academic -> Wowchemy -> HugoBlox)
- Now has commercial aspects (paid features)
- More complex template system than Jekyll
- No native GitHub Pages support (needs Actions)
- Steeper learning curve for customization

### MkDocs + Material

- **Repo:** [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material)
- **Stars:** ⭐ 26,777

**Best for:** Documentation-heavy lab sites, internal wikis, research notes
**Not ideal for:** Traditional lab website with people/publications pages

### Quartz

- **Repo:** [jackyzha0/quartz](https://github.com/jackyzha0/quartz)
- **Stars:** ⭐ 12,238

**Best for:** Publishing Obsidian-style interconnected research notes
**Not ideal for:** Traditional lab homepage

### Astro

- **Repo:** [withastro/astro](https://github.com/withastro/astro)
- **Stars:** ⭐ 59,484

**Best for:** Modern, performance-first sites with component islands
**Academic ecosystem:** Still emerging; no mature lab templates yet
**Worth watching** for future -- fastest growing SSG

---

## 3. CI/CD & Auto-Deploy Pipelines

### Option A: GitHub Pages Native Jekyll (Zero Config)

The simplest approach. GitHub Pages has **built-in Jekyll support**.

**How it works:**

1. Push `.md` files to your repo
2. GitHub automatically builds Jekyll and deploys
3. No GitHub Actions config needed

**Limitations:**

- Only supports [whitelisted Jekyll plugins](https://pages.github.com/versions/)
- `jekyll-scholar` (BibTeX) is NOT whitelisted
- Limited Ruby version

### Option B: GitHub Actions (Recommended)

Full control. This is what **al-folio uses**.

**al-folio's deploy workflow** triggers on push to main when any of these change:

- `**/*.md` (any markdown file)
- `**.bib` (bibliography)
- `**.yml` (config/data)
- `**.html`, `**.liquid` (templates)
- `assets/**`, `_sass/**` (styling)

```yaml
# .github/workflows/deploy.yml (simplified from al-folio)
name: Deploy site
on:
  push:
    branches: [main]
    paths:
      - "**/*.md"
      - "**.bib"
      - "**.yml"
      - "**.html"
  workflow_dispatch: # Manual trigger

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: ruby/setup-ruby@v1
        with:
          ruby-version: "3.3.5"
          bundler-cache: true
      - name: Build site
        run: bundle exec jekyll build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./_site
```

### Option C: Netlify

- Auto-deploys on git push
- Supports any SSG
- Free tier available
- Deploy previews on PRs
- Form handling, functions

### Option D: Vercel

- Similar to Netlify
- Better for JS-based SSGs (Astro, Next.js)
- Free tier available

### Option E: Cloudflare Pages

- Free, fast CDN
- Git integration
- Supports Jekyll, Hugo, etc.

### Comparison

| Platform               | Jekyll Native | Custom Plugins | PR Previews | Free Tier | Custom Domain |
| ---------------------- | :-----------: | :------------: | :---------: | :-------: | :-----------: |
| GitHub Pages (native)  |      ✅       |       ❌       |     ❌      |    ✅     |      ✅       |
| GitHub Pages + Actions |      ✅       |       ✅       |     ✅      |    ✅     |      ✅       |
| Netlify                |      ✅       |       ✅       |     ✅      |    ✅     |      ✅       |
| Vercel                 |      ⚠️       |       ✅       |     ✅      |    ✅     |      ✅       |
| Cloudflare Pages       |      ✅       |       ✅       |     ✅      |    ✅     |      ✅       |

**Recommendation:** GitHub Pages + GitHub Actions (what al-folio uses). Keeps everything in one place, free, and you get full plugin support.

---

## 4. CMS Connectors for Non-Technical Users

These tools give lab members a visual editor to create/edit markdown content without touching Git directly.

### Decap CMS (formerly Netlify CMS)

- **Repo:** [decaporg/decap-cms](https://github.com/decaporg/decap-cms)
- **Stars:** ⭐ 19,076
- **How it works:** Adds an `/admin` route to your static site with a visual editor that commits to Git
- **Supports:** Jekyll, Hugo, any Git-based SSG
- **Auth:** GitHub OAuth, Netlify Identity
- **Pros:** Open-source, self-hosted option, mature, works with any SSG
- **Cons:** Development has slowed, UI is dated

### TinaCMS

- **Repo:** [tinacms/tinacms](https://github.com/tinacms/tinacms)
- **Stars:** ⭐ 13,357
- **How it works:** Visual editing with live preview, commits to Git
- **Best with:** Next.js, Astro, Hugo
- **Pros:** Modern UI, real-time preview, active development
- **Cons:** Primarily designed for React-based SSGs, Jekyll support is limited

### Prose.io

- **Repo:** [prose/prose](https://github.com/prose/prose)
- **Stars:** ⭐ 4,778
- **How it works:** Web-based editor for GitHub repos, specifically designed for Jekyll
- **Pros:** Dead simple, just edit markdown in browser, commits to GitHub
- **Cons:** Older project, minimal features, no live preview

### CloudCannon

- **Website:** https://cloudcannon.com
- **How it works:** Commercial CMS with first-class Jekyll support
- **Pros:** Best-in-class Jekyll visual editing, component-based editing
- **Cons:** Paid product (free for 1 user)

### GitHub Web Editor

- **How:** Just click the pencil icon on any file in GitHub, or press `.` to open VS Code in browser
- **Pros:** Zero setup, everyone with repo access can edit
- **Cons:** No preview, no WYSIWYG, raw markdown only

### Recommendation for Lab Members

| User Type             | Best Tool                       |
| --------------------- | ------------------------------- |
| Technical (knows Git) | GitHub web editor or VS Code    |
| Semi-technical        | Prose.io or Decap CMS           |
| Non-technical         | CloudCannon (paid) or Decap CMS |

---

## 5. Notable Open-Source Lab Website Repos

### Purpose-Built Lab Templates

| Project                                                                             | Stars     | SSG    | Key Feature                                                        |
| ----------------------------------------------------------------------------------- | --------- | ------ | ------------------------------------------------------------------ |
| [greenelab/lab-website-template](https://github.com/greenelab/lab-website-template) | ⭐ 549    | Jekyll | Auto-citations from DOI via Manubot, team pages, ORCID integration |
| [ericdaat/research-lab-website](https://github.com/ericdaat/research-lab-website)   | ⭐ 63     | Jekyll | Clean lab template with news, publications, team                   |
| [alshedivat/al-folio](https://github.com/alshedivat/al-folio)                       | ⭐ 15,643 | Jekyll | BibTeX, Scholar citations, used by ~10 known labs                  |
| [isacofflab/lab_pages](https://github.com/isacofflab/lab_pages)                     | ⭐ 10     | Jekyll | Minimal lab page theme                                             |

### Real Lab Websites Using al-folio

- [Hay Lab, Caltech](https://www.haylab.caltech.edu/)
- [SJK Lab](https://sjkimlab.github.io/)
- [Decision Lab, UCSF](https://decisionlab.ucsf.edu/)
- [Programming Group](https://programming-group.com/)
- [Sailing Lab](https://sailing-lab.github.io/)
- [NUESL](https://www.nuesl.org/)
- [Cranmer Lab](https://github.com/cranmer/cranmer-lab)

### Real Lab Websites Using Minimal Mistakes

- HenriquesLab, MHM-Lab, DAVAR-Lab, iPCR-Lab, and many others

### Real Lab Websites Using Greene Lab Template

- [LINMAR Lab](https://github.com/LINMAR-Lab/linmarlab-website)
- [Biardi Lab](https://github.com/jbiardi/lab-website-template)
- Multiple others listed in their docs

---

## 6. Automation Patterns

### Pattern 1: Auto-Generate Publications from BibTeX (al-folio)

```
_bibliography/papers.bib  -->  jekyll-scholar plugin  -->  /publications/ page
```

- Add entries to `papers.bib`
- Push to GitHub
- Site rebuilds with new publications automatically
- Supports author highlighting, PDF links, abstracts, BibTeX copy

### Pattern 2: Auto-Generate Citations from DOIs (Greene Lab Template)

```
_data/sources.yaml  -->  Manubot cite.py  -->  _data/citations.yaml  -->  site
```

- Add a DOI, PMID, or ORCID to `sources.yaml`
- Python script auto-fetches full metadata
- Generates rich citation cards

### Pattern 3: Auto-Update Google Scholar Citations (al-folio)

```yaml
# .github/workflows/update-citations.yml
on:
  schedule:
    - cron: "0 0 * * 1" # Every Monday
    - cron: "0 0 * * 3" # Every Wednesday
    - cron: "0 0 * * 5" # Every Friday
```

- Cron job runs Python script
- Scrapes Google Scholar for citation counts
- Updates `_data/citations.yml`
- Auto-commits if changed
- Triggers site rebuild

### Pattern 4: Team Members via Markdown

```markdown
# \_team/jane-doe.md

---

layout: member
name: Jane Doe
role: PhD Student
image: /assets/img/jane.jpg
email: jane@drexel.edu
scholar: XXXXXXXX
github: janedoe

---

Jane's bio goes here in markdown...
```

### Pattern 5: News Items as Markdown

```markdown
# \_news/2026-05-22-new-paper.md

---

layout: post
title: "New paper accepted at NeurIPS 2026!"
date: 2026-05-22
inline: true

---

Our paper on X was accepted! [Read more](/publications/)
```

### Pattern 6: Markdown Validation CI

```yaml
# .github/workflows/validate.yml
name: Validate Content
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint Markdown
        uses: DavidAnson/markdownlint-cli2-action@v14
      - name: Check links
        uses: lycheeverse/lychee-action@v1
```

### Pattern 7: PR Preview Deploys

al-folio's workflow builds the site on PRs too, allowing review before merge. Netlify and Vercel also provide this natively.

---

## 7. Recommendations for ICE Lab

### Primary Recommendation: al-folio

**Why al-folio is the best fit:**

1. **Zero-config auto-deploy** -- push markdown, site updates automatically
2. **BibTeX-native publications** -- your lab already uses BibTeX
3. **Google Scholar auto-citation updates** -- citation counts update automatically 3x/week
4. **Battle-tested** -- 15.6k stars, 13k forks, used by labs at Caltech, UCSF, CMU
5. **Lab-ready sections** -- news, publications, projects, people, blog
6. **No coding needed** -- just edit YAML config + add markdown files
7. **GitHub Actions deploy included** -- works out of the box
8. **Active development** -- updated daily, 4 maintainers
9. **Great docs** -- INSTALL.md, CUSTOMIZE.md, FAQ.md, CONTRIBUTING.md

### Getting Started (5 Steps)

```bash
# 1. Use the template
# Go to https://github.com/alshedivat/al-folio and click "Use this template"
# Name it: icelab.github.io (or your preferred name)

# 2. Clone locally
git clone https://github.com/YOUR_ORG/icelab.github.io
cd icelab.github.io

# 3. Edit _config.yml with lab info
# 4. Add publications to _bibliography/papers.bib
# 5. Add team members, news, projects as .md files

# Push -- site auto-deploys!
git add . && git commit -m "Initial lab website" && git push
```

### Alternative: Greene Lab Template

Choose this if you want:

- **DOI/ORCID-based auto-citation** (instead of BibTeX)
- A template designed specifically for _lab groups_ (not individuals)
- Manubot integration

### What NOT to use

- **Hugo Academic / HugoBlox** -- multiple rebrandings, commercial pivot, more complex
- **Docusaurus** -- designed for docs, not lab websites
- **MkDocs** -- designed for docs/wikis
- **Quartz** -- designed for knowledge bases, not lab homepages

### Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│                  GitHub Repo                     │
│                                                  │
│  _bibliography/papers.bib  (publications)        │
│  _news/*.md                (news items)          │
│  _posts/*.md               (blog posts)          │
│  _projects/*.md            (project pages)       │
│  _pages/*.md               (static pages)        │
│  _data/cv.yml              (CV data)             │
│  _config.yml               (site config)         │
│                                                  │
│  .github/workflows/                              │
│    deploy.yml              (auto-build+deploy)   │
│    update-citations.yml    (Scholar cron job)     │
└──────────────┬──────────────────────────────────┘
               │ git push (or PR merge)
               ▼
┌──────────────────────────────────┐
│       GitHub Actions             │
│  1. Install Ruby + Jekyll        │
│  2. bundle exec jekyll build     │
│  3. Deploy to gh-pages branch    │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│       GitHub Pages               │
│  https://icelab.github.io        │
│  (or custom domain)              │
└──────────────────────────────────┘
```

### Workflow for Lab Members

```
Lab member writes content (.md file)
        │
        ├── Option A: Edit on GitHub.com (pencil icon)
        ├── Option B: Edit via Prose.io (visual editor)
        ├── Option C: Edit locally + git push
        └── Option D: Edit via Decap CMS (/admin)
        │
        ▼
   Commit to main branch
        │
        ▼
   GitHub Actions triggers
        │
        ▼
   Jekyll builds site (2-3 min)
        │
        ▼
   Site is live with new content ✅
```

---

## Appendix: All Discovered Projects

| Project              | Stars  | Type            | URL                                                      |
| -------------------- | ------ | --------------- | -------------------------------------------------------- |
| al-folio             | 15,643 | Jekyll Theme    | https://github.com/alshedivat/al-folio                   |
| academicpages        | 17,022 | Jekyll Template | https://github.com/academicpages/academicpages.github.io |
| Minimal Mistakes     | 13,504 | Jekyll Theme    | https://github.com/mmistakes/minimal-mistakes            |
| HugoBlox (Wowchemy)  | 9,439  | Hugo Theme      | https://github.com/HugoBlox/kit                          |
| Greene Lab Template  | 549    | Jekyll Template | https://github.com/greenelab/lab-website-template        |
| jekyll-scholar       | 1,197  | Jekyll Plugin   | https://github.com/inukshuk/jekyll-scholar               |
| minimal-light        | 987    | Jekyll Theme    | https://github.com/yaoyao-liu/minimal-light              |
| Decap CMS            | 19,076 | CMS             | https://github.com/decaporg/decap-cms                    |
| TinaCMS              | 13,357 | CMS             | https://github.com/tinacms/tinacms                       |
| Prose.io             | 4,778  | Editor          | https://github.com/prose/prose                           |
| Quartz               | 12,238 | SSG             | https://github.com/jackyzha0/quartz                      |
| MkDocs Material      | 26,777 | SSG Theme       | https://github.com/squidfunk/mkdocs-material             |
| Docusaurus           | 64,979 | SSG             | https://github.com/facebook/docusaurus                   |
| Astro                | 59,484 | SSG             | https://github.com/withastro/astro                       |
| Eleventy             | 19,651 | SSG             | https://github.com/11ty/eleventy                         |
| Zola                 | 17,078 | SSG             | https://github.com/getzola/zola                          |
| Pelican              | 13,302 | SSG             | https://github.com/getpelican/pelican                    |
| research-lab-website | 63     | Jekyll Template | https://github.com/ericdaat/research-lab-website         |
| jekyll-deploy-action | 365    | GitHub Action   | https://github.com/jeffreytse/jekyll-deploy-action       |
| hexo-theme-academia  | 304    | Hexo Theme      | https://github.com/PhosphorW/hexo-theme-academia         |
| academic (LeNPaul)   | 230    | Jekyll Theme    | https://github.com/LeNPaul/academic                      |

---

_This report was auto-generated by searching GitHub API, analyzing repository structures, reading READMEs, and examining CI/CD workflows of the top projects in this space._
