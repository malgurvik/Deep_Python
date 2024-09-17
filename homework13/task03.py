"""
Задача 3. Счастливое число
Напишите программу, которая запрашивает у пользователя число до тех пор, пока
сумма этих чисел не станет больше либо равна 777. Каждое введенное число при этом
дозаписывается в файл. Сделайте так, чтобы перед дозаписью программа с
вероятностью 1 к 13 выбрасывала пользователю случайное исключение и
завершалась.
Пример 1:
Введите число: 10
Введите число: 500
Введите число: 200
Введите число: 67
Вы успешно выполнили условие для выхода из порочного цикла!
Содержимое файла out_file.txt:
10
500
200
67
Пример 2:
Введите число: 10
Введите число: 500
Вас постигла неудача!
Содержимое файла out_file.txt:
10
"""
import os
import random

MAGIC_NUMBER = 777


class MagicFileProcessor:
    def __init__(self, filename):
        """Инициализация с именем файла и определение пути к файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return os.path.join(os.path.abspath('.'), self.filename)

    def is_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать ошибку."""
        return random.randint(1, 13) == 7

    def pre_init(self):
        """Удаляет файл, если он существует."""
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(ex)
            print('Данный файл не может быть удален')

    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в файл."""
        try:
            input_number = int(input('Введите число: '))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(str(input_number) + '\n')
        except (ValueError, KeyboardInterrupt) as ex:
            print(ex)
            print('Возникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.pre_init()  # Удаляет старый файл, если он существует
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
            print('Вы успешно выполнили условие для выхода из порочного цикла!')


# Запуск программы
if __name__ == "__main__":
    processor = MagicFileProcessor('out_file.txt')
    processor.run()
