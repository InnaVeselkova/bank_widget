import pytest

from src.generators import card_number_generator


@pytest.fixture
def short_number():
    return "1234 5678 9012"


@pytest.fixture
def long_number():
    return "1234 5678 9012 3456 7822 3333 4444"

@pytest.fixture
def card_numbers_for_test():
    return list(card_number_generator(1, 4))
