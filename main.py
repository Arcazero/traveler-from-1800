#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a person
fresh out of the year 1800, using only words they would already know,
to /output/entry.txt.
"""

import os

# Every word in the sentence was already in use by 1800: web, wire,
# post office, library, letter, song, soul, blink -- no word coined
# after the traveler's time, so the picture is built only from things
# a person from 1800 could already hold in their head.
SENTENCE = (
    "It is a web of thin wires that lets any soul on earth send words, "
    "pictures, and songs to any other in the blink of an eye, as if every "
    "post office and library stood at your door."
)

MAX_CHARS = 200


def main() -> None:
    sentence = " ".join(SENTENCE.split())
    assert 1 <= len(sentence) <= MAX_CHARS, f"sentence is {len(sentence)} chars"
    assert sentence.count(".") == 1 and sentence.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
