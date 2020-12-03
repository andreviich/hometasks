st_1 = input('Enter some string... ')
st_2 = input('Enter one more string... ')

lst = [st_1, st_2, len(st_1), len(st_2), st_1 < st_2]
relation = ''
if st_1 < st_2:
    relation = 'перед'
else:
    relation = 'после'
output = input('Enter output... ')
if output == "lengths":
    print('Длины строк: '+str(lst[2])+' и '+str(lst[3])+'')
else: 
    print('Строка ' + st_1 + ' идет ' + relation + ' строки ' + st_2)
