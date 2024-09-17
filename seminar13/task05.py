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
from json import load, dump
from task04 import User


class NameError(Exception):
    pass


class LevelError(Exception):
    pass


class Repo:
    users = []

    @staticmethod
    def load_users(path):
        with open(path, encoding='utf-8') as f:
            data = load(f)
        for level, value in data.items():
            for id, name in value.items():
                Repo.users.append(User(name, id, level))

    @staticmethod
    def check_login(name):
        try:
            for user in Repo.users:
                if user.name == name:
                    return f'{name} пользователь найден!'
            raise NameError
        except NameError:
            return 'Пользователь не найден'

    @staticmethod
    def create_user(name, user_id, level):
        try:
            if level > 3:
                raise LevelError
        except LevelError:
            return 'Ошибка уровня'
        else:
            Repo.users.append(User(name, user_id, level))


if __name__ == '__main__':
    repo = Repo()
    # repo.load_users('json_file.json')
    print(repo.check_login('Новиков'))
    repo.create_user('Cеменов', '56', 3)
    repo.load_users('json_file.json')
    print(*repo.users, sep='\n')
    print(repo.users[0] == repo.users[1])
