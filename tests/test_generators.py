from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тестируем фильтр по USD
def test1_filter_by_currency():
    transactions = [
        {
            'id': '1',
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        },
        {
            'id': '2',
            'operationAmount': {
                'amount': '200.00',
                'currency': {'code': 'EUR'}
            }
        },
        {
            'id': '3',
            'operationAmount': {
                'amount': '300.00',
                'currency': {'code': 'USD'}
            }
        },
        {
            # транзакция без currency
            'id': '4',
            'operationAmount': {
                'amount': '400.00'
            }
        },
        {
            # транзакция без operationAmount
            'id': '5'
        }
    ]

    try:
        result = list(filter_by_currency(transactions, 'USD'))
        # Если исключение не возникло, можно проверить результат
        print("Результат:", result)
    except KeyError as e:
        print(f"Обнаружена ошибка: {e}")


# Тестируем фильтр по 'EUR'
def test2_filter_by_currency():
    transactions = [
        {
            'id': '1',
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        },
        {
            'id': '2',
            'operationAmount': {
                'amount': '200.00',
                'currency': {'code': 'EUR'}
            }
        },
        {
            'id': '3',
            'operationAmount': {
                'amount': '300.00',
                'currency': {'code': 'USD'}
            }
        }
    ]

    result = list(filter_by_currency(transactions, 'EUR'))
    expected = [
        {
            'id': '2',
            'operationAmount': {
                'amount': '200.00',
                'currency': {'code': 'EUR'}
            }
        }
    ]

    assert result == expected


# Тестируем фильтр при отсутствии трансакций в данной валюте
def test3_filter_by_currency():
    transactions = [
        {
            'id': '1',
            'operationAmount': {
                'amount': '100.00',
                'currency': {'code': 'USD'}
            }
        },
        {
            'id': '2',
            'operationAmount': {
                'amount': '200.00',
                'currency': {'code': 'USD'}
            }
        },
        {
            'id': '3',
            'operationAmount': {
                'amount': '300.00',
                'currency': {'code': 'USD'}
            }
        },
    ]

    result = list(filter_by_currency(transactions, 'EUR'))
    expected = []
    assert result == expected


# Тестируем с разными валютами
def test_filter_by_currency_with_multiple_currencies():
    transactions = [
        {'id': '1', 'operationAmount': {'amount': '10', 'currency': {'code': 'USD'}}},
        {'id': '2', 'operationAmount': {'amount': '20', 'currency': {'code': 'EUR'}}},
        {'id': '3', 'operationAmount': {'amount': '30', 'currency': {'code': 'USD'}}}
    ]
    result = list(filter_by_currency(transactions, 'USD'))
    assert len(result) == 2
    assert all(t['operationAmount']['currency']['code'] == 'USD' for t in result)


# Тестируем фильтр при отсутствии указания валюты
def test4_filter_by_currency():
    transactions = [
        {
            'id': '1',
            'operationAmount': {
                'amount': '100.00',
            }
        },
        {
            'id': '2',
            'operationAmount': {
                'amount': '200.00',
            }
        },
        {
            'id': '3',
            'operationAmount': {
                'amount': '300.00',
            }
        },
        {
            # транзакция без currency
            'id': '4',
            'operationAmount': {
                'amount': '400.00'
            }
        },
        {
            # транзакция без operationAmount
            'id': '5'
        }
    ]

    try:
        result = list(filter_by_currency(transactions, 'USD'))
        # Если исключение не возникло, можно проверить результат
        print("Результат:", result)
    except KeyError as e:
        print(f"Обнаружена ошибка: {e}")


# Проверка с пустым списком
def test_filter_by_currency_empty_list():
    transactions = []
    result = list(filter_by_currency(transactions, 'USD'))
    assert result == []


# Проверка с отсутствующей валютой
def test_filter_by_currency_no_matching():
    transactions = [
        {'id': '1', 'operationAmount': {'amount': '50', 'currency': {'code': 'JPY'}}}
    ]
    result = list(filter_by_currency(transactions, 'USD'))
    assert result == []


# Проверяем, что функция возвращает корректные описания для каждой транзакции
def test_transaction_descriptions():
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
        }
    ]
    result = list(transaction_descriptions(transactions))
    expected = ["Перевод организации", "Перевод со счета на счет"]
    assert result == expected


# Проверка без поля description
def test_transaction_descriptions_no_description_field():
    transactions = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            }
            # description отсутствует
        }
    ]
    result = list(transaction_descriptions(transactions))
    assert result == []


# Проверка с пустой строкой
def test_transaction_descriptions_empty_description():
    transactions = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2020-01-01T00:00:00",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": " "
        }
    ]
    result = list(transaction_descriptions(transactions))
    assert result == [" "]


# Проверка правильности номеров карт в заданном диапазоне.
def test_card_number_generator(card_numbers_for_test):
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004"
    ]
    assert card_numbers_for_test == expected


# Тест с одинаковым стартовым и конечным числом
def test_card_number_generator_single():
    start = 1234
    end = 1234
    result = list(card_number_generator(start, end))
    expected = ['0000 0000 0000 1234']
    assert result == expected


# Тест с большими числами
def test_card_number_generator_large_range():
    start = 9998
    end = 10000
    result = list(card_number_generator(start, end))
    expected = [
        '0000 0000 0000 9998',
        '0000 0000 0000 9999',
        '0000 0000 0001 0000'
    ]
    assert result == expected


# Тест с end < start, то есть ничего не должно генерироваться
def test_card_number_generator_empty_range():
    # Если end < start, то ничего не должно генерироваться
    result = list(card_number_generator(10, 9))
    assert result == []
