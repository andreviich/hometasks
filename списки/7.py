import math
length = input('Enter the length of the list... ')
arr = []
for i in range(int(length)):
    st = input('Enter some information... ')
    if st.isdigit() or st.replace('.', '').isdigit():
        arr.append(math.ceil(float(st)))
    elif  st  == "False" or st == "True" :
        if st == "True":
            arr.append(True)
        else:
            arr.append(False)
    elif type( st )== str:
        arr.append(st)

print(arr)