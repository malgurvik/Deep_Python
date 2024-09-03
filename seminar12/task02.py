"""
Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""

import json


class Factorial:
    def __init__(self, k):
        self.k = k
        self.history = []

    def __call__(self, n):
        if n < 0:
            raise ValueError("Факториал не определён для отрицательных чисел")
        elif n == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            self.history.append((n, factorial))
            if len(self.history) > self.k:
                self.history.pop(0)
        return factorial

    def show_history(self):
        if not self.history:
            print("История вызовов пуста.")
        else:
            print("История вызовов:")
            for n, factorial in self.history:
                print(f"Факториал {n}: {factorial}")


class FactorialContextManager:
    def __init__(self, k, filename):
        self.k = k
        self.filename = filename
        self.factorial_calculator = Factorial(k)

    def __enter__(self):
        return self.factorial_calculator

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.filename, "w") as f:
            json.dump(self.factorial_calculator.history, f)


if __name__ == "__main__":
    with FactorialContextManager(3, "factorial_history.json") as factorial_calculator:
        print(factorial_calculator(5))  # Вывод: 120
        print(factorial_calculator(3))  # Вывод: 6
        print(factorial_calculator(8))  # Вывод: 40320

    # Проверка сохраненных данных
    with open("factorial_history.json", "r") as f:
        history = json.load(f)
        print(history)
