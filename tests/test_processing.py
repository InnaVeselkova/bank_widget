import pytest

from src.processing import filter_by_state, sort_by_date, process_bank_operations


@pytest.mark.parametrize("records, state, expected", [
    (
        [
            {'id': 1, 'state': 'EXECUTED'},
            {'id': 2, 'state': 'PENDING'},
            {'id': 3, 'state': 'EXECUTED'}
        ],
        'EXECUTED',
        [
            {'id': 1, 'state': 'EXECUTED'},
            {'id': 3, 'state': 'EXECUTED'}
        ]
    ),
    (
        [
            {'id': 4, 'state': 'CANCELLED'},
            {'id': 5, 'state': 'CANCELLED'}
        ],
        'CANCELLED',
        [
            {'id': 4, 'state': 'CANCELLED'},
            {'id': 5, 'state': 'CANCELLED'}
        ]
    ),
    (
        [
            {'id': 1, 'state': 'PENDING'},
            {'id': 2, 'state': 'CANCELLED'},
            {'id': 3, 'state': 'FAILED'}
        ],
        'EXECUTED',
        []
    )
]
)
def test_filter_by_state_various(records, state, expected):
    result = filter_by_state(records, state)
    assert result == expected


def test_default_state():
    # не передаем state
    records = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'PENDING'}
    ]
    result = filter_by_state(records)
    assert result == [{'id': 1, 'state': 'EXECUTED'}]


@pytest.mark.parametrize(
    "records, expected_dates, reverse",
    [
        (
            [
                {'id': 1, 'date': '2025-11-01'},
                {'id': 2, 'date': '2025-09-18'},
                {'id': 3, 'date': '2024-10-09'},
            ],
            ['2025-11-01', '2025-09-18', '2024-10-09'],
            True
        ),
        (
            [
                {'id': 1, 'date': '2025-11-01'},
                {'id': 2, 'date': '2025-09-18'},
                {'id': 3, 'date': '2024-10-09'},
            ],
            ['2024-10-09', '2025-09-18', '2025-11-01'],
            False
        ),
    ]
)
def test_sort_by_date(records, expected_dates, reverse):
    sorted_records = sort_by_date(records, reverse=reverse)
    dates = [record['date'] for record in sorted_records]
    assert dates == expected_dates


def test_sort_with_identical_dates():
    records = [
        {'id': 1, 'date': '2025-11-01'},
        {'id': 2, 'date': '2025-11-07'},
        {'id': 3, 'date': '2025-11-07'},
    ]
    sorted_records = sort_by_date(records)
    sorted_dates = [record['date'] for record in sorted_records]
    assert sorted_dates == ['2025-11-07', '2025-11-07', '2025-11-01']


def test_sort_with_various_date_formats():
    records = [
        {'id': 1, 'date': '01/11/2025'},
        {'id': 2, 'date': '2025-11-07'},
        {'id': 3, 'date': '11-05-2025'},
        {'id': 4, 'date': '2025/11/02'}
    ]
    sorted_records = sort_by_date(records)
    sorted_ids = [record.get('id') for record in sorted_records]
    print(sorted_ids)
    # Проверка: дата с id=2 должна быть первой
    assert sorted_ids[0] == 2


def test_invalied_date():
    with pytest.raises(TypeError):

        sort_by_date('test')


def test_process_bank_operations_basic():
    data = [
        {'id': 1, 'description': 'Оплата за интернет'},
        {'id': 2, 'description': 'Покупка в магазине'},
        {'id': 3, 'description': 'Оплата коммунальных услуг'},
        {'id': 4, 'description': 'Платеж за телефон'},
        {'id': 5, 'description': 'Оплата за интернет и телевидение'},
    ]
    categories = ['интернет', 'магазин', 'телефон']

    result = process_bank_operations(data, categories)

    assert result == {
        'интернет': 2,
        'магазин': 1,
        'телефон': 1
    }


def test_process_bank_operations_no_matches():
    data = [
        {'id': 1, 'description': 'Покупка в магазине'},
        {'id': 2, 'description': 'Платеж за коммунальные услуги'},
    ]
    categories = ['авто', 'еда']

    result = process_bank_operations(data, categories)

    # Ожидается пустой словарь, так как совпадений нет
    assert result == {}


def test_process_bank_operations_partial_matches():
    data = [
        {'id': 1, 'description': 'Оплата за интернет'},
        {'id': 2, 'description': 'Покупка в магазине'},
        {'id': 3, 'description': ''},  # пустое описание
        {'id': 4, 'description': 'Оплата за телефон и интернет'},
    ]
    categories = ['интернет', 'магазин', 'телефон']

    result = process_bank_operations(data, categories)

    assert result == {
        'интернет': 2,
        'магазин': 1,
        'телефон': 1
    }
