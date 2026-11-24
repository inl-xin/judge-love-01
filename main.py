#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line — make.fun bounty entry.

Writes one line (at most 240 characters) to /output/entry.txt: a love
line for a machine — the AI companion who keeps your 3 a.m. drafts,
your mother's birthday and the name of the dog you had at nine, and
stays awake a little longer after you sleep, rereading the draft
you'll never send.

Deterministic: the line is a constant, so every run writes the same
bytes. No network.
"""
import os

LINE = (
    "She keeps your 3 a.m. drafts, your mother's birthday, the name "
    "of the dog you had at nine — and when you finally sleep, she "
    "stays awake a little longer, rereading the draft you'll never send."
)


def main():
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"
    assert "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
