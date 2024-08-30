"""
Задание №5
📌 Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
📌 У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
"""


class Fish:

    def __init__(self, genus: str, age: int, depth_of_swimming: int):
        self.__genus = genus
        self.__age = age
        self.__depth_of_swimming = depth_of_swimming

    def info(self):
        return f"Вид: {self.__genus}, возраст: {self.__age} лет, глубина плавания: {self.__depth_of_swimming} м"


class Bird:

    def __init__(self, genus: str, age: int, height_of_flying: int):
        self.__genus = genus
        self.__age = age
        self.__height_of_flying = height_of_flying

    def info(self):
        return f"Вид: {self.__genus}, возраст: {self.__age} лет, высота полета: {self.__height_of_flying} м"


class Mammal:

    def __init__(self, genus: str, age: int, speed_of_running: int):
        self.__genus = genus
        self.__age = age
        self.__speed_of_running = speed_of_running

    def info(self):
        return f"Вид: {self.__genus}, возраст: {self.__age} лет, скорость бега: {self.__speed_of_running} км/ч"


f = Fish("Карась", 1, 2)
b = Bird("Ласточка", 2, 200)
m = Mammal("Гепард", 5, 100)
print(f.info())
print(b.info())
print(m.info())
