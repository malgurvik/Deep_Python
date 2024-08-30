"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

names = ['Alex', 'Nick', 'Michael']
count = 1
tapes = 1500
txt = 'Test'
rows = 'first'
s = -15
sym_calls = True

var = globals().copy()
new_dict = {}
for key in var.keys():
    if not key.startswith('__'):
        new_dict[key] = var[key]

for key in new_dict.copy():
    if key.endswith('s') and len(key)!=1:
        new_dict[key[:-1]] = new_dict[key]
        new_dict[key] = None

print(var)
print(new_dict)
