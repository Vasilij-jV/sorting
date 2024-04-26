# -*- config: utf-8 -*-
import json


def employees_rewrite(sort_type):
    with open('employees.json', 'r') as json_employees_in_func:
        obj_employees_in_func = json.load(json_employees_in_func)

    obj_employees_in_func_sorted = {}

    try:
        # Привожу ключ (тип сортировки) к нижнему регистру
        sort_type = sort_type.lower()
        # Создаю новый словарь из нулевого элемента исходного списка employees для преобразования ключей в нижний
        # регистр и сравнение их с ключом - образцом
        zero_element = {key.lower(): value for key, value in obj_employees_in_func['employees'][0].items()}
        # Проверяю, есть ли свойство в словаре, являющимся элементом списка и равно ли его значение строке
        if isinstance(zero_element[sort_type], str) and sort_type in zero_element:
            # Возвращаю названию ключа прежний формат
            for key, value in obj_employees_in_func['employees'][0].items():
                if value == zero_element[sort_type]:
                    sort_type = key
                    break
            # Сортирую
            obj_employees_in_func_sorted = {
                'employees': sorted(obj_employees_in_func['employees'], key=lambda x: x[sort_type])}
        # В этом блоке такие же действия, как и в предыдущем, но значение не строка, а число
        elif isinstance(zero_element[sort_type], int) and sort_type in zero_element:
            for key, value in obj_employees_in_func['employees'][0].items():
                if value == zero_element[sort_type]:
                    sort_type = key
                    break
            obj_employees_in_func_sorted = {
                'employees': sorted(obj_employees_in_func['employees'], key=lambda x: x[sort_type], reverse=True)}
        # Записываю отсортированный список в файл
        with open(f'employees_{sort_type.lower()}_sorted.json', mode='w', encoding='utf-8') as employees_sorted_write:
            json.dump(obj_employees_in_func_sorted, employees_sorted_write, indent=4)
    except KeyError as e:
        print('Bad key for sorting', e)


employees_rewrite('department')
