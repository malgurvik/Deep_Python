"""
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""
import json
import os


# def decorator(func):
#     my_dict = {}
#
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         file_name = f'{func.__name__}.json'
#         my_dict['args'] = f'{args[0]},{args[1]}'
#         for k, v in my_dict.items():
#             my_dict[k] = v
#         my_dict['res'] = res
#         with open(file_name, 'a', encoding="utf-8") as js_f:
#             json.dump(my_dict, js_f, indent=2)
#         return res
#
#     return wrapper
#
#
# @decorator
# def func(a, b):
#     return a ** b
#
#
# func(2, 5)


def read_json(file_name: str) -> dict:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:
            return json.load(file)
    return {}


def write_json(file_name: str, data: dict):
    with open(file_name, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def args_deco(func):
    def inner(*args, **kwargs):
        file_name = f'{func.__name__}.json'
        result_dict = read_json(file_name)
        result_func = func(*args, **kwargs)
        result_dict[str(result_func)] = {'args': [i for i in args]}
        result_dict[str(result_func)].update(kwargs)
        write_json(file_name, result_dict)
        return result_func

    return inner


@args_deco
def simple_func(*args, **kwargs):
    if args:
        print(*args, sep=' ')
    if kwargs:
        for key, value in kwargs.items():
            print(key, value, sep='->')
    result = []
    for item in args:
        if isinstance(item, int | float) or isinstance(item, str) and item.isdigit():
            result.append(int(item))
    for item in kwargs.values():
        if isinstance(item, int | float) or isinstance(item, str) and item.isdigit():
            result.append(int(item))
    return sum(result)


print(simple_func(4, 5, 6, '7', l=7, name='stone', age=15))
print(simple_func(43, 3, 6, '7', k=7, work='stone', age=67))
