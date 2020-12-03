lst_1 = [31,24,17]

lst_2 = lst_1.copy()

lst_3 = []
for i in range(17,32,7):
    lst_3.append(i)
lst_3 = lst_3[::-1]

print(lst_1, lst_2, lst_3)
