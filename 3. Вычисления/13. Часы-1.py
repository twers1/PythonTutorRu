# Условие: С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). По данным числам H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и выведите его в виде действительного числа.
# Решение: 
h = int(input()) * 30
m = int(input()) * 30
s = int(input()) * 30
print(h+m/60+s/3600)
