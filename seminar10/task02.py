"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


# class Rectangle:
#     def __init__(self, length, width=None):
#         self.length = length
#         self.width = width
#
#     def perimeter(self):
#         if self.width:
#             return self.length * 2 + self.width * 2
#         return self.length * 4
#
#     def square(self):
#         if self.width:
#             return self.length * self.width
#         return self.length ** 2


class Rectangle:

    # def __init__(self, *args):
    #     if len(args) == 1:
    #         self.__length = args[0]
    #         self.__width = args[0]
    #     elif len(args) == 2:
    #         self.__length = args[0]
    #         self.__width = args[1]

    def __init__(self, length, width=None):
        self.__length = length
        self.__width = width if width else length

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def square(self):
        return self.__length * self.__width


if __name__ == '__main__':
    rectangle = Rectangle(10, 5)
    print(f'Периметр прямоугольника равен {rectangle.perimeter()}\nПлощадь прямоугольника равна {rectangle.square()}')
    rectangle1 = Rectangle(5)
    print(f'Периметр прямоугольника равен {rectangle1.perimeter()}\nПлощадь прямоугольника равна {rectangle1.square()}')
