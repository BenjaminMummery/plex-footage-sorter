# Copyright (c) 2023 - 2024 Benjamin Mummery

import os

import pytest

from src import __version__


class TestSetup:
    @staticmethod
    def test_install(virtualenv):
        virtualenv.run(f"python -m pip install {os.getcwd()}")
        version_run: str = virtualenv.run("plex-footage-sorter --version", capture=True)
        assert version_run.strip() == f"plex-footage-sorter {__version__}"


@pytest.mark.parametrize("custom_name", ["'Training Videos'"])
class TestRun:
    @staticmethod
    def test_flat_folder(virtualenv, tmp_path, custom_name):
        # GIVEN
        infiles = [
            "20220202_222222.mp4",
            "20220203_222222.mp4",
            "20220203_222223.mp4",
            "20231216-0009.mp4",
            "20231216-0010.mp4",
            "20231217-0008.mp4",
            "20231217-0090.mp4",
            "20231217-0095.mp4",
        ]
        outfiles = [
            "Training Videos - 2022-02-02.mp4",
            "Training Videos - 2022-02-03 - Part1.mp4",
            "Training Videos - 2022-02-03 - Part2.mp4",
            "Training Videos - 2023-12-16 - Part1.mp4",
            "Training Videos - 2023-12-16 - Part2.mp4",
            "Training Videos - 2023-12-17 - Part1.mp4",
            "Training Videos - 2023-12-17 - Part2.mp4",
            "Training Videos - 2023-12-17 - Part3.mp4",
        ]
        for file in infiles:
            (tmp_path / file).write_text("")

        # WHEN
        virtualenv.run(f"python -m pip install {os.getcwd()}")
        virtualenv.run(f"cd {tmp_path} && plex-footage-sorter date-based {custom_name}")

        # THEN
        assert set(os.listdir(tmp_path)) == set(outfiles)

    @staticmethod
    def test_subfolder_no_recurse(virtualenv, tmp_path, custom_name):
        # GIVEN
        infiles = ["20220202_222222.mp4", "20220203_222222.mp4", "20220203_222223.mp4"]
        outfiles = [
            "Training Videos - 2022-02-02.mp4",
            "Training Videos - 2022-02-03 - Part1.mp4",
            "Training Videos - 2022-02-03 - Part2.mp4",
        ]
        subdir = "subdir"
        (tmp_path / subdir).mkdir()
        for file in infiles:
            (tmp_path / file).write_text("")
            (tmp_path / subdir / file).write_text("")

        # WHEN
        virtualenv.run(f"python -m pip install {os.getcwd()}")
        virtualenv.run(f"cd {tmp_path} && plex-footage-sorter date-based {custom_name}")

        # THEN
        assert set(os.listdir(tmp_path)) == set(outfiles + [subdir])
        assert set(os.listdir(tmp_path / subdir)) == set(infiles)

    @staticmethod
    def test_subfolder_recurse(virtualenv, tmp_path, custom_name):
        # GIVEN
        infiles = ["20220202_222222.mp4", "20220203_222222.mp4", "20220203_222223.mp4"]
        infiles_subdir = [
            "20230202_222222.mp4",
            "20230203_222222.mp4",
            "20230203_222223.mp4",
        ]
        outfiles = [
            "Training Videos - 2022-02-02.mp4",
            "Training Videos - 2022-02-03 - Part1.mp4",
            "Training Videos - 2022-02-03 - Part2.mp4",
        ]
        outfiles_subdir = [
            "Training Videos - 2023-02-02.mp4",
            "Training Videos - 2023-02-03 - Part1.mp4",
            "Training Videos - 2023-02-03 - Part2.mp4",
        ]
        subdir = "subdir"
        (tmp_path / subdir).mkdir()
        for file in infiles:
            (tmp_path / file).write_text("")
        for file in infiles_subdir:
            (tmp_path / subdir / file).write_text("")

        # WHEN
        virtualenv.run(f"python -m pip install {os.getcwd()}")
        virtualenv.run(
            f"cd {tmp_path} && plex-footage-sorter date-based {custom_name} -r"
        )

        # THEN
        assert set(os.listdir(tmp_path)) == set(outfiles + [subdir])
        assert set(os.listdir(tmp_path / subdir)) == set(outfiles_subdir)
