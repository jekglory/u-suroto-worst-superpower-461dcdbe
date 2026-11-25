#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes a single line to the grader's output directory: the worst
superpower imaginable, stated as a first-person confession. Pure
standard library.

Angle: mind-reading, the classic dream power — except it only works
on my own mind, and only out loud, in the one place where thinking
out loud costs you the most: a job interview. The power is genuine,
the usefulness is zero, and the embarrassment is total — the stinger
lands on the last two words, where the power does its damage.
"""

import os
import sys

LINE = "I can read minds \u2014 but only my own, and only out loud, during job interviews."

MAX_CHARS = 160


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The grader owns the output directory: create it only if missing,
    # never delete or recreate it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("superpower must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "superpower must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # Write exactly one line with no trailing newline: the file is the
    # entry, and the entry is the line — nothing else goes in, so the
    # judge reads the superpower and nothing but the superpower.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the artifact the judge will read is exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise SystemExit("written bytes do not match the superpower")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
