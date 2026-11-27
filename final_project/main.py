"""Executable entry point for the AutoPy Fleet & Rental System.

Usage:
    python final_project/main.py --demo   # Non-blocking automated simulation
    python final_project/main.py          # Interactive terminal menu
"""

from __future__ import annotations

import sys

try:
    from autopy.cli import main
except ImportError:  # Supports running via `python -m final_project.main`
    from final_project.autopy.cli import main


if __name__ == "__main__":
    sys.exit(main())
