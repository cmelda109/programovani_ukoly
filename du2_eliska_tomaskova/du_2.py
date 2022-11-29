import csv

# vytvoření listu s hodnotami z páteho sloupce s hodnotami průtoků
list = []
with open ("data.csv", encoding="utf-8",newline='') as f:
    reader = csv.reader(f,delimiter=",")
    for row in reader:
        list.append(row[5])
 
# vytvoření druhého listu
list_dva = []
for element in list:
    list_dva.append(float(element))

# vytvoření sublistu po 7 hodnotách v listu_dva a vypočítání jejich průměrů
sublist = [list_dva[x:x+7] for x in range(0, len(list_dva), 7)]
for x in sublist:
    vysledek = (sum(x)/len(x))
    vysledek2 = round(vysledek,4)
    output = (f'{vysledek2:.4f}')
    print(output)


# vytvoření outputu.csv a zapsání nově vypočtených hodnot
with open("data.csv", encoding="utf-8", newline='') as f, \
	open("outpu_1.csv","w",encoding="utf-8", newline='') as fout:
	reader = csv.reader(f, delimiter=";")

	next(reader)
	writer = csv.writer(fout)
	for row in reader:
		name = row[0]
		hod = output
		outrow = [name, hod]
		writer.writerow(outrow)


