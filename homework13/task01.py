"""
Задание 1. Карма
Один буддист-программист решил создать свой симулятор жизни, в котором
нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
Каждый день вызывается специальная функция one_day(), которая возвращает
количество кармы от 1 до 7 и может с вероятностью 1 к 10 выкинуть одно из
исключений:
● KillError,
● DrunkError,
● CarCrashError,
● GluttonyError,
● DepressionError.
(Исключения нужно создать самостоятельно, при помощи наследования от
Exception.)
Напишите такую программу. Функцию оберните в бесконечный цикл, выход из
которого возможен только при накоплении кармы до уровня константы.
Исключения обработайте и запишите в отдельный лог karma.log.
По итогу у вас может быть примерно такая структура программы:
открываем файл
цикл по набору кармы
try
карма += one_day()
except(ы) с указанием классов исключений, которые нужно поймать
добавляем запись в файл
закрываем файл
"""
import random

# Константа для достижения просветления
NIRVANA_KARMA = 500


# Определение пользовательских исключений
class KillError(Exception):
    def __init__(self):
        super().__init__("Убийство. Вы и убили-с!")


class DrunkError(Exception):
    def __init__(self):
        super().__init__("Пьянство. Пьянству бой!")


class CarCrashError(Exception):
    def __init__(self):
        super().__init__("Вы попали в аварию. Стоит следить за дорогой.")


class GluttonyError(Exception):
    def __init__(self):
        super().__init__("Вы обожрались. Следует сократить порции.")


class DepressionError(Exception):
    def __init__(self):
        super().__init__("На вас напала хандра. Уныние - грех.")


# Функция, моделирующая один день жизни
def one_day():
    # Случайное количество кармы от 1 до 7
    day_karma = random.randint(1, 7)
    # Случайная вероятность выброса исключения
    if random.randint(1, 10) == 5:
        # Случайный выбор исключения
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception
    return day_karma


# Основная функция симулятора
def main():
    karma = 0
    # Открываем файл для записи логов
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while True:
            try:
                # Прибавляем карму за один день
                karma += one_day()
            except Exception as ex:
                # Записываем информацию об исключении в файл
                fl_logger.write(f'{ex}\n')
            # Проверяем, достигнуто ли необходимое количество кармы
            if karma >= NIRVANA_KARMA:
                break
    # Сообщаем о достижении цели
    print('Вы достигли Нирваны! ')
    print('Омм ')


# Запуск основной функции
if __name__ == "__main__":
    main()
