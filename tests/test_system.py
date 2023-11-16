# Copyright (c) 2023 Benjamin Mummery

import os


class TestSetup:
    @staticmethod
    def test_install(virtualenv):
        virtualenv.run("pwd")
        virtualenv.run(f"python -m pip install {os.getcwd()}")  # noqa: E501
