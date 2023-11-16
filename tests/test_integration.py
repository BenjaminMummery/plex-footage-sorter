# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path

from pytest_mock import MockerFixture

from src.phone_footage_sorter import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name"])

        # WHEN
        with cwd(tmp_path):
            main()