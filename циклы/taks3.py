
# 2) С помощью цикла while ассчитать двойной факториал для произвольного числа. Двойной факториал *n!!* числа n рассчитывается как произведение всех чисел, меньших исходного на числа, кратные двум (вплоть до 1 или 2). Например: 7!! = 7 \* 5 \* 3 \* 1 = 105

# 3) Решить предыдущую задачу с помощью цикла for.
num = int(input("Enter your number...  "))
rangeStep = []
even = False
res = 1
if (num%2 == 1):
    rangeStep = iter(range(1, num+1, 2))
else:
    rangeStep = iter(range(2, num+1, 2))

for i in rangeStep:
    res *= i
print(res)


