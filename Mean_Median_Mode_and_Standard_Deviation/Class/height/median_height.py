import csv

with open("D:/WhiteHatJr. Codes/Third Module/Mean_Median_Mode/Class/Height_Weight.csv", newline="") as f:
    reader = list(csv.reader(f))

reader.pop(0)

new_list = []

for i in range(0, len(reader)):
    height = reader[i][1]
    new_list.append(float(height))

new_list.sort()
list_length = len(new_list)

if list_length % 2 == 0:
    median1 = new_list[list_length//2]
    median2 = new_list[list_length//2 + 1]
    median = (median1 + median2)/2
else:
    median = new_list[list_length//2]

print()
print("The Median is " + str(median) + ".")
print()
