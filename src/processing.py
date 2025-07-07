from typing import List, Dict, Any

from datetime import datetime


def filter_by_state(records: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    # Фильтрует список словарей по состоянию
    return [record for record in records if record.get('state') == state]


def parse_date(date_str: str) -> datetime:
    # Попытка парсинга даты в нескольких форматах
    for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    # Если ни один формат не подошел, выбрасываем исключение или возвращаем минимальную дату
    raise ValueError(f"Unknown date format: {date_str}")

def sort_by_date(records: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    def get_date(record):
        date_str = record.get('date')
        if not date_str:
            # Если дата отсутствует, считаем её минимальной (или можно оставить как есть)
            return datetime.min
        try:
            return parse_date(date_str)
        except ValueError:
            # В случае ошибки парсинга тоже считаем минимальной датой
            return datetime.min

    # Сортируем по объектам datetime
    return sorted(records, key=get_date, reverse=reverse)