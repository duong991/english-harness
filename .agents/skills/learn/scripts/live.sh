#!/usr/bin/env bash
# English Harness - Gemini Live Voice Speaking Launcher
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

# Check for .env file in repo root or script dir
if [ -f "$REPO_ROOT/.env" ]; then
    export $(grep -v '^#' "$REPO_ROOT/.env" | xargs)
elif [ -f "$SCRIPT_DIR/.env" ]; then
    export $(grep -v '^#' "$SCRIPT_DIR/.env" | xargs)
fi

if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  GEMINI_API_KEY is not set."
    read -p "🔑 Enter your Gemini API Key: " key_input
    export GEMINI_API_KEY="$key_input"
fi

# Run the live python script
python3 "$SCRIPT_DIR/live.py" "$@"
