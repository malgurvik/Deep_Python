"""
Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""


class Person:

    def __init__(self, name: str, age: int, phone: str):
        self.__name = name
        self.__age = age
        self.__phone = phone

    def birthday(self):
        self.__age += 1

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


if __name__ == '__main__':
    p = Person("Иван", 33, "1-234-567-8901")
    print(f"{p.name} / {p.age} / {p.phone}")
    p.birthday()
    print(f"{p.name} / {p.age} / {p.phone}")
