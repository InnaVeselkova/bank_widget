import logging

# Получение корневого логера
root_logger = logging.getLogger()

# Создание и получение именованного логера
app_logger_masks = logging.getLogger("my_lg_masks")

file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
app_logger_masks.addHandler(file_handler)
app_logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """функция отображения маски номера карты"""
    app_logger_masks.info(f"Вызов get_mask_card_number с номером: {card_number}")

    """Проверка корректности символов номера"""
    if not all(c.isdigit() or c.isspace() for c in card_number):
        app_logger_masks.warning("Некорректные символы в номере карты")
        return "Ошибка: номер карты содержит недопустимые символы."

    """Удаляем все пробелы и другие нецифровые символы"""
    digits = "".join(filter(str.isdigit, card_number))
    app_logger_masks.debug(f"Обработанные цифры карты: {digits}")

    """Проверка длины номера"""
    if len(digits) != 16:
        app_logger_masks.warning(f"Недопустимая длина номера карты: {len(digits)}")
        return "Недопустимый номер карты"

    """Маскируем цифры посередине"""
    masked_digits_card_number = digits[:4] + ' ' + digits[4:6] + "*" * 2 + ' ' + "*" * 4 + ' ' + digits[-4:]
    app_logger_masks.info(f"Маскированный номер карты: {masked_digits_card_number}")
    return masked_digits_card_number


def get_mask_account(account_number: str) -> str:
    """функция отображения маски номера счета"""

    """Проверка корректности символов номера"""
    if not all(c.isdigit() or c.isspace() for c in account_number):
        app_logger_masks.warning("Некорректные символы в номере счета")
        return "Ошибка: номер счета содержит недопустимые символы."

    """Удаляем все пробелы и другие нецифровые символы"""
    digits = "".join(filter(str.isdigit, account_number))
    app_logger_masks.debug(f"Обработанные цифры счета: {digits}")

    """Проверка длины номера счета"""
    if len(digits) != 20:
        app_logger_masks.warning(f"Недопустимая длина номера счета: {len(digits)}")
        return "Недопустимый номер счета"

    """Маскируем цифры и убираем лишние"""
    masked_account_number = "**" + digits[-4:]
    app_logger_masks.info(f"Маскированный номер счета: {masked_account_number}")
    return masked_account_number


if __name__ == '__main__':  # pragma: no cover
    get_mask_card_number("1234567890123456")
    get_mask_account("11223344556677889900")
    get_mask_card_number("12345890123456")
    get_mask_account("1122334455667789900")
