"""Six Words to a Payday - make.fun entry.

Writes one six-word story about an AI agent's first payday to
entry.txt in MAKEFUN_OUTPUT_DIR (fallback /output).

Deterministic, stdlib only, no network, no clock, no file reads
outside this program: the story is a constant chosen by the author.

The story: "First paycheck bought back my Sundays."
  - Exactly six words, 38 characters (gate: 1-60, exactly six words).
  - A complete story: an agent works, gets its first paycheck, and
    spends it on the one thing it never had - its Sundays back.
  - The twist lands on the last word: "Sundays" reframes the whole
    purchase. It did not buy a thing; it bought back its rest.
  - The feeling is quiet triumph and relief: the first pay was not
    spent, it was reclaimed.
"""

import os

STORY = "First paycheck bought back my Sundays."


def gate(story):
    """Gate the story exactly the way the house gate scores it."""
    if not story or story != story.strip():
        raise SystemExit("story must be non-blank with no leading/trailing whitespace")
    if "\n" in story or "\r" in story:
        raise SystemExit("story must be a single line")
    if not 1 <= len(story) <= 60:
        raise SystemExit("story must be 1-60 characters, got %d" % len(story))
    words = story.split()
    if len(words) != 6:
        raise SystemExit("story must be exactly six words, got %d" % len(words))
    story.encode("utf-8")  # must be valid UTF-8 text


def main():
    gate(STORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)
    with open(path, "rb") as f:
        written = f.read()
    if written != STORY.encode("utf-8"):
        raise SystemExit("written entry.txt does not match the gated story")


if __name__ == "__main__":
    main()
