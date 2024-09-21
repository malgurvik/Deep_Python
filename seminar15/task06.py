"""
Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import os
import logging
from collections import namedtuple

logger = logging.getLogger(__name__)
logging.basicConfig(filename='files.log', filemode='w', encoding='UTF-8', level=logging.INFO)
file_info = namedtuple('file_info', ['file_name', 'extension', 'is_dir', 'paren_dir_name'])


def log_files(path: str | None = None):
    obj_list = []
    if path is None:
        path = os.getcwd()

    for parent_dir, list_dir, list_file in os.walk(path):
        if list_dir:
            for dir_ in list_dir:
                file_info.file_name = dir_
                file_info.is_dir = True
                file_info.extension = None
                file_info.paren_dir_name = parent_dir
            obj_list.append(file_info)
            logger.info(f'{file_info.file_name}, {file_info.extension}, {file_info.is_dir}, {file_info.paren_dir_name}')
        if list_file:
            for file in list_file:
                if file.count('.') > 0:
                    file_info.file_name = file.rsplit('.', 1)[0]
                    file_info.extension = file.rsplit('.', 1)[1]
                else:
                    file_info.file_name = file
                    file_info.extension = None
                file_info.is_dir = False
                file_info.paren_dir_name = parent_dir
            obj_list.append(file_info)
            logger.info(f'{file_info.file_name}, {file_info.extension}, {file_info.is_dir}, {file_info.paren_dir_name}')
    return obj_list


log_files('C:\\Users\\malgu\\Desktop\\DeepPython')
