# ICE Lab Website

**Integrated Circuits & Electronics Lab** — Drexel University

Built with [al-folio](https://github.com/alshedivat/al-folio) and deployed automatically via GitHub Actions to GitHub Pages.

**Live site:** https://jiwanizakir.github.io/icelab-website/

---

## Quick Reference

| Action             | How                                            |
| ------------------ | ---------------------------------------------- |
| Add a news item    | Create `_posts/YYYY-MM-DD-title.md` (add `inline: true` for homepage) |
| Add a brief note   | Create `_news/YYYY-MM-DD-title.md`             |
| Add a publication  | Add BibTeX entry to `_bibliography/papers.bib` |
| Add a project      | Create `_projects/name.md`                     |
| Update site config | Edit `_config.yml`                             |
| Edit team info     | Edit files in `_team/`                         |

**All changes auto-deploy when merged to `main`.** See [CONTENT.md](CONTENT.md) for contributor workflows.

## Local Development

```bash
# Using Docker (recommended)
docker compose up
# Visit http://localhost:8080

# Or native Ruby
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000/icelab-website/
```

## Repository Structure

```
.
├── _bibliography/papers.bib   # Publications (source of truth)
├── _data/                     # Site data (featured slider, venues, coauthors)
├── _includes/                 # Reusable Liquid components
├── _layouts/                  # Page templates
├── _news/                     # Optional brief homepage-only announcements
├── _pages/                    # Static pages (about, publications, etc.)
├── _posts/                    # Blog / news archive
├── _projects/                 # Research project pages
├── _team/                     # Team member profiles
├── _sass/                     # Stylesheets
├── assets/                    # Images, PDFs, JS, CSS
├── _config.yml                # Site configuration
├── bin/check_pdf_paths.py     # PDF path validation
└── .github/workflows/         # Deploy + CI
```

## Deployment

Pushes to `main` trigger `.github/workflows/deploy.yml`, which builds the site with Jekyll and publishes `_site/` to the `gh-pages` branch. GitHub Pages serves that branch at `/icelab-website`.

Pull requests run `.github/workflows/ci.yml` (build, YAML lint, BibTeX validation).

## Documentation

- [CONTENT.md](CONTENT.md) — adding news, publications, team, projects
- [CONTRIBUTING.md](CONTRIBUTING.md) — developer setup and PR process
- [SETUP.md](SETUP.md) — GitHub branch protection and repo settings
