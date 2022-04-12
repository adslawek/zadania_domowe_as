wiek = int(input("Podaj swój wiek: "))
bilety = int(input("Ile biletów chcesz kupić: "))
cena_biletu = 3.80
if wiek <= 6:
    cena_biletu = 0
elif wiek >= 7 and wiek <= 17:
    cena_biletu = 2.28
elif wiek >= 65:
    cena_biletu = 1.90


naleznosc = bilety * cena_biletu
print(f'Należność: {naleznosc:.2f} PLN')
