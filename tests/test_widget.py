import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        # Тест для счета
        ("счет 12123344521223123456", "счет **3456"),
        ("СЧЕТ 12345543211234987654", "СЧЕТ **7654"),
        (" счет   11111234565122345432", "счет **5432"),
        # Тест для карты
        ("карта 1234567890123456", "карта 1234 56** **** 3456"),
        ("Карта 0000111122223333", "Карта 0000 11** **** 3333"),
        (" карта   9999888877776666 ", "карта 9999 88** **** 6666"),
    ]
)
def test_mask_account_card(input_str, expected_output):
    result = mask_account_card(input_str)
    assert result == expected_output


def test_valid_date():
    assert get_date("2023-10-05T14:30:00") == "05.10.2023"


def test_date_with_time():
    assert get_date("2022-01-01T00:00:00") == "01.01.2022"


def test_date_without_time():
    assert get_date("2021-12-31") == "31.12.2021"


def test_invalid_date_format():
    with pytest.raises(ValueError):
        get_date("2023/10/05")  # неправильный формат


def test_empty_date_string():
    with pytest.raises(ValueError):
        get_date("")


def test_non_iso_format():
    with pytest.raises(ValueError):
        get_date("October 5, 2023")
