st = input('Enter some text... ')
lst = list(st)
for i in range(len(st)):
    if lst[i].lower() == "s" and not i == 0 and not i == len(lst) - 1:
        lst[i] = lst[i-1]*2 + lst[i+1]

print(lst)
