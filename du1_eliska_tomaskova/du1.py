import turtle

# Definování velikosti mřížky, strany a zrychlení vykreslování
A = 3
B = 3
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

# Definice vykreslení kolečka
def kolecko():
    print("Na řadě je první hráč. Váším symbolem je kolečko.")
    
    # Pokud uživatel zadá jiné souřadnice než 1 až 3, je vyzýván, dokud je nezadá správně
    while True:
        x1 = float(input("Zadejte souřadnice x: "))
        y1 = float(input("Zadejte souřadnice y: "))
        if ((x1 in (1,2,3)) and (y1 in (1,2,3))):
            break 
        else:
            print("Zadali jste nesprávné souřadnice. Zkuste to znovu.")

    # Želva se přemístí na souřadnice zadané uživatelem
    # Předpisy ve fuknci setpos převádí souřadnice zadané uživatelem na skutečné souřadnice
    # Mřížka je definována tak, že políčko [1,1] je v levém horním rohu
    turtle.setpos(strana*x1-strana/2,-strana*y1+3.1*strana)  
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(40) 
    turtle.penup()

# Definice vykreslení křížku
def krizek ():
    print("Na řadě je duhý hráč. Váším symbolem je křížek.")

    # To stejné jak pro kolečko platí i pro křížek   
    while True:
        x2 = float(input("Zadejte souřadnice x: "))
        y2 = float(input("Zadejte souřadnice y: "))
        if ((x2 in (1,2,3)) and (y2 in (1,2,3))):
            break 
        else:
            print("Zadali jste nesprávné souřadnice. Zkuste to znovu.")
    
    # Želva se přemístí na střed daného čtverce
    turtle.setpos(strana*x2-strana/2,-strana*y2+7/2*strana)
    turtle.setheading(0)
    turtle.pendown()

    # Vykreslení křížku ze středu čtverce
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

# Jednotliví hráči se střídají, každý má čtyři tahy
for a in range (4):
    kolecko()
    krizek()

# Mřížka má 9 polí, končí tedy hráč, který začínal
kolecko()
    
print("Hra skončila.")
turtle.exitonclick()
   


