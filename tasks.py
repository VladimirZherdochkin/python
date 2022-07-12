#1. По двум заданным числам проверить является ли одно квадратом второго
#print('Введите первое число')
#a = int(input())
#print('Введите второе число')
#b = int(input())
#if a == b**2:
 #   print(f'Число {a} является квадратом числа {b}')
#elif b == a**2:
#    print(f'Число {b} является квадратом числа {a}')
#else:
 #   print (f'Числа {a} и {b} не являются квадратом друг друга')

#2. Найти максимальное из пяти чисел
#print(max([int(input()) for _ in range(int(input()))]))
#list1 = [3, 2, 8, 5, 10]
#max_number = max(list1)
#print("Наибольшее число:", max_number)

#3.Вывести на экран числа от -N до N
#print('Введите число')
#N = int(input())
#for i in range(-N,N+1):
 #   print(i)

#4.Показать первую цифру дробной части числа
#print('Введите число')
#N = float(input())
#d = float((N*10) % 10)
#print(d)

#from random import uniform
#def get_frst_fract_digit (n):
#    return int(n * 10 % 10)
#n = uniform(10,1000)
#print(n)
#print(get_frst_fract_digit(n))

#5.Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
#n = int(input('Введите число: '))
#def check_mult(n):
#    return (n % 5 == 0 or n % 10 == 0 or n % 15 == 0) and n % 30 !=0
#print(check_mult(n))

#6.Дано число обозначающее день недели.
# Вывести его название и указать является ли он выходным.

#from calendar import weekday
#from datetime import datetime


#week_days = ('Понедельник', 'Вторник', 'Среда', 'Четверг',
#             'Пятница', 'Суббота', 'Воскресенье')
#number = int(input('Введите номер дня недели: '))


#def Find_day(list, num):
#
#    if 0 < num < 6:
#        return week_days[num-1]
#    elif 5 < num < 7:
#        return f'{week_days[num-1]}, выходной день'

#day_name = Find_day(week_days, number)
#print(day_name)

# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

#x = 0
#y = 1
#left = not (x or y)
#right = not x and not y
#statement = left == right
#print (statement)


# 8. Сообщить в какой четверти координатной плоскости
#  или на какой оси находится точка с координатами Х и У

#from random import randint

#x = randint (-100, 100)
#y = randint (-100, 100)

#def get_quarter_number (x, y):
#    if x != 0 and y != 0:
#       if x * y > 0:
#            if x > 0: return 1
#            else: return 3
#        else:
#            if x < 0: return 2
#            else: return 4
#    else:
#        if x == 0: return 'OY'
#        else: return 'OX'

#print (f'Точка: {x, y}')
#print (f'Четверть: {get_quarter_number(x, y)}')



# 9. Указав номер четверти прямоугольной системы координат,
# показать допустимые значения координат для точек этой четверти

#from random import randint

#quarter = randint(1, 4)
#diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

#def show_diapasone (quart, diapasones):
#    return diapasones[quart-1]

#print (f'{quarter}: {diapasones[quarter-1]}')

# 10. Найти расстояние между двумя точками пространства

#from random import randint
#import math

#def Get_coordinates(num_plan, left, right):     # координаты точек
#    return tuple([randint(left, right) for i in range(num_plan)])

#def Find_dist(a, b):    # расстояние между точками
#    return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 3)

#num_plan = 3    # количество осей координат
#left = -10
#right = 10

#point_A = Get_coordinates(num_plan, left, right)
#point_B = Get_coordinates(num_plan,left, right)

#print(f'A {point_A}, B {point_B}')
#print (f'Расстояние между точками: {Find_dist(point_A, point_B)}')

str = input("Enter first message: ")
str2 = input("Enter second message: ")

print(str2.count(str))
print(str.count(str2))

#Напишите алгоритм, который берет массив и перемещает все нули в конец,
# сохраняя порядок других элементов.

if i.isdigit():
        print(f'Все окей, число есть {i}')
        exit()


spisok_1 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
stroka_1 = "йцу"
count = 0
print(spisok_1.count(stroka_1))
if spisok_1.count(stroka_1) <2:
    count = -1
else:
    for i in range(len(spisok_1)):
        if spisok_1[i] == stroka_1:
            count+=1
            if count ==2:
                count = i
                break
print(f'Искомое {stroka_1}, ответ {count}')




spisok_1 = [1, 654, 45, 85, 9, 6, 4, 53, 4]
sum = 0
for i in range(1, len(spisok_1), 2):
    sum += spisok_1[i]
print(sum)


float_spisok = [1.1, 1.2, 3.1, 5.002, 10.000001, 11.13, 10.11, 122324.52, 0.14]
# i=0
# while float_spisok[i]>1:
max = 0.000
min = 1.000
for i in range(len(float_spisok)):
    float_spisok[i]=round(float_spisok[i]-int(float_spisok[i]),10)
    if max<float_spisok[i]:
        max = float_spisok[i]
    if min>float_spisok[i]:
        min = float_spisok[i]
x=max-min
# print(float_spisok)
# print(max(float_spisok))
print(max,min)
print(type(x))
print(x)
