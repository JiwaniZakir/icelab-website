# Example intake files for the content pipeline.

These JSON files validate against `content-schemas/` and can be used for dry-run testing:

```bash
python3 bin/content/intake.py content-intake/examples/pilot-news.json
python3 bin/content/generate.py content-intake/examples/pilot-news.json --dry-run
python3 bin/content/validate.py --skip-build
```

**Do not merge** pilot-generated files to `main` — they use test dates/slugs for pipeline verification only.

## Test the GitHub workflow

**Issue forms (recommended):** open New Issue → Add News Post (or other typed form) on GitHub.

**Manual dispatch:** GitHub Actions → Content Intake → Run workflow with:

```
intake_path: content-intake/examples/pilot-news.json
```

**Form parser unit check:**

```bash
python3 bin/content/test_form_to_intake.py
```
