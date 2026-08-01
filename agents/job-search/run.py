#!/usr/bin/env python3
"""Entry point for the job-search agent."""

import sys
from pathlib import Path

AGENT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(AGENT_ROOT))

from src.cli import main

if __name__ == "__main__":
    main()
