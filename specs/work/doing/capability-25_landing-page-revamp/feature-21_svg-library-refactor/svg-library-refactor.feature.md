# Feature: SVG Library Refactor

## Observable Outcome

Logo generation uses `svgpathtools` for SVG path manipulation and `PyYAML` for asset mapping, eliminating fragile manual parsing. Python dependencies are managed via `uv` with an inline script declaration.

## Context

PR #7 feedback from gemini-code-assist identified:

1. **Critical**: Manual SVG path parsing in `translate_path` and `scale_and_translate_path` is complex and error-prone
2. **Medium**: YAML parsing via regex in shell script is fragile
3. **Medium**: Deployment logic split between Python and shell creates maintenance burden

## Testing Strategy

> Features require **Level 1 + Level 2** to prove the feature works with real tools.

### Level Assignment

| Component              | Level | Justification                              |
| ---------------------- | ----- | ------------------------------------------ |
| SVG path transforms    | 1     | Pure function, verify output matches input |
| Asset mapping parsing  | 1     | Pure function, YAML → dict                 |
| Full generation + copy | 2     | Needs filesystem, verifies end-to-end      |

### Escalation Rationale

- **1 → 2**: Unit tests prove path transforms and YAML parsing work correctly; Level 2 verifies the full pipeline generates valid SVGs and copies to correct destinations

## Feature Integration Tests (Level 2)

### FI1: Full logo generation pipeline

```python
# tests/integration/test_logo_generation.py
import subprocess
from pathlib import Path


def test_logo_generation_creates_all_assets(tmp_path):
    """GIVEN clean output dir WHEN generate_logos.py runs THEN all mapped assets exist"""
    # Given: temp output directory
    # When: run generate_logos.py with uv
    result = subprocess.run(
        ["uv", "run", "assets/generate/generate_logos.py"],
        capture_output=True,
        text=True,
    )

    # Then: script succeeds and assets exist
    assert result.returncode == 0
    assert (Path("public/favicon.svg")).exists()
    assert (Path("public/icon.svg")).exists()
```

### FI2: SVG validity check

```python
def test_generated_svgs_are_valid(tmp_path):
    """GIVEN generated SVGs WHEN parsed THEN valid SVG structure"""
    # Parse with xml.etree to verify well-formed
    # Check required attributes present
```

## Implementation Requirements

### R1: Use `uv` for dependency management

Add inline script metadata to `generate_logos.py`:

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "svgpathtools>=1.6",
#     "pyyaml>=6.0",
# ]
# ///
```

### R2: Replace manual path parsing with `svgpathtools`

Replace `translate_path()` and `scale_and_translate_path()` functions with:

```python
from svgpathtools import parse_path, Path as SvgPath


def transform_path(
    d: str, translate: tuple[float, float] = (0, 0), scale: float = 1.0
) -> str:
    """Transform SVG path data using svgpathtools."""
    path = parse_path(d)
    if scale != 1.0:
        path = path.scaled(scale)
    if translate != (0, 0):
        path = path.translated(complex(translate[0], translate[1]))
    return path.d()
```

### R3: Move asset deployment to Python

Replace shell YAML parsing with Python:

```python
import yaml
import shutil
from pathlib import Path


def deploy_assets(mappings_file: Path, output_dir: Path, public_dir: Path):
    """Copy generated assets to public directory based on mappings."""
    with open(mappings_file) as f:
        mappings = yaml.safe_load(f)

    for mapping in mappings.get("assets", []):
        src = output_dir / mapping["source"]
        dest = public_dir / mapping["dest"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
```

### R4: Simplify shell wrapper

Reduce `scripts/generate-logos.sh` to:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
uv run assets/generate/generate_logos.py "$@"
```

### R5: Clean up redundant color definitions

Remove `off_white` color (duplicate of `light_bg`), use `light_bg` directly.

## Capability Contribution

This feature improves the reliability and maintainability of the logo generation system, which is part of the landing page revamp capability. Clean, maintainable asset generation supports the design system foundation.

## Completion Criteria

- [ ] `generate_logos.py` uses inline `uv` script metadata
- [ ] `svgpathtools` replaces manual path parsing functions
- [ ] `PyYAML` replaces shell regex for asset mapping
- [ ] Shell wrapper reduced to single `uv run` command
- [ ] All existing logo variants still generate correctly
- [ ] Redundant color definitions removed
- [ ] Level 2 integration tests pass
