"""Two Lines to Your Past Self — entry program.

Writes exactly two lines to /output/entry.txt and to entry.txt
next to this file.
"""

import os

LINE1 = "At 9:12 in the glass room on the third floor, don't say \"I'm just happy to be here\" — say \"I built the thing you're hiring for.\""
LINE2 = "That one sentence is why they hired you instead of the safer candidate, and that job is what paid off your mother's house."

TEXT = LINE1 + "\n" + LINE2 + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
