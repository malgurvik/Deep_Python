# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
#
# Пример
# На входе:
lst = [1, 1, 2, 2, 3, 3]
#
# На выходе:
# [1, 2, 3]

lst2 = []
count_dict = {}

for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1

for key in count_dict:
    if count_dict[key] > 1:
        lst2.append(key)

print(lst2)

# Решение с платформы

# duplicates = set()
#
# for item in lst:
#     if lst.count(item) >= 2:
#         duplicates.add(item)
#
# result = list(duplicates)
# print(result)
