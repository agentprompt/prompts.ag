#!/usr/bin/env bash
# Generate logos and deploy to live locations
# Usage: pnpm run logo:generate

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ASSETS_DIR="$PROJECT_DIR/assets/generate"

echo "🎨 Agent Prompt Logo Generator"
echo "==============================="
echo

# Run Python generator
echo "Step 1: Generate SVG assets"
echo "---------------------------"
cd "$ASSETS_DIR"
python3 generate_logos.py
echo

# Deploy to live locations
echo "Step 2: Deploy to live locations"
echo "---------------------------------"

MAPPING_FILE="$ASSETS_DIR/asset-mappings.yaml"

if [[ ! -f "$MAPPING_FILE" ]]; then
    echo "❌ Error: $MAPPING_FILE not found"
    exit 1
fi

# Parse YAML and copy files
# Handles format: "  - source: path" and "    dest: path"
current_source=""
deployed=0

while IFS= read -r line; do
    # Skip comments and empty lines
    [[ "$line" =~ ^[[:space:]]*# ]] && continue
    [[ -z "${line// }" ]] && continue

    # Extract source path
    if [[ "$line" =~ ^[[:space:]]*-[[:space:]]*source:[[:space:]]*(.*) ]]; then
        current_source="${BASH_REMATCH[1]}"
        continue
    fi

    # Extract dest path and copy
    if [[ "$line" =~ ^[[:space:]]*dest:[[:space:]]*(.*) ]]; then
        dest="${BASH_REMATCH[1]}"

        if [[ -n "$current_source" && -n "$dest" ]]; then
            src_path="$PROJECT_DIR/$current_source"
            dest_path="$PROJECT_DIR/$dest"

            if [[ -f "$src_path" ]]; then
                # Create destination directory if needed
                mkdir -p "$(dirname "$dest_path")"
                cp "$src_path" "$dest_path"
                echo "  ✓ $current_source → $dest"
                deployed=$((deployed + 1))
            else
                echo "  ⚠ Skipped: $current_source (not found)"
            fi
            current_source=""
        fi
    fi
done < "$MAPPING_FILE"

echo
echo "==============================="
echo "✓ Done! Deployed $deployed assets"
echo
echo "Edit $MAPPING_FILE to add more mappings."
