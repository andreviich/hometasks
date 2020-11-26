# 4) Вывести все простые числа в произвольном интервале [a, b], используя вложенные for и конструкцию for-else.

a = int(input('Enter "a"... '))
b = int(input('Enter "b"... '))

if a >= b:
    print('"a" must be less than "b"')
    exit()

rg = range(a, b+1)

def isSimple(num):
    delit = 2
    while num % delit != 0:
        delit += 1
    return delit == num

for i in rg:
    if isSimple(i):
        print(i)
