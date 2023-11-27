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
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Affect the current directory and all subdirectories.",
    )
    args = parser.parse_args()

    print(f"Discovering files in {os.getcwd()}", end="")
    if args.recursive:
        print(" and subdirectories", end="")

    days: dict = {}
    if args.recursive:
        files = [os.path.join(dp, f) for dp, _, fn in os.walk(os.getcwd()) for f in fn]
    else:
        files = os.listdir()

    for file in files:
        print(".", end="")
        _, filename = os.path.split(file)

        try:
            if (
                date := datetime.strptime(
                    os.path.splitext(filename)[0], "%Y%m%d_%H%M%S"
                ).date()
            ) not in days:
                days[date] = [file]
            else:
                days[date].append(file)
        except ValueError:
            continue

    if len(days) == 0:
        print("No files to rename, exiting.")
        return

    print("\nRenaming files:")
    for day in days:
        if len(files := days[day]) == 1:
            dir, _ = os.path.split(files[0])
            new_name = (
                f"{args.title} - "
                f"{day.year}-{day.month:02d}-{day.day:02d}"
                f"{os.path.splitext(files[0])[1]}"
            )
            os.rename(
                files[0],
                os.path.join(dir, new_name),
            )
            print(f"  {file} --> {new_name}")
        else:
            for i, file in enumerate(sorted(files)):
                dir, _ = os.path.split(file)
                new_name = (
                    f"{args.title} - "
                    f"{day.year}-{day.month:02d}-{day.day:02d} - Part{i+1}"
                    f"{os.path.splitext(file)[1]}"
                )
                os.rename(file, os.path.join(dir, new_name))
                print(f"  {file} --> {new_name}")


if __name__ == "__main__":
    main()
