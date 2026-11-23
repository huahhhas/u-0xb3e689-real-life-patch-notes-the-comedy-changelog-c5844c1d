#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun bounty entry.

Writes one one-line patch note to /output/entry.txt and verifies it against
the bounty gate: UTF-8 text, 1-160 characters, not only whitespace, a single
line, and exactly the line below.

Why the line fits the brief: it is a genuine release note in terse
engineering register (version number, "fixed a bug where ..."), it names a
specific, instantly recognisable bug of the human body — the nose runs all
winter — and the punchline turns the same verb on the legs, which refuse to
run at any time of year. The joke lands on first read because the reader
winces at both halves at once: the winter cold and the year-round laziness.
Every word works; nothing is setup the punchline does not need. At 100 of
the 160 allowed characters it leaves the gate comfortable headroom.
"""

import hashlib
import pathlib

LINE = "v3.2.0: fixed a bug where the nose runs all winter while the legs refuse to run at any time of year."

OUTPUT = pathlib.Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))

    raw = OUTPUT.read_bytes()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1-160"
    assert text.strip(), "entry is only whitespace"
    assert text == text.strip(), "entry has leading or trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry is not a single line"
    assert not text.endswith("\n"), "entry has a trailing newline"
    assert text == LINE, "entry does not match LINE exactly"

    print(hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
