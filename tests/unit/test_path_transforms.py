"""
Level 1 Unit Tests: SVG Path Transformations using svgpathtools.

Tests verify that transform_path() correctly handles:
- Translation (moving coordinates)
- Scaling (multiplying coordinates)
- Combined transforms (scale first, then translate)
- Identity transforms (no-op)
- Complex paths with curves
"""

import pytest
from svgpathtools import parse_path  # type: ignore[import-untyped]

# Constants - paths from the actual codebase
SIMPLE_LINE_PATH = "M 0 0 L 10 10"
SQUARE_PATH = "M 0 0 L 10 0 L 10 10 L 0 10 Z"
CUBIC_BEZIER_PATH = "M 0 0 C 10 20 30 40 50 60"
QUADRATIC_PATH = "M 10 20 L 30 40"

# Real icon path from generate_logos.py (left bracket)
LEFT_BRACKET_PATH = (
    "M 10.4 32.0L 18.6 13.8L 18.6 18.6L 13.8 32.0L 18.6 45.4L 18.6 50.2L 10.4 32.0Z"
)

# Transform parameters
TRANSLATE_5_5 = (5.0, 5.0)
TRANSLATE_100_100 = (100.0, 100.0)
SCALE_2X = 2.0
IDENTITY_TRANSLATE = (0.0, 0.0)
IDENTITY_SCALE = 1.0


def get_path_bounds(d: str) -> tuple[float, float, float, float]:
    """Get bounding box (xmin, xmax, ymin, ymax) of a path."""
    path = parse_path(d)
    return path.bbox()  # type: ignore[no-any-return]


class TestTranslateMovesCoordinates:
    """Level 1: Verify translation shifts all coordinates by offset."""

    def test_translate_simple_line_shifts_start_point(self) -> None:
        """
        GIVEN a simple line from (0,0) to (10,10)
        WHEN translated by (5, 5)
        THEN the start point moves to (5, 5).
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(SIMPLE_LINE_PATH, translate=TRANSLATE_5_5)

        # Parse result and check bounds shifted
        xmin, xmax, ymin, ymax = get_path_bounds(result)
        assert xmin == pytest.approx(5.0, abs=0.1)
        assert ymin == pytest.approx(5.0, abs=0.1)

    def test_translate_simple_line_shifts_end_point(self) -> None:
        """
        GIVEN a simple line from (0,0) to (10,10)
        WHEN translated by (5, 5)
        THEN the end point moves to (15, 15).
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(SIMPLE_LINE_PATH, translate=TRANSLATE_5_5)

        xmin, xmax, ymin, ymax = get_path_bounds(result)
        assert xmax == pytest.approx(15.0, abs=0.1)
        assert ymax == pytest.approx(15.0, abs=0.1)

    def test_translate_preserves_path_shape(self) -> None:
        """
        GIVEN a square path
        WHEN translated
        THEN the path dimensions remain unchanged.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(SQUARE_PATH)
        original_width = original_bounds[1] - original_bounds[0]
        original_height = original_bounds[3] - original_bounds[2]

        result = transform_path(SQUARE_PATH, translate=TRANSLATE_100_100)

        result_bounds = get_path_bounds(result)
        result_width = result_bounds[1] - result_bounds[0]
        result_height = result_bounds[3] - result_bounds[2]

        assert result_width == pytest.approx(original_width, abs=0.1)
        assert result_height == pytest.approx(original_height, abs=0.1)


class TestScaleMultipliesCoordinates:
    """Level 1: Verify scaling multiplies all coordinates by factor."""

    def test_scale_doubles_path_dimensions(self) -> None:
        """
        GIVEN a square path from (0,0) to (10,10)
        WHEN scaled by 2
        THEN the path spans from (0,0) to (20,20).
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(SQUARE_PATH, scale=SCALE_2X)

        xmin, xmax, ymin, ymax = get_path_bounds(result)
        assert xmax == pytest.approx(20.0, abs=0.1)
        assert ymax == pytest.approx(20.0, abs=0.1)

    def test_scale_preserves_origin_at_zero(self) -> None:
        """
        GIVEN a path starting at origin (0,0)
        WHEN scaled
        THEN the origin point remains at (0,0).
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(SIMPLE_LINE_PATH, scale=SCALE_2X)

        xmin, xmax, ymin, ymax = get_path_bounds(result)
        assert xmin == pytest.approx(0.0, abs=0.1)
        assert ymin == pytest.approx(0.0, abs=0.1)


class TestScaleAndTranslateCombined:
    """Level 1: Verify correct order - scale first, then translate."""

    def test_scale_then_translate_order(self) -> None:
        """
        GIVEN a line from (0,0) to (10,10)
        WHEN scaled by 2, then translated by (5, 5)
        THEN the path spans from (5,5) to (25,25).

        Scale first: (0,0)→(0,0), (10,10)→(20,20)
        Then translate: (0,0)→(5,5), (20,20)→(25,25)
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(
            SIMPLE_LINE_PATH, translate=TRANSLATE_5_5, scale=SCALE_2X
        )

        xmin, xmax, ymin, ymax = get_path_bounds(result)
        assert xmin == pytest.approx(5.0, abs=0.1)
        assert ymin == pytest.approx(5.0, abs=0.1)
        assert xmax == pytest.approx(25.0, abs=0.1)
        assert ymax == pytest.approx(25.0, abs=0.1)


