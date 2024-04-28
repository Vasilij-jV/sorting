# -*- config: utf-8 -*-
import json


# Функция для семантического сравнения строк
def are_strings_semantically_equal(str1, obj_with_employees):
    counter = False
    for key, value in obj_with_employees['employees'][0].items():
        if str1.casefold() == key.casefold():
            return key, value
        else:
            counter = True
    if counter:
        raise ValueError('Bad key for sorting')


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as json_employees_in_func:
        obj_employees_in_func = json.load(json_employees_in_func)

    obj_employees_in_func_sorted = 0

    try:
        good_key = are_strings_semantically_equal(sort_type, obj_employees_in_func)
        # Два блока сортировки
        if isinstance(good_key[1], str):
            obj_employees_in_func_sorted = {
                'employees': sorted(obj_employees_in_func['employees'], key=lambda x: x[good_key[0]])}
        elif isinstance(good_key[1], int):
            obj_employees_in_func_sorted = {
                'employees': sorted(obj_employees_in_func['employees'], key=lambda x: x[sort_type], reverse=True)}
        # Записываю отсортированный список в файл
        with open(f'employees_{sort_type.lower()}_sorted.json', mode='w',
                  encoding='utf-8') as employees_sorted_write:
            json.dump(obj_employees_in_func_sorted, employees_sorted_write, indent=4)
    except ValueError as ver:
        print(f'Error. {ver}')


employees_rewrite('salary')
