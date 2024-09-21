"""
Задача 5. Запуск из командной строки
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.
Подсказка № 1
Используйте функцию os.path.join() для правильного построения путей к файлам
и каталогам в зависимости от операционной системы.
Подсказка № 2
Используйте os.path.isdir() для проверки, является ли указанный путь
директорией перед тем как пытаться получить его содержимое.
Подсказка № 3
Используйте os.path.splitext() для разделения имени файла на основную часть
и расширение, где расширение можно очистить от начальной точки.
Подсказка № 4
Используйте logging.basicConfig() для настройки логирования, указав уровень
логирования и формат сообщений.
Подсказка № 5
Определите namedtuple для хранения информации о файлах и каталогах, что
позволяет легко управлять структурой данных и логированием.
"""

import os
import logging
from collections import namedtuple
from argparse import ArgumentParser

# Определение namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])
# Настройка логирования
logging.basicConfig(filename='directory_contents.log',filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s')


def collect_info(directory_path):
    """Собирает информацию о содержимом директории и сохраняет в лог."""
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией.")

    # Получаем родительский каталог
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    # Перебираем содержимое директории
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        # Проверяем, является ли элемент директорией
        if os.path.isdir(entry_path):
            file_info = FileInfo(name=entry, extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, extension = os.path.splitext(entry)
            file_info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False,
                                 parent_directory=parent_directory)
        # Запись в лог
        logging.info(f'{file_info.name} | {file_info.extension if file_info.extension else "N/A"} | '
                     f'{"Directory" if file_info.is_directory else "File"} | {file_info.parent_directory}')


def main():
    """Основная функция для обработки командной строки и сбора информации."""
    parser = ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")
    parser.add_argument('directory', type=str, help="Путь до директории для анализа")
    args = parser.parse_args()
    directory_path = args.directory

    try:
        collect_info(directory_path)
        print(f'Информация о содержимом директории"{directory_path}" '
              f'успешно записана в файл "directory_contents.log".')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
