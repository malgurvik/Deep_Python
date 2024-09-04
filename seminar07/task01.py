"""
Задание №1
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint, uniform


def func(file_name, str_num):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(str_num):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            # print(f'{int_num} | {float_num}', file=file)
            file.write(f'{int_num} | {float_num:.2f}\n')


if __name__ == '__main__':
    func('task01.txt', 6)
