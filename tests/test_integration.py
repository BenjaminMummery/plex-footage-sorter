# Copyright (c) 2023 Benjamin Mummery

import os
from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestNullCases:
    @staticmethod
    def test_no_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "stub title"])

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
        mocker.patch("sys.argv", ["stub_name", "stub title"])
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
    def test_renames_single_file_correctly(
        tmp_path: Path, cwd, mocker: MockerFixture, custom_name: str, recursion_arg: str
    ):
        # GIVEN
        filename = "20220202_222222.mp4"
        (tmp_path / filename).write_text("<sentinel>")
        args = ["stub_name", custom_name]
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
    def test_renames_multiple_files_for_same_day(
        tmp_path: Path, cwd, mocker: MockerFixture, custom_name: str, recursion_arg: str
    ):
        # GIVEN
        for i, file in enumerate(["20220202_222222.mp4", "20220202_222223.mp4"]):
            (tmp_path / file).write_text(f"<{i} sentinel>")
        args = ["stub_name", custom_name]
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
        args = ["stub_name", custom_name]
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
        args = ["stub_name", custom_name]
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
        mocker.patch("sys.argv", ["stub_name", custom_name, recursion_arg])

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
