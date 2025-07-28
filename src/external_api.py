import os
from dotenv import load_dotenv
import requests
import json

# Загрузка переменных из .env-файла
load_dotenv()

# Получение значения переменной exchange_API из .env-файла
exchange_API= os.getenv('API_KEY')


def convert_to_rub(amount: float, currency: str) -> float:
    # Конвертирует из USD или EUR в рубли
    url = f"https://api.apilayer.com/exchangerates_data/covert"
    headers = {
        "apikey": exchange_API
    }
    params = {
        'from': currency,
        'to': 'RUB',
        'amount': amount
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе: {response.status_code} - {response.text}")

    # Получение распарсенных данных
    data = response.json()

    # Рассчитываем сумму в рублях
    result = data.get('result', 0)
    return result









