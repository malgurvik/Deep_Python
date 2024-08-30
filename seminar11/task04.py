"""
Задание №4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive:
    "Класс для хранения пары свойств и сохранения истории."
    def __init__(self, number, string):
        "Инициализирует новый экземпляр класса Archive."
        self.number = number
        self.string = string

        if not hasattr(self.__class__, 'numbers_archive'):
            self.__class__.numbers_archive = []
        if not hasattr(self.__class__, 'strings_archive'):
            self.__class__.strings_archive = []

        self.__class__.numbers_archive.append(number)
        self.__class__.strings_archive.append(string)

    def get_archive(self):
        return list(zip(self.__class__.numbers_archive, self.__class__.strings_archive))

    def __repr__(self):
        """Представление для программиста."""
        return f"Архив({self.number=}, {self.string=})"

    def __str__(self):
        """Представление для пользователя."""
        return f"Число: {self.number}, Строка: {self.string}"


if __name__ == '__main__':
    a1 = Archive(10, "Привет!")
    a2 = Archive(20, "Как дела?")
    a3 = Archive(30, "Отлично!")

    print(a1)
    print(repr(a1))
    print(a1.get_archive())