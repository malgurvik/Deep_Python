"""
Задание №3
� Улучшаем задачу 2.
� Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
� Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
� Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.
"""

# from random import randint
# from sys import argv
#
#
# def func(args):
#     num = randint(args[0], args[1])
#     i = 0
#     while args[2] > i:
#         u_num = int(input(
#             f"введите число в диапазоне от {args[0]} до {args[1]}: "))
#         if u_num > num:
#             print('меньше!')
#         elif u_num < num:
#             print('больше!')
#         else:
#             print('Угадал!')
#             return True
#         i += 1
#     return False
#
#
# args = [int(el) for el in argv[1:]]
#
# print(func(args))


from random import randint
from sys import argv

__all__ = ['guess_number']


def guess_number(low_limit, upper_limit, attempts=3):
    print(f'Угадайте число в диапазоне между {low_limit} и {upper_limit}. '
          f'Число попыток {attempts}.')

    number_to_guess = randint(low_limit, upper_limit)
    print(number_to_guess)  # закомментировать
    number = int(input('Введите целое число: '))
    if number == number_to_guess:
        print(f'Угадали! Это {number_to_guess}.')
        return True
    else:
        attempts -= 1
        while attempts != 0:
            print(f'Неверно. Осталось попыток {attempts}')
            print('больше' if number < number_to_guess else 'меньше')
            number = int(input('Введите целое число: '))
            attempts -= 1
        print(f'Не угадали!')
        return False


input_str = """Введите через пробел 3 целых числа: 
- нижний предел диапазона;
- верхний предел диапазона;
- количество попыток
Вводить здесь: """

if __name__ == '__main__':
    low_limit, upper_limit, attempts = [int(el) for el in argv[1:]]
    # low_limit, upper_limit, attempts = map(int, input(input_str).split())
    # low_limit, upper_limit, attempts = (int(i) for i in input(input_str).split())
    res = guess_number(low_limit, upper_limit, attempts)
    print(res)
