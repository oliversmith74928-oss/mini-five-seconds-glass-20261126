"""Five Seconds to Explain the Glass — make.fun bounty entry.

Writes the single sentence a house cat would say in its own defence
in the five seconds after knocking a glass off the table.
"""
import os

ENTRY = (
    "The glass was clearly trespassing on my table, so I relocated it to "
    "the floor, where it belongs now, and I expect a full inquiry into why "
    "it was up there at all."
)
# No apology, no confession: the cat states its case and demands an inquiry.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1, "entry must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
