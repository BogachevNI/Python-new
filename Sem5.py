# Последовательностью Фибоначчи называется последовательность чисел
# a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fibo(n): # рекурсия
#     if n in [0, 1]:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
# print(fibo(8))

# fib1 = fib2 = 1 # for
# n = int(input())
# print(fib1, fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

# fib1 = 1 # while
# fib2 = 1
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
# print("Значение этого элемента:", fib2)


# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# from random import randint

# list_1 = [randint(1, 5) for item in range(1, 11)]
# print(list_1)
# # list_1.reverse()
# # print(list_1)
# list_sort = sorted(list_1)
# print(list_sort)
# min_list_1 = min(list_1)
# max_list_1 = max(list_1)
# for item in range(len(list_1)): # при замене значения нужно бежать по индексу, нельзя бежать по самому списку,
#     #для напечатывания значения или при простом переборе можно идти по самому списку 
#     if list_1[item] == max_list_1:
#         list_1[item] = min_list_1
# print(list_1)

# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# number = int(input("Введите число для определения простого числа: "))

# def simple_number(n: int) -> bool:
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range (3, n // 2 + 1, 2):
#         if n % i == 0:
#             return False
#     return True
# simple_number(number)

# 1. Дано натуральное число *N* и последовательность из *N* элементов.
# Требуется вывести эту последовательность в обратном порядке.
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def reverse_(n: int):
    if n < 1:
        return ''
    N = input()
    return reverse_(n - 1) + ' ' + N
n = int(input("Количество: "))
print(reverse_(n))