"""
1. (Pominięte zadanie na zajęciach)
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien
mieć także możliwość naładowania baterii.
>>> car = ElectricCar(100)
>>> car.drive(70)
70
>>> car.drive(50)
30
>>> car.drive(50)
0
>>> car.charge()
>>> car.drive(50)
50
"""

class Tesla:
    def __init__(self, model, bateria, zasieg):
        self.model = model
        self.bateria = bateria
        self.zasieg = zasieg
        self.max_zasieg = zasieg

    def wypisz(self):
        if self.czy_jest_zasieg():
            print(f"{self.model}, {self.bateria} %/{self.zasieg} km")
        else:
            print(f"Bateria wyczerpana! Naladuj {self.model}, aby jechac dalej.")

    def jazda(self, km):
        if km < 0:
            self.jazda(-km)
            return
        self.zasieg -= km
        if self.zasieg < 0:
            self.zasieg = 0

    def zuzycie_baterii(self, proc):
        if proc < 0:
            self.zuzycie_baterii(-proc)
            return
        self.bateria -= proc
        if self.bateria < 0:
            self.bateria = 0

    def charge(self, km):
        if km <0:
            self.jazda(-km)
            return
        if self.czy_jest_zasieg():
            self.zasieg += km
            if self.zasieg > self.max_zasieg:
                self.zasieg = self.max_zasieg
        else:
            print(f"Akumulator jest juz pelny!")

    def czy_jest_zasieg(self):
        return self.zasieg > 0

car = Tesla("Tesla X", 100, 1000)
car.wypisz()
car.jazda(100)
car.wypisz()
car.charge(10)
car.wypisz()
car.jazda(550)
car.charge(150)
car.wypisz()

