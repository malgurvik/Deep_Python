"""
Задание №7
� Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
� Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
� Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
� Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
� Проверку года на високосность вынести в отдельную
защищённую функцию.
"""

# def func(date: str):
#     day, month, year = map(int, date.split('.'))
#     if year in range(1, 10_000) and month in range(1, 13) and day in range(1,
#                                                                            32):
#         if year % 400 == 0 and month == 2 or year % 4 == 0 and \
#                 year % 100 != 0 and month == 2:
#             if day in range(1, 30):
#                 return True
#             else:
#                 return False
#         if month in [1, 3, 5, 7, 8, 10, 12]:
#             return True
#         elif month == 2:
#             if day in range(1, 29):
#                 return True
#             else:
#                 return False
#         else:
#             if day in range(1, 31):
#                 return True
#             else:
#                 return False
#     else:
#         return False
#
#
# print(func("28.02.2025"))


__all__ = ['date_validate']

_days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


def _is_leap(year) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def date_validate(date: str) -> bool:
    day, month, year = map(int, date.split('.'))

    if year in range(1, 10_000) and month in range(1, 13):
        if month == 2 and _is_leap(year):
            days = _days_in_month[month] + 1
            if day in range(1, days + 1):
                return True

        days = _days_in_month[month]
        if day in range(1, days + 1):
            return True

    return False


if __name__ == '__main__':
    date = '29.02.2000'
    print('Корректная ли дата?', date_validate(date))
    print('Високосный ли год?', _is_leap(int(date.split('.')[2])))
