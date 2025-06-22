def filter_by_state(dict_list, state = 'EXECUTED') -> list:

#Фильтрует список словарей

    return [dict_ for dict_ in dict_list if dict_.get('state') == state]


def sort_by_date(dict_list, reverse=True) -> list:

#Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)

    return sorted(dict_list, key=lambda dict_: dict_.get('date'), reverse=reverse)
