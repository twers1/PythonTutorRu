# Условие: Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. Определите размер вклада через год. Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
# Решение: 
p = int(input())
x = int(input())
y = int(input())
money_before = 100 * x + y
money_after = int(money_before * (100 + p) / 100)
print(money_after // 100, money_after % 100)
# интернет помог мне решить
