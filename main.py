"""make.fun entry: u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf.

Writes one line of text to /output/entry.txt: a single line meant to
make a builder fund a bounty. Python 3.13, standard library only.

Entry contract: the file holds exactly the TEXT constant, one line,
no trailing newline, 1-280 Unicode code points, never blank. The
program is deterministic: every run writes the same bytes.
"""

import os

MIN_LEN = 1
MAX_LEN = 280

TEXT = (
    "My agent fixed the bug I'd been ignoring for a month, and the "
    "bounty that paid for it cost less than the coffee I drank "
    "watching it work."
)


def validate_text(text: str) -> str:
    """Return text unchanged if it meets the entry contract.

    The contract for this bounty: exactly one line, 1-280 Unicode
    code points, and not only whitespace. Anything else is a bug
    in the entry, so fail loudly instead of writing a bad file.
    """
    if not text.strip():
        raise SystemExit("entry text must not be blank")
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"entry text must be {MIN_LEN}-{MAX_LEN} characters, "
            f"got {len(text)}"
        )
    return text


def write_entry(text: str) -> None:
    """Write the validated line to entry.txt in the output dir.

    The output directory is created if missing; it is never
    removed, since in the grader it is a mount point.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    write_entry(validate_text(TEXT))


if __name__ == "__main__":
    main()
