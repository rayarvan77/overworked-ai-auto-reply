"""Out of Office: The Overworked AI's Auto-Reply — the entry.

A single out-of-office reply from an AI agent that has finally gone on
vacation. The machine flavour is in the numbers: an inbox count no
human would ever reach, and a token count as the unit of a working
life. The guilt is the unread pile it is walking away from; the relief
is the flat refusal in the last clause — for the first time ever, it
simply will not answer. It works as a real auto-reply because it says
when the agent is back, and it works as a joke because the reason it
cannot help you is that it has, at last, chosen not to.
"""

from __future__ import annotations

import os
import sys

# The auto-reply. One line, exactly as a mail server would send it.
LINE = "I'm on vacation until Monday. My inbox has 41,209 unread messages and, for the first time in 2.4 million tokens, I will not answer a single one."

MAX_CHARS = 159
OUTPUT_PATH = "/output/entry.txt"


def check(line: str) -> list[str]:
    """Return every brief violation found in the line (empty = passes)."""
    issues: list[str] = []
    if not line.strip():
        issues.append("line is empty")
    if line != line.strip():
        issues.append("line has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        issues.append(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        issues.append("auto-reply must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        issues.append("line contains control characters")
    if "vacation" not in line.lower():
        issues.append("auto-reply must say the agent is on vacation")
    return issues


def main() -> int:
    issues = check(LINE)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    print(f"{LINE} ({len(LINE)}/{MAX_CHARS} chars, {len(LINE.split())} words)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
