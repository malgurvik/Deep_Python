"""
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""
import csv
import json
import task02


# with open('task2.csv', encoding="utf-8") as f:
#     fr = csv.reader(f)
#     res = list(fr)
#     print(res)
#     for i in range(1, len(res)):
#         cur_id = res[i][1]
#         res[i][1] = f"{cur_id.zfill(10)}"
#         res[i][2] = res[i][2].title()
#         res[i].append(hash(res[i][2]))
#     res[0].append('hash')
#
# with open('new_json.json', "w", encoding="utf-8") as j:
#     json.dump(res, j, ensure_ascii=False)


def read_csv(name_file: str):
    dict_data = {}
    with open(name_file, 'r', encoding='UTF-8') as f_csv:
        csv_reader = csv.reader(f_csv)
        for i, u_data in enumerate(csv_reader):
            if i:
                u_id = u_data[1].zfill(10)
                u_name = u_data[2].title()
                dict_data[hash(u_id + u_name)] = (u_data[0], u_id, u_name)
    return dict_data


if __name__ == '__main__':
    task02.save_to_json(read_csv('task02_1.csv'), 'task03.json')
