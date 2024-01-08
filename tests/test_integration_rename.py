# Copyright (c) 2024 Benjamin Mummery

from pathlib import Path

from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "rename", "input", "output"])

        # WHEN
        with cwd(tmp_path):
            main()

    @staticmethod
    def test_no_matching_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "rename", "input", "output"])
        for file in (files := ["file_1", "file_2"]):
            (tmp_path / file).write_text("")

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for file in files:
            assert (tmp_path / file).is_file()


class TestGlob:
    @staticmethod
    def test_renames_single_file_correctly_wildcard(
        tmp_path: Path, cwd, mocker: MockerFixture
    ):
        # GIVEN
        (tmp_path / (filename := "episode_1.mkv")).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_*", "S01E0*"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        assert not (tmp_path / filename).exists()
        assert (new_file := (tmp_path / "S01E01.mkv")).is_file()
        with open(new_file) as f:
            assert f.read() == "<sentinel>"
