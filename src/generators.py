from typing import List, Dict, Iterator, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    # Генератор фильтрует транзакции по валюте
    return (transaction for transaction in transactions
            if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency)


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    # Генератор возвращает описания транзакций, если есть ключ 'description'
    return (transaction["description"] for transaction in transactions if "description" in transaction)


def card_number_generator(start: int, end: int) -> Iterator[str]:
#Генерирует номера карт в формате 'XXXX XXXX XXXX XXXX' в диапазоне от start до end включительно.
    for number in range(start, end + 1):
        yield ' '.join(f"{number:016d}"[i:i + 4] for i in range(0, 16, 4))

if __name__ == '__main__':

    transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 142264269,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "I",
                "code": "I"
            }
        },
        # Описание отсутствует у этой транзакции, чтобы проверить условие
    }
]

# Получаем транзакции в USD
usd_transactions = filter_by_currency(transactions, 'USD')

# Выводим первые 3 транзакции с валютой USD
for _ in range(3):
    try:
        print(next(usd_transactions))
    except StopIteration:
        print("Больше транзакций с валютой USD нет.")

# Получаем описания всех транзакций
descriptions = transaction_descriptions(transactions)

# Выводим первые 3 описания
for _ in range(3):
    try:
        print(next(descriptions))
    except StopIteration:
        print("Больше описаний нет.")

for card_number in card_number_generator(1, 5):
    print(card_number)