# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("Первый элемент: "))
# n = int(input("Количество элементов: "))
# d = int(input("Разность: "))
# list_1 = []
# def progression_(a1, n, d, list_1):
#     for item in range(1, n + 1, 1):
#         list_1.append(a1 + (item - 1) * d)
#     return list_1
# print(progression_(a1, n, d, list_1))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

min_val = int(input("Минимум: "))
max_val = int(input("Максимум: "))

n = int(input('Введите количество элементов в массиве: '))
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)
list_i = []

def list_between_extremum(list_1, min_val, max_val):
    for item in range(len(list_1)):
        if list_1[item] >= min_val and list_1[item] <= max_val:
            list_i.append(item)
    return list_i

print(list_between_extremum(list_1, min_val, max_val))