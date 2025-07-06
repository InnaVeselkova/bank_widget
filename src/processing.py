from typing import List, Dict, Any


def filter_by_state(records: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    # Фильтрует список словарей по состоянию
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    # Фильтрует список словарей по дате (по умолчанию — убывание)
    return sorted(records, key=lambda record: record.get('date') or '', reverse=reverse)


def test_sort_with_various_date_formats():
    records = [
        {'id': 1, 'date': '01/11/2025'},   # формат DD/MM/YYYY
        {'id': 2, 'date': '2025-11-07'},   # формат ISO
        {'id': 3, 'date': '11-05-2025'},   # другой формат
        {'id': 4, 'date': '2025/11/01'}
    ]
    sorted_records = sort_by_date(records)
    sorted_ = [record.get('id') for record in sorted_records]
    print(sorted_)