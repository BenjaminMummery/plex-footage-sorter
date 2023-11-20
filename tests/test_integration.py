# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path

from pytest_mock import MockerFixture

from src.phone_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name"])

        # WHEN
        with cwd(tmp_path):
            main()


class TestSingleFiles:
    @staticmethod
    def test_renames_correctly(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        filename = "20220202_222222.mp4"
        (tmp_path / filename).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        with open(tmp_path / "Training Videos - 2022-02-02.mp4", "r") as f:
            assert f.read() == "<sentinel>"
