#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short thank-you text to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset).

Standard library only. No network, no randomness, no file reads:
the text is a constant, so every run produces byte-identical output.
The text is validated against the bounty rules (UTF-8, 1–1,000
Unicode code points, not only whitespace) before anything is written.
"""

import os
from pathlib import Path

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 1000

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


def validate_text(text: str) -> str:
    """Check the entry text against the bounty rules; fail loudly otherwise.

    Rules: UTF-8 text, 1–1,000 Unicode code points, not only whitespace.
    Returns the text unchanged when it passes.
    """
    stripped = text.strip()
    if not stripped:
        raise SystemExit("error: entry text must not be empty or only whitespace")
    count = len(text)
    if count < MIN_CODE_POINTS or count > MAX_CODE_POINTS:
        raise SystemExit(
            f"error: entry text is {count} code points, "
            f"outside the allowed {MIN_CODE_POINTS}–{MAX_CODE_POINTS} range"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return text


def main() -> None:
    validated = validate_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(validated, encoding="utf-8")


if __name__ == "__main__":
    main()
