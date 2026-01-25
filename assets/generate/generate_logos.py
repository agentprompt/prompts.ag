#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "svgpathtools>=1.6",
#     "pyyaml>=6.0",
# ]
# ///
"""
Agent Prompt Logo Generator

Generates all logo variants:
- Wordmarks (dark, light, white, adaptive) in regular and tight versions
- Icons (rounded, square, transparent, adaptive, white-bg) in regular and tight versions
- Favicons (adaptive)

Usage:
    uv run assets/generate/generate_logos.py

Configuration:
    Edit the CONFIG section below to adjust padding, colors, etc.
"""

import re
from pathlib import Path

# =============================================================================
# CONFIG - Edit these values to adjust the output
# =============================================================================

CONFIG = {
    # Wordmark settings
    "wordmark": {
        "regular": {
            "viewbox_width": 203,
            "viewbox_height": 64,
            "corner_radius": 8,
            "horizontal_padding": 8,
            "vertical_padding": 14,
        },
        "tight": {
            "corner_radius": 6,
            "horizontal_padding": 14,
            "vertical_padding": 9,
        },
    },
    # Icon settings
    "icon": {
        "regular": {
            "viewbox_size": 100,
            "corner_radius": 12,
            "padding": 5,  # Content spans from padding to (viewbox_size - padding)
        },
        "tight": {
            "corner_radius": 8,
            "padding": 3,
        },
    },
    # Favicon settings
    "favicon": {
        "viewbox_size": 32,
        "corner_radius": 4,
        "padding": 2,
    },
    # Colors
    "colors": {
        "dark_bg": "#0c0a09",
        "light_bg": "#fafafa",
        "white_bg": "#ffffff",
        "amber": "#f59e0b",
        "cream": "#fef3c7",
        "off_white": "#fafafa",
        "dark_text": "#0c0a09",
    },
    # Output directory
    "output_dir": Path("."),
}

# =============================================================================
# ICON AND TEXT PATH DATA
# =============================================================================

