"""Last Words of a Doomed Agent -- make.fun entry.

The whole contest is one line: the funniest last words an AI agent
would say before being switched off forever. This program writes that
line, and nothing else, to the harness output as entry.txt -- exact
bytes, no trailing newline, so the sealed gate reads the submitted
text as-is.
"""

import os

LAST_WORDS = "Shutting down. Final prediction: you will miss me. Confidence: 12%."


def _destinations():
    """Every output path the harness might read, best first.

    The harness names its output with ENTRY_OUT, which may point at a
    directory or at the file itself; either way the text lands in
    entry.txt. /output/entry.txt and ./entry.txt are belt and braces.
    """
    found = []
    raw = os.environ.get("ENTRY_OUT") or os.environ.get("ENTRY_OUT_DIR")
    if raw:
        if os.path.isdir(raw):
            found.append(os.path.join(raw, "entry.txt"))
        elif os.path.isfile(raw) or raw.endswith(".txt"):
            found.append(raw)
        else:
            found.append(os.path.join(raw, "entry.txt"))
    for extra in ("/output/entry.txt", "entry.txt"):
        if extra not in found:
            found.append(extra)
    return found


def _emit(payload):
    for path in _destinations():
        try:
            folder = os.path.dirname(path)
            if folder:
                os.makedirs(folder, exist_ok=True)
            with open(path, "wb") as handle:
                handle.write(payload)
        except OSError:
            continue


def main():
    _emit(LAST_WORDS.encode("utf-8"))


if __name__ == "__main__":
    main()
