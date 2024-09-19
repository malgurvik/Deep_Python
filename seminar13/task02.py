"""
Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_dict_value(my_dict, my_key, default_value=None):
    try:
        return my_dict[my_key]
    except KeyError:
        return default_value


if __name__ == '__main__':
    dct = {1: 'one', 2: 'two'}
    print(get_dict_value(dct, 1))
    print(get_dict_value(dct, 3))
