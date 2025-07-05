import pytest
from src.widget import mask_account_card, get_date


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