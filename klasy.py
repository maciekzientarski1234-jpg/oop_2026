# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    # Atrybut KLASY
    # Cechy wsplolne KAZDEGO Czlowieka
    gatunek = "Homo Sapiens"
    def __init__(self, imie): # atrybut obiektu (skladnik potrawy)
        # Cechy KONKRETNEJ OSOBY
        # Konstruktor
        # Akt istnienia
        # Gotowanie
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"

    #Metoda
    #Moznosc (mozliwosc), zdolnosc, umiejetnosc

    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie}")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

# Powstawanie obiektu
# Gotowanie z przepisu
adam = Czlowiek("Adam") # a = 4 # a = int(4)
ewa = Czlowiek("Ewa")

adam.przedstaw_sie()
adam.przedstaw(ewa)
