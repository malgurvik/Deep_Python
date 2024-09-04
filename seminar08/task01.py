"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json

file_name = '/seminar07\\task03.txt'
json_name = 'task01.json'


# with open(file_name, 'r', encoding='utf-8') as f, open(json_name, 'w', encoding='utf-8') as j:
#     mydict = {}
#     for line in f:
#         key, value = line.split(' | ')
#         print(key, value)
#         mydict[key.title()] = float(value)
#     json.dump(mydict, j, separators=(',\n', ':'), ensure_ascii=False)

def txt_reader(file: str):
    with open(file, 'r', encoding='UTF-8') as file:
        return list(map(lambda x: x.strip(), file.readlines()))


print(txt_reader('text.txt'))


def save_to_dict(list_data: list):
    dict_to_write = {}
    for i in list_data:
        name, value = i.split(' | ')
        dict_to_write[name] = dict_to_write.get(name, []) + [value]
    return dict_to_write


def save_to_json(some_dict: dict, name: str):
    with open(name, 'w', encoding='UTF-8') as f_json:
        json.dump(some_dict, f_json, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    list_ = txt_reader(file_name)
    dict_ = save_to_dict(list_)
    save_to_json(dict_, json_name)
