#32.Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers = [10, 20, 20, 30, 30, 35, 40]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
