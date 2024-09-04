"""
Задание №6
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

import pickle
import csv

with open('task2.pickle', 'rb') as p:
    data = pickle.load(p)
    print(data)

with open("new_c.csv", "w", encoding="utf-8", newline='') as c:
    writer = csv.DictWriter(c, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)