x =  0
st = input('Enter your string... ')

#  Finding the ASKII value for "a"
aind = ord('a')

def Lec(s , x):
    for i in st:
        if ord(i) < aind:
            x = 0
        else:
            x = x + 1
    return x

while len(st) < 1 or Lec(st, x) == 0:
    if len(st) < 1:
        st = input('Enter your string... ')
    else:
        if  Lec(st, x) == 0:
            print('Too early in the dictionary. Try again!')
            st = input('Enter your string... ')
    

if st == "STOP" : 
    print('Program interrupted by user')
    exit()

if not Lec(st, x) == 0:
    print('{:_^30}'.format(st))
   