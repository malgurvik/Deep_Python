"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def my_gen(num):
    start = 2
    count = 0
    while count < num:
        for i in range(2, int(start ** 0.5 + 1)):
            if start % i == 0:
                break
        else:
            count += 1
            yield start
        start += 1


N = 10
for num in my_gen(N):
    print(num)

# my_iter = iter(my_gen(N))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# Вариант 2

# def prime_generator(n):
#     count = 0
#     num = 2
#     while count < n:
#         is_prime = True
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#             count += 1
#         num += 1
#
#
# print(*prime_generator(30))
