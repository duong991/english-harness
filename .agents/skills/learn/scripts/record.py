#!/usr/bin/env python3
"""
Lightweight Audio Recording Helper for English Learning Practice.
Runs native macOS AVFoundation audio recording with live progress and automatic file management.
"""
import sys
import os
import argparse
import subprocess
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Record speaking practice audio on macOS")
    parser.add_argument("-d", "--duration", type=float, default=60.0, help="Duration in seconds (default: 60, 0 for manual stop)")
    parser.add_argument("-o", "--output", type=str, default="", help="Output audio file path")
    parser.add_argument("-t", "--topic", type=str, default="speaking", help="Topic name for auto-generated file naming")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "../../../.."))
    audio_dir = os.path.join(repo_root, "artifacts", "audio")
    os.makedirs(audio_dir, exist_ok=True)

    if not args.output:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        topic_slug = args.topic.replace(" ", "-").lower()
        args.output = os.path.join(audio_dir, f"{timestamp}-{topic_slug}.m4a")

    binary = os.path.join(script_dir, "record-audio")
    swift_src = os.path.join(script_dir, "record.swift")

    if os.path.exists(binary) and os.access(binary, os.X_OK):
        cmd = [binary, "-d", str(args.duration), "-o", args.output]
        sys.exit(subprocess.call(cmd))
    elif os.path.exists(swift_src):
        cmd = ["/usr/bin/swift", swift_src, "-d", str(args.duration), "-o", args.output]
        sys.exit(subprocess.call(cmd))
    else:
        print("❌ Error: No audio recording engine found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
