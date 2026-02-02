"""
Level 1 Unit Tests: YAML Asset Deployment

Tests YAML parsing and file deployment logic using dependency injection
with pytest's tmp_path fixture (ephemeral, reentrant, Level 1 appropriate).
"""

from pathlib import Path
from typing import Any

import yaml

# Constants for test data
CATEGORY_FAVICON = "favicon"
CATEGORY_WORDMARK = "wordmark"
YAML_KEY_SOURCE = "source"
YAML_KEY_DEST = "dest"


class TestYamlParsing:
    """Level 1: Test YAML parsing produces categorized structure"""

    def test_parse_asset_mappings_has_categories(self) -> None:
        """GIVEN asset-mappings.yaml WHEN parsed THEN has category keys"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")

        # When
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then: At least one known category exists
        known_categories = {CATEGORY_FAVICON, CATEGORY_WORDMARK}
        assert any(cat in data for cat in known_categories)

    def test_each_category_contains_list(self) -> None:
        """GIVEN parsed mappings WHEN checked THEN each category value is a list"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for category, items in data.items():
            assert isinstance(items, list), f"Category {category} should be a list"

    def test_each_mapping_has_source_and_dest(self) -> None:
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

    def test_source_is_filename_only(self) -> None:
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

    def test_deploy_constructs_source_from_category(self, tmp_path: Path) -> None:
        """GIVEN categorized mapping WHEN deployed THEN source path uses category"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"

        mappings: dict[str, Any] = {
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logo.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "logo.svg").exists()

    def test_deploy_creates_missing_directories(self, tmp_path: Path) -> None:
        """GIVEN dest dir doesn't exist WHEN deploy THEN creates it"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_FAVICON).mkdir(parents=True)
        (assets_dir / CATEGORY_FAVICON / "icon.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"
        # Note: public_dir doesn't exist yet

        mappings: dict[str, Any] = {
            CATEGORY_FAVICON: [
                {YAML_KEY_SOURCE: "icon.svg", YAML_KEY_DEST: "icons/icon.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "icons" / "icon.svg").exists()

    def test_deploy_copies_file_content(self, tmp_path: Path) -> None:
        """GIVEN source file WHEN deployed THEN content matches"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        content = "<svg>test content</svg>"
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logo.svg"}
            ]
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "logo.svg").read_text() == content

    def test_deploy_handles_multiple_categories(self, tmp_path: Path) -> None:
        """GIVEN multiple categories WHEN deployed THEN all files copied"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_FAVICON).mkdir(parents=True)
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        (assets_dir / CATEGORY_FAVICON / "favicon.svg").write_text("<svg>fav</svg>")
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text("<svg>logo</svg>")

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            CATEGORY_FAVICON: [
                {YAML_KEY_SOURCE: "favicon.svg", YAML_KEY_DEST: "favicon.svg"}
            ],
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logos/logo.svg"}
            ],
        }

        # When
        deploy_assets(mappings, assets_dir, public_dir)

        # Then
        assert (public_dir / "favicon.svg").exists()
        assert (public_dir / "logos" / "logo.svg").exists()

    def test_deploy_is_idempotent(self, tmp_path: Path) -> None:
        """GIVEN deployed files WHEN deployed again THEN succeeds without error"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        assets_dir = tmp_path / "assets"
        (assets_dir / CATEGORY_WORDMARK).mkdir(parents=True)
        content = "<svg>original</svg>"
        (assets_dir / CATEGORY_WORDMARK / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            CATEGORY_WORDMARK: [
                {YAML_KEY_SOURCE: "logo.svg", YAML_KEY_DEST: "logo.svg"}
            ]
        }

        # When: Deploy twice
        deploy_assets(mappings, assets_dir, public_dir)
        deploy_assets(mappings, assets_dir, public_dir)

        # Then: Second deployment succeeds and content is correct
        assert (public_dir / "logo.svg").read_text() == content
