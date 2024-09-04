"""
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
from json import dump


def cash(num):
    def real_decor(func):
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

    def wrapper(*args, **kwargs):
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
    while attempts > 0:
        number = int(input("Число: "))
        if number == num:
            return 'Угадали!'
        attempts -= 1
    return 'Не угадали!'


print(guess_num(10, 3))