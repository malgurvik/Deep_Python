"""
Задание №6
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    # @property
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

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()


if __name__ == '__main__':
    rectangle1 = Rectangle(10, 5)
    rectangle2 = Rectangle(8, 3)

    print(rectangle1.get_perimeter)

    print(rectangle1 < rectangle2)
    print(rectangle1 <= rectangle2)
    print(rectangle1 == rectangle2)
    print(rectangle1 != rectangle2)
    print(rectangle1 > rectangle2)
    print(rectangle1 >= rectangle2)

    rectangle3 = Rectangle(5, 10)
    print(rectangle1 == rectangle3)

    print(type(rectangle1.get_perimeter))
    print(type(print))
