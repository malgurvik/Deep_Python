"""
Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import pytest
from task01 import convert_str


def test1():
    assert convert_str('hello world') == 'hello world'


def test2():
    assert convert_str('HelLO WorlD') == 'hello world'


def test3():
    assert convert_str('Hello, world!') == 'hello world'


def test4():
    assert convert_str('hello мой world') == 'hello  world'


def test5():
    assert convert_str('HelLO# мой$ WorlD!!') == 'hello  world'


if __name__ == '__main__':
    pytest.main()
