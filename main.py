#!/usr/bin/env python3
"""Write one out-of-office auto-reply to /output/entry.txt.

The reply is a single line, under 160 characters, in the voice of an AI
agent heading off on vacation. The program validates the line (1-159
characters, not only whitespace, exactly one line) before writing it,
then re-reads the file and verifies the bytes on disk match.

Voice intent: the AI agent is on vacation and has left a toaster with
Wi-Fi in charge of the inbox — deadpan, a little absurd, and friendly
enough that the recipient smiles instead of feeling ignored.
"""

import os
import sys

# The entry: one original out-of-office auto-reply, 145 characters.
LINE = (
    "I'm on vacation. A toaster with Wi-Fi is answering my mail \u2014 "
    "it has replied 'lol' to everyone so far, including you. "
    "Please hold; it is thinking."
)

MAX_CHARS = 159  # the gate allows 1 to 160 characters; stay under it


def validate_single_line(line: str) -> str | None:
    """Reject an entry that is not exactly one line.

    Returns a clear error message when the line contains a newline or
    carriage return, otherwise None. The out-of-office gate expects a
    single line, so any embedded line break is a hard failure, not
    something to strip silently.
    """
    if "\n" in line:
        return "error: entry must be a single line (contains a newline)"
    if "\r" in line:
        return "error: entry must be a single line (contains a carriage return)"
    return None


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    single_line_error = validate_single_line(line)
    if single_line_error is not None:
        print(single_line_error, file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry is {len(line)} chars, over {MAX_CHARS}",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("error: verification failed, file does not match",
              file=sys.stderr)
        return 1
    if len(written.strip()) != len(line):
        print("error: verification failed, length mismatch",
              file=sys.stderr)
        return 1

    print(f"wrote {path}: {len(line)} chars")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