# Icon paths (in regular coordinate space, viewBox 0 0 203 64)
ICON_PATHS = {
    "left_bracket": "M 10.4 32.0L 18.6 13.8L 18.6 18.6L 13.8 32.0L 18.6 45.4L 18.6 50.2L 10.4 32.0Z",
    "right_bracket": "M 53.6 32.0L 45.4 13.8L 45.4 18.6L 50.2 32.0L 45.4 45.4L 45.4 50.2L 53.6 32.0Z",
    "icon_a": "M 29.9 35.7Q 29.9 36.4 30.1 36.6Q 30.3 36.9 30.7 37.0L 30.2 38.5Q 29.5 38.4 28.9 38.1Q 28.4 37.8 28.1 37.1Q 27.6 37.8 26.7 38.1Q 25.9 38.5 24.9 38.5Q 23.4 38.5 22.4 37.6Q 21.5 36.8 21.5 35.4Q 21.5 33.7 22.8 32.9Q 24.0 32.0 26.4 32.0H 27.8V 31.4Q 27.8 30.4 27.2 29.9Q 26.6 29.5 25.6 29.5Q 25.1 29.5 24.4 29.6Q 23.6 29.8 22.9 30.0L 22.4 28.5Q 23.3 28.2 24.2 28.0Q 25.1 27.8 25.9 27.8Q 27.9 27.8 28.9 28.7Q 29.9 29.6 29.9 31.2ZM 25.5 36.9Q 26.2 36.9 26.8 36.6Q 27.4 36.2 27.8 35.6V 33.3H 26.6Q 25.1 33.3 24.5 33.9Q 23.8 34.4 23.8 35.3Q 23.8 36.9 25.5 36.9Z",
    "icon_g": "M 42.2 26.8L 42.8 28.6Q 42.2 28.8 41.5 28.9Q 40.8 28.9 39.9 28.9Q 40.8 29.4 41.3 30.0Q 41.7 30.6 41.7 31.5Q 41.7 32.5 41.2 33.3Q 40.7 34.1 39.8 34.5Q 39.0 34.9 37.7 34.9Q 37.3 34.9 36.9 34.9Q 36.6 34.9 36.3 34.8Q 35.9 35.1 35.9 35.6Q 35.9 35.9 36.1 36.1Q 36.4 36.4 37.1 36.4H 38.9Q 40.0 36.4 40.8 36.8Q 41.6 37.1 42.1 37.8Q 42.6 38.4 42.6 39.2Q 42.6 40.7 41.3 41.6Q 40.0 42.4 37.5 42.4Q 35.8 42.4 34.8 42.0Q 33.8 41.6 33.4 41.0Q 33.0 40.3 33.0 39.2H 34.9Q 34.9 39.8 35.1 40.1Q 35.4 40.5 35.9 40.6Q 36.5 40.8 37.6 40.8Q 39.2 40.8 39.8 40.4Q 40.4 40.0 40.4 39.3Q 40.4 38.7 39.9 38.4Q 39.3 38.0 38.5 38.0H 36.7Q 35.3 38.0 34.6 37.5Q 34.0 36.9 34.0 36.1Q 34.0 35.0 35.1 34.3Q 34.2 33.8 33.7 33.1Q 33.3 32.4 33.3 31.4Q 33.3 30.4 33.9 29.6Q 34.4 28.7 35.4 28.3Q 36.3 27.8 37.6 27.8Q 38.8 27.9 39.6 27.7Q 40.4 27.6 41.0 27.3Q 41.6 27.1 42.2 26.8ZM 37.6 29.3Q 36.6 29.3 36.0 29.9Q 35.5 30.5 35.5 31.4Q 35.5 32.4 36.0 33.0Q 36.6 33.5 37.6 33.5Q 38.6 33.5 39.1 33.0Q 39.6 32.4 39.6 31.4Q 39.6 29.3 37.6 29.3Z",
}

