"""
Unit tests for shell wrapper script.

Level 1: Static analysis of shell script structure.
Tests verify script content and structure without executing it.
"""

from pathlib import Path

# =============================================================================
# CONSTANTS
# =============================================================================

SCRIPT_PATH = Path("scripts/generate-logos.sh")
EXPECTED_MAX_NON_COMMENT_LINES = 10
PATTERN_STRICT_MODE = "set -euo pipefail"
PATTERN_STRICT_MODE_ALT = "set -e"
PATTERN_UV_RUN = "uv run"
PATTERN_ARG_PASSTHROUGH = "$@"
FORBIDDEN_PATTERN_AWK = "awk"
FORBIDDEN_PATTERN_YAML_FILE = "asset-mappings"


# =============================================================================
# TEST CASES
# =============================================================================


class TestShellWrapper:
    """Level 1: Static analysis of shell script structure"""

    def test_script_has_strict_mode(self) -> None:
        """GIVEN generate-logos.sh WHEN read THEN has set -euo pipefail"""
        # Given
        script = SCRIPT_PATH.read_text()

        # Then
        assert PATTERN_STRICT_MODE in script or PATTERN_STRICT_MODE_ALT in script, (
            f"Script must contain '{PATTERN_STRICT_MODE}' or '{PATTERN_STRICT_MODE_ALT}'"
        )

    def test_script_uses_uv_run(self) -> None:
        """GIVEN generate-logos.sh WHEN read THEN invokes uv run"""
        # Given
        script = SCRIPT_PATH.read_text()

        # Then
        assert PATTERN_UV_RUN in script, f"Script must invoke '{PATTERN_UV_RUN}'"

    def test_script_no_yaml_parsing(self) -> None:
        """GIVEN generate-logos.sh WHEN read THEN no YAML regex parsing"""
        # Given
        script = SCRIPT_PATH.read_text()

        # Then: No awk/sed/grep YAML manipulation patterns
        script_lower = script.lower()
        has_awk = FORBIDDEN_PATTERN_AWK in script_lower
        references_yaml_file = FORBIDDEN_PATTERN_YAML_FILE in script

        assert not (has_awk and "yaml" in script_lower), (
            "Script must not contain awk with YAML parsing"
        )
        assert not references_yaml_file, (
            f"Script must not reference '{FORBIDDEN_PATTERN_YAML_FILE}' file directly"
        )

    def test_script_passes_arguments(self) -> None:
        """GIVEN generate-logos.sh WHEN read THEN passes $@ to Python"""
        # Given
        script = SCRIPT_PATH.read_text()

        # Then
        assert PATTERN_ARG_PASSTHROUGH in script, (
            f"Script must pass through arguments with '{PATTERN_ARG_PASSTHROUGH}'"
        )

    def test_script_is_minimal(self) -> None:
        """GIVEN generate-logos.sh WHEN read THEN is under 10 non-comment lines"""
        # Given
        script = SCRIPT_PATH.read_text()
        lines = [
            line
            for line in script.splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]

        # Then: Minimal wrapper should be very short
        actual_count = len(lines)
        assert actual_count <= EXPECTED_MAX_NON_COMMENT_LINES, (
            f"Script has {actual_count} non-comment lines, "
            f"expected <= {EXPECTED_MAX_NON_COMMENT_LINES}"
        )
