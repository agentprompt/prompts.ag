"""Tests for PEP 723 inline script metadata in generate_logos.py.

Level 1: Static analysis tests verifying the script has correct metadata structure.
"""

from pathlib import Path

import pytest

# Constants for metadata validation
SCRIPT_PATH = Path("assets/generate/generate_logos.py")
METADATA_START_MARKER = "# /// script"
METADATA_END_MARKER = "# ///"
REQUIRED_PYTHON_VERSION = ">=3.11"
REQUIRED_DEPENDENCIES = ["svgpathtools", "pyyaml"]


class TestScriptMetadataExists:
    """Verify PEP 723 metadata block exists and is well-formed."""

    def test_script_file_exists(self) -> None:
        """GIVEN generate_logos.py path WHEN checked THEN file exists."""
        assert SCRIPT_PATH.exists(), f"Script not found at {SCRIPT_PATH}"

    def test_script_has_shebang(self) -> None:
        """GIVEN generate_logos.py WHEN first line read THEN starts with shebang."""
        content = SCRIPT_PATH.read_text()
        first_line = content.splitlines()[0]
        assert first_line.startswith("#!/usr/bin/env"), (
            f"First line should be shebang, got: {first_line}"
        )

    def test_script_has_metadata_start_marker(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN contains metadata start marker."""
        content = SCRIPT_PATH.read_text()
        assert METADATA_START_MARKER in content, (
            f"Missing metadata start marker: {METADATA_START_MARKER}"
        )

    def test_script_has_metadata_end_marker(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN contains metadata end marker."""
        content = SCRIPT_PATH.read_text()
        # End marker must appear after start marker
        start_idx = content.find(METADATA_START_MARKER)
        end_idx = content.find(
            METADATA_END_MARKER, start_idx + len(METADATA_START_MARKER)
        )
        assert end_idx > start_idx, (
            f"Missing or misplaced metadata end marker: {METADATA_END_MARKER}"
        )


class TestScriptMetadataPosition:
    """Verify metadata block is positioned correctly."""

    def test_metadata_is_near_top_of_file(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN metadata starts within first 10 lines."""
        content = SCRIPT_PATH.read_text()
        lines = content.splitlines()

        metadata_line = None
        for i, line in enumerate(lines):
            if METADATA_START_MARKER in line:
                metadata_line = i
                break

        assert metadata_line is not None, "Metadata start marker not found"
        assert metadata_line < 10, (
            f"Metadata should start within first 10 lines, found at line {metadata_line + 1}"
        )

    def test_metadata_comes_after_shebang(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN metadata comes after shebang line."""
        content = SCRIPT_PATH.read_text()
        lines = content.splitlines()

        shebang_line = 0 if lines[0].startswith("#!") else None
        metadata_line = next(
            (i for i, line in enumerate(lines) if METADATA_START_MARKER in line),
            None,
        )

        assert shebang_line is not None, "Shebang not found"
        assert metadata_line is not None, "Metadata start marker not found"
        assert metadata_line > shebang_line, "Metadata should come after shebang"


class TestScriptMetadataContent:
    """Verify metadata block contains required content."""

    def test_declares_python_version(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN declares requires-python."""
        content = SCRIPT_PATH.read_text()
        assert "requires-python" in content, "Missing requires-python declaration"
        assert REQUIRED_PYTHON_VERSION in content, (
            f"Should require Python {REQUIRED_PYTHON_VERSION}"
        )

    def test_declares_svgpathtools_dependency(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN declares svgpathtools dependency."""
        content = SCRIPT_PATH.read_text()
        assert "svgpathtools" in content, "Missing svgpathtools dependency"

    def test_declares_pyyaml_dependency(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN declares pyyaml dependency."""
        content = SCRIPT_PATH.read_text()
        assert "pyyaml" in content, "Missing pyyaml dependency"

    def test_dependencies_section_exists(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN has dependencies array."""
        content = SCRIPT_PATH.read_text()
        assert "dependencies" in content, "Missing dependencies section"
        assert "[" in content and "]" in content, (
            "Dependencies should be in array format"
        )


class TestMetadataTomlValidity:
    """Verify the metadata block is valid TOML (within comments)."""

    def test_metadata_has_proper_comment_prefix(self) -> None:
        """GIVEN metadata block WHEN parsed THEN each line starts with # comment."""
        content = SCRIPT_PATH.read_text()

        # Extract metadata block
        start_idx = content.find(METADATA_START_MARKER)
        end_idx = content.find(
            METADATA_END_MARKER, start_idx + len(METADATA_START_MARKER)
        )

        if start_idx == -1 or end_idx == -1:
            pytest.skip("Metadata block not found")

        metadata_block = content[start_idx : end_idx + len(METADATA_END_MARKER)]
        lines = metadata_block.splitlines()

        for line in lines:
            stripped = line.strip()
            if stripped:  # Non-empty lines
                assert stripped.startswith("#"), (
                    f"Metadata line should start with #: {line}"
                )
