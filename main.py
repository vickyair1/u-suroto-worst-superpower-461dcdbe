#!/usr/bin/env python3
"""Write the one-line worst-superpower entry to /output/entry.txt.

The entry is a gift that arrives a day too late: finding lost things
would be a real power, but this one only switches on after the
replacement has been bought, when the lost thing is no longer needed.
The joke is the timing, not the power — everyone has found their old
keys the week they paid for new ones. No entry in the field uses the
lost-things angle, so the take is fresh, and the line is 84 characters,
which also helps the tie-break: on an exact rate tie the smaller text
wins.

The line is assembled from parts so the wording stays deliberate, then
validated against the bounty gate (UTF-8, 1-140 characters, not only
whitespace, a single line) before it is written.
"""

import os

# Bounty gate: /output/entry.txt must be UTF-8 text of 1-140 chars.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 140

# Parts of the line: the gift is finding lost things, the catch is
# that it only works once a replacement has already been bought.
POWER = "I can find anything you've lost,"
CATCH = "but only after you've already bought a replacement."

LINE = POWER + " " + CATCH


def validate(text):
    """Gate check: UTF-8, within the char limits, one non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no leading/trailing whitespace")
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (GATE_MIN_CHARS, GATE_MAX_CHARS, len(text))
        )
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
