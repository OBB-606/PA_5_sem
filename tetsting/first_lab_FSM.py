#алфавит двоичных чисел, слово является допустимым, если оканчивается на "0".
import random
import sys

w = ''
word_length = int(input("Введите длину слова: "))
#word_length = 4
for i in range(word_length):
    w += str(random.randint(0, 1))
print("word is ", w)
s = "*"
for i in w:
    if i == '1':
        s = '0'
    if i == '0':
        s = '*'
if s == "0":
    print("Слово не является допустимым")
elif s == '*':
    print("Слово является допустимым")

#------------------------------------------------------------------------------------------------------------------------------------------------------
#С помощью ассоциативного массива для окончания "0"
S_dict = dict()
S_dict[0] = 'q1'#допускающее
S_dict[1] = 'q0'

temp_s = ' '

for i in w:
    if i == '1':
        temp_s = S_dict[int(i)]
    if i == '0':
        temp_s = S_dict[int(i)]
if temp_s == 'q1':
    print("Слово является допустимым")
elif temp_s == 'q0':
    print("Слово не является допустимым")


# допустимое слово начинается на "10"

sost = 0

for i in w:
    if sost == 0:
        if i == '0':
            sost = 0
            break
        elif i == '1':
            sost = 1
            break
    if sost == 1:
        if i == '0':
            sost = 1
            break
        elif i == '1':
            sost = 0
            break
if sost == 1:
    print("'10' Слово является допустимым")
elif sost == 0:
    print("'10' Слово не является допустимым")

#допустимое слово начинается на "01"

sosto = 0

def TSM():
    global sosto, w
    for i in w:
        if sosto == 0:
            if i == '0':
                sosto = 1
            if i == '0':
                sosto = 0

        if sosto == 1:
            if i == '0':
                sosto = 0

            if i == '1':
                break
TSM()

if sosto == 1:
    print("Слово является допустимым")
elif sosto == 0:
    print("Слово не является допустимым")
