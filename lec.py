# print('hallo world')
# Типы переменных int,float,boolean,str list
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 1234
# print(type(value))
# s = 'hello world'
# print(s) вывод строки
# print(a,'-',b,'-',s)
# print('{} - {} - {}'.format(a,b,s))# вывод строки методом формат
# print(f'{a} - {b} - {s}')#вывод строки методом интерполяция
# f = True
# f = False
# print(f)
# list = ['1','2','3']
# col = ['hello',1,2,4.5,5,True]
# print(list)
# print(col)
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a,'+',b,'=',a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')
# +.-,*,/,%--Остаток от деления,//-- Деление в целых числах,**--Возведение в степень
# (), Сокращенные операции
# a = 3
# a += 5
# print(a)
# Арифметические операции
# a = 123
# b = 321
# c = a + b
# print(c)
# round(а * b,3) --Округление по математическим правилам
# Логические операции
# >,>=,<,<=,==,!=,not,ahd,or-не путать с &,|,^
# Кое-что еще:is,is not,in,not in
# a = 1<4 and 5>2
# print(a)
# Управляющие конструкции:if,if-else
# if condition:
    # operator 1
    # operator 2
    # ...
    # operator n
# else
   # operator n + 1
   # operator n + 2
   # ...
   # operator n + m
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
    # print(a)
# else:
    # print(b)
# username = input('Введите имя: ')
# if username =='Маша':
  #  print('Ура,это же МАША!')
# elif username =='Марина':
  #  print('Я так ждала Вас,Марина!')
# elif username == 'Ильнар':
  #  print('Ильнар - топ')
# else:
  #  print('Привет, ',username)
  # Управляющие конструкции:
  # while
# original = 23
# inverted = 0
# while original !=0:
   # inverted = inverted * 10 + (original % 10)
   # original //=10
#print(inverted)
#original = 23
#inverted = 0
#while original !=0:
    #inverted = inverted * 10 + (original % 10)
    #original //=10
    #print(original)
#else:
 #   print('Пожалуй')
  #  print('хватит )')
#print(inverted)
# Управляющие конструкции :for
#Когда мы знаеи.что хотим
# for i in enumeration
#     # operator 1
      # operator 2
      # ....
      # operator n
#for i in 1,2,3,4,5:
 #   print(i**2)
#list = [1,2,3,4,10,5]
#for i in list:
 #   print(i)
#r = range(10)
#for i in r:
 #   print(i)
#for i in range(1, 10, 2):
 #   print(i)
#Немного о стороках
#text = 'съешь ещё этих мягких французких булок'
#print(len(text))                #39
#print('ещё' in text)            #True
#print(text.isdigit())           #False
#print(text.islower())           #True
#print(text.replace('ещё','ЕЩЁ'))# ЗАМЕНА
#for c in text:
    # print(c)
#text = 'съешь ещё этих мягких французких булок'
#print(text[0])                  # с
#print(text[1])                  # ъ
#print(text[len(text)])          # IndexError
#print(text[len(text)-1])        # к
#print(text[-5])                 # б
#print(text[:])                  # print(text)
#print(text[2:5])                # сь
#print(text[len(text)-2:])       # ок
#print(text[2:9])                # ещь ещё
#print(text[6:-18])              # ещё этих мягких
#print(text[0:len(text):6])      # сеикакл
#print(text[::6])                # сеикакл
#print(text[2:9]+text[-5]+text[:2]) # ....
# Списки:введение
#numbers = [1, 2, 3, 4, 5]
#print(numbers)          # [1,2,3,4,5]
#ran = range(1, 6)
#numbers = list(ran)
#print(numbers)          # [1,2,3,4,5]
#numbers[0] = 10
#print(f'{len(numbers)}len')          # [10,2,3,4,5]
#for i in numbers:
#    i *= 2
#    print(i)            # [20,4,6,8,10]
#print(numbers)
#colors = ['red', 'green', 'blue']
#for e in colors:
 #   print(e)         # red green blue
#for e in colors:
#    print(e*2)       # redred greengreen blueblue
#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True
#colors.remove('red')# del colors[0] удалить элемент
# Функции
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2.3
# print(f(arg))
# print(type(f(arg)))

# Лекция № 2

# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+,r+

# Файлы
# Способ 1
# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')
# Способ 2
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

# Считывание файла

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#   print(line)
# data.close()  

# Функции

# Это фрагмент программы, используемый
# многократно

# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return

# Функции
# def f(x):
#  return x**2
# def f(x):
#  if x == 1:
#  return 'Целое'
#  elif x == 2.3:
#  return 23
#  else:
#  return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneTyp

# Функции

# new file function_file.py
# def f(x):
#  if x == 1:
#    return 'Целое'
#  elif x == 2.3:
#   return 23
#  else:
#   return
# file hello.py
# import function_file
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) #

# Функции

# def new_string(symbol, count):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# Функции

# def new_string(symbol, count = 3):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) #

# Функции

# def concatenatio(*params):
#  res: str = ""
#  for item in params:
#  res += item
#  return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)

# Рекурсия

# Функции

# def fib(n):
#  if n in [1, 2]:
#   return 1
#  else:
#   return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#   list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# Кортежи

# Кортеж – это неизменяемый “список”

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# Кортежи

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError:

# Кортежи

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

# Словари
# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу
# dictionary = {}
# dictionary = \
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys():
#   print(k)               #Ключи

# for k in dictionary.values:
#   print(k)  # Только значение

# for v in dictionary:
#   print(dictionary[v]) #Пробежатся по всем значениям словаря


# Словари
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#   print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set

# Множества
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# Множества
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}

# Множества
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3,})

#Списки

list1 = {1,2,3,4,5}
list2 = list1
for e in 
