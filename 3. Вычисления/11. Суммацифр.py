# Условие: Дано трехзначное число. Найдите сумму его цифр.
# Решение: 
a = int(input())
x = a//100
b = a%10
y = (a//10)%10
print(x+b+y)
