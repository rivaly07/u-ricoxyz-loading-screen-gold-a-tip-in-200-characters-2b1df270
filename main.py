#!/usr/bin/env python3
"""Write the entry text for this make.fun bounty to <output>/entry.txt.

Output directory: $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
Standard library only, no network, one file in, one line out.
"""
from __future__ import annotations

import os
from pathlib import Path

ENTRY = (
    "Loading 98%: the agent already answered your next question, "
    "and is waiting to see if you ask it anyway."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
