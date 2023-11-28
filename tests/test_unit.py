# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path

from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:  # TODO: remove this as soon as we have additional units to test.
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "date-based", "stub title"])

        # WHEN
        with cwd(tmp_path):
            main()
