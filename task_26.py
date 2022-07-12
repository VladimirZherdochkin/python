#26.Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))

def negafib(n):
    if n in [-1,0,1]:
        return abs(n)
    elif n < 0:
        n = abs(n)
        return (-1)**(n+1)*(negafib(n-1)+negafib(n-2))
    else:
        return negafib(n-1)+negafib(n-2)

n = int(input('Введите число n = '))
list = []
for i in range(-n,n+1):
    list.append(negafib(i))
print(list)

number = 8

def fib_rec(number_int):
    if number_int in (1, 2):
        return 1
    return fib_rec(number_int - 1) + fib_rec(number_int - 2)

def negafib(number_int):
    fib1 = fib2 = 1
    for i in range(-number_int, 1):
        fib1, fib2 = fib2, fib1 - fib2
    return fib2

fib_list = [fib_rec(item) for item in range(number, 0, -1)]
fib_list.reverse()   

negafib_list = [negafib(item) for item in range(number + 1)]
negafib_list.reverse()

negafib_list.extend(fib_list)
print(f"k = {number}: {negafib_list}")

