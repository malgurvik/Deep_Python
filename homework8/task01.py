"""
Задание 1. Работа с основными данными
Напишите функцию, которая получает на вход директорию и рекурсивно обходит
её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
pickle. Для дочерних объектов указывайте родительскую директорию. Для
каждого объекта укажите файл это или директория. Для файлов сохраните его
размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами разных форматов.
"""
import os
import json
import csv
import pickle


def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        total_size = 0
        for dir_path, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dir_path, filename)
                total_size += os.path.getsize(file_path)
        return total_size


def traverse_dir(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for name in dirs + files:
            path = os.path.join(root, name)
            is_dir = os.path.isdir(path)
            size = get_size(path)
            parent = os.path.basename(root)
            result.append({
                'name': name,
                'path': path,
                'type': 'directory' if is_dir else 'file',
                'size': size,
                'parent': parent
            })
    return result


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=4)


def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['name', 'path', 'type', 'size', 'parent'])
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as f_pickle:
        pickle.dump(data, f_pickle)


def main(directory):
    data = traverse_dir(directory)
    save_to_json(data, 'dir_info.json')
    save_to_csv(data, 'dir_info.csv')
    save_to_pickle(data, 'dir_info.pickle')


if __name__ == '__main__':
    main('C:\\Users\\malgu\\Desktop\\DeepPython\\homework8')
