import csv
from collections import Counter as c

with open("D:/WhiteHatJr. Codes/Third Module/Mean_Median_Mode/Class/Height_Weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    first_height = file_data[1][1]

file_data.pop(0)

new_list = []
new_list.sort()

for i in range(0, len(file_data)):
    height = file_data[i][2]
    new_list.append(float(height))

data = c(new_list)
items_data = data.items()

mode_data_range = {"60-70": 0, "70-80": 0}
items_mode_data_range = mode_data_range.items()

for height, occurence in items_data:
    if (float(height) > 60 and float(height) < 70):
        mode_data_range["60-70"] += occurence
    elif (float(height) > 70 and float(height) < 80):
        mode_data_range["70-80"] += occurence

mode_range, mode_occurence = 0, 0

for range, occurence in items_mode_data_range:
    if (occurence > mode_occurence):
        mode_range = [int(range.split("-")[0]), int(range.split("-")[1])]

mode = (mode_range[0] + mode_range[1])/2

print()
print("The mode is " + str(mode) + ".")
print()
