# Hra piškovrky ve čtvercové síti, mřížka je definována tak, že políčko [1,1] je v levém horním rohu

import turtle

# Definování velikosti hrací plochy uživatelem
A = int(input("Zadej počet sloupců hrací plochy: "))
B = int(input("Zadej počet řádků hrací plochy: "))

# Definování strany a zrychlení vykreslování
strana = 100
turtle.speed(100)

# Vykreslení čtvercové sítě
for y in range(B):
	for x in range(A):
		for i in range(4):
			turtle.forward(strana)
			turtle.left(90)
		turtle.forward(strana)
	turtle.right(180)
	turtle.forward(A*strana)
	turtle.right(90)
	turtle.forward(strana)
	turtle.right(90)
turtle.penup()

# Definice vykreslení křížku
def krizek ():
    print("Na řadě je první hráč. Váším symbolem je křížek.")

    # Pokud uživatel zadá souřadnice mimo hrací plochu, je vyzýván, dokud nezadá existující souřadnice
    while True:
        x2 = float(input("Zadejte souřadnice x: "))
        y2 = float(input("Zadejte souřadnice y: "))
        if (( A >= x2 >= 1) and ( B >= y2 >= 1) ):
            break 
        else:
            print("Zadali jste nesprávné souřadnice. Zkuste to znovu.")
    
    turtle.setpos(strana*x2-1/2*strana,strana*(B-y2)+1/2*strana)  # Želva se přemístí na střed daného čtverce
    turtle.setheading(0)
    turtle.pendown()

    # Vykreslení křížku ze středu políčka
    turtle.right(45)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.penup()

# Definice vykreslení kolečka
def kolecko():
    print("Na řadě je druhý hráč. Váším symbolem je kolečko.")
    
    # Pokud uživatel zadá souřadnice mimo hrací plochu, je vyzýván, dokud nezadá existující souřadnice
    while True:
        x1 = float(input("Zadejte souřadnice x: "))
        y1 = float(input("Zadejte souřadnice y: "))
        if (( A >= x1 >= 1) and ( B >= y1 >= 1) ):
            break 
        else:
            print("Zadali jste nesprávné souřadnice. Zkuste to znovu.")

    turtle.setpos(strana*x1-1/2*strana,strana*(B-y1)+1/10*strana)  # Želva se přemístí na střed osy x a 1/10 osy y daného čtverce
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(40) 
    turtle.penup()

# Jednotliví hráčí se střídají -> hra skončí až dojdou všechna políčka
for a in range (A*B//2):
    krizek()
    kolecko()

if A*B % 2 == 1: # Pokud je políček lichý počet, hraje ještě jednou první hráč
    krizek()
   
print("Hra skončila.")
turtle.exitonclick()
   

   
