"""
Задание №1
📌 Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log1.log', filemode='w')


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as ex:
        logger.error(ex)


print(division(10, 5))
print(division(10, 0))

# logging.basicConfig(filename='example1.log.', filemode='w', encoding='utf-8',
#                     format='{levelname} - {asctime} в строке {lineno} '
#                            'функция "{funcName}()" : {msg}', style='{', level=logging.WARNING)
#
#
# def func(a, b):
#     try:
#         res = a / b
#     except ZeroDivisionError:
#         logging.warning('Нельзя делить на ноль')
#         return ''
#     else:
#         return res
#
#
# print(func(5, 0))
