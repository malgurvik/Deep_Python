"""
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import os
import json

#
# lst = []
# with open('task2.json', "w", encoding='utf-8') as js_f:
#     json.dump(lst, js_f)
#
#
# def fun_dump_json():
#     name = "Петя"
#     user_id = "002"
#     level = 4
#
#     with open('task2.json', "r", encoding='utf-8') as f:
#         res = json.load(f)
#         print(res)
#
#     my_dct = {
#         "level": level,
#         "id": user_id,
#         "name": name,
#     }
#
#     with open('task2.json', "w", encoding='utf-8') as js_f:
#         res.append(my_dct)
#         json.dump(res, js_f, indent=2, separators=(',', ':'),
#                   ensure_ascii=False)
#
#
# s = 'n'
# while s != 'y':
#     fun_dump_json()
#     s = input('выход y/n :>')

NAME_FILE = 'task02_1.json'


def enter_name():
    name = input('Введите имя: ')
    return name.title()


def enter_id(set_id: set):
    while True:
        u_id = input('Введите id пользователя: ')
        if u_id not in set_id:
            return u_id
        print('Данный id уже занят, повторите попытку')


def enter_lvl():
    while True:
        lvl = input('Введите уровень доступа: ')
        if lvl.isdigit() and 1 <= int(lvl) <= 7:
            return lvl
        print('Введите целое число от 1 до 7ми')


def input_users():
    while True:
        dict_to_write = read_json()
        if not (user_name := enter_name()):
            break
        user_id = enter_id(read_id_users(dict_to_write))
        user_lvl = enter_lvl()
        if user_lvl in dict_to_write:
            dict_to_write[user_lvl][user_id] = user_name
        else:
            dict_to_write[user_lvl] = {user_id: user_name}

        save_to_json(dict_to_write)


def read_json(name_file=NAME_FILE) -> dict:
    if not os.path.exists(name_file):
        return {}
    with open(name_file, 'r', encoding='UTF-8') as f_json:
        return json.load(f_json)


def save_to_json(some_dict: dict, name_file=NAME_FILE):
    with open(name_file, 'w', encoding='UTF-8') as f_json:
        json.dump(some_dict, f_json, indent=4, ensure_ascii=False)


def read_id_users(some_dict: dict):
    set_id = set()
    for i in some_dict.values():
        for j in i:
            set_id.add(j)
    return set_id


if __name__ == '__main__':
    input_users()
