"""Pytest configuration for the prompts.ag project."""

import sys
from pathlib import Path

# Add project root to Python path so tests can import from assets/
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
