import csv
import os
from typing import Dict, List

import pandas as pd

csv_path = "../data/transactions.csv"


def load_transactions_from_csv(csv_path: str) -> List[Dict]:
    """
    Загружает транзакции из CSV файла
    """
    transactions_csv = []

    if not os.path.exists(csv_path):
        # Возвращает пустой список если файл не существует
        return []

    # Читаем файл и добавляем каждую транзакцию в список транзакций
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transactions_csv.append(row)

    return transactions_csv


excel_path = "../data/transactions_excel.xlsx"


def load_transactions_from_excel(excel_path: str) -> List[Dict]:
    """
    Загружает транзакции из файла Excel в виде списка словарей
    """
    # Проверка существования файла
    if not os.path.exists(excel_path):
        print(f"Файл не найден по пути: {excel_path}")
        return []

    # Чтение файла Excel в DataFrame
    df = pd.read_excel(excel_path)
    if df.empty:
        print("Файл пустой или не содержит данных.")
        return []

    # Преобразование DataFrame в список словарей
    transactions_ex = df.to_dict(orient='records')

    return transactions_ex


if __name__ == '__main__':  # pragma: no cover
    print(load_transactions_from_csv(csv_path))
    print(load_transactions_from_excel(excel_path))
