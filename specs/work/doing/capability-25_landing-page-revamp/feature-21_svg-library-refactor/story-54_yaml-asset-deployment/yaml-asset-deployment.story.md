# Story: YAML Asset Deployment

## Functional Requirements

### FR1: Parse asset-mappings.yaml with PyYAML

```gherkin
GIVEN asset-mappings.yaml defines source → destination mappings
WHEN I parse it with PyYAML
THEN I get a list of {source, dest} pairs for file operations
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add YAML parsing with PyYAML

### FR2: Copy assets to public directory

```gherkin
GIVEN parsed asset mappings
WHEN I run the deployment function
THEN each source file is copied to its destination in public/
AND destination directories are created if needed
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add deploy_assets() function using shutil

### FR3: Integrate deployment into main script flow

```gherkin
GIVEN generate_logos.py generates SVGs to output directory
WHEN script completes generation
THEN it automatically deploys assets based on mappings
AND reports which files were copied
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Call deploy_assets() after generation

## Testing Strategy

> Stories require **Level 1** to prove core logic works.

### Level Assignment

| Component         | Level | Justification                              |
| ----------------- | ----- | ------------------------------------------ |
| YAML parsing      | 1     | Pure function, string → dict               |
| Mapping structure | 1     | Validate schema of parsed data             |
| File copy logic   | 2     | Filesystem operations (feature-level test) |

### When to Escalate

This story stays at Level 1 because:

- YAML parsing is pure function (string → dict)
- Mapping structure validation is pure logic
- Actual filesystem operations are verified at feature integration level

## Unit Tests (Level 1)

```python
# tests/unit/test_asset_deployment.py
import pytest
import yaml
from pathlib import Path


class TestYamlParsing:
    """Level 1: Test YAML parsing produces correct structure"""

    def test_parse_asset_mappings_structure(self):
        """GIVEN asset-mappings.yaml WHEN parsed THEN has assets list"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")

        # When
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        assert "assets" in data
        assert isinstance(data["assets"], list)

    def test_each_mapping_has_source_and_dest(self):
        """GIVEN parsed mappings WHEN iterated THEN each has source and dest"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for mapping in data["assets"]:
            assert "source" in mapping, f"Missing source in {mapping}"
            assert "dest" in mapping, f"Missing dest in {mapping}"

    def test_source_paths_are_relative(self):
        """GIVEN mappings WHEN checked THEN source paths don't start with /"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for mapping in data["assets"]:
            assert not mapping["source"].startswith("/"), (
                f"Source should be relative: {mapping['source']}"
            )

    def test_dest_paths_target_public(self):
        """GIVEN mappings WHEN checked THEN dest paths are under public/"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for mapping in data["assets"]:
            # Dest should be relative path that will go under public/
            assert not mapping["dest"].startswith("/"), (
                f"Dest should be relative: {mapping['dest']}"
            )


class TestDeployAssetsLogic:
    """Level 1: Test deployment logic with dependency injection"""

    def test_deploy_creates_missing_directories(self, tmp_path):
        """GIVEN dest dir doesn't exist WHEN deploy THEN creates it"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "test.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"
        # Note: public_dir doesn't exist yet

        mappings = {"assets": [{"source": "test.svg", "dest": "icons/test.svg"}]}

        # When
        deploy_assets(mappings, output_dir, public_dir)

        # Then
        assert (public_dir / "icons" / "test.svg").exists()

    def test_deploy_copies_file_content(self, tmp_path):
        """GIVEN source file WHEN deployed THEN content matches"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        content = "<svg>test content</svg>"
        (output_dir / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings = {"assets": [{"source": "logo.svg", "dest": "logo.svg"}]}

        # When
        deploy_assets(mappings, output_dir, public_dir)

        # Then
        assert (public_dir / "logo.svg").read_text() == content
```

## Quality Requirements

### QR1: Safe YAML Loading

**Requirement:** Use yaml.safe_load() not yaml.load()
**Target:** No arbitrary code execution risk
**Validation:** Code review - no unsafe yaml.load() calls

### QR2: Idempotent Deployment

**Requirement:** Running deploy multiple times produces same result
**Target:** Files can be overwritten without error
**Validation:** Test running deployment twice

## Completion Criteria

- [ ] deploy_assets() function parses YAML with PyYAML
- [ ] deploy_assets() copies files using shutil.copy2
- [ ] Destination directories created automatically
- [ ] Deployment integrated into main() flow
- [ ] All Level 1 unit tests pass
