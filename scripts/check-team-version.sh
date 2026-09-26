#!/usr/bin/env bash
# ==============================================================================
# check-team-version.sh
# Layer 2 Downstream Project Reference Liveness & Drift Check
#
# Can be called from downstream projects (e.g. UCBIP / ekunAi) or preflight hooks
# to verify whether the downstream project is using the expected release version
# of TIM · Professional Workflow.
#
# Usage in downstream project:
#   bash /path/to/tim-professional-workflow/scripts/check-team-version.sh <path-to-downstream-binding.yaml|lock>
# ==============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIM_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

LATEST_VERSION="unknown"
if [[ -f "${TIM_ROOT}/VERSION" ]]; then
  LATEST_VERSION="$(cat "${TIM_ROOT}/VERSION" | tr -d '[:space:]')"
fi

TARGET_FILE="${1:-}"

echo "======================================================================"
echo " TIM Professional Workflow · Downstream Binding Version Audit"
echo " Global Repository: ${TIM_ROOT}"
echo " Latest Available Version: ${LATEST_VERSION}"
echo "======================================================================"

if [[ -z "${TARGET_FILE}" ]]; then
  echo "[INFO] No downstream binding file provided as argument."
  echo "       Usage: ./scripts/check-team-version.sh <path-to-binding.yaml>"
  exit 0
fi

if [[ ! -f "${TARGET_FILE}" ]]; then
  echo "[ERROR] Binding file not found: ${TARGET_FILE}"
  exit 1
fi

PINNED_VERSION=$(grep -E "^version:" "${TARGET_FILE}" 2>/dev/null | head -n 1 | awk '{print $2}' | tr -d '"' | tr -d "'" || echo "")

if [[ -z "${PINNED_VERSION}" ]]; then
  echo "[WARNING] Could not parse 'version:' field from ${TARGET_FILE}."
  exit 0
fi

echo "[INFO] Project pinned version: ${PINNED_VERSION}"

if [[ "${PINNED_VERSION}" == "${LATEST_VERSION}" ]]; then
  echo "[SUCCESS] Project is bound to the latest stable release (${PINNED_VERSION})."
  exit 0
else
  echo "[WARNING] Version drift detected!"
  echo "          Project pinned: ${PINNED_VERSION}"
  echo "          Latest global:  ${LATEST_VERSION}"
  echo "          Please review CHANGELOG and update the downstream binding when ready."
  exit 2
fi
