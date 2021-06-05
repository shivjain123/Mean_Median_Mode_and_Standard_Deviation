import csv
import math

with open("D:\WhiteHatJr. Codes\Third Module\Mean_Median_Mode\Class\student.csv", newline="") as f:
    reader = csv.reader(f)
    file_list = list(reader)

#print(file_list)

file_list.pop(0)

new_list = []

for i in range(0, len(file_list)):
    marks = file_list[i][1]
    new_list.append(marks)

#print(new_list)

total = 0
list_length = len(new_list)

for t in new_list:
    total = total + t

#mean = total/list_length
