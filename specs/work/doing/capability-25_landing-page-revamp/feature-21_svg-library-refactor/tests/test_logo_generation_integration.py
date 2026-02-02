"""Feature Integration Tests: SVG Library Refactor

Level 2 tests verifying the full logo generation pipeline works end-to-end.
"""

import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml


# Path to the project root (prompts.ag)
# tests -> feature-21 -> capability-25 -> doing -> work -> specs -> prompts.ag
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.parent.parent.parent

# Constants
YAML_KEY_SOURCE = "source"
YAML_KEY_DEST = "dest"


def iter_mappings(mappings: dict) -> list[tuple[str, dict]]:
    """Iterate over all mappings across categories.

    Returns list of (category, mapping) tuples.
    """
    result = []
    for category, items in mappings.items():
        for mapping in items:
            result.append((category, mapping))
    return result


class TestLogoGenerationPipeline:
    """FI1: Full logo generation pipeline"""

    def test_logo_generation_script_succeeds(self) -> None:
        """GIVEN generate_logos.py WHEN run with uv THEN exits successfully"""
        result = subprocess.run(
            ["uv", "run", "assets/generate/generate_logos.py"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
        )

        assert result.returncode == 0, f"Script failed: {result.stderr}"

    def test_all_mapped_assets_exist(self) -> None:
        """GIVEN asset-mappings.yaml WHEN generation completes THEN all dest files exist"""
        # Load mappings
        mappings_file = PROJECT_ROOT / "assets" / "generate" / "asset-mappings.yaml"
        with open(mappings_file) as f:
            mappings = yaml.safe_load(f)

        project_root = PROJECT_ROOT

        # Verify each mapped asset exists
        missing = []
        for category, mapping in iter_mappings(mappings):
            dest_path = project_root / mapping[YAML_KEY_DEST]
            if not dest_path.exists():
                missing.append(f"{category}/{mapping[YAML_KEY_DEST]}")

        assert not missing, f"Missing assets at destination: {missing}"

    def test_generated_assets_are_non_empty(self) -> None:
        """GIVEN deployed assets WHEN checked THEN all have content"""
        mappings_file = PROJECT_ROOT / "assets" / "generate" / "asset-mappings.yaml"
        with open(mappings_file) as f:
            mappings = yaml.safe_load(f)

        project_root = PROJECT_ROOT

        empty = []
        for category, mapping in iter_mappings(mappings):
            dest_path = project_root / mapping[YAML_KEY_DEST]
            if dest_path.exists() and dest_path.stat().st_size == 0:
                empty.append(f"{category}/{mapping[YAML_KEY_DEST]}")

        assert not empty, f"Empty assets at destination: {empty}"


class TestSvgValidity:
    """FI2: SVG validity checks"""

    def test_generated_svgs_are_well_formed_xml(self) -> None:
        """GIVEN generated SVGs WHEN parsed as XML THEN no parse errors"""
        mappings_file = PROJECT_ROOT / "assets" / "generate" / "asset-mappings.yaml"
        with open(mappings_file) as f:
            mappings = yaml.safe_load(f)

        project_root = PROJECT_ROOT

        parse_errors = []
        for category, mapping in iter_mappings(mappings):
            dest_path = project_root / mapping[YAML_KEY_DEST]
            if dest_path.exists() and dest_path.suffix == ".svg":
                try:
                    ET.parse(dest_path)
                except ET.ParseError as e:
                    parse_errors.append(f"{category}/{mapping[YAML_KEY_DEST]}: {e}")

        assert not parse_errors, f"SVG parse errors: {parse_errors}"

    def test_generated_svgs_have_svg_root_element(self) -> None:
        """GIVEN generated SVGs WHEN parsed THEN root element is <svg>"""
        mappings_file = PROJECT_ROOT / "assets" / "generate" / "asset-mappings.yaml"
        with open(mappings_file) as f:
            mappings = yaml.safe_load(f)

        project_root = PROJECT_ROOT

        invalid = []
        for category, mapping in iter_mappings(mappings):
            dest_path = project_root / mapping[YAML_KEY_DEST]
            if dest_path.exists() and dest_path.suffix == ".svg":
                tree = ET.parse(dest_path)
                root = tree.getroot()
                # SVG namespace handling
                tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
                if tag != "svg":
                    invalid.append(
                        f"{category}/{mapping[YAML_KEY_DEST]}: root is <{tag}>, expected <svg>"
                    )

        assert not invalid, f"Invalid SVG structure: {invalid}"

    def test_generated_svgs_have_viewbox(self) -> None:
        """GIVEN generated SVGs WHEN checked THEN all have viewBox attribute"""
        mappings_file = PROJECT_ROOT / "assets" / "generate" / "asset-mappings.yaml"
        with open(mappings_file) as f:
            mappings = yaml.safe_load(f)

        project_root = PROJECT_ROOT

        missing_viewbox = []
        for category, mapping in iter_mappings(mappings):
            dest_path = project_root / mapping[YAML_KEY_DEST]
            if dest_path.exists() and dest_path.suffix == ".svg":
                tree = ET.parse(dest_path)
                root = tree.getroot()
                if "viewBox" not in root.attrib:
                    missing_viewbox.append(f"{category}/{mapping[YAML_KEY_DEST]}")

        assert not missing_viewbox, f"SVGs missing viewBox: {missing_viewbox}"
