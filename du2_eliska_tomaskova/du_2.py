import csv
import datetime

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

with open("vstupni_data.csv", encoding="utf-8") as f,\
    open("vystup_7dni.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)

    # definovani proměnných    
    prutoky = 0               
    radky = 0                   
    
    # procházeni jednotlivých řádku
    for row in reader:      
        radky += 1
        prutoky += float(row[3])                        
        
        if radky % 7 == 1:                              
            vytiskni = row[0:3]

        if radky % 7 == 0:  
            
            prumer_tyden_nezaokrouhlene = round((prutoky/7),4)      
            prumer_tyden = (f'{prumer_tyden_nezaokrouhlene:.4f}')    
            vytiskni.append(prumer_tyden)            
            writer.writerow(vytiskni)           
            prutoky = 0


with open("vstupni_data.csv", encoding="utf-8") as f,\
    open("vystup_rok.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)

    # definovani proměnných    
    prutoky_rok = 0               
    radky_rok = 0                   
    
    # procházeni jednotlivých řádku
    for row in reader:      
        radky_rok += 1
        prutoky_rok += float(row[3])                        
        
        if radky_rok % 365 == 1:                              
            vytiskni2 = row[0:3]

        if radky_rok % 365 == 0:                              
            prumer_rok_nezaokrouhlene = round((prutoky_rok/365 ),4)      
            prumer_rok = (f'{prumer_rok_nezaokrouhlene:.4f}')    
            vytiskni2.append(prumer_rok)            
            writer.writerow(vytiskni2)           
            prutoky_rok = 0  

    
# datetime knihovna
