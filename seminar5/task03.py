"""
Задание №3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

text = 'Самостоятельно сохраните в переменной строку текста.'
res = {char: ord(char) for char in text}
my_iter = iter(res.items())
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print()
my_iter = iter(res.items())
for _ in range(5):
    print(next(my_iter))
