"""
Задача 4. Агрегирование данных из CSV файла
Напишите скрипт, который считывает данные из CSV файла, содержащего
информацию о продажах (название продукта, количество, цена за единицу), и
подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
новом CSV файле.
"""

import csv


def calculate_total_sales(input_file, output_file):
    sales_totals = {}
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            price_per_unit = float(row['price'])
            total_sales = quantity * price_per_unit
            if product in sales_totals:
                sales_totals[product] += total_sales
            else:
                sales_totals[product] = total_sales

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for product, total_sales in sales_totals.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sales})


if __name__ == "__main__":
    calculate_total_sales('/homework08\\task04\\sales.csv',
                          'total_sales.csv')
