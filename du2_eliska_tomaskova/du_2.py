import csv

list = []


with open ("data.csv", encoding="utf-8",newline='') as f:
    reader = csv.reader(f,delimiter=",")
    for row in reader:
        list.append(row[5])

list_dva = []
for element in list:
    list_dva.append(float(element))

sublist = [list_dva[x:x+7] for x in range(0, len(list_dva), 7)]


for x in sublist:
    print(sum(x)/len(x))





    


