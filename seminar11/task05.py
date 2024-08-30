"""
Задание №5
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        new_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(new_perimeter / 4)

    def __sub__(self, other):
        new_perimeter = self.get_perimeter() - other.get_perimeter()
        if new_perimeter < 0:
            return Rectangle(0)
        return Rectangle(new_perimeter / 4)


"""Отступление"""


class NewClass:
    def __call__(self, *args, **kwargs):
        pass


obj = NewClass()

obj()

if __name__ == '__main__':
    rectangle1 = Rectangle(10, 5)
    rectangle2 = Rectangle(8, 3)

    rectangle_sum = rectangle1 + rectangle2
    print("Периметр суммы:", rectangle_sum.get_perimeter())

    rectangle_diff = rectangle1 - rectangle2
    print("Периметр разности:", rectangle_diff.get_perimeter())
