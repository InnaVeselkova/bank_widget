from src.utils import load_transactions
from src.readers_csv_excel import load_transactions_from_csv, load_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.utils import _print_transactions

json_path = "../data/operations.json"
csv_path = "../data/transactions.csv"
excel_path = "../data/transactions_excel.xlsx"


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями')
    print("""Выберите необходимый пункт меню: \n
    1. Получить информацию о транзакциях из JSON - файла \n
    2. Получить информацию о транзакциях из CSV - файла \n
    3. Получить информацию о транзакциях из XLSX - файла \n""")
    user_input = input('Введите ответ:')

    if user_input == '1':
        print('Для обработки выбран JSON-файл')
        transactions = load_transactions(json_path)
    elif user_input == '2':
        print('Для обработки выбран CSV-файл')
        transactions = load_transactions_from_csv(csv_path)
    elif user_input == '3':
        print('Для обработки выбран XLSX-файл')
        transactions = load_transactions_from_excel(excel_path)
    else:
        print('Некорректный выбор. Завершение программы.')
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    filtered_transactions = []
    while True:
        user_input_1 = input("""Введите статус, по которому необходимо выполнить фильтрацию.\n
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
        if user_input_1 in valid_statuses:
            if user_input_1 == "EXECUTED":
                print('Операции отфильтрованы по статусу "EXECUTED"')
                filtered_transactions = filter_by_state(transactions, "EXECUTED")
            elif user_input_1 == "CANCELED":
                print('Операции отфильтрованы по статусу "CANCELED"')
                filtered_transactions = filter_by_state(transactions, "CANCELED")
            elif user_input_1 == "PENDING":
                print('Операции отфильтрованы по статусу "PENDING"')
                filtered_transactions = filter_by_state(transactions, "PENDING")
            break  # Выход из цикла при правильном вводе
        else:
            print("Некорректный статус. Пожалуйста, попробуйте снова.")

    sort_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    sort_date_transactions = []
    if sort_date == "да":
        order = input("Отсортировать по возрастанию или по убыванию? \n").strip().lower()
        if order == "по убыванию":
            sort_date_transactions = sort_by_date(filtered_transactions)
        elif order == "по возрастанию":
            sort_date_transactions = sort_by_date(filtered_transactions, False)
        else:
            print("Неправильный выбор")
    else:
        sort_date_transactions = filtered_transactions

    only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if only_rub == "да":
        sorted_transaction_in_rub = filter_by_currency(sort_date_transactions, "RUB")
    else:
        sorted_transaction_in_rub = sort_date_transactions

    filter_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if filter_word == "да":
        keyword = input("Введите слово для поиска:\n").strip().lower()
        result_filtered_transactions = [t for t in sorted_transaction_in_rub if keyword in t['description'].lower()]
    else:
        result_filtered_transactions = sorted_transaction_in_rub


    _print_transactions(result_filtered_transactions)


if __name__ == '__main__':
    main()

