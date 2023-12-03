# Copyright (c) 2023 Benjamin Mummery

import os
from contextlib import contextmanager
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture


@pytest.fixture(scope="session")
def cwd():
    @contextmanager
    def cwd(path):
        oldcwd = os.getcwd()
        os.chdir(path)
        try:
            yield
        finally:
            os.chdir(oldcwd)

    return cwd


@pytest.fixture
def mock_entry(mocker: MockerFixture):
    return mocker.patch("src.plex_footage_sorter.entry.main", Mock())


@pytest.fixture
def mock_sort_dated_footage(mocker: MockerFixture):
    return mocker.patch(
        "src.plex_footage_sorter._sort_dated_footage_as_date_series.main", Mock()
    )


@pytest.fixture
def mock_sort_movpilot_series(mocker: MockerFixture):
    return mocker.patch("src.plex_footage_sorter._sort_movpilot_series.main", Mock())
