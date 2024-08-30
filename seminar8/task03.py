"""
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""

import json
import csv
import task02


# def create_csv():
#     with open('task2.json', "r", encoding='utf-8') as js_f:
#         res = json.load(js_f)
#         keys = res[0].keys()
#         lst = [keys]
#         for line in res:
#             values = line.values()
#             lst.append(values)
#
#     with open('task2.csv', "w", newline='', encoding='utf-8') as cs_f:
#         writer = csv.writer(cs_f)
#         writer.writerows(lst)
#
#
# create_csv()

def json_to_csv(some_dict: dict) -> list:
    list_to_write = []
    for user_lvl, user in some_dict.items():
        for user_id, user_name in user.items():
            list_to_write.append([user_lvl, user_id, user_name])
    return list_to_write


def write_to_csv(some_list: list[str], name_file: str):
    with open(name_file, 'w', encoding='UTF-8') as f_csv:
        csv_writer = csv.writer(f_csv, lineterminator='\n')
        csv_writer.writerow(['lvl', 'id', 'name'])
        csv_writer.writerows(some_list)


if __name__ == '__main__':
    write_to_csv(json_to_csv(task02.read_json()), 'task02_1.csv')
