# Условие: По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень.
# Решение: 
n = int(input())
x = 1
while n>=2**x:
    x+=1
print(x-1, 2**(x-1))
