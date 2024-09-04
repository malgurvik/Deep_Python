"""
Задача 2. Объединение данных из нескольких JSON файлов
Напишите скрипт, который объединяет данные из нескольких JSON файлов в
один. Каждый файл содержит список словарей, описывающих сотрудников
компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
содержать объединённые списки сотрудников из всех файлов.
"""

import json
import glob


def merge_json_files(input_files, output_file):
    merged_data = []
    for file in input_files:
        with open(file, 'r') as f:
            data = json.load(f)
            merged_data.extend(data)

    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)


if __name__ == '__main__':
    json_files = glob.glob('task02\\employees*.json')
    merge_json_files(json_files, 'all_employees.json')
