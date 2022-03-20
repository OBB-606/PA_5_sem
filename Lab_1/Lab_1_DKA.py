#допускает цепочку, если она содержит в начале 0101
import csv
import sys

with open("csv_message_for_DSM.csv", encoding="UTF-8") as r_file:
    file_reader = csv.reader(r_file)
    word_temp = []
    for row in file_reader:
        word_temp.append(row)

with open("structure_DKA.csv", encoding="UTF-8") as r_file:
    file_reader = csv.reader(r_file)
    adjacency_list = []
    for row in file_reader:
        adjacency_list.append(row)
adjacency_list_final = [[int(j) for j in i] for i in adjacency_list]

temp_sostojanie = int(adjacency_list_final[0][0])
dopusk_sost = int(adjacency_list_final[1][0])
for i in range(2):
    adjacency_list_final.pop(0)
print("dopusk is ", dopusk_sost)
print("start is ", temp_sostojanie)
word = ''
for i in range(len(word_temp[0])):
    word += word_temp[0][i]

for i in word:
    if i != '1' and i != '0':
        print("Word is incorrect")
        sys.exit()
print("word is ", word, '\n')
print("adjacency list: \n")
for i in range(len(adjacency_list_final)):
    print(adjacency_list_final[i])

for i in word:
    if i == '0':
        temp_sostojanie = adjacency_list_final[temp_sostojanie][1]
        # if temp_sostojanie == dopusk_sost:
        #     break
    elif i == '1':
        temp_sostojanie = adjacency_list_final[temp_sostojanie][2]
        # if temp_sostojanie == dopusk_sost:
        #     break

if temp_sostojanie == dopusk_sost:
    print("word is correct, because the state is ", temp_sostojanie)
else:
    print("word is incorrect!, because the state is ", temp_sostojanie)