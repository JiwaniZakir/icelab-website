# Google Chat app setup (personal GCP POC)

Follow [Hermes Google Chat docs](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/google_chat).

## Checklist

1. Create GCP project `ice-lab-hermes-poc`
2. Enable **Google Chat API** and **Cloud Pub/Sub API**
3. Create topic `hermes-chat-events`
4. Create pull subscription `hermes-chat-events-sub` (7-day retention)
5. Topic IAM: `chat-api-push@system.gserviceaccount.com` → **Pub/Sub Publisher**
6. Create SA `hermes-chat-bot`; download JSON → `/opt/data/google-chat-sa.json` on Akash volume
7. Subscription IAM: SA → **Pub/Sub Subscriber** + **Pub/Sub Viewer**
8. Chat API → Configuration:
   - Enable 1:1 and space messages
   - Pub/Sub topic: `projects/ice-lab-hermes-poc/topics/hermes-chat-events`
   - Visibility: specific test users (POC)
9. Create Google Chat space **ICE Lab Website Updates**; add the app
10. Set `GOOGLE_CHAT_ALLOWED_USERS` to lab `@drexel.edu` emails

## Verify

- Send a message in the space
- Pub/Sub subscription should show undelivered count > 0 before Hermes connects
- Hermes logs: `[GoogleChat] Connected`

## File attachments

Each user runs `/setup-files` once in a DM with the bot for native PDF/photo uploads. Until then, use Google Drive links in the space.
