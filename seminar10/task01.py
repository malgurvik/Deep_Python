"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5)
    print(f'Длина окружности = {circle.length()}')
    print(f'Площадь окружности = {circle.square()}')
