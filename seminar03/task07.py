# Задание №7
# Погружение в Python | Коллекции
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

text: list = 'Я я помню чудное мгновенье, я передом мной'  # .lower()
text_dict = dict()
for letter in text:
    if letter.isalpha():
        text_dict[letter] = text_dict.get(letter, 0) + 1
print(text_dict)

text_dict = {}
for letter in text.lower():
    if letter.isalpha():
        text_dict[letter] = text.count(letter)
print(text_dict)
