from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number_of_card_or_account: str) -> str:
    """функция обработки информации о картах или о счетах"""

    """Разделяем входную строку на слова и отделяем номер, как 2 элемент"""
    parts = type_and_number_of_card_or_account.strip().split()
    number = parts[-1]
    type_ = " ".join(parts[:-1])

    """Условие для определения типа"""
    if type_.lower() == "счет":
        masked_number = get_mask_account(number)
        return f"{type_} {masked_number}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{type_} {masked_number}"


def get_date(date_str: str) -> str:
    # Попытка распарсить дату в нескольких форматах
    formats = ['%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y', '%Y/%m/%d']
    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            continue
    # Если ни один формат не подошёл, можно вернуть исходную строку или поднять исключение
    raise ValueError(f"Неподдерживаемый формат даты: {date_str}")


def get_date(date_: str) -> str:
   try:
        dt = datetime.fromisoformat(date_)
        return dt.strftime("%d.%m.%Y")
   except:
        dt = datetime.fromisoformat(date_[::-1])
        print(dt)
        return dt.strftime("%d.%m.%Y")


if __name__ == '__main__':
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(get_date("2024-03-11T02:26:18.671407"))