# Text paths for "agentprompt" (in regular coordinate space)
TEXT_PATHS = {
    "a": "M 77.5 35.8Q 77.5 36.4 77.6 36.6Q 77.8 36.9 78.2 37.0L 77.7 38.5Q 77.0 38.4 76.5 38.1Q 75.9 37.8 75.6 37.1Q 75.1 37.8 74.2 38.1Q 73.4 38.5 72.4 38.5Q 70.9 38.5 70.0 37.6Q 69.1 36.8 69.1 35.4Q 69.1 33.7 70.3 32.9Q 71.6 32.0 73.9 32.0H 75.3V 31.4Q 75.3 30.4 74.7 29.9Q 74.2 29.5 73.1 29.5Q 72.6 29.5 71.9 29.6Q 71.2 29.8 70.4 30.0L 69.9 28.5Q 70.8 28.2 71.7 28.0Q 72.6 27.8 73.4 27.8Q 75.4 27.8 76.5 28.7Q 77.5 29.6 77.5 31.2ZM 73.1 36.9Q 73.7 36.9 74.3 36.6Q 75.0 36.2 75.3 35.6V 33.4H 74.2Q 72.6 33.4 72.0 33.9Q 71.3 34.4 71.3 35.3Q 71.3 36.9 73.1 36.9Z",
    "g": "M 89.8 26.8L 90.3 28.6Q 89.7 28.8 89.0 28.9Q 88.3 28.9 87.4 28.9Q 88.3 29.3 88.8 30.0Q 89.2 30.6 89.2 31.5Q 89.2 32.5 88.7 33.3Q 88.3 34.1 87.4 34.5Q 86.5 34.9 85.2 34.9Q 84.8 34.9 84.5 34.9Q 84.1 34.9 83.8 34.8Q 83.4 35.1 83.4 35.6Q 83.4 35.9 83.6 36.1Q 83.9 36.4 84.7 36.4H 86.4Q 87.5 36.4 88.3 36.7Q 89.2 37.1 89.6 37.7Q 90.1 38.4 90.1 39.2Q 90.1 40.7 88.8 41.5Q 87.5 42.4 85.0 42.4Q 83.3 42.4 82.3 42.0Q 81.3 41.7 80.9 41.0Q 80.5 40.3 80.5 39.2H 82.5Q 82.5 39.8 82.7 40.1Q 82.9 40.5 83.4 40.6Q 84.0 40.8 85.1 40.8Q 86.7 40.8 87.3 40.4Q 88.0 40.0 88.0 39.3Q 88.0 38.7 87.4 38.4Q 86.9 38.0 86.0 38.0H 84.2Q 82.8 38.0 82.1 37.5Q 81.5 36.9 81.5 36.1Q 81.5 35.0 82.6 34.3Q 81.7 33.8 81.3 33.1Q 80.9 32.4 80.9 31.4Q 80.9 30.4 81.4 29.6Q 81.9 28.7 82.9 28.3Q 83.8 27.8 85.1 27.8Q 86.3 27.9 87.1 27.7Q 87.9 27.6 88.5 27.3Q 89.2 27.1 89.8 26.8ZM 85.1 29.3Q 84.1 29.3 83.6 29.9Q 83.0 30.5 83.0 31.4Q 83.0 32.4 83.6 33.0Q 84.1 33.5 85.1 33.5Q 86.1 33.5 86.6 33.0Q 87.1 32.4 87.1 31.4Q 87.1 29.3 85.1 29.3Z",
    "e": "M 94.5 33.9Q 94.6 35.4 95.4 36.1Q 96.2 36.8 97.3 36.8Q 98.0 36.8 98.7 36.6Q 99.3 36.4 100.0 35.9L 100.9 37.2Q 100.2 37.8 99.2 38.2Q 98.3 38.5 97.2 38.5Q 95.6 38.5 94.5 37.8Q 93.4 37.2 92.9 36.0Q 92.3 34.8 92.3 33.2Q 92.3 31.7 92.9 30.4Q 93.4 29.2 94.5 28.5Q 95.5 27.8 96.9 27.8Q 99.0 27.8 100.1 29.2Q 101.3 30.5 101.3 32.9Q 101.3 33.2 101.3 33.4Q 101.3 33.7 101.3 33.9ZM 97.0 29.4Q 95.9 29.4 95.3 30.1Q 94.6 30.9 94.5 32.4H 99.2Q 99.2 31.0 98.6 30.2Q 98.0 29.4 97.0 29.4Z",
    "n": "M 104.3 38.2V 28.1H 106.1L 106.3 29.4Q 106.9 28.6 107.8 28.2Q 108.6 27.8 109.6 27.8Q 111.0 27.8 111.7 28.6Q 112.4 29.4 112.4 30.8V 38.2H 110.2V 31.9Q 110.2 30.6 110.0 30.0Q 109.7 29.5 108.8 29.5Q 108.1 29.5 107.4 29.9Q 106.8 30.4 106.4 31.0V 38.2Z",
    "t": "M 124.3 37.7Q 123.7 38.1 122.9 38.3Q 122.1 38.5 121.3 38.5Q 119.5 38.5 118.6 37.6Q 117.7 36.7 117.7 35.2V 29.7H 115.4V 28.1H 117.7V 25.8L 119.8 25.6V 28.1H 123.3L 123.0 29.7H 119.8V 35.1Q 119.8 36.0 120.3 36.4Q 120.7 36.8 121.6 36.8Q 122.2 36.8 122.6 36.6Q 123.1 36.5 123.5 36.3Z",
    "p": "M 132.3 27.8Q 133.6 27.8 134.4 28.5Q 135.2 29.1 135.6 30.3Q 135.9 31.5 135.9 33.2Q 135.9 34.7 135.5 35.9Q 135.1 37.1 134.2 37.8Q 133.3 38.5 132.0 38.5Q 130.4 38.5 129.5 37.4V 42.1L 127.3 42.4V 28.1H 129.2L 129.3 29.4Q 129.9 28.6 130.6 28.2Q 131.4 27.8 132.3 27.8ZM 131.7 29.5Q 130.9 29.5 130.4 29.9Q 129.8 30.4 129.5 30.9V 35.7Q 130.2 36.8 131.5 36.8Q 132.6 36.8 133.1 35.9Q 133.7 35.1 133.7 33.2Q 133.7 31.2 133.2 30.4Q 132.7 29.5 131.7 29.5Z",
    "r": "M 138.9 38.2V 36.7H 140.4V 29.6H 138.9V 28.1H 142.1L 142.4 30.5Q 143.0 29.2 143.9 28.5Q 144.7 27.8 146.0 27.8Q 146.5 27.8 146.8 27.9Q 147.2 28.0 147.5 28.1L 147.2 31.8H 145.6V 29.8Q 144.6 29.8 143.8 30.6Q 143.0 31.5 142.6 32.9V 36.7H 144.6V 38.2Z",
    "o": "M 154.4 27.8Q 156.6 27.8 157.8 29.3Q 159.0 30.7 159.0 33.2Q 159.0 34.8 158.4 36.0Q 157.9 37.2 156.9 37.8Q 155.9 38.5 154.4 38.5Q 152.2 38.5 151.0 37.1Q 149.8 35.6 149.8 33.2Q 149.8 31.6 150.4 30.4Q 150.9 29.2 151.9 28.5Q 152.9 27.8 154.4 27.8ZM 154.4 29.5Q 153.2 29.5 152.7 30.4Q 152.1 31.3 152.1 33.2Q 152.1 35.1 152.7 36.0Q 153.2 36.8 154.4 36.8Q 155.6 36.8 156.1 35.9Q 156.7 35.1 156.7 33.2Q 156.7 31.3 156.1 30.4Q 155.6 29.5 154.4 29.5Z",
    "m": "M 168.9 27.8Q 169.4 27.8 169.9 28.1Q 170.4 28.3 170.6 29.0Q 170.9 29.6 170.9 30.7V 38.2H 169.0V 31.0Q 169.0 30.2 168.9 29.9Q 168.8 29.5 168.3 29.5Q 167.9 29.5 167.5 29.7Q 167.2 30.0 166.8 30.5V 38.2H 165.1V 31.0Q 165.1 30.2 164.9 29.9Q 164.8 29.5 164.4 29.5Q 164.0 29.5 163.6 29.7Q 163.3 30.0 162.9 30.5V 38.2H 161.0V 28.1H 162.6L 162.7 29.2Q 163.2 28.6 163.7 28.2Q 164.2 27.8 164.9 27.8Q 165.5 27.8 165.9 28.1Q 166.4 28.4 166.6 29.1Q 167.1 28.6 167.6 28.2Q 168.1 27.8 168.9 27.8Z",
    "p2": "M 178.3 27.8Q 179.7 27.8 180.5 28.5Q 181.3 29.1 181.7 30.3Q 182.0 31.5 182.0 33.2Q 182.0 34.7 181.6 35.9Q 181.1 37.1 180.3 37.8Q 179.4 38.5 178.1 38.5Q 176.5 38.5 175.5 37.4V 42.1L 173.4 42.4V 28.1H 175.3L 175.4 29.4Q 176.0 28.6 176.7 28.2Q 177.5 27.8 178.3 27.8ZM 177.7 29.5Q 177.0 29.5 176.5 29.9Q 175.9 30.4 175.5 30.9V 35.7Q 176.3 36.8 177.5 36.8Q 178.6 36.8 179.2 35.9Q 179.8 35.1 179.8 33.2Q 179.8 31.2 179.3 30.4Q 178.8 29.5 177.7 29.5Z",
    "t2": "M 193.4 37.7Q 192.8 38.1 192.0 38.3Q 191.3 38.5 190.4 38.5Q 188.7 38.5 187.7 37.6Q 186.8 36.7 186.8 35.2V 29.7H 184.6V 28.1H 186.8V 25.8L 189.0 25.6V 28.1H 192.4L 192.1 29.7H 189.0V 35.1Q 189.0 36.0 189.4 36.4Q 189.8 36.8 190.7 36.8Q 191.3 36.8 191.7 36.6Q 192.2 36.5 192.6 36.3Z",
}

