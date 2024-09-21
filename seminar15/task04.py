"""
Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
import datetime
import logging

logging.basicConfig(filename='example4.log.', filemode='w', encoding='utf-8', level=logging.ERROR)


def user_date(data_text):
    dict_month = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
                  'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}
    dict_days = {'понедельник': 1, 'вторник': 2, 'среда': 3, 'четверг': 4,
                 'пятница': 5, 'суббота': 6, 'воскресенье': 7}
    try:
        data_text = data_text.split()
        num_week, day, month = int(data_text[0][0]), int(dict_days[data_text[1]]), int(dict_month[data_text[2]])
    except ValueError:
        logging.error('Некорректный формат данных')
        return 'Некорректный формат данных'

    # получаем параметры заданной даты
    data_month = month  # месяц заданной даты
    data_year = datetime.date.today().year  # текущий год - год заданной даты

    first_day_data_month = datetime.date(data_year, data_month, 1).weekday()  # номер дня недели первого числа месяца
    # определяем день заданной даты
    if first_day_data_month >= day:
        data_day = (7 - first_day_data_month) + (
                num_week - 1) * 7 + day  # если в первой неделе месяца нет такого дня недели
    else:
        data_day = (7 - first_day_data_month) + (
                num_week - 2) * 7 + day  # если в первой неделе месяца есть такой день недели
    try:
        data = datetime.date(data_year, data_month, data_day)
    except ValueError:
        logging.error('Нет такого дня в этом месяце')
        return 'Нет такого дня в этом месяце'

    return data


if __name__ == '__main__':
    dates = ['1-й вторник марта', '1-й четверг ноября', 'опять вторник в марте', '3-я среда мая', '5-й четверг апреля']
    # for el in dates:
    #     print(user_date(el))
    print(user_date('5-ая среда января'))

# 1-й четверг ноября

# WEEKDAYS = [
# 'понедельник',
# 'вторник',
# 'среда',
# 'четверг',
# 'пятница',
# 'суббота',
# 'воскресенье',
# ]
#
# logger = logging.getLogger(__name__)
#
#
# def _is_leap(year: int) -> bool:
#     return bool(not year % 4 and year % 100 or not year % 400)
#
#
# def _months(year: int = 2000) -> dict:
#     return {
#     'янв': (31, 1),
#     'фев': (29 if _is_leap(year) else 28, 2),
#     'мар': (31, 3),
#     'апр': (30, 4),
#     'мая': (31, 5),
#     'июн': (30, 6),
#     'июл': (31, 7),
#     'авг': (31, 8),
#     'сен': (30, 9),
#     'окт': (31, 10),
#     'ноя': (30, 11),
#     'дек': (31, 12),
#     }
#
#
# def _check_week(data: str) -> int:
#     if data[0].isdigit() and 0 < int(data[0]) < 6:
#         return int(data[0])
#     logging.error('Количество недель должно быть целым число от 1 до 5')
#     raise ValueError
#
#
# def _check_weekday(data: str) -> str:
#     if data in WEEKDAYS:
#         return data
#     logger.error(f'{data} - нет такого дня недели')
#     raise ValueError
#
#
# def _check_month(data: str) -> tuple:
#     months = _months()
#     if data[:3] in months:
#         return months[data[:3]]
#     logger.error(f'{data} - нет такого месяца')
#     raise ValueError
#
#
# def check_date(data_txt: str) -> str:
#     result = ''
#     data = data_txt.split()
#     week = _check_week(data[0])
#     weekday = _check_weekday(data[1])
#     month = _check_month(data[2])
#     month_txt = data[2]
#     year = datetime.datetime.now().year
#     first_day_of_month = datetime.datetime.strptime(f'1-{month[1]}-{year}', '%d-%m-%Y').weekday()
#     weekdays = WEEKDAYS[first_day_of_month:] + WEEKDAYS[:first_day_of_month]
#     for i in range(month[0]):
#         if weekday == weekdays[i % 7]:
#             week -= 1
#             if not week:
#                 return f'{i+1}-{month_txt}-{year}'
#     raise ValueError
#
#
# print(check_date('5-ая среда января'))