"""
Задание 1. Матрицы
Вы стажируетесь в лаборатории искусственного интеллекта, в ней вам
поручили разработать класс Matrix для обработки и анализа данных. Ваш класс
должен предоставлять функциональность для выполнения основных операций
с матрицами, таких как сложение, вычитание, умножение и транспонирование.
Это будет полезно для обработки и структурирования больших объёмов
данных, которые используются в обучении нейронных сетей.
Задача
    1. Создайте класс Matrix для работы с матрицами.
    Реализуйте методы:
        ○ сложения,
        ○ вычитания,
        ○ умножения,
        ○ транспонирования матрицы.
    2. Создайте несколько экземпляров класса Matrix и протестируйте
    реализованные операции.
Советы
    ● Методы сложения/вычитания/умножения должны получать параметром
    другую матрицу (объект класса Matrix) и выполнять указанное действие
    над своей и этой другой матрицей. Например, метод сложения должен
    получить параметром новую матрицу и сложить её со своей текущей.
    ● Метод транспонирования не должен ничего получать, он должен
    работать исключительно со своей матрицей.
    ● Транспонирование — это алгоритм, при котором строки матрицы
    меняются местами с её столбцами:
    ● Алгоритм транспонирования матрицы можно расписать следующим образом:
        1. Создать новую матрицу result с размерами, обратными размерам
        исходной матрицы. Количество строк новой матрицы равно
        количеству столбцов исходной, а количество столбцов новой
        матрицы равно количеству строк исходной.
        2. Пройтись по каждому элементу исходной матрицы. Для каждого
        элемента с индексами (i, j):
        1. Поместить значение этого элемента (i, j) в ячейку с
        индексами (j, i) новой матрицы. То есть транспонирование
        происходит с помощью обмена индексов местами.
        2. После завершения цикла новая матрица result будет
        содержать транспонированную матрицу, которую можно
        вернуть.
"""
from random import randint


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix_data = [[0 for _ in range(self.column)] for _ in range(self.row)]

    def __str__(self):
        return " \n".join(["\t".join(map(str, row)) for row in self.matrix_data])

    def add(self, other):
        if self.row != other.row or self.column != other.column:
            raise ValueError('Матрицы должны быть одного размера!')
        result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix_data[i][j] = self.matrix_data[i][j] + other.matrix_data[i][j]
        return result

    def subtract(self, other):
        if self.row != other.row or self.column != other.column:
            raise ValueError('Матрицы должны быть одного размера!')
        result = Matrix(self.row, self.column)
        for i in range(self.row):
            for j in range(self.column):
                result.matrix_data[i][j] = self.matrix_data[i][j] - other.matrix_data[i][j]
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы")
        m = len(self.matrix_data)
        n = len(other.matrix_data)
        k = len(other.matrix_data[0])
        result = Matrix(m, k)
        for i in range(m):
            for j in range(k):
                result.matrix_data[i][j] = sum(self.matrix_data[i][kk] * other.matrix_data[kk][j] for kk in range(n))
        return result

    def transpose(self):
        result = Matrix(self.column, self.row)
        result.matrix_data = list(map(list, zip(*self.matrix_data)))
        return result


def filling_the_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = randint(0, 10)
    return matrix


m1 = Matrix(2, 3)
# print(m1)
# m1.matrix_data = filling_the_matrix(m1.matrix_data)
m1.matrix_data = [[1, 2, 3], [4, 5, 6]]
print('Matrix 1')
print(m1)
m2 = Matrix(2, 3)
# m2.matrix_data = filling_the_matrix(m2.matrix_data)
m2.matrix_data = [[7, 8, 9], [10, 11, 12]]
print('Matrix 2')
print(m2)
print('Sum of Matrix')
print(m1.add(m2))
print('Subtract matrix')
print(m1.subtract(m2))
m3 = Matrix(3, 2)
m3.matrix_data = [[1, 2], [3, 4], [5, 6]]
print('Multiply matrix')
print(m1.multiply(m3))
print('Transpose matrix')
print(m1.transpose())
