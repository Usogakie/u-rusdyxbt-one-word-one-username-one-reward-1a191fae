#!/usr/bin/env python3
"""Write the entrant's own make.fun username to entry.txt.

The competition asks for one word and nothing else: the entrant's own
make.fun handle. This program writes exactly that handle, "usogakie",
to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt -- no explanation, no
links, no pitch, no trailing newline. Deterministic: every run writes
the same 8 bytes. No network, no clock, no reads outside this file.
"""

import os
import sys

USERNAME = "usogakie"

# The gate allows 1-30 characters and the brief demands one word:
# enforce it here so a typo can never ship a padded or split entry.
assert USERNAME and len(USERNAME) <= 30 and USERNAME.split() == [USERNAME]


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    return 0


if __name__ == "__main__":
    sys.exit(main())
