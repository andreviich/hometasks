
# 7) Даны две произвольные строки. Для всех символов первой строки, которые встречаются во второй строке (без учета регистра), вывести строку: "<номер\_символа\_в\_первой\_строке> встречается в строке поиска: <второе_слово>", причем второе слово выводить в нижнем регистре с найденным символом в верхнем регистре. Например, для исходной строки "Hello world!" и строки поиска 'HERD' третья строка в выводе будет содержать текст:<br> "9 символ встречается в строке поиска: heRd".

st_1 = input('Enter the first string... ')
st_2 = input('Enter the second string... ')

for i in range(len(st_1)):
    try:
        if st_2.index(st_1[i]):
            pass
    except:
        continue
    index_of_letter = st_2.rindex(st_1[i])
    st_2_edited = st_2[:index_of_letter] + st_2[index_of_letter].upper() + st_2[index_of_letter:]
    print(f"{i+1} символ в первой строке встречается во второй строке {st_2}")
    print(st_2_edited)