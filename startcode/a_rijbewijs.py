# Maak een selectie om na te gaan of iemand oud genoeg is voor een rijbewijs.
def check_rijbewijsleeftijd(leeftijd):
    rijbewijsleeftijd = 18

    if rijbewijsleeftijd > leeftijd:
        print("Je bent te jong om met de auto te rijden! ")

    else:
        print("Je bent oud genoeg om met de auto te rijden! ")

# Vraag de leeftijd aan de gebruiker
input_leeftijd = int(input("Hoe oud ben je? "))

# Roep de functie aan om de leeftijd te controleren
check_rijbewijsleeftijd(input_leeftijd)

