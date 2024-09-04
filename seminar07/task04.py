"""
Задание №4
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from random import choice, randint, randbytes
from string import ascii_lowercase


def random_name(len_name: int):
    return ''.join([choice(ascii_lowercase) for _ in range(len_name)])


def create_files(extension, min_name=6, max_name=30, min_size=256, max_size=4096, amount=42):
    for _ in range(amount):
        file_name = f'task04\\{random_name(randint(min_name, max_name))}.{extension}'
        file_data = randbytes(randint(min_size, max_size))
        with open(file_name, 'wb') as file:
            file.write(file_data)


create_files('smp')

# from os import urandom, path, makedirs
# from random import sample, choice, randint
# from string import ascii_lowercase, digits
#
#
# folder_path = 'C:/Users/D/PycharmProjects/gb_py_submerge/sem_7_files'
# if not path.exists(folder_path):
#     makedirs(folder_path)
#
#
# def create_files(extension, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, amount=42):
#     for _ in range(amount):
#         filename = (f'{choice(ascii_lowercase)}'
#                     f'{''.join((sample(ascii_lowercase + digits, randint(min_len - 1, max_len - 1))))}'
#                     f'.{extension}')
#         file_size = randint(min_bytes, max_bytes)
#
#         with open(path.join(folder_path, filename), 'wb') as f:
#             f.write(urandom(file_size))
#
#
# if __name__ == '__main__':
#     create_files('txt')
