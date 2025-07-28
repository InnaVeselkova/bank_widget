import json
import os
from typing import List, Dict

from data.path import json_path
from external_api import convert_to_rub


def load_transactions(json_path):
    # Загружает данные о финансовых операциях из файла JSON
    if not os.path.exists(json_path):
        # Выводит пустой список в случае отсутствия файла
        return []

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                # Файл пустой
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            else:
                # Не список
                return []
    except (json.JSONDecodeError):
        # Ошибка чтения файла
        return []


def get_transaction_amount_in_rub(transactions: List[Dict]) -> float:
    # Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях
    for transaction in transactions:
        amount = transaction.get("operationAmount", {}).get('amount', 0)
        currency= transaction.get("operationAmount", {}).get('currency', {}).get('code')

        if currency == 'RUB':
            result = amount
            return result
        else:
            return convert_to_rub(amount, currency)

if __name__ == '__main__':  # pragma: no cover

    data = load_transactions(json_path)

    transactions_amount = []
    result = get_transaction_amount_in_rub(data)
    transactions_amount.append(result)

print(transactions_amount)
