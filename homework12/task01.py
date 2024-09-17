"""
Задание 1. Работа с данными студентов
Создайте класс студента.
    ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только
      букв. Если ФИО не соответствует условию, выведите:
      ФИО должно состоять только из букв и начинаться с заглавной буквы
    ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
      Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
      Предмет {Название предмета} не найден
    ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до
      100). В противном случае выведите:
      Оценка должна быть целым числом от 2 до 5
      Результат теста должен быть целым числом от 0 до 100
    ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по
      оценкам всех предметов вместе взятых.
Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
следующая информация.
    Математика,Физика,История,Литература
Создайте класс Student, который будет представлять студента и его успехи по
предметам. Класс должен иметь следующие методы:
Атрибуты класса:
    name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
    качестве ключей и информацию об оценках и результатах тестов для каждого предмета в
    виде словаря.
Магические методы (Dunder-методы):
    __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента
    и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и
    вызывает метод load_subjects для загрузки предметов из файла.
    __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута
    name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.
    __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок
    и результатов тестов) по их именам.
    __str__(self): Возвращает строковое представление студента, включая имя и список
    предметов.
Студент: Иван Иванов
Предметы: Математика, История
Методы класса:
load_subjects(self, subjects_file): Загружает предметы из файла CSV.
Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут
subjects.
add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
Убеждается, что оценка является целым числом от 2 до 5.
add_test_score(self, subject, test_score): Добавляет результат теста по
заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
get_average_test_score(self, subject): Возвращает средний балл по тестам для
заданного предмета.
get_average_grade(self): Возвращает средний балл по всем предметам.
Пример
На входе:
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике:
    {average_test_score}")
    print(student)
    На выходе:
    Средний балл: 4.5
    Средний результат по тестам по математике: 85.0
    Студент: Иван Иванов
    Предметы: Математика, История
"""

import csv


class Student:
    def __init__(self, name, subjects_file):
        # Устанавливаем ФИО с помощью дескриптора
        self.__setattr__('name', name)
        self.subjects = {}
        # Загружаем предметы из файла
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        # Проверяем ФИО на правильность
        if name == 'name':
            if not (value and value[0].isupper() and value.replace(" ", "").isalpha()):
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        # Возвращаем предмет из словаря, если он существует
        if name in self.subjects:
            return self.subjects[name]
        raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        # Формируем строковое представление студента и его предметов
        subject_list = ', '.join(self.subjects.keys())
        return f"Студент: {self.name}\nПредметы: {subject_list}"

    def load_subjects(self, subjects_file):
        try:
            # Читаем предметы из файла CSV
            with open(subjects_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    subjects = [subject.strip() for subject in row]
                    for subject in subjects:
                        if subject:
                            self.subjects[subject] = {'grades': [], 'test_scores': []}
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {subjects_file} не найден")

    def add_grade(self, subject, grade):
        # Добавляем оценку по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(grade, int) and 2 <= grade <= 5):
            print("Оценка должна быть целым числом от 2 до 5")
            return
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        # Добавляем результат теста по предмету с проверкой корректности
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return
        if not (isinstance(test_score, int) and 0 <= test_score <= 100):
            print("Результат теста должен быть целым числом от 0 до 100")
            return
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        # Возвращаем средний балл по тестам для заданного предмета
        if subject not in self.subjects:
            print(f"Предмет {subject} не найден")
            return None
        scores = self.subjects[subject]['test_scores']
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    def get_average_grade(self):
        # Возвращаем средний балл по всем предметам
        all_grades = [grade for sub in self.subjects.values() for
                      grade in sub['grades']]
        if not all_grades:
            return 0.0
        return sum(all_grades) / len(all_grades)


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр студента, загружаем предметы из файла subjects.csv
    student = Student("Иван Иванов", "subjects.csv")
    # Добавляем оценки и результаты тестов
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 92)
    # Получаем средний балл и результат по тестам
    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")
    # Выводим информацию о студенте
    print(student)
