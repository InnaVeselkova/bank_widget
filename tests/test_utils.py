import json
import os
import pytest

from src.utils import load_transactions, get_transaction_amount_in_rub


def test_load_transactions_valid_json_list():
    # Создаем временный файл с валидным списком
    filename = 'test_valid_list.json'
    data = [{"id": 1}, {"id": 2}]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    result = load_transactions(filename)
    assert result == data

    os.remove(filename)


def test_load_transactions_data_not_list():
    # Проверяем работу функции, если в файле не список
    filename = 'test_invalid_data.json'
    # Записываем в файл словарь вместо списка
    data = {"id": 1}
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

    result = load_transactions(filename)
    assert result == []

    os.remove(filename)


def test_load_transactions_data_not():
    # Проверяем работу функции, если файл пустой
    filename = 'test_invalid_data.json'
    with open(filename, 'w', encoding='utf-8') as f:
    # Ничего не записываем
        f.write('')
    result = load_transactions(filename)
    assert result == []

    os.remove(filename)


@pytest.mark.parametrize(
    "data, expected",
[
    (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": " ",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            0
        ),
        (
            {
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
            },
            31957.58
        ),
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": 0.0,
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            0
        )
    ]
)


def test_get_transaction_amount_in_rub(data, expected):

    """
    Проверка корректности работы при разных условиях (валюта: рубли, количество: указано;
    валюта: рубли, количество: не указано; валюта: RUB, количество: float)
    """
    assert get_transaction_amount_in_rub(data) == expected
