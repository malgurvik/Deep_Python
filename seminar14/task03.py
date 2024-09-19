"""
Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""
import unittest
from task01 import convert_str


class TestCaseName(unittest.TestCase):
    def test1(self):
        self.assertEqual(convert_str('hello world'), 'hello world')

    def test2(self):
        self.assertEqual(convert_str('HelLO WorlD'), 'hello world')

    def test3(self):
        self.assertEqual(convert_str('Hello, world!'), 'hello world')

    def test4(self):
        self.assertEqual(convert_str('hello мой world'), 'hello  world')

    def test5(self):
        self.assertEqual(convert_str('HelLO# мой$ WorlD!!'), 'hello  world')


if __name__ == '__main__':
    unittest.main(verbosity=2)
