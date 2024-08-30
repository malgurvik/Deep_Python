"""
Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

from random import uniform as uni, randint as ri
from pprint import pprint


def is_profitable(companies_income: dict) -> bool:
    print()
    for name, profit in companies_income.items():
        print(name, sum(profit))
    print()
    return all((sum(income) >= 0 for income in companies_income.values()))


companies_income = {
    'horns and hooves': [uni(-100_000, 100_000) for _ in range(ri(3, 10))],
    'cheburashka artel': [uni(-100_000, 100_000) for _ in range(ri(3, 10))],
    'tasteless, period': [uni(-100_000, 100_000) for _ in range(ri(3, 10))],
}

pprint(companies_income)
print(is_profitable(companies_income))

data = {"company_1": [70, 12, 25, -28, 10, 36],
        "company_2": [-55, 10, -20, -10, -15, -15],
        "company_3": [40, 12, 21, -70, 11, 65]}


def task_7(dat):
    for el in dat.values():
        if sum(el) < 0:
            return False
    return True


print(task_7(data))

print(all([sum(value) > 0 for value in data.values()]))
