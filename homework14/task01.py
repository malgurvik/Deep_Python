"""
Задание 1. Тестирование класса с использованием pytest
Напишите класс BankAccount, который управляет балансом счета. Он должен
поддерживать следующие методы:
    ● deposit(amount): добавляет указанную сумму к балансу.
    ● withdraw(amount): снимает указанную сумму с баланса, если достаточно
      средств.
    ● get_balance(): возвращает текущий баланс счета.
      При попытке снять больше средств, чем доступно на счете, должно
      выбрасываться исключение InsufficientFundsError. Напишите как минимум
      5 тестов для проверки работы классов и его методов.

Подсказка № 1
    Проверьте, что начальный баланс создаваемого объекта BankAccount корректен,
    используя значение, переданное в конструкторе. Убедитесь, что баланс
    инициализируется правильно при создании объекта.
Подсказка № 2
    Проверьте, что метод deposit корректно добавляет указанную сумму к текущему
    балансу. Убедитесь, что сумма депозита положительна и увеличивает баланс на
    ожидаемое значение.
Подсказка № 3
    Убедитесь, что метод withdraw корректно уменьшает баланс на указанную сумму,
    если на счету достаточно средств. Проверьте правильность работы метода при
    различных значениях суммы.
Подсказка № 4
    Убедитесь, что метод withdraw корректно выбрасывает исключение
    InsufficientFundsError, когда пытаются снять больше средств, чем доступно на
    счету. Используйте pytest.raises для проверки этого поведения.
Подсказка № 5
    Проверьте, что при создании объекта BankAccount без указания начального баланса,
    баланс инициализируется как 0. Это поможет убедиться в правильности работы
    конструктора с дефолтными значениями.
"""
import pytest


class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__('На счете не достаточно средств!')


class BankAccount:
    def __init__(self, default_balance=0):
        self.balance = default_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма не может быть меньше или равной 0!')
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError
        self.balance -= amount

    def get_balance(self):
        return f'Баланс счета {self.balance}'


@pytest.fixture
def func():
    obj = BankAccount(100)
    return obj


def test_get_balance(func):
    assert func.get_balance() == 'Баланс счета 100'


def test_deposit(func):
    func.deposit(100)
    assert func.get_balance() == 'Баланс счета 200'


def test_withdraw(func):
    func.withdraw(50)
    assert func.get_balance() == 'Баланс счета 50'


def test_withdraw_insufficient_funds_error(func):
    with pytest.raises(InsufficientFundsError):
        func.withdraw(150)


if __name__ == '__main__':
    pytest.main()

# bank = BankAccount(100)
# print(bank.get_balance())
# bank.deposit(100)
# print(bank.get_balance())
# bank.withdraw(250)
# print(bank.get_balance())
