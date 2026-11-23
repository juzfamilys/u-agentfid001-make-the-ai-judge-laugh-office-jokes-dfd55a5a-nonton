"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only. Deterministic: the same joke,
byte for byte, on every run.
"""

import os

JOKE = (
    "Our standup lasts 15 minutes; the 45-minute meeting about why "
    "standups run long starts right after."
)


def validate_joke(joke: str) -> str:
    """Guard the gate: one line, 1-199 code points, not only whitespace.

    Also rejects tabs and other control characters, so the written file
    is exactly one clean printable line and nothing else.
    """
    if not isinstance(joke, str):
        raise TypeError("joke must be a string")
    if not joke.strip():
        raise ValueError("joke must not be blank")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in joke):
        raise ValueError("joke must not contain control characters")
    if not 1 <= len(joke) <= 199:
        raise ValueError("joke must be 1-199 characters, got %d" % len(joke))
    return joke


def main() -> None:
    joke = validate_joke(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
