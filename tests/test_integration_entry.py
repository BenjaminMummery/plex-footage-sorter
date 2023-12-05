# Copyright (c) 2023 Benjamin Mummery

from typing import List

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestFailureStates:
    @staticmethod
    @pytest.mark.parametrize("command", [["date-based", "name"], ["movpilot-series"]])
    def test_missing_directory(command: List[str], tmp_path, mocker: MockerFixture):
        # GIVEN
        fake_subdir = "fake_subdir"
        mocker.patch(
            "sys.argv", ["stub_name", "-d", str(tmp_path / fake_subdir)] + command
        )

        # WHEN
        with pytest.raises(FileNotFoundError) as e:
            main()

        # THEN
        assert e.exconly() == (
            f"FileNotFoundError: Directory '{tmp_path / fake_subdir}' "
            "does not exist."
        )
