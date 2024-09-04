"""
Задание №3
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(map(lambda x: x.strip(), file.readlines()))


def create_new_file(new_file_name, names_file, numbers_file):
    number_data = read_file(numbers_file)
    name_data = read_file(names_file)
    max_len = sorted([len(name_data), len(number_data)])[1]
    new_data = []
    for i in range(max_len):
        int_num, float_num = map(float, number_data[i % len(number_data)].split(' | '))
        if (new_num := int_num * float_num) >= 0:
            new_data.append(f'{name_data[i % len(name_data)].upper()} | {int(new_num)}')
        else:
            new_data.append(f'{name_data[i % len(name_data)].lower()} | {abs(new_num)}')
    new_data = '\n'.join(new_data)
    with open(new_file_name, 'w', encoding='utf-8') as file:
        file.write(new_data)


create_new_file('task03.txt', 'task02.txt', 'task01.txt')

# from functools import reduce
#
#
# def read_2_files(filename_1: str, filename_2: str):
#     with (
#         open(filename_1, 'r', encoding='utf-8') as f_numbers,
#         open(filename_2, 'r', encoding='utf-8') as f_names,
#     ):
#
#         num_products = [reduce(lambda x, y: x * y, map(float, line.split('|')))
#                         for line in f_numbers.readlines()]
#         names = [name.strip('\n') for name in f_names.readlines()]
#         delta = abs(len(names) - len(num_products))
#
#         if delta:
#             for i in range(delta):
#                 if len(names) > len(num_products):
#                     num_products.append(num_products[i])
#                 else:
#                     names.append(names[i])
#
#         return zip(names, num_products)
#
#
# def write_2_files(filename: str, func):
#     with open(filename, 'w', encoding='utf-8') as f:
#         for name, number in func:
#             name = name.lower() if number < 0 else name.upper()
#             number = -number if number < 0 else int(number)
#             print(f'{name} {number}', file=f)
#
#
# if __name__ == '__main__':
#     print(*read_2_files('sem_7_task_1.txt', 'sem_7_task_2.txt'), sep='\n')
#     print(write_2_files('sem_7_task_3.txt',
#     read_2_files('sem_7_task_1.txt',
#     'sem_7_task_2.txt')))
