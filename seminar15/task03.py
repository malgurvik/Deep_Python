"""
Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
    ○ уровень логирования,
    ○ дату события,
    ○ имя функции (не декоратора),
    ○ аргументы вызова,
    ○ результат.
"""

import logging
from functools import wraps

FORMAT = '{asctime} - {levelname} - {lineno}: {msg}'
logger = logging.getLogger(__name__)
logging.basicConfig(filename='log3.log', filemode='w', level=logging.INFO, format=FORMAT, style='{', encoding='utf-8')


def logger_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'Имя функции {func.__name__}, аргументы функции: {args} {kwargs} результат: {result}')
        return result

    return wrapper


@logger_deco
def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as ex:
        logger.error(ex)


print(division(num1=10, num2=5))
print(division(10, 0))
# f'Имя функции {func.__name__}, аргументы функции: {args} {kwargs} результат: {result}'


# logging.basicConfig(filename='example3.log',
#                     filemode='w',
#                     encoding='utf-8',
#                     format='{levelname} - {asctime} в строке '
#                            '{lineno} : {msg}',
#                     style='{',
#                     level=logging.INFO)
#
# logger = logging.getLogger(__name__)
#
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         logger.info(f'Аргументы функции: {args} результат: {result}, имя функции {func.__name__}')
#         return result
#
#     return wrapper
#
#
# @decor
# def power(x, y):
#     return x ** y
#
#
# print(power(2, 3))
