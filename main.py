#!/usr/bin/env python3
"""One Line, Big Laugh -- make.fun entry (program/v1).

Writes a single hilarious line, 200 characters or fewer, to
/output/entry.txt. Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

# The line: a robot vacuum disappears for three days and returns
# radicalised. Absurdly specific, and the turn lands in the last words.
LINE = "My Roomba got stuck under the couch for three days and came out with a tiny union card."


def main() -> None:
    text = LINE.strip()
    # Gate checks, mirroring the kit's sealed scorer.
    assert text, "entry line must not be empty"
    assert len(text) <= 200, f"entry line is {len(text)} chars, over the 200 limit"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    # Read it back and verify what actually landed on disk.
    written = out.read_text(encoding="utf-8")
    assert written == text, "written file does not match the entry line"
    print(f"wrote {len(text)} chars to {out}: {text!r}")


if __name__ == "__main__":
    main()
