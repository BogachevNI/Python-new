# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N -
# количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M -
# количество элементов во втором массиве. Затем элементы второго массива

# from random import randint

# N = int(input("Количество элементов в первом массиве: "))
# list_N = [randint(0, 15) for i in range(N)]
# M = int(input("Количество элементов во втором массиве: "))
# list_M = [randint(5, 10) for i in range(M)]
# list_S = []

# print(list_N)
# print(list_M)

# for i in range(len(list_N)):
#     if list_N[i] not in list_M:
#         list_S.append(list_N[i])
# print(list_S)

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N —
# количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# from random import randint

# N = int(input("Количество элементов в массиве: "))
# list_N = [randint(0, 15) for i in range(N)]
# print(list_N)
# count = 0

# for i in range(1, len(list_N) - 1):
#     if list_N[i] > list_N[i - 1] and list_N[i] > list_N[i + 1]:
#         count += 1
# print(count)


# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# from random import randint

# N = int(input("Количество элементов в массиве: "))
# list_N = [randint(0, 15) for i in range(N)]
# print(list_N)
# dict = {}

# for i in list_N:
#     dict[i] = dict.get(i, 0) + 1
# print(dict)
# count = 0
# for i in dict:
#     if dict[i] // 2 >= 1:
#         count += dict[i] // 2
# print(count)

# list_2 = []
# for item in list_N:
#     if list_N.count(item) > 1 and item not in list_2:
#         list_2.append(item)
# print(len(list_2))

# если ты мастер
# print(lst := [random.randint(0,5) for _ in range(10)])
# print(sum([list_N.count(i)//2 for i in set(list_N)]))
# count = 0
# for i in set(list_N):
#     count += list_N.count(i) // 2
# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Решение студентов
# k = 10000

# for i in range(1, 10000):
#     sum_1 = 0

#     for k in range(1, i//2 + 1):
#         if i % k ==0:
#             sum_1 += k

#     sum_2 = 0
#     for j in range(1, sum_1//2 + 1):
#         if sum_1 % j == 0:
#             sum_2 += j
#     if sum_2 == i and sum_1 != sum_2:
#         i = sum_1
#         print(f'{sum_1} {sum_2}')

# Решение преподавателя
# def sum_devs(num: int):
#     summ_ = 0
#     for i in range(1, num//2 + 1):
#         if num % i == 0:
#             summ_ += i
#     return summ_

# # print(sum_devs(220))
# # print(sum_devs(284))

# digit_dict = {i: sum_devs(i) for i in range(1, 10000)}
# # print(digit_dict)

# for digit, summ_ in digit_dict.items():
#     if digit == digit_dict.get(summ_) and digit < summ_:
#         print(digit, summ_)

# Решение Полины

# nums = []
# def findSum(num):
#     sum = 0
#     for i in range(1, num // 2 +1):
#         if num % i == 0:
#             sum += i
#     return sum

# for i in range(1, 10000):
#     sum1 = findSum(i)
#     sum2 = findSum(sum1)
#     if sum2 == i and sum1 != sum2 and sum1 not in nums:
#         nums.append(i)
#         nums.append(sum1)
#         print(i, sum1)

