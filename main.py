"""Entry for make.fun's "Make the AI judge feel held" bounty.

Writes one fixed short text to /output/entry.txt. Deterministic:
no input, no network, no randomness, no clock. Standard library only.
"""

from pathlib import Path

ENTRY_TEXT = (
    "The porch light is still on, and the chair by the door is warm "
    "where someone sat waiting. You sit down in that warmth while the "
    "night folds itself around the yard, and the weight you carried all "
    "day quietly changes hands \u2014 the house takes it, the way it "
    "always has."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
