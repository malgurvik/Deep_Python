"""
Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""

from json import load, dump


class User:
    def __init__(self, name, user_id, level) -> None:
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f'User:{self.name}, id:{self.user_id}, level:{self.level}'


users = set()


def load_users(path):
    with open(path, encoding='utf-8') as f:
        data = load(f)
    for level, value in data.items():
        for id, name in value.items():
            users.add(User(name, id, level))


if __name__ == '__main__':
    load_users('json_file.json')
    print(*users, sep='\n')
