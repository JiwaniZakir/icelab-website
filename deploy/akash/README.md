# Deploy ICE Lab Hermes agent on Akash

Google Chat is the input channel. Hermes runs on Akash with **human-in-the-loop** approvals before any repo writes or PRs.

## Prerequisites

- [Akash Console](https://console.akash.network) account (free trial OK for POC — **24h max lease**)
- Personal GCP project with Chat app + Pub/Sub ([gcp-setup.md](gcp-setup.md))
- Google Chat space **ICE Lab Website Updates**
- Fine-grained GitHub PAT (`GH_TOKEN`): Contents + Pull requests on `icelab-website`
- LLM API key (e.g. OpenRouter)

## Build and push image

```bash
docker build -f deploy/akash/Dockerfile -t ghcr.io/jiwanizakir/icelab-hermes:0.1.0 .
docker push ghcr.io/jiwanizakir/icelab-hermes:0.1.0
```

Update the image tag in [deploy.yaml](deploy.yaml) if you use a different registry.

## Secrets

Copy [`.env.example`](.env.example). In Akash Console, set environment variables on the deployment. Upload the Google service account JSON to persistent volume `/opt/data/google-chat-sa.json`.

## Deploy on Akash Console

1. **Create Deployment** → paste [deploy.yaml](deploy.yaml)
2. Set env vars from `.env.example`
3. Accept a provider bid
4. Check logs for `[GoogleChat] Connected`

No public ports are required (Pub/Sub pull + outbound HTTPS only).

## Persistent volumes

| Mount | Path | Purpose |
|-------|------|---------|
| hermes-data | `/opt/data` | Hermes config, sessions, skills, SA JSON |
| website-repo | `/data/icelab-website` | Git clone for content CLI |

## HITL workflow in Chat

Pin in the Google Chat space:

```
1. Start a NEW THREAD per submission
2. Describe the update (news, paper, team, project)
3. Review the PLAN from the bot
4. Reply APPROVE PLAN
5. Review the PREVIEW
6. Reply APPROVE PR → draft PR on GitHub
7. Maintainer merges → site deploys (~2 min)

CANCEL — discard | REVISE: feedback — change plan
```

## Hermes config (auto-seeded)

- `approvals.mode: manual`
- `MESSAGING_CWD=/data/icelab-website`
- Skill: `ice-website-content` from repo

## Rollback

See [content-snapshots/ROLLBACK.md](../../content-snapshots/ROLLBACK.md).

## POC limitations

- Akash trial leases expire after 24 hours — export `/opt/data` before close
- Personal GCP Chat app visibility may need lab emails added manually
- File uploads in Chat require `/setup-files` OAuth per user
