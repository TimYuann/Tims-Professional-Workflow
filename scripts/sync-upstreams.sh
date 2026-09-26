#!/usr/bin/env bash
# ==============================================================================
# sync-upstreams.sh
# Layer 1 Upstream Sync Script for TIM · Professional Workflow
#
# Inspects and fetches updates from upstream repositories:
# - cursor-plugins (pstack)
# - mattpocock-skills
# - addyosmani-agent-skills
#
# Usage:
#   ./scripts/sync-upstreams.sh          # Check status & show diff summary (read-only)
#   ./scripts/sync-upstreams.sh --pull   # Fetch & pull latest upstream updates
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
UPSTREAMS_DIR="${ROOT_DIR}/upstreams"

PULL_MODE=false
if [[ "${1:-}" == "--pull" ]]; then
  PULL_MODE=true
fi

echo "======================================================================"
echo " TIM Professional Workflow · Upstream Source Sync Inspection"
echo " Time: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo " Mode: $([ "$PULL_MODE" = true ] && echo "FETCH & PULL" || echo "CHECK & REPORT (Read-Only)")"
echo "======================================================================"

declare -a REPOS=("cursor-plugins" "mattpocock-skills" "addyosmani-agent-skills")

for repo in "${REPOS[@]}"; do
  REPO_PATH="${UPSTREAMS_DIR}/${repo}"
  echo ""
  echo ">>> Checking upstream: [${repo}]"
  if [[ ! -d "${REPO_PATH}/.git" ]]; then
    echo "    [ERROR] .git not found at ${REPO_PATH}. Skipping."
    continue
  fi

  cd "${REPO_PATH}"
  CURRENT_COMMIT=$(git rev-parse --short HEAD)
  CURRENT_DATE=$(git log -1 --format="%ci")
  echo "    Current Pinned Commit: ${CURRENT_COMMIT} (${CURRENT_DATE})"

  # Fetch remote
  git fetch origin --quiet

  UPSTREAM_BRANCH="origin/$(git rev-parse --abbrev-ref HEAD)"
  BEHIND_COUNT=$(git rev-list --count HEAD..${UPSTREAM_BRANCH} 2>/dev/null || echo "0")

  if [[ "${BEHIND_COUNT}" -eq 0 ]]; then
    echo "    [STATUS] Up to date with ${UPSTREAM_BRANCH}."
  else
    echo "    [NOTICE] ${BEHIND_COUNT} new commit(s) available upstream!"
    echo "    Recent upstream commits:"
    git log --oneline -n 5 HEAD..${UPSTREAM_BRANCH} | sed 's/^/      - /'

    if [[ "$PULL_MODE" = true ]]; then
      echo "    Pulling latest commits..."
      git pull --ff-only
      NEW_COMMIT=$(git rev-parse --short HEAD)
      echo "    [SUCCESS] Updated to ${NEW_COMMIT}."
    else
      echo "    Run './scripts/sync-upstreams.sh --pull' to update local copy."
    fi
  fi
done

echo ""
echo "======================================================================"
echo " Upstream sync check complete."
echo "======================================================================"
