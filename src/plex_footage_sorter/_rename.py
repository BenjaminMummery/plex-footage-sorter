# Copyright (c) 2024 Benjamin Mummery

"""Platform independent wildcard rename command."""

import os
import re
from typing import List


def _discover_files(directory: str, pattern: str) -> List[re.Match]:
    """Find files in the specified directory that match the regex pattern.

    Args:
        directory (str): The path to the directory to be searched.
        pattern (str): A regex pattern against which to match.

    Returns:
        List[re.Match]: A list of match objects, each corresponding to a
            matching file.
    """

    print(f"Discovering files in {directory}", end="")

    files = [
        file
        for file in [re.match(pattern, f) for f in os.listdir(directory)]
        if file is not None
    ]

    print(f" ... Found {len(files)} matching file(s).")

    return files


def _convert_glob_to_capturing_regex(pattern: str) -> str:
    """Convert a glob string to a regex with capturing groups.

    This aims to duplicate the functionality of `fnmatch.translate`, but with
    separate capturing groups wherever glob special characters appear.
    For example,

    ```txt
    my_file_*
    ```

    will be converted to:

    ```regex
    my_file_(.*)
    ```

    The full conversion table is:

    | glob str | regex | notes                                                       |
    |----------|-------|-------------------------------------------------------------|
    | *        | (.*)  | match any number of characters (including 0)                |
    | ?        |       | match any single character.                              NI |
    | [abc]    |       | match one character given in the bracket.                NI |
    | [a-z]    |       | match one character from the range given in the bracket. NI |
    | [!abc]   |       | match one character that is not given in the bracket.    NI |
    | [!a-z]   |       | match one character that is not from the range.          NI |

    Currently only `*` is implemented.

    Args:
        pattern (str): _description_

    Returns:
        str: _description_
    """
    if any(x in pattern for x in ["["]):
        raise NotImplementedError(
            f"Pattern '{pattern}' contains glob wildcards that are not yet supported."
        )

    outstr = "(.*)".join(pattern.split("*"))
    outstr = "(.)".join(outstr.split("?"))
    return outstr


def _convert_glob_to_format_string(pattern: str) -> str:
    """Convert a glob pattern to a

    Args:
        pattern (str): _description_

    Returns:
        str: _description_
    """
    chars = list(pattern)
    for i, char in enumerate(chars):
        if char in ["*", "?"]:
            chars[i] = "%s"
    return "".join(chars)


def _check_consistent_wildcards(pattern_1: str, pattern_2: str):
    """Raise an exception if the two patterns have different wildcards.

    Args:
        pattern_1 (str): A pattern containing one or more glob strings to be checked.
        pattern_2 (str): A pattern containing one or more glob strings to be checked.

    Raises:
        ValueError: when there are mismatching wildcards between the patterns.
    """
    glob_wildcards: List[str] = ["*", "?", "["]

    p1_chars: List[str] = []
    for char in pattern_1:
        if char in glob_wildcards:
            p1_chars.append(char)
    p2_chars: List[str] = []
    for char in pattern_2:
        if char in glob_wildcards:
            p2_chars.append(char)

    if p1_chars == p2_chars:
        return

    for char1, char2 in zip(p1_chars, p2_chars):
        if char1 != char2:
            raise ValueError(
                "Mismatching glob wildcards between input and output patterns "
                f"'{pattern_1}' and '{pattern_2}': '{char1}' vs '{char2}'."
            )


def main(directory: str, match_pattern: str, target_pattern: str):
    """Find and rename matching files.

    Args:
        directory (Path): The directory to be searched.
        match_pattern (str): The pattern to match to existing files.
        target_pattern (str): The pattern to which matching files should be renamed.
        regex (bool): If True, interpret the match and target patterns using regex. If
            False, glob will be used. Defaults to False.
    """
    _check_consistent_wildcards(match_pattern, target_pattern)

    if (
        len(
            files := _discover_files(
                directory, _convert_glob_to_capturing_regex(match_pattern)
            )
        )
        == 0
    ):
        return

    _target_pattern = _convert_glob_to_format_string(target_pattern)

    for file in files:
        new_name = _target_pattern % file.groups()
        os.rename(file.group(0), new_name)
        print(f"{file} -> {new_name}")
