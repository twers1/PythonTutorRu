# Условие: Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
# Решение: 
n = int(input()) # кол-во стран
cities = {}
for _ in range(n):
    l = input().split()
    for city in l[1:]: # первое слово это город, остальные - страны
        cities[city] = l[0]
        
for _ in range(int(input())):
    print(cities[input()])
