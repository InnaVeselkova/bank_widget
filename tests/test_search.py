from src.search import process_bank_search


def test_process_bank_search():
    data = [
        {'id': 1, 'description': 'Оплата за ресторан'},
        {'id': 2, 'description': 'Покупка в интернете'},
        {'id': 3, 'description': 'Оплата коммунальных услуг'},
        {'id': 4, 'description': 'Платеж за интернет'},
        {'id': 5, 'description': ''},
    ]

    # Поиск по слову "интернет"
    result = process_bank_search(data, 'интернет')
    assert len(result) == 2
    assert all('интернет' in r['description'].lower() for r in result)
    assert [r['id'] for r in result] == [2, 4]

    # Поиск по слову "оплата"
    result = process_bank_search(data, 'оплата')
    assert len(result) == 2
    assert all('оплата' in r['description'].lower() for r in result)
    assert [r['id'] for r in result] == [1, 3]

    # Поиск по слову "авто" (нет совпадений)
    result = process_bank_search(data, 'авто')
    assert len(result) == 0

    # Проверка с пустым описанием
    result = process_bank_search(data + [{'id': 6, 'description': ''}], 'платеж')
    assert len(result) == 1
    assert result[0]['id'] == 4
