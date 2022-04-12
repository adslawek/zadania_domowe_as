towar = input("Co chcesz kupić?: ")
cena = float(input("Podaj cenę za kilogram: "))
ilosc = float(input("Podaj ilość wybranego towaru w kilogramach: "))
naleznosc = cena * ilosc
print(f'Należność za wybrany towar wynosi {naleznosc:.2f} PLN.')