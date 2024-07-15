# Copyright (c) 2023 - 2024 Benjamin Mummery

import os
from pathlib import Path
from typing import List

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "date-based", "stub title"])

        # WHEN
        with cwd(tmp_path):
            main()

    @staticmethod
    def test_all_renamable_files_in_subdirs_and_not_recursive(
        tmp_path: Path, cwd, mocker: MockerFixture
    ):
        # GIVEN
        filename = "20220202_222222.mp4"
        subdir = "subdir"
        (tmp_path / subdir).mkdir()
        (filepath := tmp_path / subdir / filename).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "date-based", "stub title"])
        assert filepath.is_file()

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        assert filepath.is_file()


@pytest.mark.parametrize("custom_name", ["Training Videos", "FOO"])
@pytest.mark.parametrize("recursion_arg", ["-r", "--recursive", None])
class TestFlatDir:
    @staticmethod
    @pytest.mark.parametrize(
        "filename",
        [
            "20220202_222222.mp4",
            "20220202_222222222.mp4",
            "20220202_2222.mp4",
            "2022-02-02-22-22-222.mp4",
            "2022-02-02_22-22-222.mp4",
            "2022-02-02_22-22-222_1.mp4",
        ],
    )
    def test_renames_single_file_correctly(
        tmp_path: Path,
        cwd,
        mocker: MockerFixture,
        custom_name: str,
        recursion_arg: str,
        filename: str,
    ):
        # GIVEN
        (tmp_path / filename).write_text("<sentinel>")
        args = ["stub_name", "date-based", custom_name]
        if recursion_arg is not None:
            args.append(recursion_arg)
        mocker.patch("sys.argv", args)

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        with open(tmp_path / f"{custom_name} - 2022-02-02.mp4", "r") as f:
            assert f.read() == "<sentinel>"

    @staticmethod
    @pytest.mark.parametrize(
        "filenames",
        [
            ["20220202_222222.mp4", "20220202_222223.mp4"],
            ["20220202_222222222.mp4", "20220202_222222223.mp4"],
            ["20220202_2222.mp4", "20220202_2223.mp4"],
            ["20220202_2222.mp4", "20220202_222222223.mp4"],
            ["20220202_2222.mp4", "20220202_2222_1.mp4"],
            ["20220202_2222_1.mp4", "20220202_2222_1_1.mp4"],
        ],
    )
    def test_renames_multiple_files_for_same_day(
        tmp_path: Path,
        cwd,
        mocker: MockerFixture,
        custom_name: str,
        recursion_arg: str,
        filenames: List[str],
    ):
        # GIVEN
        for i, file in enumerate(filenames):
            (tmp_path / file).write_text(f"<{i} sentinel>")
        args = ["stub_name", "date-based", custom_name]
        if recursion_arg is not None:
            args.append(recursion_arg)
        mocker.patch("sys.argv", args)

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for i, file in enumerate(
            [
                f"{custom_name} - 2022-02-02 - Part1.mp4",
                f"{custom_name} - 2022-02-02 - Part2.mp4",
            ]
        ):
            with open(tmp_path / file, "r") as f:
                assert f.read() == f"<{i} sentinel>"

    @staticmethod
    def test_ignores_non_matching_files(
        tmp_path: Path, cwd, mocker: MockerFixture, custom_name: str, recursion_arg: str
    ):
        # GIVEN
        for file in [
            "20220202_222222.mp4",
            "20220202_222223.mp4",
            "not_a_matching_file.mp4",
        ]:
            (tmp_path / file).write_text("")
        args = ["stub_name", "date-based", custom_name]
        if recursion_arg is not None:
            args.append(recursion_arg)
        mocker.patch("sys.argv", args)

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        assert set(os.listdir(tmp_path)) == {
            f"{custom_name} - 2022-02-02 - Part1.mp4",
            f"{custom_name} - 2022-02-02 - Part2.mp4",
            "not_a_matching_file.mp4",
        }

    @staticmethod
    def test_reports_renamed_files(
        tmp_path: Path,
        cwd,
        mocker: MockerFixture,
        custom_name: str,
        capsys,
        recursion_arg: str,
    ):
        # GIVEN
        files = [
            "20220202_222222.mp4",
            "20220202_222223.mp4",
        ]
        outfiles = [
            f"{custom_name} - 2022-02-02 - Part1.mp4",
            f"{custom_name} - 2022-02-02 - Part2.mp4",
        ]
        for file in files:
            (tmp_path / file).write_text("")
        args = ["stub_name", "date-based", custom_name]
        if recursion_arg is not None:
            args.append(recursion_arg)
        mocker.patch("sys.argv", args)

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        out = capsys.readouterr().out
        assert "Renaming files:" in out
        for i, file in enumerate(files):
            assert f"{file} --> {outfiles[i]}" in out


@pytest.mark.parametrize("custom_name", ["Training Videos", "FOO"])
@pytest.mark.parametrize("recursion_arg", ["-r", "--recursive"])
class TestSubDirs:
    @staticmethod
    def test_renames_single_file_correctly(
        tmp_path: Path, cwd, mocker: MockerFixture, custom_name: str, recursion_arg: str
    ):
        # GIVEN
        filename = "20220202_222222.mp4"
        subdir = "subdir"
        (tmp_path / subdir).mkdir()
        (tmp_path / subdir / filename).write_text("<sentinel>")
        mocker.patch(
            "sys.argv", ["stub_name", "date-based", custom_name, recursion_arg]
        )

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        expected_outpath = tmp_path / subdir / f"{custom_name} - 2022-02-02.mp4"
        assert (
            expected_outpath.is_file()
        ), f"{expected_outpath}\n{os.listdir(tmp_path / subdir)}"
        with open(expected_outpath, "r") as f:
            assert f.read() == "<sentinel>"


@pytest.mark.parametrize("directory_arg", ["-d", "--directory"])
class TestCustomDirectory:
    @staticmethod
    def test_absolute_dir(tmp_path: Path, mocker: MockerFixture, directory_arg: str):
        # GIVEN
        custom_name = "foo"
        filename = "20220202_222222.mp4"
        (tmp_path / filename).write_text("<sentinel>")

        mocker.patch(
            "sys.argv",
            ["stub_name", directory_arg, str(tmp_path), "date-based", custom_name],
        )

        # WHEN
        main()

        # THEN
        with open(tmp_path / f"{custom_name} - 2022-02-02.mp4", "r") as f:
            assert f.read() == "<sentinel>"
