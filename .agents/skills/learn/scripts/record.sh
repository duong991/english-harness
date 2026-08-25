#!/usr/bin/env bash
# English Harness - Native Audio Recording Helper for Speaking Practice
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

# Ensure audio directory exists
mkdir -p "$REPO_ROOT/artifacts/audio"

BINARY="$SCRIPT_DIR/record-audio"
SWIFT_SRC="$SCRIPT_DIR/record.swift"

if [ -f "$BINARY" ] && [ -x "$BINARY" ]; then
    "$BINARY" "$@"
elif [ -f "$SWIFT_SRC" ]; then
    /usr/bin/swift "$SWIFT_SRC" "$@"
else
    echo "❌ Error: Neither $BINARY nor $SWIFT_SRC found."
    exit 1
fi
