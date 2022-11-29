import csv

with open("vstupni_data.csv", encoding="utf-8") as f,\
    open("vystup_zatim.csv", "w", newline='', encoding="utf-8") as fout:
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
            prumer_tyden_nezaokrouhlene = round((prutoky/7 ),4)      
            prumer_tyden = (f'{prumer_tyden_nezaokrouhlene:.4f}')    
            vytiskni.append(prumer_tyden)            
            writer.writerow(vytiskni)           
            prutoky = 0   




    

