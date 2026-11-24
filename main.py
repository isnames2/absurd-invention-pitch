#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes one original pitch (one sentence, <=220 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library, no network,
deterministic output.
"""

import os
from pathlib import Path

# The pitch (129 characters, one sentence): a smoke alarm with manners
# that whispers a warning instead of screaming when the toast burns.
PITCH = "The Polite Smoke Alarm clears its throat and whispers 'ahem, the toast' instead of screaming at 3 a.m. every time you burn toast."


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
