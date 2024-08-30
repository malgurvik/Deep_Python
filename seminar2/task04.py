"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

from decimal import Decimal, getcontext
from math import pi

getcontext().prec = 42
d = 12


def area(d):
    p = Decimal(pi)
    d = Decimal(d)
    return p * (d / 2) ** 2


def len_circle(d):
    p = Decimal(pi)
    d = Decimal(d)
    return p * d


print(area(d))
print(len_circle(d))
