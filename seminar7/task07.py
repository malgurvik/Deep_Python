"""
Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os


def sort_files(dir_path, **kwargs):
    if not os.path.exists(dir_path):
        print('Такой директории не существует')
        exit(1)
    file_list = list(map(lambda x: x.rsplit('.', 1), os.listdir(dir_path)))
    for dir_name, list_ext in kwargs.items():
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        for file_name, file_ext in file_list:
            if file_ext in list_ext:
                os.replace(os.path.join(dir_path, file_name + '.' + file_ext),
                           os.path.join(dir_name, file_name + '.' + file_ext))


sort_files('task07', audio=['mp3', 'wav'], video=['mp4', 'avi', 'mkv'], picture=['bmp', 'jpg'])

# EXTENSIONS = {
#     'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', 'mpeg', 'flv', 'vob'],
#     'image': ['jpg', 'jpeg', 'png', 'bmp', 'psd', 'ico', 'tiff'],
#     'text': ['txt', 'doc', 'docx', 'pdf', 'rtf'],
#     'data': ['sql', 'csv', 'dat', 'db', 'mdb'],
#     'audio': ['mp3', 'wav', 'wma', 'cda', 'ogg', 'flac'],
# }
#
#
# def sort_files(current_dir, extensions):
#     file_list = [file.split('.') for dirs, folders, files
#                  in os.walk(current_dir) for file in files]
#     for name, ext in file_list:
#         for k, v in extensions.items():
#             if ext in v:
#                 new_dir = os.path.join(os.getcwd(), current_dir, k)
#                 old_place = os.path.join(current_dir, f'{name}.{ext}')
#                 new_place = os.path.join(new_dir, f'{name}.{ext}')
#                 if not os.path.isdir(new_dir):
#                     os.makedirs(new_dir)
#                 os.replace(old_place, new_place)
#
#
# if __name__ == '__main__':
#     sort_files(folder_path, EXTENSIONS)
