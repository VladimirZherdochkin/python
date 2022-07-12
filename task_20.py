# 20.Определить, присутствует ли в заданном списке строк, некоторое число 
s = 'qwerty,fork,orr,96969,3030'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
       digits.append(int(symbol))
print('Число существует')
else:
print('Числа не существует')        
    
