# Story: SVGPathTools Transforms

## Functional Requirements

### FR1: Replace translate_path with svgpathtools

```gherkin
GIVEN the existing translate_path() function uses manual regex parsing
WHEN I replace it with svgpathtools
THEN SVG path data is translated using the library's translate method
AND output paths are mathematically equivalent to the original implementation
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Replace translate_path() implementation

### FR2: Replace scale_and_translate_path with svgpathtools

```gherkin
GIVEN the existing scale_and_translate_path() function uses manual regex parsing
WHEN I replace it with svgpathtools
THEN SVG path data is scaled and translated using the library's methods
AND output paths are mathematically equivalent to the original implementation
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Replace scale_and_translate_path() implementation

### FR3: Create unified transform_path function

```gherkin
GIVEN both translation and scaling are needed
WHEN I create a unified transform_path() function
THEN it accepts optional translate and scale parameters
AND applies transformations in correct order (scale first, then translate)
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add unified transform_path() function, remove old functions

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component          | Level | Justification                         |
| ------------------ | ----- | ------------------------------------- |
| Path translation   | 1     | Pure function, string in → string out |
| Path scaling       | 1     | Pure function, string in → string out |
| Combined transform | 1     | Pure function, composition of above   |

### When to Escalate

This story stays at Level 1 because:

- Path transformation is a pure function (input path string → output path string)
- No filesystem or external tool interaction needed
- Visual verification of SVG output is a feature-level concern

## Unit Tests (Level 1)

```python
# tests/unit/test_path_transforms.py
import pytest
from assets.generate.generate_logos import transform_path


class TestTransformPath:
    """Level 1: Pure function tests for SVG path transformations"""

    def test_translate_moves_path_coordinates(self):
        """GIVEN simple path WHEN translated THEN coordinates shift by offset"""
        # Given: A simple line from (0,0) to (10,10)
        input_path = "M 0 0 L 10 10"

        # When: Translate by (5, 5)
        result = transform_path(input_path, translate=(5, 5))

        # Then: Path is shifted
        # Note: svgpathtools may normalize path format
        assert "5" in result  # Start point moved
        assert "15" in result  # End point moved

    def test_scale_multiplies_coordinates(self):
        """GIVEN simple path WHEN scaled THEN coordinates multiply by factor"""
        # Given: A square path
        input_path = "M 0 0 L 10 0 L 10 10 L 0 10 Z"

        # When: Scale by 2
        result = transform_path(input_path, scale=2.0)

        # Then: Coordinates are doubled
        assert "20" in result

    def test_scale_and_translate_combined(self):
        """GIVEN path WHEN scaled then translated THEN both applied correctly"""
        # Given: Simple path
        input_path = "M 0 0 L 10 10"

        # When: Scale by 2, then translate by (5, 5)
        result = transform_path(input_path, translate=(5, 5), scale=2.0)

        # Then: Scale applied first (0→0, 10→20), then translate (0→5, 20→25)
        assert "5" in result
        assert "25" in result

    def test_identity_transform_preserves_path(self):
        """GIVEN path WHEN no transform applied THEN path unchanged"""
        # Given
        input_path = "M 10 20 L 30 40"

        # When: No translation or scaling
        result = transform_path(input_path)

        # Then: Path data preserved (may be normalized)
        assert "10" in result
        assert "20" in result

    def test_complex_path_with_curves(self):
        """GIVEN path with curves WHEN transformed THEN curves preserved"""
        # Given: Path with cubic bezier
        input_path = "M 0 0 C 10 20 30 40 50 60"

        # When: Translate
        result = transform_path(input_path, translate=(100, 100))

        # Then: Curve command preserved, coordinates shifted
        assert "C" in result or "c" in result  # Curve command exists
        assert "100" in result  # Shifted coordinates
```

## Quality Requirements

### QR1: Backward Compatibility

**Requirement:** Generated SVGs must be visually identical to previous output
**Target:** No visual regression in logo variants
**Validation:** Compare generated SVGs before/after refactor

### QR2: No Manual Path Parsing

**Requirement:** All SVG path manipulation must use svgpathtools, no regex
**Target:** Zero regex operations on path data
**Validation:** Code review - no `re.` calls on path strings

## Completion Criteria

- [ ] translate_path() removed or replaced
- [ ] scale_and_translate_path() removed or replaced
- [ ] New transform_path() uses svgpathtools exclusively
- [ ] All Level 1 unit tests pass
- [ ] Generated logos visually match previous output (manual check)
