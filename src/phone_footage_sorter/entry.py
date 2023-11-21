# Copyright (c) 2023 Benjamin Mummery

"""Process android phone footage default names into plex-friendly filename."""

import argparse
import os
from datetime import datetime


def main():
    """Search the dir for matching files and rename them."""

    # Parse args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "title",
        type=str,
        help="A custom name to be attached to the start of the new file names.",
    )
    args = parser.parse_args()

    days: dict = {}
    for file in os.listdir():
        try:
            if (
                date := datetime.strptime(
                    os.path.splitext(file)[0], "%Y%m%d_%H%M%S"
                ).date()
            ) not in days:
                days[date] = [file]
            else:
                days[date].append(file)
        except ValueError:
            continue

    for day in days:
        if len(files := days[day]) == 1:
            os.rename(
                files[0],
                f"{args.title} - "
                f"{day.year}-{day.month:02d}-{day.day:02d}"
                f"{os.path.splitext(file)[1]}",
            )
        else:
            for i, file in enumerate(sorted(files)):
                os.rename(
                    file,
                    f"{args.title} - "
                    f"{day.year}-{day.month:02d}-{day.day:02d} - Part{i+1}"
                    f"{os.path.splitext(file)[1]}",
                )


if __name__ == "__main__":
    main()
