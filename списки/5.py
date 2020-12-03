max_val = int(input('Enter a positive int... '))
repeat = int(input('Enter a positive int... '))

lst = list(range(1, max_val+1))

print(lst*repeat)

lst_copy = lst.copy() 
count = len(lst_copy)*0.2
before = round(count/2)
after = round(len(lst_copy) - count/2)

for i in range(len(lst_copy)):
    if i < before:
        lst_copy[i] = ''
    if i > after-1:
        lst_copy[i] = ''

for i in range(len(lst)):
    if lst[i] in lst_copy:
        lst[i] *=10 
print(lst, lst_copy)