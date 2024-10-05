# Maak een programma dat de gebruiker in staat stelt een vorm te kiezen (vierkant, driehoek of cirkel)
# en de gekozen vorm op het scherm te tekenen.
#
# Als de gebruiker een ongeldige vorm invoert, moet het programma een foutmelding weergeven.

import turtle

size = int(input("hoeveel hoeken: "))
for i in range(size):
    turtle.right(180-180/size)
    turtle.forward(100)
turtle.forward(50)
turtle.done()



input_vorm = input("Welke vorm wil je tekenen? ")

if input_vorm == "vierkant":
    turtle.shape("square")
elif input_vorm == "cirkel":
    turtle.circle(100)
elif input_vorm == "rechthoek":
    turtle.shape("rectangle")
elif input_vorm == "driehoek":
    turtle.shape("triangle")
elif input_vorm == "ster":
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)
elif input_vorm == "ster met 6":
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.left(120)

else:
    print ("Geen geldige figuur")

#size = int(input("hoeveel hoeken: "))
#for i in range(size):
    #turtle.right(180-180/size)
    #turtle.forward(100)
#turtle.forward(50)
#turtle.done()

turtle.done ()