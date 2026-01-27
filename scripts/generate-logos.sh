#!/usr/bin/env bash
#
# Logo Generation Wrapper
#
# Invokes the Python logo generator with uv.
# Pass any arguments through to the Python script.
#

set -euo pipefail

# Change to repository root
cd "$(dirname "$0")/.."

# Run Python script with uv, passing through all arguments
uv run assets/generate/generate_logos.py "$@"
