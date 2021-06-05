import csv

with open("D:/WhiteHatJr. Codes/Third Module/Mean_Median_Mode/Class/Height_Weight.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    #print(file_data)

file_data.pop(0)

new_list = []

for i in range(0, len(file_data)):
    weight = file_data[i][2]
    new_list.append(float(weight))

#print(new_list)

total = 0
list_length = len(new_list)

for t in new_list:
    total = total + t

mean = total/list_length

print()
print("The mean is " + str(mean) + ".")
print()
