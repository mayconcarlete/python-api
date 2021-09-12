import pytest


@pytest.fixture
def print_fixture():
    print('Im fixture')
    