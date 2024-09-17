"""
Задание №1
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов.
"""


# class Factorial:
#     def __init__(self, k):
#         self.k = k
#         self.history = []
#
#     def __call__(self, n):
#         if n < 0:
#             raise ValueError("Факториал не определён для отрицательных чисел")
#         elif n == 0:
#             return 1
#         else:
#             factorial = 1
#             for i in range(1, n + 1):
#                 factorial *= i
#             self.history.append((n, factorial))
#             if len(self.history) > self.k:
#                 self.history.pop(0)
#         return factorial
#
#     def show_history(self):
#         if not self.history:
#             print("История вызовов пуста.")
#         else:
#             print("История вызовов:")
#             for n, factorial in self.history:
#                 print(f"Факториал {n}: {factorial}")
#
#
# if __name__ == "__main__":
#     factorial_calculator = Factorial(3)
#
#     print(factorial_calculator(5))
#     print(factorial_calculator(3))
#     print(factorial_calculator(8))
#
#     factorial_calculator.show_history()

class Factorial:
    fact_arch = []

    def __init__(self, amount: int):
        self.amount = amount

    @staticmethod
    def _factorial(num):
        if num in (0, 1):
            return 1
        fact = 1
        for i in range(2, num + 1):
            fact *= i
        return fact

    def show_last(self):
        return Factorial.fact_arch[-self.amount:]

    def __call__(self, fact_num: int):
        current_fact = Factorial._factorial(fact_num)
        Factorial.fact_arch.append(current_fact)
        return current_fact
