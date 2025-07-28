import os
from unittest.mock import patch
from src.external_api import convert_to_rub
from dotenv import load_dotenv

load_dotenv()

@patch('requests.get')
def test_convert_to_rub_USD(mock_get):
    mock_get.return_value.json.return_value = {'rates': {'RUB': 1.1}}
    mock_get.return_value.status_code = 200
    assert convert_to_rub(currency= 'USD') == 1.1
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/latest', params= {
        'base': 'USD',
        'symbols': 'RUB',
    }, headers= {
        "apikey": os.getenv('API_KEY')
    })


@patch('requests.get')
def test_convert_to_rub_EUR(mock_get):
    mock_get.return_value.json.return_value = {'rates': {'RUB': 1.1}}
    mock_get.return_value.status_code = 200
    assert convert_to_rub(currency= 'EUR') == 1.1
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/latest', params= {
        'base': 'EUR',
        'symbols': 'RUB',
    }, headers= {
        "apikey": os.getenv('API_KEY')
    })
