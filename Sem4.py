# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# from random import randint
# a = [2, 3, 1, 4, 5, 1, 5, 2, 3, 5, 1, 4, 5, 3, 5]
# number = input("Введите число: ").split() # ввод через разделитель
# list_1 = list(input("Введите число: ")) # ввод через list (без разделителя)
# count = 0
# string_2 = ""
# list_2 = []

# for i in range(len(list_1)):
#     for j in range(len(list_1[:i])):
#         if list_1[j] == list_1[i]:
#             count += 1
#             print(list_1[:i])
    
#     string_2 = list_1[i] +'_' + str(count)
#     if list_1[i] not in list_2:
#         list_2.append(list_1[i])
#     else:
#         list_2.append(string_2)
#     count = 0
#     string = ""
# print(list_2)

# st = "qwerewrweqwerwe"
# list_st = list(st)
# dict = {}
# for s in list_st:
#     if s in dict:
#         dict[s] += 1
#     else:
#         dict[s] = 1
# print(dict)

# number = input('Введите строку: ')
# count_dict = {}

# for i in number:
#     count_dict[i] = count_dict.get(i, 0) + 1 # счетчик
#     print(f'{i}' + (f'_{count_dict[i]-1}' if count_dict[i] > 1 else ''), end =' ') # питонирование

# Как я бы сделал на шарпе:
# for i in number:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
#     if count_dict[i] > 1:
#         print(f'{i}' + (f'_{count_dict[i]-1}'), end =' ')
#     else: 
#         print(f'{i}', end =' ')
# .get(i, 0) в словаре подтягивает значение по ключу i и возвращает 0, если ключа нет.

# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним
# или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
# Текст: Бык тупогуб, тупогубенький бычок, у быка губа тупа.
# number = "Бык тупогуб, тупогубенький бычок, у быка губа тупа."
# number = number.replace(',', '')
# number = number.replace('.', '')
# list_number = list(number.lower().split())

# set_list_number = set(list_number)

# print(set_list_number)
# print(len(set_list_number))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание. Они решили так:
# у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью
# товарищи обратились к Вам, студентам.

# n = int(input())
# max_number = n
# while n != 0:  
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)