Dokumentace

Vstupem je tabulka (.csv) obsahující datum a naměřený průtok daného dne (oddělovacím znakem je čárka). 

Program využívá funkce for pro procházení jednotlivých řádků. Řádky jsou stejně jako průtoky postupně sčítány a ve chvíli, kdy program narazí na podmínku, vypočítá průměr průtoků a zapíše ho do nové tabulky.

Program vytvoří dva výstupy:

  1. Sedmidenní průměry (vystup_7dni.csv)
     Nová tabulka obshauje informace vždy z prvního dne s vypočítaným průměrem průtoku daného týdne, pokud je na konci týden neúplný, vypočítá se průměr z tolika dní,        kolik je jich k dispozici.
     
  2. Roční průměry (vystup_rok.csv)
     Nová tabulka obsahuje informace z prvního dne daného roku s vypočtenými průměry průtoků za celý rok.
     
Program dále vypíše do terminálu nalezený maximální a minimální průtok z celého seznamu.

Program umí ošetřit následující chyby: neexistující vstupní soubor, neoprávněný přistup k souboru, index mimo rozsah a chybné hodnoty průtoků (nulový, záporný, nečíselný).

