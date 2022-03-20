# допускает цепочку, если она содержит  01
import csv
import sys

with open("csv_message_for_DSM.csv", encoding="UTF-8") as r_file:
    file_reader = csv.reader(r_file)
    word_temp = []
    for row in file_reader:
        word_temp.append(row)
#
with open("structure_Lab_2.csv", encoding="UTF-8") as r_file:
    file_reader = csv.reader(r_file)
    adjacency_list = []
    for row in file_reader:
        adjacency_list.append(row)
# adjacency_list_final = [[int(j) for j in i] for i in adjacency_list]

for i in range(len(adjacency_list)):
    for j in range(len(adjacency_list[i])):
        if adjacency_list[i][j] == " " or adjacency_list[i][j] == "  " or adjacency_list[i][j] == "":
            adjacency_list[i][j] = None
        else:
            adjacency_list[i][j] = int(adjacency_list[i][j])

adjacency_list_final = list(adjacency_list)

for i in range(len(adjacency_list_final)): #отделение двух состояний
    for j in range(len(adjacency_list_final[i])):
        temp = []
        if adjacency_list_final[i][j] == "":
            adjacency_list_final[i][j] = None
        if len(str(adjacency_list_final[i][j])) == 2:
            try:
                temp = [int(adjacency_list_final[i][j]) // 10, int(adjacency_list_final[i][j] % 10)]
                adjacency_list_final[i][j] = temp
            except:
                pass

temp_sostojanie_1 = int(adjacency_list_final[0][0])
temp_sostojanie_2 = int(adjacency_list_final[0][0])
dopusk_sostojanie = int(adjacency_list_final[1][0])
for i in range(2):
    adjacency_list_final.pop(0)
print('start is ', temp_sostojanie_1)
print("dopusk is ", dopusk_sostojanie)

# for i in range(len(adjacency_list_final)):
#     print(adjacency_list_final[i])
word = ''
for i in range(len(word_temp[0])):
    word += word_temp[0][i]
a = 0
b = 0
# word = "1010"
print("word is: ", word)

for i in word:
    if i == "0":
        try:
            if adjacency_list_final[temp_sostojanie_1][0][0] is None or adjacency_list_final[temp_sostojanie_2][0][1] is None:
                continue
            else:
                temp_sostojanie_1 = adjacency_list_final[temp_sostojanie_1][0][0]
                temp_sostojanie_2 = adjacency_list_final[temp_sostojanie_2][0][1]

        except:
            if adjacency_list_final[temp_sostojanie_1][0] is None or adjacency_list_final[temp_sostojanie_2][0] is None:
                continue
            else:
                temp_sostojanie_1 = adjacency_list_final[temp_sostojanie_1][0]
                temp_sostojanie_2 = adjacency_list_final[temp_sostojanie_2][0]
    elif i == "1":
        try:
            if adjacency_list_final[temp_sostojanie_1][1][0] is None or adjacency_list_final[temp_sostojanie_2][1][1] is None:
                continue
            else:
                temp_sostojanie_1 = adjacency_list_final[temp_sostojanie_1][1][0]
                temp_sostojanie_2 = adjacency_list_final[temp_sostojanie_2][1][1]
        except:
            if adjacency_list_final[temp_sostojanie_1][1] is None or adjacency_list_final[temp_sostojanie_2][1] is None:
                continue
            else:
                temp_sostojanie_1 = adjacency_list_final[temp_sostojanie_1][1]
                temp_sostojanie_2 = adjacency_list_final[temp_sostojanie_2][1]

if dopusk_sostojanie == temp_sostojanie_1 or dopusk_sostojanie == temp_sostojanie_2:
    print("word is correct, because the state is: " + str(temp_sostojanie_1) + " and " + str(temp_sostojanie_2))
else:
    print("word is INCORRECT, because the state is: " + str(temp_sostojanie_1) + " and " + str(temp_sostojanie_2))
