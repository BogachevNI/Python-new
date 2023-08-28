# # имя файла: относительный адрес или абсолютный, флаг действия: w - перезапись, r - чтение, a - дозапись, encoding - для работы с кириллицей
# file = open('new.txt', 'w', encoding='UTF-8')
# file.write('24356754\n456734\n3456fdz') # write - принимает только строки
# # file.close()
# # использовать \n и \t для обозначения новых строк и абзацев
# # data = file.read()
# # file.close()
# # print(data)# выводит одной строкой (не обманываться)
# # print(data.__repr__())# демонстрация одной строки
# # print(data.split('\n')) # split - делит строку через \n на список
# file = open('new.txt', 'r', encoding='UTF-8')
# # readline - читает файл построчно
# data1 = file.readline()
# data2 = file.readline()
# data3 = file.readline()
# file.close()
# file = open('new.txt', 'r', encoding='UTF-8')
# # автоматическая генерация списка (readlines) (с \n)
# data4 = file.readlines()
# file.close()

# print(data1)
# print(data2)
# print(data3)
# print(data4)

# data5 = list(map(lambda x: x.strip(), data4)) # убрать \n
# print(data5)
# data5[1] = 'FFFFFFFFF'
# data6 = '\n'.join(data5)

# # file = open('new.txt', 'w', encoding='UTF-8')
# # file.write(data6)
# # file.close()
# # print(data6)

# # контекстный менеджер with ... as ... позволяет не писать .close()
# with open('new.txt', 'w', encoding='UTF-8') as file:
#     file.write(data6)

# # .txt - работа только с текстом
# # .json позволяет работать и со списками, и со словарями


# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи 
# (Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной

# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход

def menu():
    print('\n')
    print('Команды для работы со справочником:')
    print('lst - показать весь список контактов')
    print('add - добавить контакт')
    print('find - найти контакт')
    print('edit - редактировать контакт')
    print('delete - удалить контакт')
    print('stop - прекращение работы программы')

def full_list_print():
    path = 'dict.txt'
    data = open(path, 'r', encoding='UTF-8')

    while True:
        line = data.readline()
        if not line:
            break
        print(line)
        data.close

def data_open_a(new_str):
    with open('dict.txt', 'a', encoding='UTF-8') as data:
        data.write(new_str)

def data_open_w(data, path):
    with open(path, 'w', encoding='UTF-8') as data1:
        for i in data:
            data1.write(i)

def add_data():
    new_last_name = input('Введите фамилию: ')
    new_first_name = input('Введите имя: ')
    new_second_name = input('Введите отчество: ')
    new_phone_number = input('Введите номер телефона: ')
    while not new_phone_number.isdigit():
        new_phone_number = input('Введите номер телефона: ')

    new_str = f'\n{new_last_name} {new_first_name} {new_second_name}: {new_phone_number}'
    data_open_a(new_str)

def find_data(str):
    print('Введите фамилию для поиска данных: ')
    path = 'dict.txt'
    with open(path, 'r', encoding='UTF-8') as data:
        for line in data:
            if str.lower() in line.lower().split():
                print(line)

def del_data(str):
    i = 0
    path = 'dict.txt'
    with open(path, 'r', encoding='UTF-8') as data:
        data = data.readlines()
        print(data)
        for i in range(len(data)):
            if str.lower() in data[i].lower().split():
                data[i] = ''
    data_open_w(data, path)

def edit_data(str):
    del_data(str)
    add_data()
    
while True:
    menu()
    com = input('\n\n')
    if com.lower() == 'stop':
        break
    elif com.lower() == 'lst':
        print('\n')
        full_list_print()
    elif com.lower() == 'add':
        print('\n')
        add_data()
    elif com.lower() == 'find':
        str = input('Введите фамилию для поиска: ')
        print('\n')
        find_data(str)
    elif com.lower() == 'edit':
        str = input('Введите фамилию для редакции: ')
        print('\n')
        edit_data(str)
    elif com.lower() == 'delete':
        str = input('Введите строку для удаления уданных: ')
        print('\n')
        del_data(str)