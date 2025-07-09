from typing import List, Dict, Any


def filter_by_state(records: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    # Фильтрует список словарей по состоянию
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    # Фильтрует список словарей по дате (по умолчанию — убывание)
    try:
        return sorted(records, key=lambda record: record.get('date').replace("/", "-") or '', reverse=reverse)
    except Exception as e:
        raise TypeError("Некорректный формат данных")


records = [
        {'id': 1, 'date': '01/11/2025'},
        {'id': 2, 'date': '2025-11-07'},
        {'id': 3, 'date': '11-05-2025'},
        {'id': 4, 'date': '2025/11/02'}
    ]
print(sort_by_date(records))
