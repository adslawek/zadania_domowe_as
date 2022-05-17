class Przedmiot:
    def __init__(self, item, bonus):
        self.item = item
        self.bonus = bonus

    def __str__(self):
        return f"Przedmiot {self.item} daje bonus >>>{self.bonus}<<< punktow HP i tyle samo srebrnikow."

class Postac:
    def __init__(self, imie, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie

    def wypisz(self):
        if self.czy_zyje():
            print(f"{self.imie}, {self.zdrowie}/{self.max_zdrowie} HP")
        else:
            print(f"{self.imie}, nie żyje")

    # zmniejsza zdrowie o dmg; zdrowie nie powinno spaść poniżej 0
    def otrzymaj_obrazenia(self, dmg):
        if dmg < 0:
            self.wylecz(-dmg)
            return
        self.zdrowie -= dmg
        if self.zdrowie < 0:
            self.zdrowie = 0

    def daj_atak(self, atak):
        if atak < 0:
            self.wylecz(-atak)
            return
        if self.czy_zyje():
            self.zdrowie += atak
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print("Nie można wyleczyć ani zaatakować trupa!")

    # przywraca `hp` utraconych punktów zdrowia;
    # zdrowie nie powinno przekroczyć maksymalnej wartosci
    # leczenie nie działa jesli postac nie zyje
    def wylecz(self, hp):
        if hp < 0:
            self.otrzymaj_obrazenia(-hp)
            return
        if self.czy_zyje():
            self.zdrowie += hp
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print("Nie można wyleczyć trupa!")

    # tutaj jeszcze nie wiem:
    # def daj_przedmiot(self, eq):
    # if eq

    # zwraca iformację, czy postać żyje
    def czy_zyje(self):
        return self.zdrowie > 0

    def daj_przedmiot(self, p: Przedmiot, ile=1):
        if not isinstance(p, Przedmiot):
            print("Nie masz mozliwosci zabrania tego przedmiotu.")
            return
        if p.item in self.eq:
            self.eq[p.item].ilosc += ile
        else:
            self.eq[p.item] = Przedmiot.eq(p, ile)

    #do dopracowania
    #def wypisz_eq(self):
        #if self.daj_przedmiot(p):
            #print(f"{self.imie} posiada w eq: {self.item}")




rufus = Postac("Rufus", 120)
rufus.wypisz() # Rufus, 120/120 HP
rufus.otrzymaj_obrazenia(15)
rufus.wypisz() # Rufus, 105/120 HP
rufus.wylecz(3)
rufus.wypisz() # Rufus, 108/120 HP
rufus.daj_atak(10)
rufus.wypisz()

p = Przedmiot("Toprek", 15)
print(p)

rufus.daj_przedmiot("Tarcza", 20)
rufus.wypisz()