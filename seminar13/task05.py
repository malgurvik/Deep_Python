"""
Задание №5
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""
# from json import load, dump
# from task04 import User


# class NameError(Exception):
#     pass
#
#
# class LevelError(Exception):
#     pass
#
#
# class Repo:
#     users = []
#
#     @staticmethod
#     def load_users(path):
#         with open(path, encoding='utf-8') as f:
#             data = load(f)
#         for level, value in data.items():
#             for id, name in value.items():
#                 Repo.users.append(User(name, id, level))
#
#     @staticmethod
#     def check_login(name):
#         try:
#             for user in Repo.users:
#                 if user.name == name:
#                     return f'{name} пользователь найден!'
#             raise NameError
#         except NameError:
#             return 'Пользователь не найден'
#
#     @staticmethod
#     def create_user(name, user_id, level):
#         try:
#             if level > 3:
#                 raise LevelError
#         except LevelError:
#             return 'Ошибка уровня'
#         else:
#             Repo.users.append(User(name, user_id, level))
#
#
# if __name__ == '__main__':
#     repo = Repo()
#     # repo.load_users('json_file.json')
#     print(repo.check_login('Новиков'))
#     repo.create_user('Cеменов', '56', 3)
#     repo.load_users('json_file.json')
#     print(*repo.users, sep='\n')
#     print(repo.users[0] == repo.users[1])


import json
from task03 import AccessError, LevelError


class User:
    def __init__(self, name, user_id, user_lvl):
        self.name = name
        self.id = user_id
        self.level = user_lvl

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name and self.id == other.id
        raise TypeError

    def __hash__(self):
        return hash(self.name + self.id + self.level)


class Company:

    def __init__(self, name, user_db_path):
        self.name = name
        self.path = user_db_path
        self.authorized_user = None

    def _load_json(self):
        result = set()
        with open(self.path, 'r', encoding='UTF-8') as file_json:
            for level, user in json.load(file_json).items():
                for user_id, name in user.items():
                    result.add(User(name, user_id, level))
        return result

    def _save_json(self, new_user):
        users_set = self.users
        users_set.add(new_user)
        dct_to_write = {}
        for user in users_set:
            if user.level in dct_to_write:
                dct_to_write[user.level][user.id] = user.name
            else:
                dct_to_write[user.level] = {user.id: user.name}
        with open(self.path, 'w', encoding='UTF-8') as json_file:
            json.dump(dct_to_write, json_file, indent=4, ensure_ascii=False)

    @property
    def users(self) -> set[User]:
        return self._load_json()

    @users.setter
    def users(self, new_user: User):
        self._save_json(new_user)

    def login(self, user_name, user_id):
        login_user = User(user_name, user_id, 0)
        for user in self.users:
            if user == login_user:
                print(f'Привет, {user.name}! Твой уровень доступа {user.level}!')
                self.authorized_user = user
                return user.level
        raise AccessError

    def logout(self):
        print(f'До свидания {self.authorized_user.name}, до новых встреч!')
        self.authorized_user = None

    def add_user(self, user_name, user_id, user_lvl):
        if not self.authorized_user:
            raise AccessError
        if int(self.authorized_user.level) <= int(user_lvl):
            raise LevelError
        new_user = User(user_name, user_id, user_lvl)
        self.users = new_user
        print(f'Пользователь "{new_user.name}" успешно создан')


company = Company('abibas', 'json_file.json')

company.login('Гурьев', '08')
company.add_user('Софья', '123', '3')
