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

MAX_CHARS = 160


def validate(label: str) -> str:
    """Check the label the way the gate does, and fail loudly if it is off.

    Returns the label unchanged when it passes: one line, 1 to 160
    characters, not only white space, in the voice of a printed warning.
    """
    if not label or label.strip() == "":
        raise ValueError("label must not be blank")
    if "\n" in label or "\r" in label:
        raise ValueError("label must be a single line")
    if len(label) > MAX_CHARS:
        raise ValueError(f"label is {len(label)} characters, over {MAX_CHARS}")
    if not label.startswith("WARNING:"):
        raise ValueError("label must read like a printed warning label")
    return label


def main() -> int:
    try:
        label = validate(LABEL)
    except ValueError as exc:
        print(f"invalid label: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(label + "\n")
    print(f"wrote {len(label)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
