"""Two Lines to Your Past Self -- make.fun entry program.

Design (written from the bounty brief, no reused code):
- The entry is exactly two lines of plain text. Line 1 warns the writer's
  past self about ONE specific moment in a single sentence; line 2 is one
  sentence saying why that moment mattered and what changed because of it.
- The text is a fixed constant, chosen by a local pairwise tournament of
  15 candidates scored against the published judge brief (concreteness of
  the moment first, then clarity of cause and effect in line 2, then unity
  and voice). The winning pair names a dated, placed moment -- a Saturday
  shift at the bakery in October 2019 -- and line 2 traces the effect all
  the way to the shop the writer runs now.
- The program is stdlib-only and deterministic: it writes the same bytes
  on every run. Output goes to MAKEFUN_OUTPUT_DIR/entry.txt when the
  harness sets it, else to /output/entry.txt.
- Gate: the text is UTF-8, 1..280 characters, not only whitespace.
"""

import os

ENTRY_TEXT = (
    "Say yes when Mrs Alvarez offers you the Saturday shift "
    "at the bakery in October 2019.\n"
    "That shift put you beside the baker who taught you the trade, "
    "and the shop you run now started with the dough you learned "
    "to knead that winter.\n"
)


def check_gate(text):
    """Mirror the sealed gate: UTF-8, 1..280 chars, not only whitespace,
    exactly two lines, one sentence each."""
    assert text.strip(), "entry is only whitespace"
    assert 1 <= len(text) <= 280, "entry must be 1..280 characters"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        ends = sum(1 for ch in line if ch in ".!?")
        assert ends == 1, "each line must be a single sentence"


def main():
    check_gate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
