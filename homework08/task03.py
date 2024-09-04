"""
Задача 3. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
файл. JSON файл содержит данные о продуктах (название, цена, количество на
складе). В CSV файле каждая строка должна соответствовать одному продукту.
"""
import json
import csv


def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Некорректный формат данных в JSON файле")
    with open(csv_file, 'w', newline='') as f:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    json_to_csv('/homework08\\task03\\products.json', 'products.csv')
