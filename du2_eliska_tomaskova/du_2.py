import csv
import math
list = []


with open ("data.csv", encoding="utf-8",newline='') as f:
    reader = csv.reader(f,delimiter=",")
    for row in reader:
        list.append(row[5])

list2 = []
for element in list:
    list2.append(float(element))


average = (sum(list2[0:6]))/7
print(average)