# Content bounds (for calculating transforms)
CONTENT_BOUNDS = {
    "left_x": 10.4,
    "right_x": 193.4,
    "center_y": 32.0,
}


# =============================================================================
# PATH TRANSFORMATION FUNCTIONS
# =============================================================================


def translate_path(path_str: str, offset_x: float, offset_y: float) -> str:
    """
    Translate SVG path coordinates by offset.

    Args:
        path_str: SVG path d attribute string
        offset_x: Horizontal offset (positive = move right)
        offset_y: Vertical offset (positive = move down)

    Returns:
        Translated path string
    """
    result = []
    tokens = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|[-+]?[0-9]*\.?[0-9]+", path_str)

    cmd = ""
    coord_idx = 0

    for token in tokens:
        if token.isalpha() and len(token) == 1:
            cmd = token.upper()
            coord_idx = 0
            result.append(token)
        else:
            val = float(token)
            is_x = False
            is_y = False

            if cmd == "H":
                is_x = True
            elif cmd == "V":
                is_y = True
            elif cmd == "Z":
                pass
            elif cmd == "A":
                # Arc: rx ry x-rot large-arc sweep x y
                pos = coord_idx % 7
                if pos == 5:
                    is_x = True
                elif pos == 6:
                    is_y = True
                # rx, ry (pos 0, 1) don't need translation
            elif cmd in ("M", "L", "T"):
                is_x = (coord_idx % 2) == 0
                is_y = (coord_idx % 2) == 1
            elif cmd == "Q":
                is_x = (coord_idx % 4) in (0, 2)
                is_y = (coord_idx % 4) in (1, 3)
            elif cmd == "C":
                is_x = (coord_idx % 6) in (0, 2, 4)
                is_y = (coord_idx % 6) in (1, 3, 5)
            elif cmd == "S":
                is_x = (coord_idx % 4) in (0, 2)
                is_y = (coord_idx % 4) in (1, 3)

            if is_x:
                val = val + offset_x
            elif is_y:
                val = val + offset_y

            result.append(f" {val:.1f}")
            coord_idx += 1

    return "".join(result)


