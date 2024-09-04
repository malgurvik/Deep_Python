"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""
from random import randint


# def guess_num(num, attempts):
#     def inner():
#         nonlocal attempts
#         while attempts > 0:
#             number = int(input("Число: "))
#             if number == num:
#                 return 'Угадали!'
#             attempts -= 1
#         return 'Не угадали!'
#
#     return inner
#
#
# print(guess_num(15, 1)())


def guess_number(number: int, attempts: int):
    g_number = randint(1, number)
    n_attempts = randint(1, attempts)

    def inner():
        nonlocal n_attempts
        while n_attempts > 0:
            user_number = int(input(f'Угадай число от 1 до {number} за {n_attempts + 1}: '))
            if g_number > user_number:
                print('Загаданное число больше')
            elif g_number < user_number:
                print('Загаданное число меньше')
            else:
                print(f'Поздравляю! Ты угадал, это было число {g_number}!')
                return
            n_attempts -= 1
        print(f'Вы проиграли! Загаданное число - {g_number}')

    return inner


game = guess_number(50, 10)
game()
