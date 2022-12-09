import csv

# Kontrola existence/přístupnosti vstupního souboru
try:
    with open("bum.csv", encoding="utf8") as fcsvinfile,\
            open("vystup_7dni.csv", "w", encoding="utf8") as f,\
                open("vystup_rok.csv", "w", encoding="utf8") as f:
        reader = csv.reader(f, delimiter = ",")
except FileNotFoundError:
    print("Soubor neexistuje")
    exit()
except PermissionError:
    print("Neoprávněný přístup")
    exit()   

# definovani proměnných    
prutoky = 0               
radky = 0 
zbytek = 0 
rok = 0
prutoky_rok = 0
radky = 0
min_prutok, max_prutok = [],[]

# Sedmidenní průměry
with open("vstupni_data_carky.csv", encoding="utf-8") as f,\
    open("vystup_7dni.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)                     
    
    # procházeni jednotlivých řádku
    for row in reader:      
        radky += 1
        prutoky += float(row[-1]) 
                                          
        if radky % 7 == 1:                                   # prvni radek ze sedmi se ulozi do promenne vytiskni    
            vytiskni = row[0:-1]

        if radky  == 7:                                      # pokud narazi na sedmy radek vypise sedmidenni prumer    
            prumer_tyden = (f'{(prutoky/7):.4f}')   
            vytiskni.append(prumer_tyden)            
            writer.writerow(vytiskni)           
            prutoky = 0
            radky = 0

    if (radky-1) % 7 != 6:                                    # pokud se na konci seznamu nachází méně, jak 7 řádků, vypočítá se průměr pouze z nich
        prumer_prutok_tyden_zbytek = prutoky / radky
        zbytky = (f"{prumer_prutok_tyden_zbytek:.4f}")
        vytiskni.append(zbytky) 
        writer.writerow(vytiskni)

# Roční průměry
with open("vstupni_data_carky.csv", encoding="utf-8") as f,\
    open("vystup_rok.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)
   
    for row in reader:                                              
        
        if rok == 0: 
            vytiskni2 = row[0:-1]   
        if rok != int(row[4]) and rok !=0: 
            prumer_rok = (f'{(prutoky_rok/radky):.4f}')
            vytiskni2.append(prumer_rok)
            writer.writerow(vytiskni2)
            prutoky_rok = 0
            radky = 0 
            vytiskni2 = row[0:-1]
        radky += 1
        prutoky_rok +=  float(row[5])
        rok = int(row[4]) 

        min_prutok.append(row[-1])
        max_prutok.append(row[-1])

    zbyle_dny_prumer = (f'{(prutoky_rok/radky):.4f}')
    vytiskni2.append((zbyle_dny_prumer)) 
    writer.writerow(vytiskni2)
    
    print ("Nejmenší průtok:", min(min_prutok))
    print ("Největší průtok:", max(max_prutok))


print("Úspěch!")


    
