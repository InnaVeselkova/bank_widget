import json
import logging
import os
from typing import Dict, List, Any
from src.widget import get_date, mask_account_card
from src.external_api import convert_to_rub


# Получение корневого логера
root_logger = logging.getLogger()

# Создание и получение именованного логера
app_logger_utils = logging.getLogger("my_lg_utils")

file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
app_logger_utils.addHandler(file_handler)
app_logger_utils.setLevel(logging.DEBUG)


def load_transactions(json_path):
    """ Загружает данные о финансовых операциях из файла JSON """
    app_logger_utils.info(f"Загрузка транзакций из файла: {json_path}")
    if not os.path.exists(json_path):
        # Выводит пустой список в случае отсутствия файла
        app_logger_utils.warning(f"Файл не найден: {json_path}. Возвращаю пустой список.")
        return []

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                app_logger_utils.info(f"Успешно загружено {len(data)} транзакций.")
                return data
            else:
                app_logger_utils.warning("Данные в файле не являются списком.")
                # Не список
                return []
    except json.JSONDecodeError as e:
        app_logger_utils.error(f"Ошибка декодирования JSON: {e}")
        # Ошибка чтения файла
        return []


def get_transaction_amount_in_rub(transaction: Dict) -> float:
    """  Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях """
    app_logger_utils.info(f"Обработка транзакции: {transaction}")

    amount = transaction.get("operationAmount", {}).get('amount', 0)
    app_logger_utils.debug(f"Исходная сумма: {amount}")

    if amount == ' ':
        app_logger_utils.warning(f"Пустая сумма для транзакции: {transaction}. Возвращаю 0.")
        return 0

    currency = transaction.get("operationAmount", {}).get('currency', {}).get('code')
    app_logger_utils.info(f"Валюта транзакции: {transaction}: {currency}")

    if currency == 'RUB':
        app_logger_utils.info(f"Для транзакции {transaction} сумма в рублях {float(amount)}")
        return float(amount)
    else:
        app_logger_utils.info(f"Транзакция {transaction} в валюте {currency}")
        from external_api import convert_to_rub
        return convert_to_rub(currency) * float(amount)


def _print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит отформатированный список транзакций."""
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}\n")

    for transaction in transactions:
        date = get_date(transaction['date']) if 'date' in transaction else 'Нет даты'
        description = transaction.get('description', 'Без описания')

        # Обработка отправителя и получателя
        from_info = mask_account_card(transaction.get('from', '')) if transaction.get('from') else ''
        to_info = mask_account_card(transaction.get('to', '')) if transaction.get('to') else ''

        # Обработка суммы
        amount_info = transaction.get('operationAmount', {})
        amount = float(amount_info.get('amount', 0)) if amount_info.get('amount') else 0
        currency = amount_info.get('currency', {}).get('code', '')

        if currency and currency != 'RUB':
            amount_rub = convert_to_rub(transaction)
            amount_str = f"{amount} {currency} (~{amount_rub:.2f} руб.)" if amount_rub else f"{amount} {currency}"
        else:
            amount_str = f"{amount} руб."

        # Вывод информации о транзакции
        print(f"{date} {description}")
        if from_info and to_info:
            print(f"{from_info} -> {to_info}")
        elif from_info:
            print(f"{from_info}")
        elif to_info:
            print(f"{to_info}")
        print(f"Сумма: {amount_str}\n")


if __name__ == '__main__':  # pragma: no cover

    print(get_transaction_amount_in_rub({
        "id": 641945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }))

    print(get_transaction_amount_in_rub({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }))
