st  = 'слово1,слово2,слово3,слово4'

arr = {}
key = ''
startNum = 1
for i in st:
    key = key + i
    if i == ',':
        newitem = {key.replace(',', '') : f'номер {startNum} в строке'}
        arr.update(newitem)
        startNum += 1
        key = ''
print(arr)

