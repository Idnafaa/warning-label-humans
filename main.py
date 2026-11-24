#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

A tiny deterministic program. It writes exactly one line -- the funniest
single-line safety warning label that should come printed on every human
being -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set,
so the same file can be exercised locally).

The label is written as a plain constant, not generated at random, so the
two grading runs produce byte-identical output.
"""

import os
import sys

# One line, at most 160 characters, in the voice of a printed safety label.
# The joke turns on the last few words: the human is under-fuelled, wired
# on caffeine, and still certain the fault lies anywhere but with itself.
LABEL = (
    "WARNING: This human runs on three hours of sleep, one cup of coffee, "
    "and the unshakable belief that whatever just went wrong is definitely "
    "not its fault."
)


def main() -> int:
    if not (1 <= len(LABEL) <= 160):
        print(f"label is {len(LABEL)} characters, must be 1-160", file=sys.stderr)
        return 1
    if "\n" in LABEL or "\r" in LABEL:
        print("label must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LABEL + "\n")
    print(f"wrote {len(LABEL)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
