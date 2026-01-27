# Story: UV Script Metadata

## Functional Requirements

### FR1: Add inline script metadata to generate_logos.py

```gherkin
GIVEN generate_logos.py exists without dependency management
WHEN I add PEP 723 inline script metadata
THEN the script declares Python >=3.11 and dependencies (svgpathtools, pyyaml)
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add inline script metadata block after shebang

### FR2: Script runs via uv without prior setup

```gherkin
GIVEN generate_logos.py has inline metadata
WHEN I run `uv run assets/generate/generate_logos.py`
THEN uv automatically installs dependencies and executes the script
```

#### Files created/modified

No additional files - this is a verification requirement.

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component             | Level | Justification                      |
| --------------------- | ----- | ---------------------------------- |
| Metadata block syntax | 1     | Static analysis, no execution      |
| Script execution      | 2     | Requires uv runtime (feature test) |

### When to Escalate

This story stays at Level 1 because:

- We're testing that the metadata block is syntactically correct
- Actual execution with uv is verified at the feature integration level

## Unit Tests (Level 1)

```python
# tests/unit/test_script_metadata.py
import re
from pathlib import Path


def test_script_has_inline_metadata():
    """GIVEN generate_logos.py WHEN parsed THEN contains PEP 723 metadata block"""
    # Given
    script_path = Path("assets/generate/generate_logos.py")
    content = script_path.read_text()

    # When/Then
    assert "# /// script" in content
    assert "# ///" in content
    assert 'requires-python = ">=3.11"' in content


def test_script_declares_required_dependencies():
    """GIVEN generate_logos.py WHEN parsed THEN declares svgpathtools and pyyaml"""
    # Given
    script_path = Path("assets/generate/generate_logos.py")
    content = script_path.read_text()

    # Then
    assert "svgpathtools" in content
    assert "pyyaml" in content


def test_script_metadata_is_after_shebang():
    """GIVEN generate_logos.py WHEN parsed THEN metadata comes after shebang"""
    # Given
    script_path = Path("assets/generate/generate_logos.py")
    lines = script_path.read_text().splitlines()

    # Then
    assert lines[0].startswith("#!/usr/bin/env")
    # Metadata block should start within first 10 lines
    metadata_start = next(i for i, line in enumerate(lines) if "# /// script" in line)
    assert metadata_start < 10
```

## Quality Requirements

### QR1: PEP 723 Compliance

**Requirement:** Metadata block must follow PEP 723 inline script metadata format
**Target:** Valid TOML within comment block
**Validation:** Script runs with `uv run` without errors

### QR2: Minimal Dependencies

**Requirement:** Only declare actually-needed dependencies
**Target:** svgpathtools>=1.6, pyyaml>=6.0
**Validation:** No unused dependencies in metadata

## Completion Criteria

- [ ] generate_logos.py has `# /// script` metadata block
- [ ] Metadata declares `requires-python = ">=3.11"`
- [ ] Metadata declares `svgpathtools>=1.6` dependency
- [ ] Metadata declares `pyyaml>=6.0` dependency
- [ ] `uv run assets/generate/generate_logos.py --help` works (manual verification)
