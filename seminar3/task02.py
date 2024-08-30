# Задание №3
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

user_input = input("Введите что-нибудь: ")
if user_input.isdigit():
    user_input = int(user_input)
else:
    try:
        user_input = float(user_input)
    except ValueError:
        if not user_input.islower():
            user_input = user_input.lower()
        else:
            user_input = user_input.lower()

print(user_input, type(user_input))
