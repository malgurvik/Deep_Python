"""
Задание №1
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""

val1, key_1, key_2, *val2 = '1/2/3/4/5/6/7'.split('/')
res = {int(key_1): int(val1), int(key_2): tuple(map(int, val2))}
print(res)
