"""
Задание №1
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
import re


def convert_str(text):
    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res


if __name__ == '__main__':
    print(convert_str('hello& 2345 world'))
