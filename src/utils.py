import json
import os
from typing import Dict


def load_transactions(json_path):
    # Загружает данные о финансовых операциях из файла JSON
    if not os.path.exists(json_path):
        # Выводит пустой список в случае отсутствия файла
        return []

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                # Не список
                return []
    except json.JSONDecodeError:
        # Ошибка чтения файла
        return []


def get_transaction_amount_in_rub(transaction: Dict) -> float:
    # Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях

    amount = transaction.get("operationAmount", {}).get('amount', 0)

    if amount == ' ':
        return 0

    currency = transaction.get("operationAmount", {}).get('currency', {}).get('code')

    if currency == 'RUB':
        return float(amount)
    else:
        from external_api import convert_to_rub
        return convert_to_rub(currency) * float(amount)


if __name__ == '__main__':  # pragma: no cover

    print(get_transaction_amount_in_rub({
        "id": 441945886,
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
