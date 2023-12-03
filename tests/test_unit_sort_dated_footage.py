# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter._sort_dated_footage_as_date_series import main


@pytest.mark.usefixtures("mock_entry", "mock_sort_movpilot_series")
class TestNullCases:
    @staticmethod
    def test_no_files(
        tmp_path: Path,
    ):
        main(tmp_path, "stub title", recursive=False)

    @staticmethod
    def test_all_renamable_files_in_subdirs_and_not_recursive(
        tmp_path: Path, cwd, mocker: MockerFixture
    ):
        # GIVEN
        filename = "20220202_222222.mp4"
        subdir = "subdir"
        (tmp_path / subdir).mkdir()
        (filepath := tmp_path / subdir / filename).write_text("<sentinel>")
        assert filepath.is_file()

        # WHEN
        main(tmp_path, "stub title", recursive=False)

        # THEN
        assert filepath.is_file()
