#!/usr/bin/env bash
# Wrapper around scripts/validate.py for quick local validation.
# Usage: bash tests/validate.sh

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

echo "Re-generating workflows from canonical content map..."
python3 scripts/generate_workflows.py
echo "Re-generating indexes..."
python3 scripts/generate_indexes.py
echo
echo "Running validation..."
python3 scripts/validate.py