class TestIdentityTransform:
    """Level 1: Verify no-op transforms preserve path data."""

    def test_no_transform_preserves_bounds(self) -> None:
        """
        GIVEN a path with known coordinates
        WHEN no transformation is applied
        THEN the path bounds remain unchanged.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(QUADRATIC_PATH)

        result = transform_path(QUADRATIC_PATH)

        result_bounds = get_path_bounds(result)
        assert result_bounds[0] == pytest.approx(original_bounds[0], abs=0.1)
        assert result_bounds[1] == pytest.approx(original_bounds[1], abs=0.1)
        assert result_bounds[2] == pytest.approx(original_bounds[2], abs=0.1)
        assert result_bounds[3] == pytest.approx(original_bounds[3], abs=0.1)

    def test_explicit_identity_values_preserve_bounds(self) -> None:
        """
        GIVEN a path
        WHEN transform called with explicit identity values (0,0) and scale=1.0
        THEN the path bounds remain unchanged.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(QUADRATIC_PATH)

        result = transform_path(
            QUADRATIC_PATH, translate=IDENTITY_TRANSLATE, scale=IDENTITY_SCALE
        )

        result_bounds = get_path_bounds(result)
        assert result_bounds[0] == pytest.approx(original_bounds[0], abs=0.1)
        assert result_bounds[1] == pytest.approx(original_bounds[1], abs=0.1)


class TestComplexPathsWithCurves:
    """Level 1: Verify bezier curves are handled correctly."""

    def test_cubic_bezier_translates_correctly(self) -> None:
        """
        GIVEN a path with cubic bezier curve
        WHEN translated by (100, 100)
        THEN all control points and endpoints shift.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(CUBIC_BEZIER_PATH)

        result = transform_path(CUBIC_BEZIER_PATH, translate=TRANSLATE_100_100)

        result_bounds = get_path_bounds(result)
        # All bounds should shift by 100
        assert result_bounds[0] == pytest.approx(original_bounds[0] + 100, abs=0.1)
        assert result_bounds[1] == pytest.approx(original_bounds[1] + 100, abs=0.1)
        assert result_bounds[2] == pytest.approx(original_bounds[2] + 100, abs=0.1)
        assert result_bounds[3] == pytest.approx(original_bounds[3] + 100, abs=0.1)

    def test_curve_command_preserved_in_output(self) -> None:
        """
        GIVEN a path with cubic bezier curve (C command)
        WHEN transformed
        THEN the output contains curve command.
        """
        from assets.generate.generate_logos import transform_path

        result = transform_path(CUBIC_BEZIER_PATH, translate=TRANSLATE_5_5)

        # svgpathtools may use uppercase or lowercase commands
        assert "C" in result.upper()


class TestRealIconPaths:
    """Level 1: Verify with actual icon paths from the codebase."""

    def test_left_bracket_path_translates(self) -> None:
        """
        GIVEN the actual left bracket path from generate_logos.py
        WHEN translated
        THEN the path bounds shift correctly.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(LEFT_BRACKET_PATH)

        result = transform_path(LEFT_BRACKET_PATH, translate=TRANSLATE_5_5)

        result_bounds = get_path_bounds(result)
        assert result_bounds[0] == pytest.approx(original_bounds[0] + 5, abs=0.1)
        assert result_bounds[2] == pytest.approx(original_bounds[2] + 5, abs=0.1)

    def test_left_bracket_path_scales(self) -> None:
        """
        GIVEN the actual left bracket path
        WHEN scaled by 2
        THEN the path dimensions double.
        """
        from assets.generate.generate_logos import transform_path

        original_bounds = get_path_bounds(LEFT_BRACKET_PATH)
        original_width = original_bounds[1] - original_bounds[0]
        original_height = original_bounds[3] - original_bounds[2]

        result = transform_path(LEFT_BRACKET_PATH, scale=SCALE_2X)

        result_bounds = get_path_bounds(result)
        result_width = result_bounds[1] - result_bounds[0]
        result_height = result_bounds[3] - result_bounds[2]

        assert result_width == pytest.approx(original_width * 2, abs=0.1)
        assert result_height == pytest.approx(original_height * 2, abs=0.1)
