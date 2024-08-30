# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
# Пример
# На входе:
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0
#
# На выходе, например, один из допустимых вариантов может быть таким:
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}

backpack_weight = 0
backpack = {}

for key in items:
    if items[key] <= max_weight and backpack_weight + items[key] <= max_weight:
        backpack_weight += items[key]
        backpack.setdefault(key, items[key])

#  Решение с платформы
# backpack = {}
#
# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight
