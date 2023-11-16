# Copyright (c) 2023 Benjamin Mummery

import os


class TestSetup:
    @staticmethod
    def test_install(virtualenv):
        print(os.getcwd())
        virtualenv.run("pwd")
        virtualenv.run(
            f"python -m pip install {os.getcwd()}/dist/phone_footage_sorter-0.0.0-py2.py3-none-any.whl"  # noqa: E501
        )
