import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_shorter_number_card(short_number):
    assert get_mask_card_number(short_number) == "Недопустимый номер карты"


def test_shorter_number_account(short_number):
    assert get_mask_account(short_number) == "Недопустимый номер счета"


def test_longer_number_card(long_number):
    assert get_mask_card_number(long_number) == "Недопустимый номер карты"


def test_longer_number_account(long_number):
    assert get_mask_account(long_number) == "Недопустимый номер счета"


def test_valid_number_card():
    assert get_mask_card_number("1784 5608 6542 6741") == "1784 56** **** 6741"


def test_valid_number_account():
    assert get_mask_account("178456") == "**8456"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("fh", "Ошибка: номер карты содержит недопустимые символы."),
        ("1234 6578 @678 9078", "Ошибка: номер карты содержит недопустимые символы."),
        ("1234 rgfr 8976 000g", "Ошибка: номер карты содержит недопустимые символы."),
        ("", 'Недопустимый номер карты'),
        (" ", 'Недопустимый номер карты'),
        ("                ", 'Недопустимый номер карты')
    ]
)
def test_correct_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("fh", "Ошибка: номер счета содержит недопустимые символы."),
        ("1234 6578 @678 9078", "Ошибка: номер счета содержит недопустимые символы."),
        ("1234 rgfr 8976 000g", "Ошибка: номер счета содержит недопустимые символы."),
        ("", 'Недопустимый номер счета'),
        (" ", 'Недопустимый номер счета'),
        ("                ", 'Недопустимый номер счета')
    ]
)
def test_correct_account_number(account_number, expected):
    assert get_mask_account(account_number) == expected



