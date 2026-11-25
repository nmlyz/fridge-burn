#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a roast of a fridge, told through
the oldest thing inside it.

The line was picked from 36 candidates by pairwise judging against the
brief — a roast that names one concrete thing (the Tupperware at the back
of the fridge) and turns on it in the last words, comparing its age with
the owner's last three relationships combined. It is 94 characters: short
enough to read aloud in one breath, long enough to carry the setup, the
specific noun, and the turn. The program builds the line from two
clauses — the container and its age, then the comparison that closes the
joke — and checks the result against the entry gate (length, single line,
no leading or trailing space, exact judged length) before writing it,
then reads the file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "There's a Tupperware in the back of my fridge older than "
    "my last three relationships combined."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if len(LINE) != 94:
        sys.exit(f"line is {len(LINE)} characters, judged line is 94")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
