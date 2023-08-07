# Функции высшего порядка
# lambda - безымянная однострочная функция, которая что-то возвращает
# def summa(a,b):
#     result = a + b
#     return result
# аналог
# lambda a, b: a + b - лямбда не сохраняется в памяти, создается в алгоритме, отрабатывает и удаляется
# можно объявить через func = lambda <текст>, но в целом не нужно.
# можно использовать для возврата констант, но бесполезно.
# используется в сортировках, поисках максимума/минимума при работе с кортежем
# lst = [(1,2), (6,7), (5,9)]
# print (max(lst, key = lambda x: x[1]))
# аналог
# def key_sort(a):
#   return a[1]
# lst = [(1,2), (6,7), (5,9)]
# print (max(lst, key = key_sort))
# lambda сокращает код, использовать везде подряд не нужно, для ключей, сравнения, бинарных операторов - одной строчкой.

# map - на вход принимает функцию и коллекцию; функция применяется к каждому элементу коллекции
# nums = list('1234567890')
# print(nums)

# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# аналог:
# nums = list(map(int, nums)) # map возвращает генератор, который 1 раз развенётся, и ни разу больше не покажется, list позволяет сохранить объект как список
# nums = list(map(lambda x: x**2, nums))
# print(nums)
# nums = list(map(lambda x: str(x) if x%2 ==0 else x, nums))
# print(nums)
# nums = input('Введите числа через пробел: ')
# nums = list(map(int, filter(lambda x: x.isdigit(), nums.split())))
# print(nums)
# filter
# zip - поразрядное соединение элементов списков в кортежи
# nums = list('1234567890')
# lets = list('ASDFGTREWQ')
# punct = list('!@#$%^&*()')
# # new_list = []
# # for i in range(len(nums)):
# #     new_list.append((nums[i], lets[i]))
# new_list = list(zip(nums, lets, punct))
# print(new_list)

# Если будет неравное количество элементов, то zip дойдёт до минимального последнего вхождения
# Чтобы преодолеть это ограничение нужно использовать zip_longest 
# Пример
# from itertools import zip_longest
# new_list = list(zip_longest(nums, lets, punct, fillvalue = 'ПУСТО'))

# enumerate - замена range
# lets = list('ASDFGTR')
# for i, item in enumerate(lets):
#     print(i, item)

# for i, item in enumerate(lets, 10): # 10 - первый номер
#     print(i, item)

# Практика

# У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине программы используется множество раз
# и вы не хотите ничего сломать):

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.

# transformation = lambda a: a
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(values)
# print(transormed_values)

# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета. 
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато 
# искусственные спутники были были запущены на круговые орбиты. 
# Результатом функции должен быть кортеж, содержащий длины полуосей (радиусы) эллипса орбиты самой далекой планеты. 
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

# Решение задачи
# Создать рандомно список кортежей, состоящий из осей. Одинаковых осей быть не может. Найти площадь.
# Функция принимает список кортежей и возвращает кортеж с самой большой площадью.

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_fartest_orbit(list_of_orbits):
#     list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     print(list_of_orbits)
#     list_of_squares = list(map(lambda x: x[0]*x[1], list_of_orbits))
#     print(list_of_squares)
#     list_of_squares_and_orbits = list(zip(list_of_squares, list_of_orbits))
#     return max(list_of_squares_and_orbits)
# print(find_fartest_orbit(orbits)[1])