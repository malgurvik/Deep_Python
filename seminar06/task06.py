"""
Задание №6
� Добавьте в модуль с загадками функцию, которая
принимает на вход строку (текст загадки) и число (номер
попытки, с которой она угадана).
� Функция формирует словарь с информацией о результатах
отгадывания.
� Для хранения используйте защищённый словарь уровня
модуля.
� Отдельно напишите функцию, которая выводит результаты
угадывания из защищённого словаря в удобном для чтения
виде.
� Для формирования результатов используйте генераторное
выражение.
"""

_dct = {}

# def func(que, count):
#     print(que)
#     a = "в правде"
#
#     i = 0
#     while count > i:
#         ans = input("Напишите ответ>")
#         if ans == a:
#             _dct[i + 1] = "Вы угадали"
#             return
#         else:
#             _dct[i + 1] = "Не угадали"
#         i += 1


from pprint import pprint

__all__ = ['riddles', 'show_riddles_results']


def guess_what(riddle: str, guesses: list, attempts: int = 3) -> int:
    print(f'Отгадайте загадку "{riddle}" {'\n'}'
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
    return {k: guess_what(k, v) for k, v in riddles_dict.items()}


def show_riddles_results():
    print()
    pprint(_riddles_results_dict)


_riddles_results_dict = riddles()

if __name__ == '__main__':
    show_riddles_results()
