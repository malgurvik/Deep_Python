"""
Задача 5. Конвертация CSV в JSON с изменением структуры данных
Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
JSON файл с другой структурой. CSV файл содержит данные о книгах (название,
автор, год издания). В JSON файле данные должны быть сгруппированы по
авторам, а книги каждого автора должны быть записаны как список.
"""

import csv
import json


def convert_csv_to_json(input_file, output_file):
    books_by_author = {}
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            author = row['автор']
            book = {
                'название': row['название'],
                'год издания': row['год издания']
            }
            if author in books_by_author:
                books_by_author[author].append(book)
            else:
                books_by_author[author] = [book]
    with open(output_file, 'w') as f:
        json.dump(books_by_author, f, indent=4)


if __name__ == "__main__":
    convert_csv_to_json('books.csv', 'books_by_author.json')
