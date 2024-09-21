"""
Задание №5
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
from datetime import datetime
from task04 import user_date
import argparse


parser = argparse.ArgumentParser(description="Принимаем строку с датой")
parser.add_argument('-cnt', type=str, default='1')
parser.add_argument('-wd', type=str, default=str(datetime.now().weekday()))
parser.add_argument('-m', type=str, default=str(datetime.now().month))
args = parser.parse_args()
print(args)
print(user_date(f'{args.cnt} {args.wd} {args.m}'))
