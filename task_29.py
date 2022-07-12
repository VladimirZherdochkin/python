#29.Найти НОК двух чисел


# def nod(a,b):

#     if b==0:
#         return a
#     else:
#         return nod(b,a%b)
 
# def nok(a,b):
#     return a*b//nod(a,b)

number1 = int(input('Введите первую цифру = '))
number2 = int(input('Введите вторую цифру = '))

nok = min(number1, number2)
while True:
    if nok%number1==0 and nok%number2==0:
        break
    nok += 1
print(nok)
