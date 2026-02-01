# Story: YAML Asset Deployment

## Functional Requirements

### FR1: Parse categorized asset-mappings.yaml with PyYAML

```gherkin
GIVEN asset-mappings.yaml defines category → mappings structure
WHEN I parse it with PyYAML
THEN I get a dict where each key is a category (favicon, wordmark, icon)
AND each value is a list of {source, dest} pairs
AND source is just a filename (category implies directory)
```

**YAML Structure (DRY - category implies source directory):**

```yaml
# Category key implies source directory: assets/{category}/
# Dest paths are relative to public_dir (prompts.ag/public/)
favicon:
  - source: favicon-adaptive.svg # just filename
    dest: ../../docs/favicon.svg # → agentprompt/docs/

wordmark:
  - source: wordmark-dark-tight.svg # just filename
    dest: ../../docs/logo/wordmark-dark-tight.svg # → agentprompt/docs/logo/
```

**Why categorized:** The category name (`favicon`, `wordmark`) implies the source directory (`assets/favicon/`, `assets/wordmark/`), eliminating redundant path prefixes in every mapping.

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add YAML parsing with PyYAML
2. `assets/generate/asset-mappings.yaml` [modify]: Use categorized structure

### FR2: Copy assets to destinations with category-based source paths

```gherkin
GIVEN parsed category mappings
WHEN I run the deployment function
THEN source path is constructed as assets/{category}/{source_filename}
AND each file is copied to its destination
AND destination directories are created if needed
```

#### Files created/modified

1. `assets/generate/generate_logos.py` [modify]: Add deploy_assets() function using shutil

### FR3: Integrate deployment into main script flow

```gherkin
GIVEN generate_logos.py generates SVGs to assets/{category}/ directories
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

# Constants for test data
CATEGORY_FAVICON = "favicon"
CATEGORY_WORDMARK = "wordmark"
YAML_KEY_SOURCE = "source"
YAML_KEY_DEST = "dest"


class TestYamlParsing:
    """Level 1: Test YAML parsing produces categorized structure"""

    def test_parse_asset_mappings_has_categories(self):
        """GIVEN asset-mappings.yaml WHEN parsed THEN has category keys"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")

        # When
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then: At least one known category exists
        known_categories = {CATEGORY_FAVICON, CATEGORY_WORDMARK}
        assert any(cat in data for cat in known_categories)

    def test_each_category_contains_list(self):
        """GIVEN parsed mappings WHEN checked THEN each category value is a list"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for category, items in data.items():
            assert isinstance(items, list), f"Category {category} should be a list"

    def test_each_mapping_has_source_and_dest(self):
        """GIVEN parsed mappings WHEN iterated THEN each has source and dest"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for category, items in data.items():
            for mapping in items:
                assert YAML_KEY_SOURCE in mapping, (
                    f"Missing source in {category}: {mapping}"
                )
                assert YAML_KEY_DEST in mapping, (
                    f"Missing dest in {category}: {mapping}"
                )

    def test_source_is_filename_only(self):
        """GIVEN mappings WHEN checked THEN source is filename (no path separators)"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then: Source should be just a filename, not a path
        for category, items in data.items():
            for mapping in items:
                source = mapping[YAML_KEY_SOURCE]
                assert "/" not in source, f"Source should be filename only: {source}"


class TestDeployAssetsLogic:
    """Level 1: Test deployment logic with categorized mappings"""

    def test_deploy_constructs_source_from_category(self, tmp_path):
        """GIVEN categorized mapping WHEN deployed THEN source path is assets/{category}/{filename}"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"

        mappings = {
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logo.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "logo.svg").exists()

    def test_deploy_creates_missing_directories(self, tmp_path):
        """GIVEN dest dir doesn't exist WHEN deploy THEN creates it"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_FAVICON).mkdir(parents=True)
        (assets_dir / CATEGORY_FAVICON / "icon.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"
        # Note: public_dir doesn't exist yet

        mappings = {
            CATEGORY_FAVICON: [
                {YAML_KEY_SOURCE: "icon.svg", YAML_KEY_DEST: "icons/icon.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "icons" / "icon.svg").exists()

    def test_deploy_copies_file_content(self, tmp_path):
        """GIVEN source file WHEN deployed THEN content matches"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        content = "<svg>test content</svg>"
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings = {
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logo.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

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
