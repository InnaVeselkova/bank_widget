from typing import List, Dict, Any


def filter_by_state(records: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    # Фильтрует список словарей по состоянию
    return [record for record in records if record.get('state') == state]


def sort_by_date(records: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    # Фильтрует список словарей по дате (по умолчанию — убывание)
    return sorted(records, key=lambda record: record.get('date') or '', reverse=reverse)
