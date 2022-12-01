import csv


# Kontrola existence/přístupnosti vstupního souboru
try:
    with open("vstupni_data.csv", encoding="utf8") as fcsvinfile,\
            open("vystup_7dni.csv", "w", encoding="utf8") as f,\
                open("vystup_rok.csv", "w", encoding="utf8") as f:
        reader = csv.reader(f, delimiter = ",")
except FileNotFoundError:
    print("Soubor neexistuje")
    exit()
except PermissionError:
    print("Neoprávněný přístup")
    exit()   


# Sedmidenní průměry
with open("vstupni_data_carky.csv", encoding="utf-8") as f,\
    open("vystup_7dni.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)

    # definovani proměnných    
    prutoky = 0               
    radky = 0                           
    
    # procházeni jednotlivých řádku
    for row in reader:      
        radky += 1
        prutoky += float(row[-1])                        
        
        if radky % 7 == 1:                              
            vytiskni = row[0:-1]

        if radky % 7 == 0:  
            
            prumer_tyden_nezaokrouhlene = round((prutoky/7),4)      
            prumer_tyden = (f'{prumer_tyden_nezaokrouhlene:.4f}')    
            vytiskni.append(prumer_tyden)            
            writer.writerow(vytiskni)           
            prutoky = 0


# Roční průměry
with open("vstupni_data_carky.csv", encoding="utf-8") as f,\
    open("vystup_rok.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)

    # definovani proměnných
    rok = 0    
    prutoky_rok = 0               
    pocet_dni = 0                   
    
    # procházeni jednotlivých řádku
    for row in reader: 

        prutoky_rok += 1
        pocet_dni += 1                              
        
        if rok == 0:                             
            vytiskni2 = row[0:-1]

        if rok != int(row[2]):
            prumer_rok_nezaokrouhlene = round((prutoky_rok/pocet_dni),4)      
            prumer_rok = (f'{prumer_rok_nezaokrouhlene:.4f}')    
            vytiskni.append(prumer_rok)            
            writer.writerow(vytiskni)           
            prutoky_rok = 0
 




    
