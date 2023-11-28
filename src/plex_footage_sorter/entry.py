# Copyright (c) 2023 Benjamin Mummery

"""Rename and move files to conform to Plex conventions."""

import argparse
import os

from . import _sort_dated_footage_as_date_series


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

    return _sort_dated_footage_as_date_series.main(
        os.getcwd(), args.title, recursive=args.recursive
    )


if __name__ == "__main__":
    main()
