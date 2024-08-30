"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def guess_num(num, attempts):
    def inner():
        nonlocal attempts
        while attempts > 0:
            number = int(input("Число: "))
            if number == num:
                return 'Угадали!'
            attempts -= 1
        return 'Не угадали!'

    return inner


print(guess_num(15, 1)())
