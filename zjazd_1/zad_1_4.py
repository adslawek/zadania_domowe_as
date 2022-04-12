wiek = int(input('Podaj swój wiek: '))
ilosc_nocy = int(input('Podaj ile nocy spędzisz w hotelu: '))
oplata = 200
if wiek < 18:
    oplata = 100
elif ilosc_nocy >= 2 and ilosc_nocy < 5:
    oplata = 180
elif ilosc_nocy >= 5:
    oplata = 150

if wiek >= 65:
    oplata = oplata * 0.9
    if wiek >= 65 and ilosc_nocy >= 2 and ilosc_nocy < 5:
        oplata = 180 * 0.9
    elif wiek >= 65 and ilosc_nocy >= 5:
        oplata = 150 * 0.9

oplata_koncowa = oplata * ilosc_nocy

print("Opłata za pobyt wynosi: ", oplata_koncowa, "PLN")