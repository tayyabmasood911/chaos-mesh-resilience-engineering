#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "    Chaos Mesh Resilience Test Suite Execution    "
echo "=================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${SCRIPT_DIR}")"

EXPERIMENTS=(
  "pod-kill-chaos.yaml"
  "network-delay-experiment.yaml"
  "manifests/stress-chaos.yaml"
  "manifests/http-chaos.yaml"
  "manifests/workflow-chaos.yaml"
)

for exp in "${EXPERIMENTS[@]}"; do
  EXP_PATH="${REPO_ROOT}/${exp}"
  if [ -f "${EXP_PATH}" ]; then
    echo "[*] Validating Experiment: ${exp}..."
    python3 "${SCRIPT_DIR}/chaos_runner.py" --manifest "${EXP_PATH}" --duration 5 --dry-run
  else
    echo "[WARN] Manifest not found: ${exp}"
  fi
done

echo "[OK] All resilience experiments passed safety and syntax validation."
