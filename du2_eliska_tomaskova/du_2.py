import csv

with open ("data.csv", encoding="utf-8",newline='') as f:
    reader = csv.reader(f,delimiter=",")
    for row in reader:
        
        print(row)