"""
Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:

    def __init__(self, genus: str, age: int):
        self.__genus = genus
        self.__age = age

    def get_genus(self):
        return self.__genus

    def get_age(self):
        return self.__age

    def info(self):
        return f"Вид: {self.__genus}, возраст: {self.__age} лет"


class Fish(Animal):

    def __init__(self, genus: str, age: int, depth_of_swimming: int):
        super().__init__(genus, age)
        self.__depth_of_swimming = depth_of_swimming

    def info(self):
        return f"{super().info()}, глубина плавания: {self.__depth_of_swimming} м"


class Bird(Animal):

    def __init__(self, genus: str, age: int, height_of_flying: int):
        super().__init__(genus, age)
        self.__height_of_flying = height_of_flying

    def info(self):
        return f"{super().info()}, высота полета: {self.__height_of_flying} м"


class Mammal(Animal):

    def __init__(self, genus: str, age: int, speed_of_running: int):
        super().__init__(genus, age)
        self.__speed_of_running = speed_of_running

    def info(self):
        return f"{super().info()}, скорость бега: {self.__speed_of_running} км/ч"


f = Fish("Карась", 1, 2)
b = Bird("Ласточка", 2, 200)
m = Mammal("Гепард", 5, 100)
print(f.info())
print(b.info())
print(m.info())
