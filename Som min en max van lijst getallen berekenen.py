# Schrijf een programma dat de som, het minumum en het maximum  van een reeks van ingevoerde getallen bepaald.
# Het programma print de resultaten nadat het woord “klaar” is ingevoerd.

# Het minimum is zo groot mogelijk om ervoor te zorgen dat alles wat je invoert kleiner is dan het minimum, dus voer je 1000 in dan wordt 1000 je nieuwe minimum
# Want 1000 is kleiner dan 9223372036854775807
minimum = 9223372036854775807
# Het maximum is juist zo klein mogelijk gemaakt om ervoor te zorgen dat alles wat je invoert groter is dan het maximum, dus voer je 1 in dan wordt 1 je nieuwe maximum
# Want 1 is groter dan -9223372036854775807
maximum = -9223372036854775807

# Lege lijst initialiseren om later te kunnen vullen
reeksGetallen = []

som = 0
gebruikerGetallenWilInvoeren = True # initialisatie waarde loop

while gebruikerGetallenWilInvoeren: # stopcriterium loop
    inputGebruiker = input("Vul een getal in of klaar om te rekenen.")
    if inputGebruiker == "klaar":
        gebruikerGetallenWilInvoeren = False # beinvloeding stopcriterium
        
    else:
        inputGetal = int(inputGebruiker)
        som += inputGetal

        if inputGetal < minimum:
            minimum = inputGetal

        if inputGetal > maximum:
            maximum = inputGetal

        reeksGetallen.append(inputGetal)

print(f"De som van de getallen is {som}")
print(f"Het maximum van de getallen is {maximum}")
print(f"Het minimum van de getallen is {minimum}")

#### Op deze manier kun je de handige functies van Python gebruiken
# print(f"De som van de getallen is {sum(reeksGetallen)}")
# print(f"Het maximum van de getallen is {max(reeksGetallen)}")
# print(f"Het minimum van de getallen is {min(reeksGetallen)}")


