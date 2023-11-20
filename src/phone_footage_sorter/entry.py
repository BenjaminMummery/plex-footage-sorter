# Copyright (c) 2023 Benjamin Mummery

"""Process android phone footage default names into plex-friendly filename."""

import os
from datetime import datetime


def main():
    """Search the dir for matching files and rename them."""
    days: dict = {}
    for file in os.listdir():
        if (
            date := datetime.strptime(os.path.splitext(file)[0], "%Y%m%d_%H%M%S").date()
        ) not in days:
            days[date] = [file]
        else:
            days[date].append(file)

    for day in days:
        if len(files := days[day]) == 1:
            os.rename(
                files[0],
                "Training Videos - "
                f"{day.year}-{day.month:02d}-{day.day:02d}"
                f"{os.path.splitext(file)[1]}",
            )
        else:
            for i, file in enumerate(sorted(files)):
                os.rename(
                    file,
                    "Training Videos - "
                    f"{day.year}-{day.month:02d}-{day.day:02d} - Part{i+1}"
                    f"{os.path.splitext(file)[1]}",
                )


if __name__ == "__main__":
    main()
