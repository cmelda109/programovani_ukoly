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


# Sedmidenní průměry
with open("bum.csv", encoding="utf-8") as f,\
    open("vystup_7dni.csv", "w", newline='', encoding="utf-8") as fout:
    reader = csv.reader(f, delimiter = ",")
    writer = csv.writer(fout)

    # definovani proměnných    
    prutoky = 0               
    radky = 0 
    zbytek = 0                       
    
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

  

print("Úspěch!")


    
