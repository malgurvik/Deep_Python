"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
from random import choice, randint, randbytes
from string import ascii_lowercase


def random_name(len_name: int):
    return ''.join([choice(ascii_lowercase) for _ in range(len_name)])


def create_file(extension: str, min_name=6, max_name=30, min_size=256, max_size=4096):
    file_name = f'task05\\{random_name(randint(min_name, max_name))}.{extension}'
    file_data = randbytes(randint(min_size, max_size))
    with open(file_name, 'wb') as file:
        file.write(file_data)


def create_files(**kwargs):
    for ext, amount in kwargs.items():
        for _ in range(amount):
            create_file(ext)


create_files(bmp=5, txt=3, mp3=2, mkv=6)

# from os import listdir, path, remove
# from shutil import rmtree
# from random import choice
# from task04 import create_files
#
#
# folder_path = 'C:/Users/D/PycharmProjects/gb_py_submerge/sem_7_files'
#
#
# def gen_files(*args, files_amount=5):
#     for _ in range(files_amount):
#         extension = choice(args)
#         create_files(extension, amount=1)
#
#
# def clear_folder(dir_path):
#     if path.exists(dir_path):
#         for filename in listdir(dir_path):
#             file_path = path.join(dir_path, filename)
#             if path.isfile(file_path):
#                 remove(file_path)
#             elif path.isdir(file_path):
#                 rmtree(file_path)
#         print(f"Directory '{dir_path}' has been cleared.")
#     else:
#         print(f"Directory '{dir_path}' not found.")
#
#
# if __name__ == '__main__':
#     if listdir(folder_path):
#         clear_folder(folder_path)
#     else:
#         gen_files('txt', 'jpg', 'zip', 'rtf')
