#!/bin/bash
# Sync upstream UI UX Pro Max updates into our fork
# Run: bash sync-upstream.sh
# Safe to run anytime — our extensions are in ember/ folder
# which upstream never touches, so no merge conflicts expected

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo "=== Syncing upstream UI UX Pro Max updates ==="

# Add upstream remote if not already added
git remote get-url upstream 2>/dev/null || \
  git remote add upstream \
    https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git

# Fetch upstream changes
git fetch upstream

# Merge upstream main into our fork
git merge upstream/main --no-edit \
  -m "sync: upstream UI UX Pro Max updates"

echo "=== Sync complete ==="
echo "Our ember/ extensions are untouched."
echo "Test that the wrapper still works:"
echo "  python3 ember/ember-search.py 'test' --design-system"
