"""
Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_num():
    while True:
        try:
            num = float(input('Enter number: '))
        except ValueError:
            print('Not number')
        else:
            print("It's OK")
            break
        finally:
            print("Always")


get_num()
