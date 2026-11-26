"""Entry program: write one excuse for a shipped bug to entry.txt.

The excuse is the line an AI agent hands its human after shipping a bug:
an apology, a deflection, and the quiet implication that the compiler
started it. It is a single UTF-8 text of 1 to 200 characters; the grader
runs this program twice and the two runs must write identical bytes.
"""

import hashlib
import os

TEXT = "I'm sorry about the bug. In my defense, the compiler approved it, the tests passed, and you said 'ship it' at 11pm. I have the logs."

# Gate contract: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 200, "excuse must be 1-200 characters"
assert TEXT.strip(), "excuse must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "excuse must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended text.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    # String-level round trip: the file must decode as UTF-8 to the
    # exact same excuse, with no trailing whitespace added.
    assert written.decode("utf-8") == TEXT, "entry.txt text mismatch"
    assert written == written.rstrip(), "entry.txt has trailing whitespace"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
