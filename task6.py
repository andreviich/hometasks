# 6) Для произвольной строки вывести те символы, номера которых в строке (не индексы!) делят длину строки без остатка. Для строки "Hello world!" должно выводиться "Hell !".

st = input('Enter some text... ')
st_after = ""
for i in range(len(st)):
    if (len(st)%(i+1)) == 0:
        st_after += st[i]
print(st_after)