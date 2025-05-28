from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number_of_card_or_account: str) -> str:
    """функция обработки информации о картах или о счетах"""

    """Разделяем входную строку на слова и отделяем номер, как 2 элемент"""
    parts = type_and_number_of_card_or_account.strip().split()
    number = parts[-1]
    type_ = " ".join(parts[:-1])

    """Условие для определения типа"""
    if type_.lower() == 'счет':
        masked_number = get_mask_account(number)
        return f"{type_} {masked_number}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{type_} {masked_number}"


def get_date(date_str: str) -> str:


print(mask_account_card('Visa Classic 6831982476737658'))