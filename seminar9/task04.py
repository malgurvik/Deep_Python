"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""


def decorator(num):
    def real_decor(func):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(num):
                res = func(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return real_decor


# @decorator(10)
def func(a, b):
    return a ** b

# print(decorator(10)(func)(2, 5))

# print(func(2, 5))
