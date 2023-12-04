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


class TestAmazonPattern:
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

    @staticmethod
    def test_multiple_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name = "Star Trek (1966)"

        # Create file structure
        old_files = []
        old_subdirs = []
        (tmp_path / series_name).mkdir()
        old_subdirs.append(tmp_path / series_name / "1")
        old_subdirs[0].mkdir()
        for file in ["S01E001_the_man_trap.mp4", "S01E002_charlie_x.mp4"]:
            (old_file := (tmp_path / series_name / "1" / file)).write_text("<sentinel>")
            old_files.append(old_file)
        old_subdirs.append(tmp_path / series_name / "2")
        old_subdirs[1].mkdir()
        for file in ["S02E001_amok_time.mp4", "S02E002_who_mourns_for_adonais.mp4"]:
            (old_file := (tmp_path / series_name / "2" / file)).write_text("<sentinel>")
            old_files.append(old_file)

        expected_files = [
            tmp_path / series_name / "Season01" / file
            for file in [
                f"{series_name} - S01E01 - the man trap.mp4",
                f"{series_name} - S01E02 - charlie x.mp4",
            ]
        ] + [
            tmp_path / series_name / "Season02" / file
            for file in [
                f"{series_name} - S02E01 - amok time.mp4",
                f"{series_name} - S02E02 - who mourns for adonais.mp4",
            ]
        ]

        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        for file in old_files:
            assert not file.exists()
        for subdir in old_subdirs:
            assert not subdir.exists()
        for file in expected_files:
            with open(file) as f:
                assert f.read() == "<sentinel>"
