#!/usr/bin/env python3
"""Entry point for the yamba-ai-math benchmark instrument (see .claude/bench/README.md)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from yambench.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
