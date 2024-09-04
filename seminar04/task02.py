"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def func(string):
    return sorted(set([ord(symbol) for symbol in string]), reverse=True)


txt = 'Сформируйте список с уникальными кодами Unicode каждого'

print(func(txt))
