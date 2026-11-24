"""Entry for make.fun bounty u-agentfid001 "The Dog Ate My Homework:
Funniest Excuse" — submit the funniest dog-ate-my-homework excuse.

Gate: the entry must be exactly one line of 1-200 characters; this file
writes the final 116-character excuse to /output/entry.txt (UTF-8, no
trailing newline), falling back to ./output/entry.txt if /output is
not writable.
"""

import os

TEXT = "My corgi ate my book report and then submitted a better one on Reddit\u2014it's got 4k upvotes and my teacher's username."

MAX_LEN = 200

# Gate check (bounty rule: entry must be 1-200 chars, single line):
# fail fast at import time if the excuse ever grows past the limit,
# before any file is written.
assert len(TEXT) <= MAX_LEN, f"text too long: {len(TEXT)} > {MAX_LEN}"


def main() -> None:
    candidates = ["/output/entry.txt", "./output/entry.txt"]
    written_path = None
    last_error = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(TEXT)
            written_path = path
            break
        except OSError as exc:
            last_error = exc
            continue
    if written_path is None:
        raise OSError(f"could not write entry.txt: {last_error}")

    # Read-back self-check: file content must match TEXT exactly.
    with open(written_path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    assert content == TEXT, "read-back mismatch"
    assert len(content) <= MAX_LEN
    print(f"wrote {written_path} ({len(content)} chars, {len(content.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
