"""
Задание №4
� Создайте модуль с функцией внутри.
� Функция получает на вход загадку, список с возможными
вариантами отгадок и количество попыток на угадывание.
� Программа возвращает номер попытки, с которой была
отгадана загадка или ноль, если попытки исчерпаны.
"""

# def func(qws, ans, count):
#     print(f"загадка: {qws}")
#     print(f"варианты ответов: {ans}")
#     i = 0
#     while count >= i:
#         u_ans = input(f"введите ваш ответ: ")
#         if u_ans == ans[0]:
#             print(f'Правильно! Угадал за {i + 1} попытку')
#             return i + 1
#         else:
#             print('Не угадал!')
#             i += 1
#         if i == count:
#             return 0
#
#
# print(func("Не лает, не кусает, в дом не пускает",
#            ['замок', 'охранник', 'собака'], 3))


__all__ = ['guess_what']


def guess_what(riddle: str, guesses: list, attempts: int = 3) -> int:
    print(f'Отгадайте загадку {riddle}. {'\n'}'
          f'Число попыток: {attempts}.')

    count = 1
    guess = input('Введите отгадку: ').lower()

    while count < attempts:
        if guess in guesses:
            print(f'Угадали! Это {guess}.')
            return count
        print(f'Неверно. Число попыток {attempts - count}.')
        guess = input('Введите отгадку: ').lower()
        count += 1
        if guess in guesses:
            print(f'Угадали! Это {guess}.')
            return count

    print(f'Не угадали!')
    return 0


if __name__ == '__main__':
    riddle = 'Маленькое, зеленое, висит на стене и свистит'
    guesses = ['рыба', 'fish']
    attempts = 3
    res = guess_what(riddle, guesses, attempts)
    print(res)
