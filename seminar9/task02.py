"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from random import randint


def decorator(func):
    def wrapper(*args, **kwargs):
        count = args[0] if args[0] in range(1, 11) else randint(1, 10)
        number = args[1] if args[1] in range(1, 101) else randint(1, 100)
        print(number)
        res = func(number, count)
        return res

    return wrapper


@decorator
def guess_num(num, attempts):
    while attempts > 0:
        number = int(input("Число: "))
        if number == num:
            return 'Угадали!'
        attempts -= 1
    return 'Не угадали!'


# print(decorator(guess_num)(15, 1))

print(guess_num(15, 1))
