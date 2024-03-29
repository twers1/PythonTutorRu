# Условие: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
# Решение: 
a = {}

for _ in range(int(input())):
    l = input().split()
    for word in l:
        a[word] = a.get(word, 0) + 1
        
for word in sorted(a.items(), key = lambda x:(-x[1], x[0])):
    print(word[0])
    
