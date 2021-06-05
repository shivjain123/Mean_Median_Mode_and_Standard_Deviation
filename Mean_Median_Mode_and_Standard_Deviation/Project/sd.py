import csv
import math

with open("D:\WhiteHatJr. Codes\Third Module\Mean_Median_Mode\Project\data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #print(file_data)

new_list = []

for i in range(0, len(file_data)):
    column = file_data[i][0]
    new_list.append(float(column))

total = 0
list_length = len(new_list)

for t in new_list:
    total = total + t

mean = total/list_length

print()
print("The mean is " + str(mean) + ".")
print()

squared_list = []

for i in new_list:
    a = (i - mean)**2
    squared_list.append(a)

sum = 0

for i in squared_list:
    sum = sum + i

deviation = math.sqrt(sum/list_length)

print("The Standard Devaition is " + str(deviation) + ".")
print()
