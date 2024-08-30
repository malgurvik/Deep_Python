"""
Дескрипторы - это атрибуты экземпляра класса со связанным поведением,
которое обеспечивается за счет перегрузки соответсвующих методов
"""


class Validate:

    def __init__(self, atr):
        self.atr = atr

    def __get__(self, instance, owner):
        print("Полезная нагрузка")
        return instance.__dict__[self.atr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Неверно")
        self.atr = value


class Worker:
    hours = Validate("hours")
    rate = Validate("rate")

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculation(self):
        return self.rate * self.hours


w = Worker(-10, 100)
# w.hours = -10
