#!/usr/bin/env bash
# English Harness - Gemini Live Web UI Launcher
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

if [ -f "$REPO_ROOT/.env" ]; then
    export $(grep -v '^#' "$REPO_ROOT/.env" | xargs)
fi

echo "🚀 Starting Gemini Live Web Server at http://127.0.0.1:8000..."
echo "🌐 Opening browser with Hardware Echo Cancellation..."

# Open browser automatically on macOS
(sleep 1.5 && open "http://127.0.0.1:8000") &

python3 "$SCRIPT_DIR/live_web.py"
