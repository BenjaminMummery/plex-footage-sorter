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

    @staticmethod
    def test_multiple_series(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name_1 = "firefly"
        (tmp_path / series_name_1).mkdir()
        (old_subdir_1 := (tmp_path / series_name_1 / "1")).mkdir()
        (
            old_file_1 := (tmp_path / series_name_1 / "1" / "S01E001_serenity.mp4")
        ).write_text("<sentinel>")
        series_name_2 = "Doctor Who (2005)"
        (tmp_path / series_name_2).mkdir()
        (old_subdir_2 := (tmp_path / series_name_2 / "1")).mkdir()
        (
            old_file_2 := (tmp_path / series_name_2 / "1" / "S01E001_rose.mp4")
        ).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        assert not old_file_1.exists()
        assert not old_file_2.exists()
        for file in [
            tmp_path / series_name_1 / "Season01" / "firefly - S01E01 - serenity.mp4",
            tmp_path
            / series_name_2
            / "Season01"
            / "Doctor Who (2005) - S01E01 - rose.mp4",
        ]:
            with open(file) as f:
                assert f.read() == "<sentinel>"
        assert not old_subdir_1.exists()
        assert not old_subdir_2.exists()

    @staticmethod
    def test_misfiled_episode_wrong_season(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name = "Sleepy Hollow"
        (tmp_path / series_name).mkdir()
        (old_subdir := (tmp_path / series_name / "1")).mkdir()
        (
            old_file := (tmp_path / series_name / "1" / "S02E001_This_is_War.mp4")
        ).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        assert not old_file.exists()
        with open(
            tmp_path
            / series_name
            / "Season02"
            / "Sleepy Hollow - S02E01 - This is War.mp4"
        ) as f:
            assert f.read() == "<sentinel>"
        assert not old_subdir.exists()

    @staticmethod
    def test_misfiled_episode_not_in_season(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name = "Sleepy Hollow"
        (tmp_path / series_name).mkdir()
        (old_file := (tmp_path / series_name / "S02E001_This_is_War.mp4")).write_text(
            "<sentinel>"
        )
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        assert not old_file.exists()
        with open(
            tmp_path
            / series_name
            / "Season02"
            / "Sleepy Hollow - S02E01 - This is War.mp4"
        ) as f:
            assert f.read() == "<sentinel>"

    @staticmethod
    def test_supplemental_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        series_name = "firefly"
        (tmp_path / series_name).mkdir()
        (tmp_path / series_name / "1").mkdir()
        (tmp_path / series_name / "poster.jpeg").write_text("<poster sentinel>")
        (tmp_path / series_name / "1" / "S01E001_serenity.mp4").write_text(
            "<episode sentinel>"
        )
        (tmp_path / series_name / "1" / "S01E001_serenity.srt").write_text(
            "<subtitles sentinel>"
        )
        (tmp_path / series_name / "1" / "season_poster.png").write_text(
            "<season poster sentinel>"
        )

        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        with open(tmp_path / series_name / "poster.jpeg") as f:
            assert f.read() == "<poster sentinel>"
        with open(
            tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.mp4"
        ) as f:
            assert f.read() == "<episode sentinel>"
        with open(
            tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.srt"
        ) as f:
            assert f.read() == "<subtitles sentinel>"
        with open(tmp_path / series_name / "Season01" / "season_poster.png") as f:
            assert f.read() == "<season poster sentinel>"
