#!/usr/bin/env python3
"""
Ember Design Intelligence — Extended UI UX Pro Max
Wraps the original search.py and layers Ember-specific
extensions on top of the output.

Usage:
  python3 ember-search.py "beauty spa" --design-system -p "Client"
  python3 ember-search.py "agency dashboard" --domain style
"""

import sys
import os
import csv
import subprocess
import json

# Path to original search script
SEARCH_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    '../src/ui-ux-pro-max/scripts/search.py'
)

# Path to Ember extension data
EMBER_DIR = os.path.dirname(__file__)
EMBER_EXTENSIONS = os.path.join(EMBER_DIR, 'ember-extensions.csv')
EMBER_STYLES = os.path.join(EMBER_DIR, 'ember-styles.csv')

# Ember design system constants
EMBER_SYSTEM = {
    'display_font': 'Syne (700-800 weight)',
    'mono_font': 'IBM Plex Mono',
    'bg': '#0B0B0A',
    'accent': '#F5A623 (amber)',
    'loading_animation': 'filament sweep',
    'active_animation': 'breathing border',
    'spacing': 'rule-of-4 rem scale via --space-* vars',
    'type_scale': '--text-* rem vars with 18px clamp cap',
    'component_library': '@evokedmedia/evoke-ui',
}

# Ember design principles
EMBER_PRINCIPLES = {
    'restraint': 'One accent event per viewport. Add only what removal loses.',
    'typography': 'Syne for display/KPIs. IBM Plex Mono for data/metadata.',
    'color': 'Color is information not decoration. Amber = important only.',
    'motion': 'Motion communicates state. Filament sweep + breathing border only.',
    'composition': 'Hero pane + KPI strip + detail region. Match reading pattern.',
}

def load_ember_extensions():
    """Load Ember-specific extensions for each category."""
    extensions = {}
    if not os.path.exists(EMBER_EXTENSIONS):
        return extensions
    with open(EMBER_EXTENSIONS, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat_id = row.get('category_id', '').strip()
            if cat_id:
                extensions[cat_id] = row
    return extensions

def load_ember_styles():
    """Load Ember-specific style adaptations."""
    styles = {}
    if not os.path.exists(EMBER_STYLES):
        return styles
    with open(EMBER_STYLES, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            style_id = row.get('style_id', '').strip()
            if style_id:
                styles[style_id] = row
    return styles

def run_original_search(args):
    """Run the original UI UX Pro Max search script."""
    cmd = [sys.executable, SEARCH_SCRIPT] + args
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(SEARCH_SCRIPT)
    )
    return result.stdout, result.returncode

def format_ember_layer(extensions, styles, query):
    """Format the Ember-specific additions to append to output."""
    output = []
    output.append('')
    output.append('=' * 80)
    output.append('  EMBER DESIGN SYSTEM LAYER')
    output.append('  (Applied on top of UI UX Pro Max baseline)')
    output.append('=' * 80)
    output.append('')
    output.append('  DESIGN SYSTEM:')
    output.append(f'    Display font:  {EMBER_SYSTEM["display_font"]}')
    output.append(f'    Data font:     {EMBER_SYSTEM["mono_font"]}')
    output.append(f'    Background:    {EMBER_SYSTEM["bg"]}')
    output.append(f'    Accent:        {EMBER_SYSTEM["accent"]}')
    output.append(f'    Loading:       {EMBER_SYSTEM["loading_animation"]}')
    output.append(f'    Active:        {EMBER_SYSTEM["active_animation"]}')
    output.append(f'    Components:    {EMBER_SYSTEM["component_library"]}')
    output.append('')
    output.append('  EMBER DESIGN PRINCIPLES:')
    for key, principle in EMBER_PRINCIPLES.items():
        output.append(f'    [{key.upper()}] {principle}')
    output.append('')
    output.append('  CSS TOKEN MAPPING:')
    output.append('    Replace generic colors with:')
    output.append('      Primary/accent  → var(--color-accent)')
    output.append('      Background      → var(--color-bg)')
    output.append('      Surface         → var(--color-surface-1/2/3)')
    output.append('      Text primary    → var(--color-text)')
    output.append('      Text muted      → var(--color-text-muted)')
    output.append('      Success         → var(--color-success)')
    output.append('      Danger          → var(--color-danger)')
    output.append('      Warning         → var(--color-warning)')
    output.append('')
    output.append('  ANTI-PATTERNS FOR EMBER (universal):')
    output.append('    × Hardcoded hex values in components')
    output.append('    × Multiple amber/accent elements per viewport')
    output.append('    × Spinners (use filament sweep instead)')
    output.append('    × Decorative animations (motion = state only)')
    output.append('    × Generic fonts (Inter, Roboto, Arial)')
    output.append('    × Purple gradients on dark backgrounds')
    output.append('')
    output.append('  READ BEFORE BUILDING:')
    output.append(
        '    /root/.openclaw/shared/design-library/DESIGN_PHILOSOPHY.md'
    )
    output.append(
        '    /root/.openclaw/shared/training/design/component-inventory.md'
    )
    output.append('=' * 80)
    return '\n'.join(output)

def main():
    args = sys.argv[1:]

    # Run original search
    original_output, return_code = run_original_search(args)
    print(original_output)

    # Load Ember extensions
    extensions = load_ember_extensions()
    styles = load_ember_styles()

    # Append Ember layer
    query = args[0] if args else ''
    ember_layer = format_ember_layer(extensions, styles, query)
    print(ember_layer)

    sys.exit(return_code)

if __name__ == '__main__':
    main()