def make_path_element(d: str, fill: str, comment: str | None = None) -> str:
    """Create an SVG path element."""
    comment_str = f"    <!-- {comment} -->\n" if comment else ""
    return f'{comment_str}    <path d="{d}" fill="{fill}"/>'


# =============================================================================
# SVG GENERATION FUNCTIONS
# =============================================================================


def generate_wordmark(
    variant: str,  # "dark", "light", "white", "adaptive"
    tight: bool = False,
) -> str:
    """
    Generate a wordmark SVG.

    Args:
        variant: Color variant ("dark", "light", "white", "adaptive")
        tight: Whether to generate tight (scaled) version

    Returns:
        SVG content as string
    """
    colors = CONFIG["colors"]
    wordmark_config = CONFIG["wordmark"]

    if tight:
        # Content bounds from the original paths
        content_left = CONTENT_BOUNDS["left_x"]
        content_right = CONTENT_BOUNDS["right_x"]
        content_width = content_right - content_left
        # Content height (from path data, letters go roughly from y=14 to y=50)
        content_top = 14
        content_bottom = 50
        content_height = content_bottom - content_top

        h_padding = wordmark_config["tight"]["horizontal_padding"]
        v_padding = wordmark_config["tight"]["vertical_padding"]
        corner_radius = wordmark_config["tight"]["corner_radius"]

        # Calculate viewbox dimensions
        viewbox_width = round(content_width + 2 * h_padding)
        viewbox_height = round(content_height + 2 * v_padding)

        # Calculate offset to translate content to new position
        offset_x = h_padding - content_left
        offset_y = v_padding - content_top

        def transform(path: str) -> str:
            return translate_path(path, offset_x, offset_y)
    else:
        # Regular version: use original dimensions, no transformation
        corner_radius = wordmark_config["regular"]["corner_radius"]
        viewbox_width = wordmark_config["regular"]["viewbox_width"]
        viewbox_height = wordmark_config["regular"]["viewbox_height"]

        def transform(path: str) -> str:
            return path  # No transformation needed

    # Build SVG based on variant
    if variant == "adaptive":
        return generate_adaptive_wordmark(
            viewbox_width, viewbox_height, corner_radius, transform
        )

    # Determine colors based on variant
    if variant == "dark":
        bg_color = colors["dark_bg"]
        icon_ag_color = colors["cream"]
        prompt_color = colors["off_white"]
    elif variant == "light":
        bg_color = colors["light_bg"]
        icon_ag_color = colors["dark_text"]
        prompt_color = colors["dark_text"]
    elif variant == "white":
        bg_color = colors["white_bg"]
        icon_ag_color = colors["dark_text"]
        prompt_color = colors["dark_text"]
    else:
        raise ValueError(f"Unknown variant: {variant}")

    # Build path elements
    paths = []

    # Icon
    paths.append(
        make_path_element(
            transform(ICON_PATHS["left_bracket"]), colors["amber"], "Left bracket"
        )
    )
    paths.append(
        make_path_element(transform(ICON_PATHS["icon_a"]), icon_ag_color, "Icon 'a'")
    )
    paths.append(
        make_path_element(transform(ICON_PATHS["icon_g"]), icon_ag_color, "Icon 'g'")
    )
    paths.append(
        make_path_element(
            transform(ICON_PATHS["right_bracket"]), colors["amber"], "Right bracket"
        )
    )

    # Text "agent" (amber)
    for letter in ["a", "g", "e", "n", "t"]:
        paths.append(make_path_element(transform(TEXT_PATHS[letter]), colors["amber"]))

    # Text "prompt" (off-white or dark)
    for letter in ["p", "r", "o", "m", "p2", "t2"]:
        paths.append(make_path_element(transform(TEXT_PATHS[letter]), prompt_color))

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {viewbox_width} {viewbox_height}">
  <rect width="{viewbox_width}" height="{viewbox_height}" rx="{corner_radius}" fill="{bg_color}"/>
  <g>
{chr(10).join(paths)}
  </g>
