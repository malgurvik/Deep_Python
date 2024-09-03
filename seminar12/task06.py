"""
Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


# def __init__(self, atr):
#     self.atr = atr
#
#
# def __get__(self, instance, owner):
#     print("Полезная нагрузка")
#     return instance.__dict__[self.atr]
#
#
# def __set__(self, instance, value):
#     if value < 0:
#         raise ValueError("Неверно")
#     self.atr = value


class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set__(self, instance, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} меньше, чем {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} больше, чем {self.max_value}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Rectangle:
    width = Validator(10, 20)
    length = Validator(10, 40)

    def __init__(self, width, length):
        self.width = width
        if length == 0:
            length = width
        self.length = length

    def get_perimeter(self):
        return 2 * (self.width + self.length)

    def get_area(self):
        return self.width * self.length


if __name__ == '__main__':
    r1 = Rectangle(10, 40)
