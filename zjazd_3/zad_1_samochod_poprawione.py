class Tesla:
    def __init__(self, model, zasieg):
        self.model = model
        self.zasieg = zasieg
        self.max_zasieg = zasieg

    def wypisz(self):
        if self.czy_jest_zasieg():
            print(f"{self.model}, zasieg: {self.zasieg} km")
        else:
            print(f"Bateria wyczerpana! Naladuj {self.model}, aby jechac dalej.")

    def jazda(self, km):
        if km < 0:
            self.jazda(-km)
            return

        self.zasieg -= km
        if self.zasieg < 0:
            self.zasieg = 0

        """if km < 0:
            self.jazda(-km)
            return

        self.bateria -= proc
        if self.bateria < 0:
            self.bateria = 0"""

    """def zuzycie_baterii(self, proc):
        if proc < 0:
            self.zuzycie_baterii(-proc)
            return
        self.bateria -= proc
        if self.bateria < 0:
            self.bateria = 0"""
#CHARGE DO POPRAWY

    def charge(self, km):
        if km <0:
            self.zasieg(-km)
            return
        if self.czy_jest_zasieg():
            self.zasieg += km
            if self.zasieg > self.max_zasieg:
                self.zasieg = self.max_zasieg
        else:
            print(f"Akumulator jest juz pelny!")

    def czy_jest_zasieg(self):
        return self.zasieg > 0

car = Tesla("Tesla X", 1000)
car.wypisz()
car.jazda(100)
car.wypisz()
car.charge(50)
car.wypisz()
car.jazda(95)
car.wypisz()
car.charge(100)
car.wypisz()
car.jazda(500)
car.wypisz()
#CHARGE DO POPRAWY