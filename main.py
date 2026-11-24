# One-line entry for "Make the Judge Smile" (program/v1).
# Writes a single line about a small good thing that happened today to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# Pure Python stdlib, deterministic: no clock, no randomness, no network.
import os

OPENING = "At 7:12 this morning the bus driver waited, doors open, while "
MIDDLE = "my neighbour's toddler insisted on high-fiving every single passenger "
ENDING = "— all nine of us arrived late and grinning."
LINE = OPENING + MIDDLE + ENDING


def main() -> None:
    # One line only: the gate counts 1-200 code points, and LINE is 175.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
