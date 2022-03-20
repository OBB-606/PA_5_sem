import csv
import sys
#допускает цепочку, если начинается на "0101"

with open ("csv_message_for_DSM.csv", encoding="utf-8") as r_file:
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
s = 0 #состояние автомата
print("word is ", word)

for i in word:
    if s == 0:
        if i == '0':
            s = 1
            continue
        if i == '1':
            s = 0
            break
    if s == 1:
        if i == '0':
            s = 0
            break
        if i == '1':
            s = 2
            continue
    if s == 2:
        if i == '0':
            s = 3
            continue
        if i == '1':
            s = 0
            break
    if s == 3:
        if i == '0':
            s = 0
            break
        if i == '1':
            s = 3
            break

if s == 3:#если автомат оказался в допускающем состоянии, то слово - допустимое
    print("Слово является допустимым")
elif s == 0:
    print("Слово не является допустимым")