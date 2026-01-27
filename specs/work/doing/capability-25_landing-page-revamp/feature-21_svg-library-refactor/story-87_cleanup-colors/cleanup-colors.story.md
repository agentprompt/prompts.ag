# Story: Cleanup Colors

## Functional Requirements

### FR1: Remove redundant off_white color

```gherkin
GIVEN CONFIG["colors"] defines both "light_bg" and "off_white" with same value "#fafafa"
WHEN I remove the redundant off_white entry
THEN only light_bg remains with value "#fafafa"
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Remove off_white from CONFIG["colors"]

### FR2: Update references to use light_bg

```gherkin
GIVEN some functions reference CONFIG["colors"]["off_white"]
WHEN I update these references
THEN they use CONFIG["colors"]["light_bg"] instead
AND generated output is identical
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Replace off_white references with light_bg

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component    | Level | Justification                  |
| ------------ | ----- | ------------------------------ |
| Color config | 1     | Static analysis of config dict |
| Color usage  | 1     | Grep for string references     |

### When to Escalate

This story stays at Level 1 because:

- This is a simple refactoring of constant references
- Visual output verification is a feature-level concern

## Unit Tests (Level 1)

```python
# tests/unit/test_color_config.py
from pathlib import Path
import ast


class TestColorConfig:
    """Level 1: Verify color configuration is clean"""

    def test_no_off_white_in_config(self):
        """GIVEN generate_logos.py WHEN parsed THEN no off_white color defined"""
        # Given
        script = Path("assets/generate/generate_logos.py").read_text()

        # Then: off_white should not appear as a config key
        assert '"off_white"' not in script
        assert "'off_white'" not in script

    def test_light_bg_is_defined(self):
        """GIVEN generate_logos.py WHEN parsed THEN light_bg color exists"""
        # Given
        script = Path("assets/generate/generate_logos.py").read_text()

        # Then
        assert "light_bg" in script

    def test_no_off_white_references(self):
        """GIVEN generate_logos.py WHEN searched THEN no off_white usage"""
        # Given
        script = Path("assets/generate/generate_logos.py").read_text()

        # Then: No references to off_white anywhere
        assert "off_white" not in script.lower()

    def test_fafafa_only_for_light_bg(self):
        """GIVEN generate_logos.py WHEN parsed THEN #fafafa only used for light_bg"""
        # Given
        script = Path("assets/generate/generate_logos.py").read_text()

        # Then: #fafafa should appear exactly once (for light_bg)
        count = script.lower().count("#fafafa")
        assert count == 1, f"#fafafa appears {count} times, expected 1"
```

## Quality Requirements

### QR1: No Behavioral Change

**Requirement:** Refactoring must not change generated SVG output
**Target:** Byte-identical output before/after
**Validation:** Diff generated SVGs

### QR2: Single Source of Truth

**Requirement:** Each color value defined exactly once
**Target:** No duplicate hex values in CONFIG
**Validation:** Code review of CONFIG dict

## Completion Criteria

- [ ] off_white removed from CONFIG["colors"]
- [ ] All off_white references replaced with light_bg
- [ ] #fafafa appears exactly once in config
- [ ] Generated SVGs unchanged (manual diff check)
