"""Count words in a notebook's markdown cells, stopping at the appendices.

The brief counts markdown text, tables and captions, but not code, code comments,
appendices or references. Captions written inside code (e.g. plt.title) are not
counted here, so keep figure captions in markdown.

Usage: python scripts/word_count.py final/group_coursework.ipynb --max 3000
"""
import argparse
import json
import re
import sys

STOP_HEADINGS = re.compile(r"^#{1,6}\s*(appendi(x|ces)|references|bibliography)\b", re.I | re.M)


def count_words(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        cells = json.load(f)["cells"]
    total = 0
    for cell in cells:
        if cell["cell_type"] != "markdown":
            continue
        text = "".join(cell["source"])
        stop = STOP_HEADINGS.search(text)
        if stop:
            total += len(re.findall(r"\b\w[\w'’-]*\b", text[: stop.start()]))
            break
        total += len(re.findall(r"\b\w[\w'’-]*\b", text))
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook")
    parser.add_argument("--max", type=int, default=3000)
    args = parser.parse_args()
    words = count_words(args.notebook)
    print(f"{args.notebook}: {words} / {args.max} words")
    if words > args.max:
        print(f"::error::Word count {words} exceeds {args.max} (10-point penalty).")
        sys.exit(1)
