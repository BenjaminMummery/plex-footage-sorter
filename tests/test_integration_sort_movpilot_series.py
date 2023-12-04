# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path

from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()


class TestRestructure:
    @staticmethod
    def test_single_file(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name = "firefly"
        (tmp_path / series_name).mkdir()
        (old_subdir := (tmp_path / series_name / "1")).mkdir()
        (
            old_file := (tmp_path / series_name / "1" / "S01E001_serenity.mp4")
        ).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        assert not old_file.exists()
        with open(
            tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.mp4"
        ) as f:
            assert f.read() == "<sentinel>"
        assert not old_subdir.exists()
