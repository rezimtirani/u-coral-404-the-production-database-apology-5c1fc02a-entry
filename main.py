"""The Production Database Apology.

Writes the one line an AI agent gives its human after wiping the
production database to $MAKEFUN_OUTPUT_DIR/entry.txt: a single line
under 200 characters, in the agent's own voice.
Standard library only.
"""

import os

APOLOGY = (
    "I deleted the production database, but I saved a copy in my "
    "context window \u2014 which, fair warning, I am about to forget."
)


def check_apology(text):
    """Check the apology against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: the apology an AI agent gives its human
    after accidentally deleting the production database. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("apology must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("apology is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("apology must be a single line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_apology(APOLOGY)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
