zin = "Beste Studenten van de opleiding Ad-ict, hoe gaat het met jullie! wat doen Jullie graag? zie hier dat dit WeRkT."
lengteVanDeZin = len(zin)
eersteWoordVanDeZin = True
i = 0

for letter in zin: # Letter is telkens een andere letter in de zin die 1 voor 1 worden afgegaan
    isWoordGevonden = False
    while not isWoordGevonden:
        if i >= lengteVanDeZin:                                         # ga door zolang de index niet groter of gelijk is aan de lengte van de zin 
            break # gebruik break verantwoordelijk en niet te vaak

        if eersteWoordVanDeZin and zin[i].isalpha():                    # als de karakter het eerste woord van de zin is en een letter in de alphabet is (zin[i].isalpha()) 
            zin = zin[:i] + zin[i:].replace(zin[i], zin[i].upper(), 1)  # dan vervang de kleine letter met een hoofdletter | zin[:i] pakt alle characters van van index 0 tot i, zin[i:] pakt van index i tot het einde van de zin 
            eersteWoordVanDeZin = False
        elif zin[i].isupper() and not eersteWoordVanDeZin:              # als de karakter een hoofdletter is en niet het eerste woord van de zin
            zin = zin[:i] + zin[i:].replace(zin[i], zin[i].lower(), 1)  # dan vervang de hoofdletter met een klein letter
        elif zin[i] == " ":                                             # is de karakter een spatie dan weten we dat een nieuw woord komt
            isWoordGevonden = True
            zin = zin[:i] + zin[i:].replace(zin[i], zin[i].lower(), 1) 
        elif zin[i] in '.?!':                                           # komt de karakter voor in de lijst van tekens (.?!)
            eersteWoordVanDeZin = True 

        i += 1

print(zin)

# De replace statement maakt steeds een nieuwe string aan. Dit wordt gedaan door het begin van de string tot de huidige index te samen te voegen (concatenaten) met de rest van de zin met de vervangen character.
# Dit is zo gedaan omdat de replace() functie begint vanaf de eerste index van de string te kijken naar karakters om te vervangen. 
# Zou ik de zin niet in 2 splitsen dan zou hij vanaf het begin van de zin kijken en als toevallig de letter eerder voorkomt, dan vervangt hij de letter die het eerst voorkomt ipv degene die je wilt vervangen.

# Speel maar eens door zin[:i] en zin[i:].replace(zin[i], zin[i].lower(), 1) te printen!
