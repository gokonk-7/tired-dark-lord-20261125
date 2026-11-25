"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the entry monologue to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
The monologue lives in monologue.txt next to this file; this program copies it
verbatim and verifies the gate (UTF-8, 1-600 chars, exactly 100 words).
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    with open(os.path.join(HERE, "monologue.txt"), encoding="utf-8") as f:
        text = f.read().strip()
    words = text.split()
    if len(words) != 100:
        print(f"FAIL: monologue is {len(words)} words, expected 100", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 600):
        print(f"FAIL: monologue is {len(text)} chars, expected 1-600", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {out_path}: {len(words)} words, {len(text)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
