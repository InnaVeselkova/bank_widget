import json
import os

from data.path import json_path


def load_transactions(json_path):
    # Загружает данные из файла JSON
    if not os.path.exists(json_path):
        # Выводит пустой список в случае отсутствия файла
        return []

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                # Файл пустой
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            else:
                # Не список
                return []
    except (json.JSONDecodeError):
        # Ошибка чтения файла
        return []


if __name__ == '__main__':  # pragma: no cover
    data = load_transactions(json_path)
    print(data)
