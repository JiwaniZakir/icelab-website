# Inbox drop folder

Place validated intake JSON files here to trigger the **Content Intake** workflow on push to `main`.

```bash
cp my-news.json content-intake/inbox/my-news.json
git add content-intake/inbox/my-news.json
git commit -m "content: submit news via inbox"
git push origin main
```

The workflow will:

1. Validate and normalize the JSON
2. Generate Jekyll/BibTeX files
3. Move the intake file to `content-intake/processed/`
4. Open a **draft PR** for maintainer review

**For most lab members:** use **New Issue** → typed forms (Add News Post, Add Publication, etc.) instead — no git required.

See [CONTENT.md](../../CONTENT.md) for full instructions.
