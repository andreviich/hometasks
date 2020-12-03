st = input('Enter your string... ')

lst_1 = list(st)
lst_2 = st.split()
lst_3 = []

for i in st:
    if i.isnumeric():
        lst_3.append(i)
print(lst_1, lst_2 , lst_3)