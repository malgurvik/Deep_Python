"""
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Ширина должна быть положительной")
        self._width = value


if __name__ == '__main__':
    rectangle = Rectangle(10)

    perimeter = rectangle.get_perimeter()
    print("Периметр:", perimeter)

    area = rectangle.get_area()
    print("Площадь:", area)

    rectangle.length = 5
    rectangle.width = 7

    perimeter = rectangle.get_perimeter()
    print("Новый периметр:", perimeter)

    area = rectangle.get_area()
    print("Новая площадь:", area)

    try:
        rectangle.length = -10  # Попытка установить отрицательную длину
    except ValueError as e:
        print(e)
