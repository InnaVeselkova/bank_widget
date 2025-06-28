def test_shorter_number(short_number):
    assert get_mask_card_number(short_number) == "Недопустимый номер карты"


def test_longer_number():
    assert get_mask_card_number("1234 5678 9012 3456 78") == "Недопустимый номер карты"


def test_valid_number():
    assert get_mask_card_number("1784 5608 6542 6741") == "1784 56** **** 6741"