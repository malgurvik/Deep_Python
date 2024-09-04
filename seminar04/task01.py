"""
Задание №1
Погружение в Python | Функции
✔ Напишите функцию, которая принимает строку текста.
  Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
  длинного слова был один пробел между ним и номером строки.
"""

text = 'Я помню чудное мгновение'


def from_sentence(sentence):
    sentence_split = sorted(sentence.lower().split())
    max_len = len(max(sentence_split, key=len))
    for i, item in enumerate(sentence_split, 1):
        print(f'{i}. {item:>{max_len}}')


from_sentence(text)
