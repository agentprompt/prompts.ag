"""
Level 1 Unit Tests: YAML Asset Deployment

Tests YAML parsing and file deployment logic using dependency injection
with pytest's tmp_path fixture (ephemeral, reentrant, Level 1 appropriate).
"""

from pathlib import Path
from typing import Any

import yaml


class TestYamlParsing:
    """Level 1: Test YAML parsing produces correct structure"""

    def test_parse_asset_mappings_structure(self) -> None:
        """GIVEN asset-mappings.yaml WHEN parsed THEN has assets list"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")

        # When
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        assert "assets" in data
        assert isinstance(data["assets"], list)

    def test_each_mapping_has_source_and_dest(self) -> None:
        """GIVEN parsed mappings WHEN iterated THEN each has source and dest"""
        # Given
        mappings_path = Path("assets/generate/asset-mappings.yaml")
        with open(mappings_path) as f:
            data = yaml.safe_load(f)

        # Then
        for mapping in data["assets"]:
            assert "source" in mapping, f"Missing source in {mapping}"
            assert "dest" in mapping, f"Missing dest in {mapping}"

    def test_source_paths_are_relative(self) -> None:
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

    def test_dest_paths_are_relative(self) -> None:
        """GIVEN mappings WHEN checked THEN dest paths are relative"""
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

    def test_deploy_creates_missing_directories(self, tmp_path: Path) -> None:
        """GIVEN dest dir doesn't exist WHEN deploy THEN creates it"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "test.svg").write_text("<svg></svg>")

        public_dir = tmp_path / "public"
        # Note: public_dir doesn't exist yet

        mappings: dict[str, Any] = {
            "assets": [{"source": "test.svg", "dest": "icons/test.svg"}]
        }

        # When
        deploy_assets(mappings, output_dir, public_dir)

        # Then
        assert (public_dir / "icons" / "test.svg").exists()

    def test_deploy_copies_file_content(self, tmp_path: Path) -> None:
        """GIVEN source file WHEN deployed THEN content matches"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        content = "<svg>test content</svg>"
        (output_dir / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            "assets": [{"source": "logo.svg", "dest": "logo.svg"}]
        }

        # When
        deploy_assets(mappings, output_dir, public_dir)

        # Then
        assert (public_dir / "logo.svg").read_text() == content

    def test_deploy_handles_multiple_files(self, tmp_path: Path) -> None:
        """GIVEN multiple mappings WHEN deployed THEN all files copied"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "file1.svg").write_text("<svg>1</svg>")
        (output_dir / "file2.svg").write_text("<svg>2</svg>")

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            "assets": [
                {"source": "file1.svg", "dest": "file1.svg"},
                {"source": "file2.svg", "dest": "icons/file2.svg"},
            ]
        }

        # When
        deploy_assets(mappings, output_dir, public_dir)

        # Then
        assert (public_dir / "file1.svg").exists()
        assert (public_dir / "icons" / "file2.svg").exists()

    def test_deploy_is_idempotent(self, tmp_path: Path) -> None:
        """GIVEN deployed files WHEN deployed again THEN succeeds without error"""
        # Given
        from assets.generate.generate_logos import deploy_assets

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        content = "<svg>original</svg>"
        (output_dir / "logo.svg").write_text(content)

        public_dir = tmp_path / "public"
        public_dir.mkdir()

        mappings: dict[str, Any] = {
            "assets": [{"source": "logo.svg", "dest": "logo.svg"}]
        }

        # When: Deploy twice
        deploy_assets(mappings, output_dir, public_dir)
        deploy_assets(mappings, output_dir, public_dir)

        # Then: Second deployment succeeds and content is correct
        assert (public_dir / "logo.svg").read_text() == content
