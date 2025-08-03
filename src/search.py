import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Ищет в списке операций те, у которых в описании есть строка поиска
    """
    result = []

    for transaction in data:
        description = transaction.get('description', '')
        if re.findall(search, description, re.IGNORECASE):
            result.append(transaction)

    return result


if __name__ == '__main__':  # pragma: no cover
