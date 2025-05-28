def get_mask_card_number(card_number: str) -> str:
    """функция отображения маски номера карты"""

    """Удаляем все пробелы и другие нецифровые символы"""
    digits = "".join(filter(str.isdigit, card_number))

    """Проверка длины номера"""
    if len(digits) != 16:
        return "Недопустимый номер карты"

    """Маскируем цифры посередине"""
    masked_digits_card_number = digits[:4] + ' ' + digits[4:6] + "*" * 2 + ' ' + "*" * 4 + ' ' + digits[-4:]

    return masked_digits_card_number


def get_mask_account(account_number: str) -> str:
    """функция отображения маски номера счета"""

    """Удаляем все пробелы и другие нецифровые символы"""
    digits = "".join(filter(str.isdigit, account_number))

    """Маскируем цифры и убираем лишние"""
    masked_account_number = "**" + digits[-4:]

    return masked_account_number


