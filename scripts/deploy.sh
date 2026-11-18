#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:?usage: ./scripts/deploy.sh <version>}"
URL='http://localhost:8080/health'

echo "==> Building homelab-app:${VERSION}"
docker build -t "homelab-app:${VERSION}" .

echo "==> Starting stack with version ${VERSION}"
APP_VERSION="${VERSION}" docker compose up -d --no-build

echo '==> Waiting for the new version to report healthy (max 60s)'
for i in $(seq 1 30); do
  if body=$(curl -fsS "${URL}" 2>/dev/null) && echo "${body}" | grep -qF "${VERSION}"; then
    echo "==> Deployment successful: ${body}"
    exit 0
  fi
  sleep 2
done

echo "==> Deployment FAILED: ${URL} never reported version ${VERSION}" >&2
docker compose logs --tail 20 app >&2
exit 1
