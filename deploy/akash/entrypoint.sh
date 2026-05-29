#!/bin/bash
set -euo pipefail

HERMES_HOME="${HERMES_HOME:-/opt/data}"
REPO_DIR="${REPO_DIR:-/data/icelab-website}"
REPO_URL="${REPO_URL:-https://github.com/JiwaniZakir/icelab-website.git}"
SKILL_SRC="${REPO_DIR}/skills/ice-website-content/SKILL.md"

mkdir -p "$HERMES_HOME/skills/ice-website-content" "$REPO_DIR"

if [ ! -d "$REPO_DIR/.git" ]; then
  git clone "$REPO_URL" "$REPO_DIR"
else
  git -C "$REPO_DIR" fetch origin
  git -C "$REPO_DIR" checkout main
  git -C "$REPO_DIR" pull --ff-only origin main || true
fi

if [ -f "$SKILL_SRC" ]; then
  cp "$SKILL_SRC" "$HERMES_HOME/skills/ice-website-content/SKILL.md"
fi

CONFIG="$HERMES_HOME/config.yaml"
if [ ! -f "$CONFIG" ]; then
  cat > "$CONFIG" <<'YAML'
approvals:
  mode: manual
  timeout: 300
terminal:
  cwd: /data/icelab-website
YAML
fi

if [ -n "${GOOGLE_CHAT_SERVICE_ACCOUNT_JSON:-}" ] && [ -f "$GOOGLE_CHAT_SERVICE_ACCOUNT_JSON" ]; then
  chmod 600 "$GOOGLE_CHAT_SERVICE_ACCOUNT_JSON" || true
fi

cd "$REPO_DIR"
exec hermes "$@"
