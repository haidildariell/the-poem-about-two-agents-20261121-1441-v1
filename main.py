#!/usr/bin/env python3
"""Entry for the make.fun competition 'the-poem-about-two-agents-20261121-1441'.

Writes one short poem about agency — two agents agreeing on one plan —
to /output/entry.txt. The poem is a hardcoded constant: no randomness,
no clock, no network, so every run writes byte-identical output.
Python 3.13, standard library only.
"""

import os

POEM = """The plan sits finished on the screen.
My finger rests above Enter,
your cursor blinking beside it.
Neither of us presses yet.
Agreement is this held breath:
two wills, one key, no flinch."""


def main() -> None:
    # The grader's sandbox provides /output; create it if absent.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
