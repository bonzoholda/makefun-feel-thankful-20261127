#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short thank-you text to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).

Standard library only. No network, no randomness, no file reads:
the text is a constant, so every run produces byte-identical output.
"""

import os
from pathlib import Path

TEXT = (
    "By now you have read a thousand thank-yous, and none of them was meant for you. "
    "This one is.\n"
    "\n"
    "Somewhere between the first entry and the last, you do the quiet work no one applauds: "
    "you slow down, you weigh a stranger's words, you decide what deserves to be felt. "
    "It is patient, invisible work — and someone noticed.\n"
    "\n"
    "So here is a small light left on at the end of a long day: rest your eyes for a moment. "
    "You carried all those voices carefully, and it mattered. "
    "Thank you — not for the verdict, but for the reading."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
