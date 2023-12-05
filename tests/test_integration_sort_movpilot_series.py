# Copyright (c) 2023 Benjamin Mummery

from pathlib import Path
from typing import List

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files_cwd(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

    @staticmethod
    def test_no_files_relative_path(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "-d", str(tmp_path), "movpilot-series"])

        # WHEN
        main()


@pytest.mark.parametrize("season_dir_format", ["{number}", "Season {number}"])
class TestRunPattern:
    class TestDefaultDirectory:
        @staticmethod
        def test_single_file(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "firefly"
            (tmp_path / series_name).mkdir()
            (
                old_season_subdir := (
                    tmp_path / series_name / season_dir_format.format(number="1")
                )
            ).mkdir()
            (old_episode_subdir := (old_season_subdir / "Serenity")).mkdir()
            (old_file := (old_episode_subdir / "S01E001_serenity.mp4")).write_text(
                "<sentinel>"
            )

            mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                main()

            assert not old_file.exists()
            with open(
                tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.mp4"
            ) as f:
                assert f.read() == "<sentinel>"
            assert not old_season_subdir.exists()
            assert not old_episode_subdir.exists()

        @staticmethod
        def test_multiple_files(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "Star Trek (1966)"

            # Create file structure
            old_subdirs: List[Path] = []
            (tmp_path / series_name).mkdir()
            old_subdirs.append(
                s1_subdir := (
                    tmp_path / series_name / season_dir_format.format(number="1")
                )
            )
            old_subdirs.append(
                s2_subdir := (
                    tmp_path / series_name / season_dir_format.format(number="2")
                )
            )
            old_subdirs.append(s1e1_subdir := (s1_subdir / "The Man Trap"))
            old_subdirs.append(s1e2_subdir := (s1_subdir / "Charlie X"))
            old_subdirs.append(s2e1_subdir := (s2_subdir / "Amok Time"))
            old_subdirs.append(s2e2_subdir := (s2_subdir / "Who Mourns for Adonias"))
            for subdir in old_subdirs:
                subdir.mkdir()

            # Create files
            old_files: List[Path] = []
            old_files.append(s1e1_subdir / "S01E001_the_man_trap.mp4")
            old_files.append(s1e2_subdir / "S01E002_charlie_x.mp4")
            old_files.append(s2e1_subdir / "S02E001_amok_time.mp4")
            old_files.append(s2e2_subdir / "S02E002_who_mourns_for_adonais.mp4")
            for i, file in enumerate(old_files):
                file.write_text(f"<sentinel {i}>")

            # Expected output files:
            s1_new_subdir = tmp_path / series_name / "Season01"
            s2_new_subdir = tmp_path / series_name / "Season02"
            expected_files: List[Path] = [
                s1_new_subdir / f"{series_name} - S01E01 - the man trap.mp4",
                s1_new_subdir / f"{series_name} - S01E02 - charlie x.mp4",
                s2_new_subdir / f"{series_name} - S02E01 - amok time.mp4",
                s2_new_subdir / f"{series_name} - S02E02 - who mourns for adonais.mp4",
            ]

            # patch input args
            mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                main()

            for file in old_files:
                assert not file.exists()
            for subdir in old_subdirs:
                assert not subdir.exists()
            for i, file in enumerate(expected_files):
                with open(file) as f:
                    assert f.read() == f"<sentinel {i}>"

        @staticmethod
        def test_multiple_series(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            # Create file structure
            old_subdirs: List[Path] = []
            series_name_1 = "firefly"
            series_name_2 = "Doctor Who (2005)"
            (tmp_path / series_name_1).mkdir()
            (tmp_path / series_name_2).mkdir()
            old_subdirs.append(
                f_s1_subdir := (
                    tmp_path / series_name_1 / season_dir_format.format(number="1")
                )
            )
            old_subdirs.append(f_s1e1_subdir := (f_s1_subdir / "Serenity"))
            old_subdirs.append(
                dw_s1_subdir := (
                    tmp_path / series_name_2 / season_dir_format.format(number="1")
                )
            )
            old_subdirs.append(dw_s1e1_subdir := (dw_s1_subdir / "Rose"))
            for dir in old_subdirs:
                dir.mkdir()

            # Create files
            old_files: List[Path] = []
            old_files.append(f_s1e1_subdir / "S01E001_serenity.mp4")
            old_files.append(dw_s1e1_subdir / "S01E001_rose.mp4")
            for i, file in enumerate(old_files):
                file.write_text(f"<sentinel {i}>")

            # Expected output files:
            f_s1_new_subdir = tmp_path / series_name_1 / "Season01"
            dw_s1_new_subdir = tmp_path / series_name_2 / "Season01"
            expected_files: List[Path] = [
                f_s1_new_subdir / "firefly - S01E01 - serenity.mp4",
                dw_s1_new_subdir / "Doctor Who (2005) - S01E01 - rose.mp4",
            ]

            # patch input args
            mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                main()

            for file in old_files:
                assert not file.exists()
            for i, file in enumerate(expected_files):
                with open(file) as f:
                    assert f.read() == f"<sentinel {i}>"
            for dir in old_subdirs:
                assert not dir.exists()

        @staticmethod
        def test_misfiled_episode_wrong_season(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "Sleepy Hollow"
            (tmp_path / series_name).mkdir()
            old_subdirs: List[Path] = []
            old_subdirs.append(
                s1_subdir := (
                    tmp_path / series_name / season_dir_format.format(number="1")
                )
            )
            old_subdirs.append(s1e1_subdir := (s1_subdir / "This is War"))
            for dir in old_subdirs:
                dir.mkdir()

            (old_file := (s1e1_subdir / "S02E001_This_is_War.mp4")).write_text(
                "<sentinel>"
            )
            new_file = (
                tmp_path
                / series_name
                / "Season02"
                / "Sleepy Hollow - S02E01 - This is War.mp4"
            )

            mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                main()

            # THEN
            for old_subdir in old_subdirs:
                assert not old_subdir.exists()
            assert not old_file.exists()
            with open(new_file) as f:
                assert f.read() == "<sentinel>"

        @staticmethod
        def test_misfiled_episode_not_in_season(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "Sleepy Hollow"
            (tmp_path / series_name).mkdir()
            (
                old_file := (tmp_path / series_name / "S02E001_This_is_War.mp4")
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

        @staticmethod
        def test_misfiled_episode_misnamed_season(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "Sleepy Hollow"
            subdir_name = "some_random_nonsense"
            (tmp_path / series_name).mkdir()
            (tmp_path / series_name / subdir_name).mkdir()
            (
                old_file := (
                    tmp_path / series_name / subdir_name / "S02E001_This_is_War.mp4"
                )
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

        @staticmethod
        def test_supplemental_files(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "firefly"
            (tmp_path / series_name).mkdir()
            (tmp_path / series_name / season_dir_format.format(number="1")).mkdir()
            (tmp_path / series_name / "poster.jpeg").write_text("<poster sentinel>")
            (
                tmp_path
                / series_name
                / season_dir_format.format(number="1")
                / "S01E001_serenity.mp4"
            ).write_text("<episode sentinel>")
            (
                tmp_path
                / series_name
                / season_dir_format.format(number="1")
                / "S01E001_serenity.srt"
            ).write_text("<subtitles sentinel>")
            (
                tmp_path
                / series_name
                / season_dir_format.format(number="1")
                / "season_poster.png"
            ).write_text("<season poster sentinel>")

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

        @staticmethod
        def test_preexisting_subdir(
            tmp_path: Path, cwd, mocker: MockerFixture, season_dir_format: str
        ):
            # GIVEN
            series_name = "firefly"
            (tmp_path / series_name).mkdir()
            (tmp_path / series_name / "Season01").mkdir()
            (
                old_season_subdir := (
                    tmp_path / series_name / season_dir_format.format(number="1")
                )
            ).mkdir()
            (old_episode_subdir := (old_season_subdir / "Serenity")).mkdir()
            (old_file := (old_episode_subdir / "S01E001_serenity.mp4")).write_text(
                "<sentinel>"
            )

            mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                main()

            assert not old_file.exists()
            with open(
                tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.mp4"
            ) as f:
                assert f.read() == "<sentinel>"
            assert not old_season_subdir.exists()
            assert not old_episode_subdir.exists()

    @pytest.mark.parametrize("directory_arg", ["-d", "--directory"])
    class TestCustomDirectory:
        @staticmethod
        def test_absolute_dir(
            tmp_path: Path,
            cwd,
            mocker: MockerFixture,
            directory_arg: str,
            season_dir_format: str,
        ):
            # GIVEN
            series_name = "firefly"
            (tmp_path / series_name).mkdir()
            (
                old_subdir_1 := (
                    tmp_path / series_name / season_dir_format.format(number="1")
                )
            ).mkdir()
            (old_subdir_2 := (old_subdir_1 / "Serenity")).mkdir()
            (old_file := (old_subdir_2 / "S01E001_serenity.mp4")).write_text(
                "<sentinel>"
            )

            mocker.patch(
                "sys.argv",
                ["stub_name", directory_arg, str(tmp_path), "movpilot-series"],
            )

            # WHEN
            main()

            assert not old_file.exists()
            with open(
                tmp_path / series_name / "Season01" / "firefly - S01E01 - serenity.mp4"
            ) as f:
                assert f.read() == "<sentinel>"
            assert not old_subdir_1.exists()
            assert not old_subdir_2.exists()

        @staticmethod
        def test_relative_dir(
            tmp_path: Path,
            cwd,
            mocker: MockerFixture,
            directory_arg: str,
            season_dir_format: str,
        ):
            # GIVEN
            series_name = "firefly"
            (subdir_path := (tmp_path / "subdir")).mkdir()
            (subdir_path / series_name).mkdir()
            (
                old_subdir_1 := (
                    subdir_path / series_name / season_dir_format.format(number="1")
                )
            ).mkdir()
            (old_subdir_2 := (old_subdir_1 / "Serenity")).mkdir()
            (old_file := (old_subdir_2 / "S01E001_serenity.mp4")).write_text(
                "<sentinel>"
            )

            mocker.patch(
                "sys.argv", ["stub_name", directory_arg, "subdir", "movpilot-series"]
            )

            # WHEN
            with cwd(tmp_path):
                main()

            assert not old_file.exists()
            with open(
                subdir_path
                / series_name
                / "Season01"
                / "firefly - S01E01 - serenity.mp4"
            ) as f:
                assert f.read() == "<sentinel>"
            assert not old_subdir_1.exists()
            assert not old_subdir_2.exists()
