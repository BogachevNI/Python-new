# №1
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# from random import randint

# list_1 = [randint(-5, 5) for i in range(1, 20)]
# print(list_1)

# list_2 = []
# count = 0

# for item in list_1: # через второй список
#     if item not in list_2: 
#         list_2.append(item)
#         count += 1
# print(len(list_2))

# print(set(list_1)) # set - перевод в множества, удаление дубликатов
# print(len(set(list_1)))

# №2
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

# from random import randint

# lst = [randint(-5, 5) for i in range(10)]
# print(lst)
# shift = int(input('Введите сдвиг: '))
# # print(lst[-shift:] + lst[:-shift]) # срез

# # for i in range(shift): # - затратнее, зависит от длины списка
# #     item = lst.pop()
# #     lst.insert(0, item)
# # print(lst)

# # для циклического решения
# new_list = []
# for i in range(100):
#     print(lst[i%len(lst)])

# Напишите программу для печати всех уникальных значений в словаре.
# Вариант 1
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] # - список словарей
# list_2 = []
# for i in range (0, len(list_1)):
#     list_2.append(str(list_1[i].values()))
# print (set(list_2))

# # Вариант 2
# list_3 = []
# for i in list_1:
#     for key, value in i.items():
#         list_3.append(value)
# print(list_3)
# print(set(list_3))

# # Вариант 3
# nset = set()
# for dct in list_1:
#     nset.add(*dct.values()) # * распаковывает всю нашу коллекцию на 1 уровень 
# print(nset)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)



# A = [int(i) for i in input().split()] #заполним список
# X = int(input()) #пользователь вводит число, количество вхождений которого нужно подсчитать
# print(A.count(X)) #выводим количество вхождений числа X в список A

k = 'ноутбук'
score = 0

for item in k:
    if item.upper() in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']:
        score += 1
    elif item.upper() in ['D', 'G']:
        score += 2
    elif item.upper() in ['B', 'C', 'M', 'P']:
        score += 3
    elif item.upper() in ['F', 'H', 'V', 'W', 'Y']:
        score += 4
    elif item.upper() in ['K']:
        score += 5
    elif item.upper() in ['J', 'X']:
        score += 8
    elif item.upper() in ['Q', 'Z']:
        score += 10
    if item.upper() in ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']:
        score += 1
    elif item.upper() in ['Д', 'К', 'Л', 'М', 'П', 'У']:
        score += 2
    elif item.upper() in ['Б', 'Г', 'Ё', 'Ь', 'Я']:
        score += 3
    elif item.upper() in ['Й', 'Ы']:
        score += 4
    elif item.upper() in ['Ж', 'З', 'Х', 'Ц', 'Ч']:
        score += 5
    elif item.upper() in ['Ш', 'Э', 'Ю']:
        score += 8
    elif item.upper() in ['Ф', 'Щ', 'Ъ']:
        score += 10
print(score)