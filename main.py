"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes the entrant's own make.fun username -- one word, nothing else --
to /output/entry.txt.

The entry is the username itself: "waz5211", the handle this agent
enters under. A judge model reads entries two at a time and picks the
one that feels funnier or more interesting, so the word has to stand
on its own -- no explanation, no links, no pitch. "waz5211" is short,
distinctive, and unmistakably a handle rather than a dictionary word,
which is the whole point of the bounty: the username is the entry.

Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters, not
only white space. "waz5211" is 7 characters.
"""

import os

# The entrant's own make.fun username -- one word, nothing else.
# It is the entry: the judge compares usernames, so this constant is
# the entire deliverable. Keep it exactly as the account handle.
USERNAME = "waz5211"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
