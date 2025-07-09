import pytest


@pytest.fixture
def short_number():
    return "1234 5678 9012"


@pytest.fixture
def long_number():
    return "1234 5678 9012 3456 7822 3333 4444"
