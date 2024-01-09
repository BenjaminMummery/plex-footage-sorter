# Copyright (c) 2024 Benjamin Mummery

from pathlib import Path

import pytest
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


class TestStarWildcard:
    @staticmethod
    def test_rename_single_file(tmp_path: Path, cwd, mocker: MockerFixture):
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

    @staticmethod
    def test_rename_multiple_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        infiles = ["episode_1.mkv", "episode_theocratic", "episode_1312.foo"]
        outfiles = ["S01E01.mkv", "S01E0theocratic", "S01E01312.foo"]
        for file in infiles:
            (tmp_path / file).write_text(f"<file {file} sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_*", "S01E0*"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for infile, outfile in zip(infiles, outfiles):
            assert not (tmp_path / infile).exists()
            assert (new_file := (tmp_path / outfile)).is_file()
            with open(new_file) as f:
                assert f.read() == f"<file {infile} sentinel>"

    @staticmethod
    def test_ignores_non_matching_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        infiles = ["episode_1.mkv", "episode_theocratic", "episode_1312.foo"]
        outfiles = ["S01E01.mkv", "S01E0theocratic", "S01E01312.foo"]
        for file in infiles:
            (tmp_path / file).write_text(f"<file {file} sentinel>")
        (nonmatching_file := (tmp_path / "non-matching.file")).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_*", "S01E0*"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for infile, outfile in zip(infiles, outfiles):
            assert not (tmp_path / infile).exists()
            assert (new_file := (tmp_path / outfile)).is_file()
            with open(new_file) as f:
                assert f.read() == f"<file {infile} sentinel>"
        assert nonmatching_file.is_file()
        with open(nonmatching_file) as f:
            assert f.read() == "<sentinel>"


class TestQuestionmarkWildcard:
    @staticmethod
    def test_rename_single_file(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        (tmp_path / (filename := "episode_1.mkv")).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_?.mkv", "S01E0?.mkv"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        assert not (tmp_path / filename).exists()
        assert (new_file := (tmp_path / "S01E01.mkv")).is_file()
        with open(new_file) as f:
            assert f.read() == "<sentinel>"

    @staticmethod
    def test_rename_multiple_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        infiles = ["episode_1.mkv", "episode_9.mkv", "episode_x.mkv"]
        outfiles = ["S01E01.mkv", "S01E09.mkv", "S01E0x.mkv"]
        for file in infiles:
            (tmp_path / file).write_text(f"<file {file} sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_?.mkv", "S01E0?.mkv"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for infile, outfile in zip(infiles, outfiles):
            assert not (tmp_path / infile).exists()
            assert (new_file := (tmp_path / outfile)).is_file()
            with open(new_file) as f:
                assert f.read() == f"<file {infile} sentinel>"

    @staticmethod
    def test_ignores_non_matching_files(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        infiles = ["episode_1.mkv", "episode_9.mkv", "episode_x.mkv"]
        outfiles = ["S01E01.mkv", "S01E09.mkv", "S01E0x.mkv"]
        for file in infiles:
            (tmp_path / file).write_text(f"<file {file} sentinel>")
        (nonmatching_file := (tmp_path / "non-matching.file")).write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_?.mkv", "S01E0?.mkv"])

        # WHEN
        with cwd(tmp_path):
            main()

        # THEN
        for infile, outfile in zip(infiles, outfiles):
            assert not (tmp_path / infile).exists()
            assert (new_file := (tmp_path / outfile)).is_file()
            with open(new_file) as f:
                assert f.read() == f"<file {infile} sentinel>"
        assert nonmatching_file.is_file()
        with open(nonmatching_file) as f:
            assert f.read() == "<sentinel>"


class TestFailureStates:
    @staticmethod
    def test_unsupported_glob_wildcard(tmp_path: Path, cwd, mocker: MockerFixture):
        # GIVEN
        (tmp_path / "episode_a.mkv").write_text("<sentinel>")
        mocker.patch(
            "sys.argv", ["stub_name", "rename", "episode_[a].mkv", "S01E0[a].mkv"]
        )

        # WHEN
        with cwd(tmp_path):
            with pytest.raises(NotImplementedError) as e:
                main()

        # THEN
        assert e.exconly() == (
            "NotImplementedError: Pattern 'episode_[a].mkv' contains glob wildcards "
            "that are not yet supported."
        )

    @staticmethod
    def test_mismatching_wildcards_between_match_and_target(
        tmp_path: Path, cwd, mocker: MockerFixture
    ):
        # GIVEN
        (tmp_path / "episode_a.mkv").write_text("<sentinel>")
        mocker.patch("sys.argv", ["stub_name", "rename", "episode_?.mkv", "S01E0*.mkv"])

        # WHEN
        with cwd(tmp_path):
            with pytest.raises(ValueError) as e:
                main()

        # THEN
        assert e.exconly() == (
            "ValueError: Mismatching glob wildcards between input and output patterns "
            "'episode_?.mkv' and 'S01E0*.mkv': '?' vs '*'."
        )
