"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, no network, no randomness.
"""

import os
import sys

ENTRY = (
    "v2.0.4: fixed a bug where the mouth replied 'you too' when the "
    "waiter said 'enjoy your meal'. Fix failed. Mouth now says it twice."
)


def main() -> int:
    line = ENTRY
    if not (1 <= len(line) <= 160):
        print(f"entry must be 1-160 chars, got {len(line)}", file=sys.stderr)
        return 1
    if line != line.strip() or not line.strip():
        print("entry must be a single non-whitespace line", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify what was written is exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
