"""
Level 1: Unit tests for color configuration cleanup.

Verifies that redundant off_white color has been removed and all references
have been updated to use light_bg instead.
"""

from pathlib import Path


class TestColorConfig:
    """Level 1: Verify color configuration is clean."""

    def test_no_off_white_in_config(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN no off_white color defined."""
        # Given
        script_path = Path("assets/generate/generate_logos.py")
        script = script_path.read_text()

        # Then: off_white should not appear as a config key
        assert '"off_white"' not in script
        assert "'off_white'" not in script

    def test_light_bg_is_defined(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN light_bg color exists."""
        # Given
        script_path = Path("assets/generate/generate_logos.py")
        script = script_path.read_text()

        # Then
        assert "light_bg" in script

    def test_no_off_white_references(self) -> None:
        """GIVEN generate_logos.py WHEN searched THEN no off_white usage."""
        # Given
        script_path = Path("assets/generate/generate_logos.py")
        script = script_path.read_text()

        # Then: No references to off_white anywhere
        assert "off_white" not in script.lower()

    def test_fafafa_only_for_light_bg(self) -> None:
        """GIVEN generate_logos.py WHEN parsed THEN #fafafa only used for light_bg."""
        # Given
        script_path = Path("assets/generate/generate_logos.py")
        script = script_path.read_text()

        # Then: #fafafa should appear exactly once (for light_bg)
        count = script.lower().count("#fafafa")
        assert count == 1, f"#fafafa appears {count} times, expected 1"
