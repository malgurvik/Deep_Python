# Задание №1
# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.


num = 5
string = 'пять'
tup = 1,
my_list = [1, 1, 2, 3]
my_set = set(my_list)
dct = {}

for el in (num, string, tup, my_list, my_set, dct):
    print(type(el))
