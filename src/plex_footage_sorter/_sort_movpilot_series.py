# Copyright (c) 2023 Benjamin Mummery

"""Move anr rename Movpilot Series files into plex-friendly patterns."""


import logging
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Episode:
    """Class for keeping track of all episode-specific parameters."""

    season: int
    episode: int
    title: str
    ext: str
    path: Path


def _discover_files(directory: Path) -> dict:
    """Find files that match the format we want to convert.

    Args:
        directory (Path): The directory to be searched.

    Returns:
        dict: A ampping of datetime date objects to file paths, where the date is
            derived from the file name.
    """

    print(f"Discovering files in {directory}", end="")
    files = [
        os.path.join(path, name)
        for path, subdirs, files in os.walk(directory)
        for name in files
    ]

    outfiles: list = []

    for file in files:
        print(".", end="")
        _, filename = os.path.split(file)
        filename, ext = os.path.splitext(filename)
        if (
            match := re.match(
                r"^S(?P<season>\d{2})E(?P<episode>\d{3})_(?P<title>.*)$", filename
            )
        ) is None:
            continue
        outfiles.append(
            Episode(
                int(match["season"]),
                int(match["episode"]),
                match["title"].replace("_", " "),
                ext,
                file,
            )
        )

    print(f" Found {len(files)} file(s).")
    return outfiles


def main(directory: str):
    """Find and rename matching files.

    Args:
        directory (Path): The directory to be searched. The subdirectories of this
            directory should be the folders for each series. For example:
            ```txt
            directory
            ├── Castlevania
            |   ├── 1
            |   |   └── Witchbottle
            |   |       └── S01E001_witchbottle.mp4
            |   └── 2
            |       └── Old Homes
            |           └── S02E002_old_homes.mp4
            └── Goblin Slayer
                └── S01E001_The_goblin_crown.mp4
            ```
            will be remapped as
            ```txt
            directory
            ├── Castlevania
            |   ├── Season01
            |   |   └── Castlevania - S01E01 - witchbottle.mp4
            |   └── Season02
            |       └── Castlevania - S02E02 - old homes.mp4
            └── Goblin Slayer
                └── Season01
                    └── Goblin Slayer - S01E01 - The goblin crown.mp4
            ```
    """
    _directory: Path = Path(directory)
    for series_name in next(os.walk(_directory))[1]:
        # Rename season subdirs
        for subdir in next(os.walk(_directory / series_name))[1]:
            season_no: int
            try:
                season_no = int(subdir)
            except ValueError:
                match = re.match(r"^season\s*(?P<number>\d+)", subdir, re.IGNORECASE)
                if match is None:
                    logging.warning(
                        f"Subdirectory '{subdir}' does not conform to a recognised "
                        "naming pattern and will be ignored."
                    )
                    continue
                season_no = int(match["number"])
            os.rename(
                _directory / series_name / subdir,
                _directory / series_name / f"Season{season_no:02d}",
            )

        # Find files that need to be modified
        episodes: List[Episode] = _discover_files(
            filedir := (Path(directory) / series_name)
        )

        subdirs = next(os.walk(filedir))[1]
        for episode in episodes:
            # Create season subdir if it doesn't already exist
            if (season_subdir := f"Season{episode.season:02d}") not in subdirs:
                os.mkdir(_directory / series_name / season_subdir)

            # move / rename episode
            new_filename = (
                _directory
                / series_name
                / season_subdir
                / (
                    f"{series_name}"
                    f" - S{episode.season:02d}E{episode.episode:02d}"
                    f" - {episode.title}{episode.ext}"
                )
            )
            print(f"{episode.path} --> {new_filename}")
            os.rename(episode.path, new_filename)

        # Remove empty subdirs
        deleted = set()
        for current_dir, subdirs, files in os.walk(_directory, topdown=False):
            still_has_subdirs = False
            for subdir in subdirs:
                if os.path.join(current_dir, subdir) not in deleted:
                    still_has_subdirs = True
                    break
            if not any(files) and not still_has_subdirs:
                os.rmdir(current_dir)
                deleted.add(current_dir)
