import csv

with open("data.csv", encoding="utf-8", newline='') as f:
	reader = csv.reader(f, delimiter=";")
	next(reader)
	for row in reader:
		print(f"{row[0]}")