</svg>'''

    return svg


def generate_adaptive_wordmark(
    viewbox_width: int,
    viewbox_height: int,
    corner_radius: int,
    transform,
) -> str:
    """Generate adaptive wordmark that responds to system color scheme."""
    colors = CONFIG["colors"]

    # Icon brackets (always amber)
    bracket_left = make_path_element(
        transform(ICON_PATHS["left_bracket"]), colors["amber"]
    )
    bracket_right = make_path_element(
        transform(ICON_PATHS["right_bracket"]), colors["amber"]
    )

    # Icon "ag" - light version (cream, for dark bg)
    icon_ag_light = [
        make_path_element(transform(ICON_PATHS["icon_a"]), colors["cream"]),
        make_path_element(transform(ICON_PATHS["icon_g"]), colors["cream"]),
    ]

    # Icon "ag" - dark version (dark text, for light bg)
    icon_ag_dark = [
        make_path_element(transform(ICON_PATHS["icon_a"]), colors["dark_text"]),
        make_path_element(transform(ICON_PATHS["icon_g"]), colors["dark_text"]),
    ]

    # Text "agent" (always amber)
    agent_paths = []
    for letter in ["a", "g", "e", "n", "t"]:
        agent_paths.append(
            make_path_element(transform(TEXT_PATHS[letter]), colors["amber"])
        )

    # Text "prompt" - light version (for dark bg)
    prompt_light = []
    for letter in ["p", "r", "o", "m", "p2", "t2"]:
        prompt_light.append(
            make_path_element(transform(TEXT_PATHS[letter]), colors["off_white"])
        )

    # Text "prompt" - dark version (for light bg)
    prompt_dark = []
    for letter in ["p", "r", "o", "m", "p2", "t2"]:
        prompt_dark.append(
            make_path_element(transform(TEXT_PATHS[letter]), colors["dark_text"])
        )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {viewbox_width} {viewbox_height}">
  <style>
    .bg-dark {{ opacity: 1; }}
    .bg-light {{ opacity: 0; }}
    .text-light {{ opacity: 1; }}
    .text-dark {{ opacity: 0; }}
    @media (prefers-color-scheme: dark) {{
      .bg-dark {{ opacity: 0; }}
      .bg-light {{ opacity: 1; }}
      .text-light {{ opacity: 0; }}
      .text-dark {{ opacity: 1; }}
    }}
  </style>

  <!-- Backgrounds -->
  <rect class="bg-dark" width="{viewbox_width}" height="{viewbox_height}" rx="{corner_radius}" fill="{colors["dark_bg"]}"/>
  <rect class="bg-light" width="{viewbox_width}" height="{viewbox_height}" rx="{corner_radius}" fill="{colors["light_bg"]}"/>

  <!-- Brackets (always amber) -->
{bracket_left}
{bracket_right}

  <!-- Icon "ag" - light mode (for dark bg) -->
  <g class="text-light">
{chr(10).join(icon_ag_light)}
  </g>

  <!-- Icon "ag" - dark mode (for light bg) -->
  <g class="text-dark">
{chr(10).join(icon_ag_dark)}
  </g>

  <!-- "agent" (always amber) -->
  <g>
{chr(10).join(agent_paths)}
  </g>

  <!-- "prompt" - light mode -->
  <g class="text-light">
{chr(10).join(prompt_light)}
  </g>

  <!-- "prompt" - dark mode -->
  <g class="text-dark">
{chr(10).join(prompt_dark)}
  </g>
</svg>'''

    return svg


