"""
Задача 2. Тестирование класса с использованием unittest
Напишите класс Library, который управляет книгами. Класс должен поддерживать
следующие методы:
    ● add_book(title): добавляет книгу в библиотеку.
    ● remove_book(title): удаляет книгу из библиотеки.
    ● list_books(): возвращает список всех книг в библиотеке.
При попытке удалить книгу, которая не существует, должно выбрасываться исключение
BookNotFoundError. Для тестирования используйте unitest.
Подсказка № 1
    Убедитесь, что метод add_book корректно добавляет книги в библиотеку. Для этого
    добавьте книгу и проверьте, что она присутствует в списке всех книг.
Подсказка № 2
    Проверьте, что метод remove_book корректно удаляет книгу из библиотеки. Добавьте
    книгу, удалите ее и убедитесь, что она больше не присутствует в списке.
Подсказка № 3
    Убедитесь, что метод remove_book корректно выбрасывает исключение
    BookNotFoundError, если пытаетесь удалить книгу, которой нет в библиотеке.
Подсказка № 4
    Проверьте, что метод list_books возвращает правильный список книг после
    выполнения нескольких операций добавления и удаления книг.
"""
import unittest


class BookNotFoundError(Exception):
    def __init__(self):
        super().__init__("Книга не найдена в библиотеке.")


class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        self.books.add(title)

    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError()
        self.books.remove(title)

    def list_books(self):
        return list(self.books)


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("1984")
        self.assertIn("1984", self.library.list_books())

    def test_remove_book(self):
        self.library.add_book("Brave New World")
        self.library.remove_book("Brave New World")
        self.assertNotIn("Brave New World", self.library.list_books())

    def test_remove_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")


if __name__ == '__main__':
    unittest.main()
