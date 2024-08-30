"""
Задание №6
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""

from json import dump
from functools import wraps


def cash(num):
    def real_decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(num):
                res = func(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return real_decor


def decorator(func):
    my_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Обертка"""
        res = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        my_dict['args'] = f'{args[0]},{args[1]}'
        for k, v in my_dict.items():
            my_dict[k] = v
        my_dict['res'] = res
        with open(file_name, 'a', encoding="utf-8") as js_f:
            dump(my_dict, js_f, indent=2)
        return res

    return wrapper


@cash(1)
@decorator
def guess_num(num, attempts):
    """Исх"""
    while attempts > 0:
        number = int(input("Число: "))
        if number == num:
            return 'Угадали!'
        attempts -= 1
    return 'Не угадали!'


print(guess_num(10, 3))

print(guess_num.__name__)
help(guess_num)