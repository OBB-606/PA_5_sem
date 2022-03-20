import csv
import sys
#НКА допускает цепочку, если в ней присутствует "01"

with open ("../progect_1/algs/csv_message_for_DSM", encoding="utf-8") as r_file:
    file_reader = csv.reader(r_file)
    word_temp = []
    for row in file_reader:
        word_temp.append(row)

word = ""#слово
for i in range (len(word_temp[0])):
    word += word_temp[0][i]
for i in word:#проверка на принадлежность слова к допустимому алфавиту автомата
    if i != '1' and i != '0':
        print("Алфавит данного слова не удовлетворяет этому атвомату")
        sys.exit()

print("word is ", word)

s1 = 0
s2 = 0
#word  = '11111'
for i in word:
    if s1 == 0:
        if i == '0':
            s1 = 0
        if i == '1':
            s1 = 0
    if s2 == 0:
        if i == '0':
            s2 = 1
        if i == '1':
            s2 = 0
    if s1 == 1:
        if i == '0':
            pass
        if i == '1':
            s1 = 2
    if s2 == 1:
        if i == '0':
            pass
        if i == '1':
            s2 = 2
    if s1 == 2:
        if i == '0':
            pass
        if i == '1':
            pass
    if s2 == 2:
        if i == '0':
            pass
        if i == '1':
            pass

if s1 == 2 or s2 == 2:
    print("dopusk")
else:
    print("nedopusk")

