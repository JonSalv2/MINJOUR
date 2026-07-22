#!/bin/bash
# Double-clickable launcher for MINJOUR on macOS.
# Opens Terminal automatically and runs the packaged binary.

DIR="$(cd "$(dirname "$0")" && pwd)"
"$DIR/dist/minjour/minjour"
