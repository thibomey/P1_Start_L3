# Maak een programma dat de gebruiker in staat stelt een vorm te kiezen (vierkant, driehoek of cirkel)
# en de gekozen vorm op het scherm te tekenen.
#
# Als de gebruiker een ongeldige vorm invoert, moet het programma een foutmelding weergeven.

import turtle
input_vorm = input("Welke vorm wil je tekenen? ")
if input_vorm == "vierkant":
    turtle.shape("square")
elif input_vorm == "cirkel":
    turtle.circle(100)
elif input_vorm == "rechthoek":
    turtle.shape("rectangle")
elif input_vorm == "driehoek":
    turtle.shape("triangle")
else:
    print ("Geen geldige figuur")

turtle.done ()