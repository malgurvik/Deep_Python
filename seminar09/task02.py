"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from random import randint


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         count = args[0] if args[0] in range(1, 11) else randint(1, 10)
#         number = args[1] if args[1] in range(1, 101) else randint(1, 100)
#         print(number)
#         return func(number, count)
#
#     return wrapper
#
#
# @decorator
# def guess_num(num, attempts):
#     while attempts > 0:
#         number = int(input("Число: "))
#         if number == num:
#             return 'Угадали!'
#         attempts -= 1
#     return 'Не угадали!'
#
#
# # print(decorator(guess_num)(15, 1))
#
# print(guess_num(15, 1))

def game_validator(func):
    def inner(number: int, attempts: int):
        g_number = number if 1 <= number <= 100 else randint(1, 100)
        n_attempts = attempts if 1 <= attempts <= 10 else randint(1, 10)
        return func(g_number, n_attempts)

    return inner


@game_validator
def guess_number(number: int, attempts: int):
    g_number = randint(1, number)
    while attempts > 0:
        user_number = int(input(f'Угадай число от 1 до 100 за {attempts}: '))
        if g_number > user_number:
            print('Загаданное число больше')
        elif g_number < user_number:
            print('Загаданное число меньше')
        else:
            print(f'Поздравляю! Ты угадал, это было число {g_number}!')
            break
        attempts -= 1
    print(f'Вы проиграли! Загаданное число - {g_number}')


guess_number(150, 10)
