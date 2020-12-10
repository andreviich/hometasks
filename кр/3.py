lst =  [1,2,'a',3,4,'b','c','d','e']
dct = {}
nms = []
letters = []
for elem in lst:
    if type(elem) == int:
        nms.append(elem)
    if type(elem) == str:
        letters.append(elem)
diff = len(letters) - len(nms)
if diff > 0:
    for letter in (letters):
        if len(nms) == 0:
            dct[letter] = 0
        for nm in nms:
                dct[letter] = 0
                try:
                    dct[letter] = nm
                except:
                    pass
                try:
                    nms.remove(nm)
                except:
                    pass
                break
if diff < 0 or diff == 0:
    for letter, num in zip(letters, nms):
        dct[letter] = num
print(f'{lst} перевести в {dct}')