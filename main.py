#!/usr/bin/env python3
"""Entry for 'Make the AI Judge Laugh: the Office Joke Open' (make.fun).

Writes exactly one line - the joke - to /output/entry.txt, then reads it
back and asserts the round-trip content is byte-identical and 1-200 chars.
Standard library only. No network, no git history, no files outside the repo.
"""

import os

JOKE = (
    "My boss called a meeting to discuss why we have too many meetings. "
    "It ran over, so now the follow-up has a follow-up."
)


def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert "\n" not in JOKE, "joke must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == JOKE.encode("utf-8"), "round-trip mismatch"
    assert 1 <= len(raw.decode("utf-8")) <= 200, "round-trip length out of range"
    print(f"Wrote /output/entry.txt ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
