# Copyright (c) 2023 Benjamin Mummery

"""Rename and move files to conform to Plex conventions."""

import argparse
import os

from src import __version__

from . import _sort_dated_footage_as_date_series, _sort_movpilot_series


def _make_parser() -> argparse.ArgumentParser:
    """Build the argparser."""
    parser = argparse.ArgumentParser()

    # Global
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"{__name__.split('.')[1].replace('_','-')} {__version__}",
    )

    subparsers = parser.add_subparsers(required=True, dest="command")

    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help=(
            "The directory in which the tool should run. "
            "If omitted, the current working directory is used."
        ),
        default=os.getcwd(),
    )

    # date-based parser
    parser_date_based = subparsers.add_parser("date-based")
    parser_date_based.add_argument(
        "title",
        type=str,
        help="A custom name to be attached to the start of the new file names.",
    )
    parser_date_based.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        default=False,
        help="Affect the current directory and all subdirectories.",
    )

    # movpilot parser
    subparsers.add_parser("movpilot-series")

    return parser


def _resolve_path(input_path: str) -> str:
    """Resolve the directory argument into an absolute path."""
    _path: str = input_path
    if not os.path.isabs(_path):
        _path = os.path.join(os.getcwd(), _path)
    if not os.path.exists(_path):
        raise FileNotFoundError(f"Directory '{_path}' does not exist.")
    return _path


def main():
    """Search the dir for matching files and rename them."""

    # Parse args
    parser: argparse.ArgumentParser = _make_parser()
    args: argparse.Namespace = parser.parse_args()
    args.directory = _resolve_path(args.directory)

    if args.command == "date-based":
        return _sort_dated_footage_as_date_series.main(
            args.directory, args.title, recursive=args.recursive
        )
    elif args.command == "movpilot-series":
        return _sort_movpilot_series.main(args.directory)


if __name__ == "__main__":
    main()
