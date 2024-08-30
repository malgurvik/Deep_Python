"""
Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл
"""

from random import randint, choice
from string import ascii_lowercase

# def random_nickname():
#     while True:
#         nickname = ''.join(choice(ascii_lowercase) for _ in range(randint(3, 7)))
#
#         nickname = nickname[0].upper() + nickname[1:]  # .capitalize()
#
#         for char in nickname:  # if any(char in 'aeiouAEIOU' for char in nickname)
#             if char in 'aeiouAEIOU':
#                 return nickname
#
#
# def random_nickname_in_file(path, lines):
#     with open(path, 'a', encoding='utf-8') as file:
#         for _ in range(lines):
#             print(f'{random_nickname()}', file=file)
#
#
# random_nickname_in_file('task2.txt', 3)


ALPHA = {chr(i) for i in range(ord('а'), ord('я') + 1)}
VOWELS = set('уеаоэёяию')
CONSONANT = ALPHA.difference(VOWELS)


def create_name(len_name):
    name = ''
    for i in range(len_name):
        name += choice(list(CONSONANT)) if not i % 2 else choice(list(VOWELS))
    return name.title()


def mix_name(file_name, count):
    with open(file_name, "a", encoding="utf-8") as f:
        for _ in range(count):
            f.write(create_name(randint(4, 7)) + "\n")


mix_name("task02.txt", 10)
