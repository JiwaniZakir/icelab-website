# Branch Protection & Repository Setup Guide

After creating the GitHub repository, configure these settings for production-grade quality.

## 1. Create the Repository

```bash
# On GitHub: Create new repository named "icelab.github.io"
# Under the org or your username

# Push this code:
git remote add origin git@github.com:YOUR_ORG/icelab.github.io.git
git push -u origin main
```

## 2. Enable GitHub Pages

1. Go to **Settings > Pages**
2. Wait for the first deploy to create the `gh-pages` branch
3. Set **Source** to "Deploy from a branch"
4. Set **Branch** to `gh-pages` / `/ (root)`
5. Optionally add a custom domain

## 3. Branch Protection Rules

Go to **Settings > Branches > Add branch protection rule**

### Rule for `main`:

| Setting                                                | Value                                                                 |
| ------------------------------------------------------ | --------------------------------------------------------------------- |
| Branch name pattern                                    | `main`                                                                |
| Require a pull request before merging                  | **Yes**                                                               |
| Required approvals                                     | **1**                                                                 |
| Dismiss stale PR approvals when new commits are pushed | **Yes**                                                               |
| Require status checks to pass before merging           | **Yes**                                                               |
| Required status checks                                 | `Build & Validate`, `Check Links`, `Code Format`, `BibTeX Validation` |
| Require branches to be up to date before merging       | **Yes**                                                               |
| Require conversation resolution before merging         | **Yes**                                                               |
| Do not allow bypassing the above settings              | Optional (enable for strict teams)                                    |

### Rule for `gh-pages`:

| Setting               | Value                |
| --------------------- | -------------------- |
| Branch name pattern   | `gh-pages`           |
| Restrict who can push | Only GitHub Actions  |
| Allow force pushes    | Only deploy workflow |

## 4. Repository Settings

### General

- **Default branch:** `main`
- **Features:** Enable Issues, disable Wiki (use the site itself)
- **Pull Requests:** Allow squash merging (recommended), disable merge commits

### Actions > General

- **Workflow permissions:** Read and write permissions
- **Allow GitHub Actions to create and approve pull requests:** Yes

### Secrets (if using Google Scholar citations)

- Add `SCHOLAR_USER_ID` with your Google Scholar profile ID
- Add `PAT` with a Personal Access Token (for citation auto-commits to trigger deploys)

## 5. Labels

Create these labels for issue/PR organization:

| Label              | Color     | Description                 |
| ------------------ | --------- | --------------------------- |
| `content`          | `#0E8A16` | Content additions/changes   |
| `bug`              | `#D73A4A` | Something isn't working     |
| `enhancement`      | `#A2EEEF` | New feature or improvement  |
| `design`           | `#F9D0C4` | Visual/CSS changes          |
| `infrastructure`   | `#BFD4F2` | CI/CD, config, dependencies |
| `good first issue` | `#7057FF` | Good for newcomers          |
| `help wanted`      | `#008672` | Extra attention needed      |
| `stale`            | `#FFFFFF` | Auto-applied by stale bot   |

## 6. Team Permissions

| Role           | Access   | Can Do                      |
| -------------- | -------- | --------------------------- |
| Lab PI / Admin | Admin    | Full control, merge to main |
| Lab Manager    | Maintain | Review PRs, manage issues   |
| Lab Members    | Write    | Create branches, open PRs   |
| External       | Read     | View only                   |
