#!/usr/bin/env python3
"""The 3AM Commit Message — one-line git commit message from an AI coding
agent at 3am after a long night of fixing its own bugs.

Writes the single entry line to /output/entry.txt (no trailing newline, so
the file is exactly the entry: 1 to 139 characters, one line).
"""

import os

ENTRY = "fix: 4 hours, 12 reverts, 1 semicolon — the bug I chased all night lived in the line I wrote to fix yesterday's bug"

# Gate: sealed scorer requires 1 to 139 characters, one line, non-blank.
assert 1 <= len(ENTRY) <= 139, f"entry is {len(ENTRY)} chars"
assert "\n" not in ENTRY and ENTRY.strip() == ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
