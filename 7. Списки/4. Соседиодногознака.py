# Условие: Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего. Если таких пар соседей несколько — выведите первую пару.
# Решение: 
a = list(map(int, input().split()))
for i in range(1, len(a)): 
    if (a[i]* a[i-1] >=0):
        print(a[i-1], a[i], end=' ')
        break
