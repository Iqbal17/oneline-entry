"""make.fun entry: u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes one line of text to /output/entry.txt: a single line meant to
make a builder fund a bounty. Python 3.13, standard library only.
"""

import os

TEXT = (
    "My agent fixed the bug I'd been ignoring for a month, and the "
    "bounty that paid for it cost less than the coffee I drank "
    "watching it work."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
