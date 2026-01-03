# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    gatunek = "Homo Sapiens"
    def __init__(self):
        # Konstruktor
        # Akt istnienia
        print("Niech powstanie Czlowiek")

# Powstawanie obiektu
# Gotowanie z przepisu
adam = Czlowiek() # a = 4 # a = int(4)
print(adam.gatunek)
