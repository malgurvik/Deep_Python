"""
Задание №5
� Добавьте в модуль с загадками функцию, которая хранит
словарь списков.
� Ключ словаря - загадка, значение - список с отгадками.
� Функция в цикле вызывает загадывающую функцию, чтобы
передать ей все свои загадки.
"""

# def func(qws, ans, count):
#     print(f"загадка: {qws}")
#     print(f"варианты ответов: {ans}")
#     i = 0
#     while count >= i:
#         u_ans = input(f"введите ваш ответ:>")
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
# def func_2(dct):
#     for k, v in dct.items():
#         print(func(k, v, 3))
#
#
# dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
#        "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}
#
# func_2(dct)


__all__ = ['riddles']


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


def riddles():
    riddles_dict = {
        "Что такое всегда перед вами, но вы не можете видеть?": ["будущее", "грядущее"],
        "Что имеет шею, но не имеет головы?": ["Бутылка", "бутылка"],
        "Что можно найти в Москве, но никогда в Париже?": ["Буква \"О\" (в слове Москва)", "О", "о"],
        "Что имеет ноги, но не может ходить?": ["стол", "стул"],
        "Что может лететь, но не имеет крыльев?": ["время"],
    }
    return [guess_what(k, v) for k, v in riddles_dict.items()]


if __name__ == '__main__':
    res = riddles()
    print(res)
