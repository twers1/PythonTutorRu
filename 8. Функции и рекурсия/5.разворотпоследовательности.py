# Условие: Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
# Решение: 
def reversal():
    x = int(input())
    if x != 0:
        reversal()
    print(x)
 
reversal()
