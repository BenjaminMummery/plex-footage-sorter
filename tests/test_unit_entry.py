# Copyright (c) 2023 - 2024 Benjamin Mummery

import os
from pathlib import Path
from typing import List
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from src.plex_footage_sorter.entry import main


class TestCallingSortDatedFootage:
    @staticmethod
    def test_no_recursive(
        cwd,
        tmp_path: Path,
        mocker: MockerFixture,
        mock_sort_dated_footage: Mock,
        mock_sort_movpilot_series: Mock,
        mock_rename: Mock,
    ):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "date-based", "<title sentinel>"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        mock_sort_dated_footage.assert_called_once_with(
            str(tmp_path), "<title sentinel>", recursive=False
        )
        mock_sort_movpilot_series.assert_not_called()
        mock_rename.assert_not_called()

    @staticmethod
    @pytest.mark.parametrize("recursive_arg", ["-r", "--recursive"])
    def test_recursive_args(
        cwd,
        tmp_path: Path,
        mocker: MockerFixture,
        mock_sort_dated_footage: Mock,
        mock_sort_movpilot_series: Mock,
        mock_rename: Mock,
        recursive_arg: str,
    ):
        # GIVEN
        mocker.patch(
            "sys.argv", ["stub_name", "date-based", "<title sentinel>", recursive_arg]
        )

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        mock_sort_dated_footage.assert_called_once_with(
            str(tmp_path), "<title sentinel>", recursive=True
        )
        mock_sort_movpilot_series.assert_not_called()
        mock_rename.assert_not_called()


class TestCallingSortMovpilotSeries:
    @staticmethod
    def test_arg_passing(
        cwd,
        tmp_path: Path,
        mocker: MockerFixture,
        mock_sort_dated_footage: Mock,
        mock_sort_movpilot_series: Mock,
        mock_rename: Mock,
    ):
        # GIVEN
        mocker.patch("sys.argv", ["stub_name", "movpilot-series"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        mock_sort_dated_footage.assert_not_called()
        mock_sort_movpilot_series.assert_called_once_with(str(tmp_path))
        mock_rename.assert_not_called()


class TestCallingRename:
    @staticmethod
    @pytest.mark.parametrize(
        "regex_arg, parsed_regex_arg",
        [
            (["--regex"], True),
            (["-R"], True),
            ([], False),
        ],
    )
    def test_arg_passing(
        cwd,
        tmp_path,
        mocker: MockerFixture,
        mock_sort_dated_footage: Mock,
        mock_sort_movpilot_series: Mock,
        mock_rename: Mock,
        regex_arg: str,
        parsed_regex_arg: bool,
    ):
        # GIVEN
        mocker.patch(
            "sys.argv",
            ["stub_name", "rename", "<match sentinel>", "<target sentinel>"]
            + regex_arg,
        )

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        mock_sort_dated_footage.assert_not_called()
        mock_sort_movpilot_series.assert_not_called()
        mock_rename.assert_called_once_with(
            str(tmp_path), "<match sentinel>", "<target sentinel>", parsed_regex_arg
        )

    @staticmethod
    @pytest.mark.parametrize(
        "args, missing",
        [
            (
                [
                    "<match sentinel>",
                ],
                "target",
            ),
            ([], "match, target"),
        ],
    )
    def test_raises_exception_for_missing_args(
        cwd,
        tmp_path,
        mocker: MockerFixture,
        mock_rename: Mock,
        args: List[str],
        missing: str,
        capsys: pytest.CaptureFixture,
    ):
        # GIVEN
        mocker.patch(
            "sys.argv",
            ["stub_name", "rename"] + args,
        )

        # THEN
        with cwd(tmp_path):
            with pytest.raises(SystemExit):
                main()

        captured = capsys.readouterr()
        assert captured.out == ""
        assert f"error: the following arguments are required: {missing}" in captured.err
        mock_rename.assert_not_called()


class TestSharedLogic:
    class TestDirectoryArg:
        @staticmethod
        def test_relative_path(
            cwd, tmp_path: Path, mock_sort_movpilot_series: Mock, mocker
        ):
            # GIVEN
            tmp_dir = "temp_dir"
            mocker.patch("sys.argv", ["stub_name", "-d", tmp_dir, "movpilot-series"])
            os.mkdir(tmp_path / tmp_dir)

            # WHEN
            with cwd(tmp_path):
                main()

            # THEN
            mock_sort_movpilot_series.assert_called_once_with(str(tmp_path / tmp_dir))

        @staticmethod
        def test_absolute_path(tmp_path: Path, mock_sort_movpilot_series: Mock, mocker):
            # GIVEN
            mocker.patch(
                "sys.argv", ["stub_name", "-d", str(tmp_path), "movpilot-series"]
            )

            # WHEN
            main()

            # THEN
            mock_sort_movpilot_series.assert_called_once_with(str(tmp_path))

        @staticmethod
        def test_raises_filenotfounderror_for_missing_dir(
            cwd, tmp_path: Path, mock_sort_movpilot_series: Mock, mocker
        ):
            # GIVEN
            tmp_dir = "temp_dir"
            mocker.patch("sys.argv", ["stub_name", "-d", tmp_dir, "movpilot-series"])

            # WHEN
            with cwd(tmp_path):
                with pytest.raises(FileNotFoundError) as e:
                    main()
            assert e.exconly() == (
                f"FileNotFoundError: Directory '{tmp_path / tmp_dir}' "
                "does not exist."
            )
