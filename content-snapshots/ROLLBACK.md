# Rolling back a bad website deploy

Each successful deploy to `main` creates an annotated git tag `site-snapshot/YYYY-MM-DDTHHMMSSZ` and appends an entry to [manifest.json](manifest.json).

## Before anything goes live

- Content agent opens **draft PRs** only — close the PR if the change is wrong.
- Maintainer reviews CI and the **site-build** artifact before merging.

## Draft PR not merged

1. Close the PR on GitHub.
2. Delete the remote branch (`content/...`).

No live site impact.

## Bad merge on `main` (revert source)

Reverting the merge commit on `main` triggers a new deploy from the previous content:

```bash
git checkout main
git pull origin main
git log --oneline -5          # find the merge commit SHA
git revert -m 1 <merge-commit-sha>
git push origin main
```

Wait ~2 minutes for [deploy.yml](../.github/workflows/deploy.yml) to finish.

## List recent snapshots

```bash
git fetch --tags
git tag -l 'site-snapshot/*' | tail -10
```

Inspect a snapshot:

```bash
git show site-snapshot/2026-05-24T120000Z --stat
```

## gh-pages branch (last resort)

If `main` is correct but `gh-pages` is wrong, reset `gh-pages` to a known good deploy commit (maintainer only):

```bash
git fetch origin gh-pages
git checkout gh-pages
git log --oneline -5
# reset to a good commit, then force-push gh-pages (coordinate with PI)
```

## After rollback

Run live verification:

```bash
python3 bin/content/verify_live.py --intake content-intake/pending/<thread>/intake.json
```

Or spot-check https://jiwanizakir.github.io/icelab-website/
