"""
Функция группового переименования файлов

Напишите функцию группового переименования файлов в папке test_folder под названием rename_files.
Она должна:
a. принимать параметр желаемое конечное имя файлов desired_name. При переименовании в
   конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере num_digits.
c. принимать параметр расширение исходного файла source_ext . Переименование должно работать только
   для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла target_ext.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы
   с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
   Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории.

Пример использования.
На входе:
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

На выходе:
new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc,
new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc
"""

import os

path = 'C:\\Users\\malgu\\Desktop\\DeepPython\\test_folder'


def rename_files(desired_name, num_digits, source_ext, target_ext):
    count = 0
    files = os.listdir('test_folder')
    print(files)
    for file in files:
        if file.endswith(source_ext):
            count += 1
            os.rename(os.path.join("test_folder", file),
                      os.path.join("test_folder", desired_name + str(count).zfill(num_digits) + '.' + target_ext))

    # for path, dir, name in os.walk('test_folder'):
    #     for name in name:
    #         print(name)
    #         if name.split('.')[1] == source_ext:
    #             count += 1
    #             os.rename(os.path.join("test_folder", name),
    #                       os.path.join("test_folder", desired_name + str(count).zfill(num_digits) + '.' + target_ext))


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
