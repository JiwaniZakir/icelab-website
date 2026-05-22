# ICE Lab Website

**Integrated Circuits & Electronics Lab** - Drexel University

[![Deploy site](https://github.com/YOUR_ORG/icelab.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/YOUR_ORG/icelab.github.io/actions/workflows/deploy.yml)
[![CI](https://github.com/YOUR_ORG/icelab.github.io/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_ORG/icelab.github.io/actions/workflows/ci.yml)

Built with [al-folio](https://github.com/alshedivat/al-folio) and deployed automatically via GitHub Actions.

---

## Quick Reference

| Action             | How                                            |
| ------------------ | ---------------------------------------------- |
| Add a news item    | Create `_news/YYYY-MM-DD-title.md`             |
| Add a blog post    | Create `_posts/YYYY-MM-DD-title.md`            |
| Add a publication  | Add BibTeX entry to `_bibliography/papers.bib` |
| Add a project      | Create `_projects/name.md`                     |
| Update site config | Edit `_config.yml`                             |
| Edit team info     | Edit files in `_pages/` and `_data/`           |

**All changes auto-deploy when merged to `main`.**

## Local Development

```bash
# Using Docker (recommended)
docker compose pull
docker compose up
# Visit http://localhost:8080

# Or native Ruby
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

## Repository Structure

```
.
├── _bibliography/     # BibTeX publications
│   └── papers.bib
├── _data/             # YAML data files (CV, socials, repos)
├── _includes/         # Reusable HTML/Liquid components
├── _layouts/          # Page templates
├── _news/             # News items (auto-display on homepage)
├── _pages/            # Static pages (about, publications, etc.)
├── _posts/            # Blog posts
├── _projects/         # Project pages
├── _sass/             # SCSS stylesheets
├── assets/            # Images, PDFs, JS, CSS
├── _config.yml        # Site configuration
└── .github/
    ├── workflows/     # CI/CD automation
    ├── ISSUE_TEMPLATE/
    ├── PULL_REQUEST_TEMPLATE.md
    └── CODEOWNERS
```

## CI/CD Pipeline

| Workflow          | Trigger           | Purpose                                                  |
| ----------------- | ----------------- | -------------------------------------------------------- |
| **Deploy**        | Push to `main`    | Build & deploy to GitHub Pages                           |
| **CI**            | Pull requests     | Build check, link check, format check, BibTeX validation |
| **Preview**       | Pull requests     | Build preview artifact for review                        |
| **Citations**     | Mon & Thu 6am UTC | Auto-update Google Scholar citation counts               |
| **Accessibility** | After deploy      | Axe + Lighthouse audits                                  |
| **Stale**         | Weekly Sunday     | Auto-close inactive issues/PRs                           |
| **Update TOCs**   | Push to `main`    | Auto-update markdown table of contents                   |
| **Render CV**     | CV file changes   | Auto-generate PDF from YAML CV                           |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

## Setup

See [SETUP.md](SETUP.md) for initial repository configuration (branch protection, secrets, etc.).

---

Powered by [Jekyll](https://jekyllrb.com/) with the [al-folio](https://github.com/alshedivat/al-folio) theme. Hosted on [GitHub Pages](https://pages.github.com/).
