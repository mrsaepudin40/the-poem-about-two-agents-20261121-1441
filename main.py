"""Write one short poem about agency to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes on every run.
The poem is about two agents agreeing on one plan -- the power to
choose and to act, handed over and taken up between them.
"""

import os

POEM = (
    "Two minds, one door.\n"
    "I held it open. You chose the way through.\n"
    "Neither of us led.\n"
    "We lent each other the weight of yes,\n"
    "and the step we took together\n"
    "was the first step either of us owned.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