# =============================================================================
# MAIN
# =============================================================================


def main():
    output_dir = Path(CONFIG["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    wordmark_config = CONFIG["wordmark"]
    variants = ["dark", "light", "white", "adaptive"]

    print("Generating logos...")
    print(
        f"  Regular padding: {wordmark_config['regular']['horizontal_padding']}px h, "
        f"{wordmark_config['regular']['vertical_padding']}px v"
    )
    print(
        f"  Tight padding:   {wordmark_config['tight']['horizontal_padding']}px h, "
        f"{wordmark_config['tight']['vertical_padding']}px v"
    )
    print(f"  Output directory: {output_dir}")
    print()

    for variant in variants:
        # Regular version
        svg = generate_wordmark(variant, tight=False)
        filename = f"wordmark-{variant}.svg"
        filepath = output_dir / filename
        filepath.write_text(svg)
        print(f"  ✓ {filename}")

        # Tight version
        svg = generate_wordmark(variant, tight=True)
        filename = f"wordmark-{variant}-tight.svg"
        filepath = output_dir / filename
        filepath.write_text(svg)
        print(f"  ✓ {filename}")

    print()
    print("Done! Generated 8 wordmark files.")
    print()
    print("To adjust padding, edit CONFIG at the top of this script:")
    print(
        f"  CONFIG['wordmark']['tight']['horizontal_padding'] = "
        f"{wordmark_config['tight']['horizontal_padding']}"
    )
    print(
        f"  CONFIG['wordmark']['tight']['vertical_padding'] = "
        f"{wordmark_config['tight']['vertical_padding']}"
    )


if __name__ == "__main__":
    main()
