"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

Writes the entrant's own make.fun username -- one word, nothing else --
to /output/entry.txt.
"""

import os

USERNAME = "waz5211"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
