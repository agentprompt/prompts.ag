# Story: Simplify Shell Wrapper

## Functional Requirements

### FR1: Remove YAML parsing from shell script

```gherkin
GIVEN scripts/generate-logos.sh currently parses YAML with regex
WHEN I remove the shell-based parsing logic
THEN the script no longer contains awk/sed/grep YAML manipulation
```

#### Files created/modified

1. `scripts/generate-logos.sh` [modify]: Remove YAML parsing section

### FR2: Reduce wrapper to uv invocation

```gherkin
GIVEN Python script handles all generation and deployment
WHEN shell wrapper is simplified
THEN it contains only: set options, cd to repo root, uv run command
```

#### Files created/modified

1. `scripts/generate-logos.sh` [modify]: Simplify to minimal wrapper

### FR3: Pass through command line arguments

```gherkin
GIVEN user may want to pass flags to generate_logos.py
WHEN shell wrapper is invoked with arguments
THEN arguments are passed through to Python script via "$@"
```

#### Files created/modified

1. `scripts/generate-logos.sh` [modify]: Add "$@" to uv run command

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component            | Level | Justification                     |
| -------------------- | ----- | --------------------------------- |
| Script structure     | 1     | Static analysis of shell script   |
| Argument passthrough | 2     | Requires execution (feature test) |

### When to Escalate

This story stays at Level 1 because:

- We're verifying script structure, not execution
- Actual script execution is verified at feature integration level

## Unit Tests (Level 1)

```python
# tests/unit/test_shell_wrapper.py
from pathlib import Path


class TestShellWrapper:
    """Level 1: Static analysis of shell script structure"""

    def test_script_has_strict_mode(self):
        """GIVEN generate-logos.sh WHEN read THEN has set -euo pipefail"""
        # Given
        script = Path("scripts/generate-logos.sh").read_text()

        # Then
        assert "set -euo pipefail" in script or "set -e" in script

    def test_script_uses_uv_run(self):
        """GIVEN generate-logos.sh WHEN read THEN invokes uv run"""
        # Given
        script = Path("scripts/generate-logos.sh").read_text()

        # Then
        assert "uv run" in script

    def test_script_no_yaml_parsing(self):
        """GIVEN generate-logos.sh WHEN read THEN no YAML regex parsing"""
        # Given
        script = Path("scripts/generate-logos.sh").read_text()

        # Then: No awk/sed/grep YAML manipulation patterns
        assert "awk" not in script.lower() or "yaml" not in script.lower()
        assert "asset-mappings" not in script  # No direct YAML file reference

    def test_script_passes_arguments(self):
        """GIVEN generate-logos.sh WHEN read THEN passes $@ to Python"""
        # Given
        script = Path("scripts/generate-logos.sh").read_text()

        # Then
        assert '"$@"' in script or "'$@'" in script or "$@" in script

    def test_script_is_minimal(self):
        """GIVEN generate-logos.sh WHEN read THEN is under 15 lines"""
        # Given
        script = Path("scripts/generate-logos.sh").read_text()
        lines = [
            l
            for l in script.splitlines()
            if l.strip() and not l.strip().startswith("#")
        ]

        # Then: Minimal wrapper should be very short
        assert len(lines) <= 10, (
            f"Script has {len(lines)} non-comment lines, expected <= 10"
        )
```

## Quality Requirements

### QR1: Shell Best Practices

**Requirement:** Script follows shell best practices
**Target:** Uses strict mode, proper quoting
**Validation:** shellcheck passes (if available)

### QR2: Single Responsibility

**Requirement:** Script only orchestrates, doesn't implement logic
**Target:** All logic in Python, shell just launches
**Validation:** Script under 10 non-comment lines

## Completion Criteria

- [ ] YAML parsing code removed from shell script
- [ ] File copying code removed from shell script
- [ ] Script reduced to ~5-10 lines
- [ ] Script passes through arguments with "$@"
- [ ] `pnpm run logo:generate` still works (manual verification)
